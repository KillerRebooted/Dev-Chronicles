import customtkinter as ctk
import keyring
from argon2 import PasswordHasher
from time import sleep
import os
import io
import urllib.request
import threading
import shutil
import time
from PIL import Image, ImageEnhance, ImageDraw
from Book_Scouter import get_book_details
from Book_Data import longest_completed, track_book, read_data, get_total_pages, total_stats

# Ignores DPI scaling to work in Full Screen for all Systems
ctk.deactivate_automatic_dpi_awareness()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

data_loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data")

SERVICE_NAME = "Bookmark"

win = ctk.CTk(fg_color="#121212")
win.title("Login")
win.geometry("0x0")

w = win.winfo_screenwidth()
h = win.winfo_screenheight()

# Check for removing Folders for which a User doesn't exist or remove Users for which Folders don't exist and removing Auto-Logins and Saved Passwords if necessary
Users = keyring.get_password(SERVICE_NAME, "Users")
if Users: Users = Users.split("\n")
else: Users = []

for user in Users:
    if not os.path.exists(os.path.join(data_loc, "Accounts", user, "User.db")):
        Users.remove(user)
        keyring.delete_password(SERVICE_NAME, user)
        if keyring.get_password(SERVICE_NAME, "Auto-Login") == user:
            keyring.delete_password(SERVICE_NAME, "Auto-Login")

for dir in os.listdir(os.path.join(data_loc, "Accounts")):
    if dir not in Users:
        shutil.rmtree(os.path.join(data_loc, "Accounts", dir))

keyring.set_password(SERVICE_NAME, "Users", "\n".join(Users))

# Center Window Method
def center(win, screen_resolution, animation_time):

    x1, y1 = 0, 0

    while (x1 < screen_resolution[0]) or (y1 < screen_resolution[1]):

        if x1 != screen_resolution[0]: x1 += screen_resolution[0]/(animation_time*10)
        if y1 != screen_resolution[1]: y1 += screen_resolution[1]/(animation_time*10)

        win.geometry(f"{int(x1)}x{int(y1)}")

        x2 = w//2 - win.winfo_width()//2
        y2 = h//2 - win.winfo_height()//2

        win.geometry(f"+{x2}+{y2}")

        sleep(0.008)
        win.update()

    x1, y1 = screen_resolution

    win.geometry(f"{int(x1)}x{int(y1)}")

    x2 = w//2 - win.winfo_width()//2
    y2 = h//2 - win.winfo_height()//2

    win.geometry(f"+{x2}+{y2}")

    win.update()

# Marquee Text Functions
home_page_cap = 70
search_page_cap = 20

def start_marquee(home, btn, text, speed=200):
    def scroll():
        nonlocal text
        text = text[1:] + text[0]  # shift text left
        btn.configure(text=text[:home_page_cap if home else search_page_cap])
        btn._marquee_job = btn.after(speed, scroll)

    btn._marquee_job = btn.after(speed, scroll)

def stop_marquee(home, btn, original_text):
    if hasattr(btn, "_marquee_job"):
        btn.after_cancel(btn._marquee_job)
        btn.configure(text=original_text[:home_page_cap if home else search_page_cap])

# -------------- Login and Sign Up Functions -------------- #

# Switch Between Login and Sign Up Windows
def switch_method(button):

    def make_selector(x, length):
        for i in range(1, length):

            text = "_"*i

            selector.configure(text=text)
            selector.place(x=x)

            sleep(0.04)

            win.update()

    if username.get() != "":
        username.delete(0, ctk.END)
    if password.get() != "":
        password.delete(0, ctk.END)

    try:
        pass_notification.destroy()
    except:
        pass
    
    check_var.set("")
    show_pass([password])

    if button == "login":

        login_page(False)
        make_selector(133, 6)

    else:

        signup_page()
        make_selector(267, 7)

# Show Password
def show_pass(inputs):

    show = check_var.get()

    if show == "*":
        check_var.set("")
        show_password.configure(image=ctk.CTkImage(dark_image=Image.open(os.path.join(data_loc, "Images", "Eye Show.png")), size=(30,30)))
    else:
        check_var.set("*")
        show_password.configure(image=ctk.CTkImage(dark_image=Image.open(os.path.join(data_loc, "Images", "Eye Hide.png")), size=(30,30)))

    for input in inputs:
        input.configure(show=check_var.get())

# Login Page
def login_page(first_time):

    global frame, selector, username, password, check_var, show_password, login_button

    win.title("Login")

    try:
        confirm_password.destroy()
        signup_button.destroy()
        login_button.destroy()
    except:
        try:
            login_button.destroy()
        except:
            pass

    if first_time:

        center(win, (600, 400), 1.5)

        frame = ctk.CTkFrame(win, fg_color="#1f1f1f")
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(frame, text="BOOKMARK", text_color="#9a4cfa", font=("Helvetica", 24, "bold"))
        label.pack(pady=12, padx=10)
    
    if first_time:

        selector = ctk.CTkLabel(frame, text="_____", text_color="#9a4cfa", font=("Helvetica", 24, "bold"))
        selector.place(x=133, y=55)

    login_switch_method = ctk.CTkButton(frame, text="LOGIN", text_color="#9a4cfa", font=("Helvetica", 16, "bold"), fg_color="#1f1f1f", hover_color="#1f1f1f", cursor="hand2", height=0, width=0, command=lambda: switch_method("login"))
    login_switch_method.place(x=136, y=50)

    sign_up_switch_method = ctk.CTkButton(frame, text="SIGN UP", text_color="#9a4cfa", font=("Helvetica", 16, "bold"), fg_color="#1f1f1f", hover_color="#1f1f1f", cursor="hand2", height=0, width=0, command=lambda: switch_method("sign_up"))
    sign_up_switch_method.place(x=270, y=50)

    if first_time:    
        
        username = ctk.CTkEntry(frame, placeholder_text="Username", fg_color="#1f1f1f", show="", font=("Helvetica", h/90, "bold"), height=40, width=200)
        username.pack(pady=(50, 12), padx=10)

        check_var = ctk.StringVar()
        check_var.set("*")

        password = ctk.CTkEntry(frame, placeholder_text="Password", fg_color="#1f1f1f", show="*", font=("Helvetica", h/90, "bold"), height=40, width=200)
        password.pack(pady=12, padx=10)

        show_password = ctk.CTkButton(frame, text="", fg_color="#1f1f1f", hover_color="#191919", image=ctk.CTkImage(dark_image=Image.open(os.path.join(data_loc, "Images", "Eye Hide.png")), size=(30,30)), width=30, height=30, command=lambda: show_pass([password]))
        show_password.place(x=345, y=168)

    else:

        show_password.configure(command=lambda: show_pass([password]))

    login_button = ctk.CTkButton(frame, text="Login", text_color="#121212", fg_color="#9a4cfa", hover_color="#b87bff", font=("Helvetica", 13, "bold"), cursor="hand2", command=login)
    login_button.pack(pady=12, padx=10)

    win.bind("<Return>", lambda event: login())

# Sign Up Page
def signup_page():

    global confirm_password, signup_button, return_key_bind

    win.title("Sign Up")

    try:
        login_button.destroy()
        confirm_password.destroy()
        signup_button.destroy()
    except:
        try:
            confirm_password.destroy()
            signup_button.destroy()
        except:
            pass

    confirm_password = ctk.CTkEntry(frame, placeholder_text="Confirm Password", fg_color="#1f1f1f", show="*", font=("Helvetica", h/90, "bold"), height=40, width=200)
    confirm_password.pack(pady=12, padx=10)

    show_password.configure(command=lambda: show_pass([password, confirm_password]))

    signup_button = ctk.CTkButton(frame, text="Sign Up", text_color="#121212", fg_color="#9a4cfa", hover_color="#b87bff", font=("Helvetica", 13, "bold"), cursor="hand2", command=sign_up)
    signup_button.pack(pady=12, padx=10)

    return_key_bind = win.bind("<Return>", lambda event: sign_up())

# Login Button Function
def login():

    global pass_notification, account_loc

    if (username.get() != "") and (password.get() != ""):

        user = username.get()
        passw = password.get()

        # Kind of useless (Basically useless) since App opens immediately after login
        try:
            if PasswordHasher().verify(keyring.get_password(SERVICE_NAME, user), passw): text = "Login Successful!"; color = "#21c065"; x = 90
        except:
            text = "Username or Password is Incorrect."; color = "red"; x = 92

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Helvetica", 10, "bold"), text_color=color, height=0, width=300)
        pass_notification.place(x=x, y=212)

        frame.after(5000, pass_notification.destroy)

        if text == "Login Successful!":
            account_loc = os.path.join(data_loc, "Accounts", user)
            
            os.makedirs(account_loc, exist_ok=True)

            book_collection(user)

    else:

        if username.get() == "": text = "You have a Username right?"; x = 92
        else: text = "I believe you forgot the Password"; x = 91

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Helvetica", 10, "bold"), text_color="red", height=0, width=300)
        pass_notification.place(x=x, y=212)

        frame.after(5000, pass_notification.destroy)

# Signup Button Function
def sign_up(username_taken = False):
    
    global pass_notification
    
    if (password.get() == confirm_password.get()) and (password.get() != "" and confirm_password.get() != "" and username.get() != "") and (not username_taken):

        user = username.get()
        passw = PasswordHasher().hash(password.get())

        # Use Keyring to use OS Token Authentication and store passwords securely if Username is not taken
        if not keyring.get_password(SERVICE_NAME, user):

            keyring.set_password(SERVICE_NAME, user, passw)

            Users = keyring.get_password(SERVICE_NAME, "Users")
            if Users:
                Users = Users.split("\n")
            else:
                Users = []
            keyring.set_password(SERVICE_NAME, "Users", "\n".join(Users + [user]))

            pass_notification = ctk.CTkLabel(frame, text="Registered Successfully", font=("Helvetica", 10, "bold"), text_color="#21c065", height=0, width=300)
            pass_notification.place(x=89, y=276)

            frame.after(5000, pass_notification.destroy)

        else:
            
            username_taken = True
            sign_up(username_taken)

        if not username_taken:
            os.makedirs(os.path.join(data_loc, "Accounts", user), exist_ok=True)

    else:

        if username.get() == "": text = "Don't you need a Username?"; x = 140
        elif (password.get() == "") and (confirm_password.get() == ""): text = "Trust Me. You need a Password"; x = 140
        elif password.get() != confirm_password.get(): text = "The Passwords do not Match"; x = 140
        else: text = "Username is already taken"; x = 140

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Helvetica", 10, "bold"), text_color="red", height=0, width=200)
        pass_notification.place(x=x, y=276)

        frame.after(5000, pass_notification.destroy)


# -------------- Main App Functions -------------- #

# --> Quit Functions

# Quit Application
def quit_application(event):
    win.destroy()

# Quit Add Book Section
def quit_add_books(frame, widgets):

    # In case there are no Saved Widgets; In the case User is accessing a Saved Book
    if saved_widgets:
        saved_widgets[0].configure(state="disabled")

    win.unbind("<Motion>")
    for widget in frame.winfo_children():
        widget.destroy()

    size = 0.8
    while size >= 0:
        frame.place_configure(relwidth=size, relheight=size)
        
        win.update()
        sleep(0.001)

        size -= 0.04

    size=0
    frame.place_configure(relwidth=size, relheight=size)

    frame.destroy()
    win.unbind("<Escape>")

    # Enabling Widgets on closing Search Window
    widgets[0].configure(state="normal")
    widgets[1].configure(state="normal", fg_color="#9a4cfa")
    widgets[2].configure(state="normal")
    for widget in widgets[0].tab(widgets[0].get()).winfo_children():
        try:
            if ("label" not in str(widget)) and (widget.cget("text") in ["◀", "▶"]):
                widget.configure(state="normal", fg_color="#9a4cfa")
            else:
                widget.configure(state="normal")
        except:
            pass
    win.bind("<Escape>", quit_application)

# Quit Logout Confirmation
def quit_logout_confirmation(logout_confirmation, widgets):

    logout_confirmation.destroy()
    win.unbind("<Escape>")

    # Enabling Widgets on closing Search Window
    widgets[0].configure(state="normal")
    widgets[1].configure(state="normal", fg_color="#9a4cfa")
    widgets[2].configure(state="normal")
    for widget in widgets[0].tab(widgets[0].get()).winfo_children():
        if ("label" not in str(widget)) and (widget.cget("text") in ["◀", "▶"]):
            widget.configure(state="normal", fg_color="#9a4cfa")
        else:
            widget.configure(state="normal")
    win.bind("<Escape>", quit_application)

# --> Other Functions

# Create Rounded Corners for a given Image
def create_rounded_image(image_path, radius):
    img = Image.open(image_path).convert("RGBA")
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

    alpha = Image.new('L', img.size, 255)
    w, h = img.size

    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))

    img.putalpha(alpha)
    return img

# Open Saved Book Details
def open_book_details(widgets, search_term, books, book_num):

    # Get the specified Book and make a separate Dictionary
    book = {}
    for content_title in books.keys():
        book[content_title] = books[content_title][book_num]

    add_book(widgets, collection_search_term=search_term, book=book, search=False)

# User Book Collection
def book_collection(user):
    global update_tab

    # Execute Frame Destroy only if it isn't an Auto-Login
    if not keyring.get_password(SERVICE_NAME, "Auto-Login"):
        # Set up Default Auto-Login
        keyring.set_password(SERVICE_NAME, f"Auto-Login", user)
        frame.destroy()
    
    win.unbind("<Return>")

    center(win, (w, h), 2)
    win.title("Application")
    win.attributes("-fullscreen", True)
    win.geometry(f"{w}x{h}+0+0")

    # Main App Frame
    main_frame = ctk.CTkFrame(win, fg_color="#121212")
    main_frame.pack(fill="both", expand=True)

    # Add/Update Buttons to Tab
    def update_tab(widgets, search_term=None):

        category = tabs.get()

        if category != "Stats":

            filter_search.place(relx=0.5, rely=0.11, relwidth=0.45, relheight=0.06, anchor=ctk.CENTER)

            for widget in tabs.tab(category).winfo_children():
                if ("button" in str(widget)) and (widget.cget("text") not in ["◀", "▶"]):
                    widget.destroy()

            if (search_term) and (search_term.get() != "Enter Name or ISBN No. of the Book..."):
                books = read_data(account_loc, category, int(page_counters[category].get()), search_term.get())
            else:
                books = read_data(account_loc, category, int(page_counters[category].get()))

            for book_num in range(len(books.get("id", ""))):

                image = create_rounded_image(io.BytesIO(books["thumbnail"][book_num]), 35)

                btn = ctk.CTkButton(tabs.tab(category), text=books["title"][book_num][:home_page_cap], fg_color="#1f1f1f", hover_color="#9a4cfa", border_color="#9a4cfa", border_width=2, image=ctk.CTkImage(dark_image=image, size=(150, 115)), compound=ctk.LEFT, anchor="w", corner_radius=15, command=lambda search_term=search_term, book_num=book_num: open_book_details(widgets, search_term, books, book_num))
                btn.configure(font=("Helvetica", h/32, "bold"))
                btn._text_label.configure(padx=20)
                btn.bind("<Enter>", lambda event, btn=btn, book_num=book_num: start_marquee(True, btn, books["title"][book_num]+"      ", speed=150))
                btn.bind("<Leave>", lambda event, btn=btn, book_num=book_num: stop_marquee(True, btn, books["title"][book_num]))
                
                if book_num == 0:
                    btn.place(relx=0.02, rely=0.1, relwidth=0.958, relheight=0.145)
                else:
                    btn.place(in_=prev_widget, relx=0, rely=1.1, relwidth=1, relheight=1)

                if (search_term) and (search_term.get() != "Enter Name or ISBN No. of the Book..."):
                    total_pages[category].set(str(get_total_pages(account_loc, category, search_term.get())))
                else:
                    total_pages[category].set(str(get_total_pages(account_loc, category, None)))

                prev_widget = btn

            win.update()

        else:

            filter_search.place_forget()

            for widget in tabs.tab(category).winfo_children():
                widget.destroy()

            # Stats to Display
            reading_stat = total_stats(account_loc, "Reading")
            completed_stat = total_stats(account_loc, "Completed")
            planned_stat = total_stats(account_loc, "Plan To Read")

            reading_frame = ctk.CTkFrame(tabs.tab(category), fg_color="#1f1f1f", corner_radius=h/108, border_width=h/540, border_color="#9a4cfa")
            reading_frame.place(relx=0.024, rely=0.1, relwidth=0.3, relheight=0.55)

            completed_frame = ctk.CTkFrame(tabs.tab(category), fg_color="#1f1f1f", corner_radius=h/108, border_width=h/540, border_color="#9a4cfa")
            completed_frame.place(in_=reading_frame, relx=1.09, rely=0, relwidth=1, relheight=1)

            planned_frame = ctk.CTkFrame(tabs.tab(category), fg_color="#1f1f1f", corner_radius=h/108, border_width=h/540, border_color="#9a4cfa")
            planned_frame.place(in_=completed_frame, relx=1.09, rely=0, relwidth=1, relheight=1)

            longest_completed_book = longest_completed(account_loc)

            if longest_completed_book:

                image = create_rounded_image(io.BytesIO(longest_completed_book["thumbnail"][0]), 35)

                btn = ctk.CTkButton(tabs.tab(category), text=longest_completed_book["title"][0][:home_page_cap], fg_color="#1f1f1f", hover_color="#9a4cfa", border_color="#9a4cfa", border_width=2, image=ctk.CTkImage(dark_image=image, size=(150, 115)), compound=ctk.LEFT, anchor="w", corner_radius=h/108, command=lambda search_term=search_term: open_book_details(widgets, search_term, longest_completed_book, 0))
                btn.configure(font=("Helvetica", h/32, "bold"))
                btn._text_label.configure(padx=20)
                btn.bind("<Enter>", lambda event, btn=btn: start_marquee(True, btn, longest_completed_book["title"][0]+"      ", speed=150))
                btn.bind("<Leave>", lambda event, btn=btn: stop_marquee(True, btn, longest_completed_book["title"][0]))

                btn.place(relx=0.5, rely=0.78, relwidth=0.958, relheight=0.145, anchor=ctk.CENTER)

            else:

                info = ctk.CTkLabel(tabs.tab(category), text="No Completed Books Yet", font=("Helvetica", h/18, "bold"), text_color="#818181")
                info.place(relx=0.5, rely=0.77, relwidth=0.958, relheight=0.145, anchor=ctk.CENTER)

    # Change Page
    def page_change(change_qty):
        category = tabs.get()

        page_var = page_counters[category]
        new_page_count = int(page_var.get()) + change_qty

        if not ((new_page_count == 0) or (new_page_count > int(total_pages[category].get()))):
            page_var.set(new_page_count)

        update_tab([tabs, add_btn, logout_btn])

    # Create Tabular View
    tabs = ctk.CTkTabview(main_frame,
                        corner_radius=h/108,
                        border_width=h/540,
                        fg_color="#1f1f1f",
                        border_color="#9a4cfa",
                        segmented_button_fg_color="#1f1f1f",
                        segmented_button_selected_color="#9a4cfa",
                        segmented_button_unselected_color="#2a2a2a",
                        segmented_button_selected_hover_color="#b87bff",
                        segmented_button_unselected_hover_color="#393939",
                        command=lambda: update_tab([tabs, add_btn, logout_btn], search_term))
    tabs._segmented_button.configure(font=("Helvetica", h/45, "bold"))
    tabs.pack(padx=w/32, pady=h/54, fill="both", expand=True)

    # Add tabs
    tabs.add("Plan To Read")
    tabs.add("Reading")
    tabs.add("Completed")
    tabs.add("On Hold")
    tabs.add("Dropped")
    tabs.add("Stats")

    all_tabs = ["Plan To Read", "Reading", "Completed", "On Hold", "Dropped"]

    # Setting Up default Page Count and Total Pages for each tab
    page_counters = {tab_name:ctk.StringVar(value="1") for tab_name in all_tabs}
    total_pages = {tab_name:ctk.StringVar(value="1") for tab_name in all_tabs}

    # Add Previous/Next Buttons and Page Counter
    for tab in all_tabs:
        previous_button = ctk.CTkButton(tabs.tab(tab), text="◀", fg_color="#9a4cfa", bg_color="#1f1f1f", hover_color="#b87bff", font=("Helvetica", h/36, "bold"), text_color="#121212", command=lambda: page_change(-1))
        previous_button.place(relx=0.424, rely=0.942, relwidth=0.02)

        page_text_info = ctk.CTkLabel(tabs.tab(tab), text="Page          of ", font=("Helvetica", h/50), text_color="#9a4cfa")
        page_text_info.place(in_=previous_button, relx=1.4, rely=0.1)

        page_counter = ctk.CTkLabel(tabs.tab(tab), textvariable=page_counters[tab], font=("Helvetica", h/50), text_color="#9a4cfa")
        page_counter.place(in_=page_text_info, relx=0.38, rely=0, relwidth=0.4, relheight=1)

        total_pages_counter = ctk.CTkLabel(tabs.tab(tab), textvariable=total_pages[tab], font=("Helvetica", h/50), text_color="#9a4cfa")
        total_pages_counter.place(in_=page_text_info, relx=1, rely=0, relwidth=0.4, relheight=1)

        next_button = ctk.CTkButton(tabs.tab(tab), text="▶", fg_color="#9a4cfa", bg_color="#1f1f1f", hover_color="#b87bff", font=("Helvetica", h/36, "bold"), text_color="#121212", command=lambda: page_change(1))
        next_button.place(in_=previous_button, relx=7.65, rely=0, relwidth=1, relheight=1)

    # Set Default Tab to Reading
    tabs.set("Reading")

    # String Variable that keeps track of the Text in the Search Bar
    search_term = ctk.StringVar()
    search_term.trace_add('write', lambda var, index, mode: update_tab([tabs, add_btn, logout_btn], search_term=search_term))

    # Search Bar to Filter Books through Keywords
    filter_search = ctk.CTkEntry(main_frame, text_color="#818181", fg_color="#1f1f1f", font=("Helvetica", h/42, "bold"), textvariable=search_term)
    filter_search.place(relx=0.5, rely=0.11, relwidth=0.45, relheight=0.06, anchor=ctk.CENTER)

    # Reset Search Bar and open Search Menu
    def add_book_initiator():
        #search_term.set("")  # Clear Search Term
        add_book([tabs, add_btn, logout_btn], collection_search_term=search_term)

    # Log Out Confirmation and Execution
    def logout(widgets):
        
        win.unbind("<Escape>")

        # Disabling Widgets to avoid complications
        widgets[0].configure(state="disabled")
        widgets[1].configure(state="disabled", fg_color="#3a3a3a", text_color_disabled="#777777")
        widgets[2].configure(state="disabled")
        for widget in widgets[0].tab(widgets[0].get()).winfo_children():
            if ("label" not in str(widget)) and (widget.cget("text") in ["◀", "▶"]):
                widget.configure(state="disabled", fg_color="#3a3a3a", text_color_disabled="#777777")
            else:
                widget.configure(state="disabled")

        logout_confirmation = ctk.CTkFrame(win, bg_color="#1f1f1f", fg_color="#0f0f0f", corner_radius=h/45)
        logout_confirmation.place(relx=0.5, rely=0.49, relheight=0.15, relwidth=0.25, anchor=ctk.CENTER)

        def escape_function(logout_confirmation):
            quit_logout_confirmation(logout_confirmation, widgets)
            update_tab(widgets)

        def return_to_login():
            quit_logout_confirmation(logout_confirmation, widgets)
            main_frame.destroy()
            win.attributes("-fullscreen", False)
            keyring.delete_password(SERVICE_NAME, "Auto-Login")
            login_page(True)

        win.bind("<Escape>", lambda event, logout_confirmation=logout_confirmation: escape_function(logout_confirmation))

        prompt_question = ctk.CTkLabel(logout_confirmation, text="Are you sure you want to Log Out?", font=("Helvetica", h/54, "bold"), fg_color="#0f0f0f")
        prompt_question.pack(pady=(30, 0))

        prompt_yes = ctk.CTkButton(logout_confirmation, text="Yes", text_color="#121212", fg_color="#9a4cfa", hover_color="#b87bff", font=("Helvetica", h/67.5, "bold"), command=return_to_login)
        prompt_yes.pack(side="left", padx=(50,0), pady=(5, 0))

        prompt_no = ctk.CTkButton(logout_confirmation, text="No", text_color="#121212", fg_color="#9a4cfa", hover_color="#b87bff", font=("Helvetica", h/67.5, "bold"), command=lambda logout_confirmation=logout_confirmation: escape_function(logout_confirmation))
        prompt_no.pack(side="right", padx=(0,50), pady=(5, 0))

    # Button to open Search for Adding or Removing Books
    add_btn = ctk.CTkButton(main_frame, text="+", text_color="#121212", fg_color="#9a4cfa", bg_color="#1f1f1f", hover_color="#b87bff", font=("Helvetica", h/24, "bold"), width=w/24, height=h/13.5, corner_radius=h/36, command=add_book_initiator)
    add_btn.place(relx=0.91, rely=0.895)

    # Log Out Button
    logout_btn = ctk.CTkButton(main_frame, text="", text_color="#121212", fg_color="#1f1f1f", bg_color="#1f1f1f", hover_color="#2f2f2f", font=("Helvetica", h/24, "bold"), image=ctk.CTkImage(dark_image=Image.open(os.path.join(data_loc, "Images", "Log Out.png")), size=(30,30)), width=0, height=15, command=lambda: logout([tabs, add_btn, logout_btn]))
    logout_btn.place(relx=0.933, rely=0.045)

    search_term.set("Enter Name or ISBN No. of the Book...")
    filter_search.bind("<FocusIn>", lambda event: [filter_search.configure(text_color="#FFFFFF"), search_term.set("")])

    win.update()

    update_tab([tabs, add_btn, logout_btn])

# Add New Books
def add_book(widgets, collection_search_term=None, book=None, search=True):
    global saved_widgets, search_bar

    win.unbind("<Escape>")

    # Disabling Widgets to avoid complications
    widgets[0].configure(state="disabled")
    widgets[1].configure(state="disabled", fg_color="#3a3a3a", text_color_disabled="#777777")
    widgets[2].configure(state="disabled")
    for widget in widgets[0].tab(widgets[0].get()).winfo_children():
        try: 
            if ("label" not in str(widget)) and (widget.cget("text") in ["◀", "▶"]):
                widget.configure(state="disabled", fg_color="#3a3a3a", text_color_disabled="#777777")
            else:
                widget.configure(state="disabled")
        except:
            pass

    search_frame = ctk.CTkFrame(win, bg_color="#1f1f1f", fg_color="#0f0f0f", corner_radius=h/27)
    search_frame.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.1, anchor=ctk.CENTER)

    size = 0
    while size <= 0.8:
        search_frame.place_configure(relwidth=size, relheight=size)
        
        win.update()
        sleep(0.008)

        size += 0.06

    size=0.8
    search_frame.place_configure(relwidth=size, relheight=size)

    def escape_function(search_frame, collection_search_term):
        quit_add_books(search_frame, widgets)
        update_tab(widgets, collection_search_term)

    win.bind("<Escape>", lambda event, search_frame=search_frame, collection_search_term=collection_search_term: escape_function(search_frame, collection_search_term))

    if search:
        # String Variable that keeps track of the Text in the search_bar
        search_term = ctk.StringVar()
        search_term.trace_add('write', lambda var, index, mode: run_thread(search_frame, search_term))

        # Search Bar has no Placeholder Text since Textvariable used, a bug in CustomTkinter
        search_bar = ctk.CTkEntry(search_frame, text_color="#818181", fg_color="#1f1f1f", textvariable=search_term)
        search_bar.place(relx=0.48, rely=0.1, relwidth=0.45, relheight=0.06, anchor=ctk.CENTER)

        search_term.set("Enter Name or ISBN No. of the Book...")
        search_bar.bind("<FocusIn>", lambda event: [search_bar.configure(text_color="#FFFFFF"), search_term.set("")])

        saved_widgets = [search_bar]

    else:
        saved_widgets = None
        
        win.after(100, lambda: get_book(search_frame, book))

# Run threads to run searches
def run_thread(search_frame, search_term):

    if search_term.get() != "Enter Name or ISBN No. of the Book...":
        thread = threading.Thread(target=lambda: update_search(search_frame, search_term))
        thread.start()

# Remove outdated recommendations from screen
def kill_recommendation(recommendation, search_term, search_text):

    def check_and_destroy():
        if search_text != search_term.get():
            recommendation.destroy()

        win.after(100, check_and_destroy)

    check_and_destroy()

# Fetch Book Recommendations based on Search Term
def update_search(search_frame, search_term):

    search_text = search_term.get()

    time.sleep(0.5)

    if (search_term.get() != search_text) or (len(search_term.get()) == 0):
        return

    recommendations = get_book_details(search_text)

    list_of_recommendations = []
    def load_recommendation(book):

        with urllib.request.urlopen(book["thumbnail"]) as u:
            raw_data = u.read()

        image = create_rounded_image(io.BytesIO(raw_data), 35)

        recommendation = ctk.CTkButton(search_frame, text=book["title"][:search_page_cap], font=("Helvetica", h/65, "bold"), image=ctk.CTkImage(dark_image=image, size=(w/8.53, h/4.32)), fg_color="#0f0f0f", hover_color="#1f1f1f", compound=ctk.TOP, anchor="w", width=w/8.53 + 25, height=h/4.32 + 65, command=lambda book=book: get_book(search_frame, book, search_term))
        recommendation.bind("<Enter>", lambda event, recommendation=recommendation: start_marquee(False, recommendation, book["title"]+"      ", speed=150))
        recommendation.bind("<Leave>", lambda event, recommendation=recommendation: stop_marquee(False, recommendation, book["title"]))
        try:
            thread = threading.Thread(target=lambda search_text=search_text: kill_recommendation(recommendation, search_term, search_text))
            thread.start()

            list_of_recommendations.append(recommendation)

        except:
            pass

    threads = []

    for book in recommendations:
        thread = threading.Thread(target=lambda book=book: load_recommendation(book))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    win.unbind("<Motion>")

    for widget in search_frame.winfo_children():
        if "ctklabel" in str(widget):
            widget.destroy()
    
    iteration = 0
    relative_y = 0.2

    try:
        for recommendation in list_of_recommendations:

            if iteration % 5 == 0:
                recommendation.place(in_=search_frame, relx=0.03, rely=relative_y, relwidth=0.16, relheight=0.35)
                relative_y = 0.6
            else:
                recommendation.place(in_=prev_recommendation, relx=1.2, rely=0, relwidth=1, relheight=1)

            prev_recommendation = recommendation
            iteration += 1
    except:
        pass

# Fetch Book Details
def get_book(search_frame, book, search_term=None):

    # To check whether this function is being used by the Search Method or just to see a Saved Book
    if search_term:
        search_term.set("")

        with urllib.request.urlopen(book["thumbnail"]) as u:
            raw_data = u.read()
    else:
        raw_data = book["thumbnail"]

    image = Image.open(io.BytesIO(raw_data)).convert('RGB')
    image_enhancer = ImageEnhance.Brightness(image)
    enhanced_image = image_enhancer.enhance(1)

    for widget in search_frame.winfo_children():
        if widget not in saved_widgets:
            widget.destroy()
    
    bg = ctk.CTkLabel(search_frame, text="", fg_color="#0f0f0f")
    
    # To check whether this function is being used by the Search Method or just to see a Saved Book. Place everything slightly higher in absence of the Search Bar
    if search_term:
        bg.place(relx=0.05, rely=0.25, relwidth=0.2, relheight=0.5)
    else:
        bg.place(relx=0.05, rely=0.2, relwidth=0.2, relheight=0.5)

    image = ctk.CTkLabel(search_frame, text="", image=ctk.CTkImage(dark_image=enhanced_image, size=(search_frame.winfo_width()/100 * 20, search_frame.winfo_height()/100 * 50)))
    image.place(in_=bg, relx=0, rely=0, relwidth=1, relheight=1)

    details_order = {"title":"Title", "authors":"Author(s)", "language":"Language", "isbn10":"ISBN-10", "isbn13":"ISBN-13", "publisher":"Publisher", "publish_date":"Publish Date", "categories": "Categories", "page_count":"Pages", "description":"Description", "maturity_rating":"Maturity Rating"}

    # Filling Book Details
    text = ""

    for heading in details_order.keys():
        heading_content = book[heading]
        if heading_content != "":
            text += f"{details_order[heading]}: {heading_content}\n\n"

    text_widget = ctk.CTkTextbox(search_frame, font=("Helvetica", h/67.5, "bold"), fg_color="#0f0f0f", wrap=ctk.WORD)
    text_widget.insert(ctk.END, text)
    text_widget.configure(state=ctk.DISABLED)
    text_widget.place(in_=bg, relx=1.2, rely=0, relheight=1.4, relwidth=3.2)

    # Display Buttons if hovering over the Image
    def check_hover(event):
        if (win.winfo_pointerx() > bg.winfo_rootx()) and (win.winfo_pointerx() < bg.winfo_rootx()+bg.winfo_width()) and (win.winfo_pointery() > bg.winfo_rooty()) and (win.winfo_pointery() < bg.winfo_rooty()+bg.winfo_height()):
            enhanced_image = image_enhancer.enhance(0.5)
            image.configure(image=ctk.CTkImage(dark_image=enhanced_image, size=(search_frame.winfo_width()/100 * 20, search_frame.winfo_height()/100 * 50)))

            new_properties = False

            prev_widget = bg
            for widget in place_order:
                if not new_properties: widget.place(in_=prev_widget, relx=0.2, rely=0.12, relheight=0.1, relwidth=0.6)
                else: widget.place(in_=prev_widget, relx=0, rely=1.35, relheight=1, relwidth=1)
                prev_widget = widget
                new_properties = True
        
        else:
            
            for widget in place_order:
                widget.place_forget()
            
            enhanced_image = image_enhancer.enhance(1)
            image.configure(image=ctk.CTkImage(dark_image=enhanced_image, size=(search_frame.winfo_width()/100 * 20, search_frame.winfo_height()/100 * 50)))

    # Perform Actions based on Button Pressed
    def button_action(btn, var):
        
        btn.configure(state="disabled")

        book["thumbnail"] = raw_data
        
        btn_text = var.get()
        track_book(account_loc, book, btn_text)

        var.set("✔")
        win.after(500, lambda: var.set(btn_text))

        win.after(500, lambda: btn.configure(state="normal"))

    # Buttons Displayed on Hovering and Add Book to SQL Database
    book_plan_var = ctk.StringVar(value="Plan To Read")
    book_reading_var = ctk.StringVar(value="Reading")
    book_completed_var = ctk.StringVar(value="Completed")
    book_hold_var = ctk.StringVar(value="On Hold")
    book_dropped_var = ctk.StringVar(value="Dropped")
    book_remove_var = ctk.StringVar(value="Remove From List")

    book_plan_btn = ctk.CTkButton(search_frame, textvariable=book_plan_var, font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0, command=lambda: button_action(book_plan_btn, book_plan_var))
    book_reading_btn = ctk.CTkButton(search_frame, textvariable=book_reading_var, font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0, command=lambda: button_action(book_reading_btn, book_reading_var))
    book_completed_btn = ctk.CTkButton(search_frame, textvariable=book_completed_var, font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0, command=lambda: button_action(book_completed_btn, book_completed_var))
    book_hold_btn = ctk.CTkButton(search_frame, textvariable=book_hold_var, font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0, command=lambda: button_action(book_hold_btn, book_hold_var))
    book_dropped_btn = ctk.CTkButton(search_frame, textvariable=book_dropped_var, font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0, command=lambda: button_action(book_dropped_btn, book_dropped_var))
    book_remove_btn = ctk.CTkButton(search_frame, textvariable=book_remove_var, font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0, command=lambda: button_action(book_remove_btn, book_remove_var))

    place_order = [book_plan_btn, book_reading_btn, book_completed_btn, book_hold_btn, book_dropped_btn, book_remove_btn]

    win.bind("<Motion>", check_hover)

def main():
    global account_loc

    win.resizable(False, False)
    
    if not keyring.get_password(SERVICE_NAME, "Auto-Login"):
        login_page(True)
    else:
        user = keyring.get_password(SERVICE_NAME, "Auto-Login")
        account_loc = os.path.join(data_loc, "Accounts", user)
        book_collection(user)

    win.bind("<Escape>", quit_application)

    win.mainloop()

if __name__ == "__main__":
    
    main()