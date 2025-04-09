import customtkinter as ctk
from time import sleep
import json
import hashlib
import os
import io
import urllib.request
import threading
import time
from PIL import Image, ImageEnhance
from Book_Scouter import get_book_details
from Book_Data import track_book

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

data_loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data")
database_loc = os.path.join(data_loc, "Account Data Base.json")

win = ctk.CTk(fg_color="#121212")
win.title("Login")
win.geometry("0x0")

w = win.winfo_screenwidth()
h = win.winfo_screenheight()

"""w=1280
h=720"""

# Quit Application
def quit_application(event):
    win.destroy()

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


    x1 = screen_resolution[0]
    y1 = screen_resolution[1]

    win.geometry(f"{int(x1)}x{int(y1)}")

    x2 = w//2 - win.winfo_width()//2
    y2 = h//2 - win.winfo_height()//2

    win.geometry(f"+{x2}+{y2}")

    win.update()


# Login and Sign Up Functions

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

        center(win, (600, 400), 2)

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
        
        username = ctk.CTkEntry(frame, placeholder_text="Username", fg_color="#1f1f1f", show="", height=40, width=200)
        username.pack(pady=(50, 12), padx=10)

        check_var = ctk.StringVar()
        check_var.set("*")

        password = ctk.CTkEntry(frame, placeholder_text="Password", fg_color="#1f1f1f", show="*", height=40, width=200)
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

    confirm_password = ctk.CTkEntry(frame, placeholder_text="Confirm Password", fg_color="#1f1f1f", show="*", height=40, width=200)
    confirm_password.pack(pady=12, padx=10)

    show_password.configure(command=lambda: show_pass([password, confirm_password]))

    signup_button = ctk.CTkButton(frame, text="Sign Up", text_color="#121212", fg_color="#9a4cfa", hover_color="#b87bff", font=("Helvetica", 13, "bold"), cursor="hand2", command=sign_up)
    signup_button.pack(pady=12, padx=10)

    return_key_bind = win.bind("<Return>", lambda event: sign_up())

# Login Button Function
def login():

    global pass_notification, account_loc

    try:

        with open(database_loc, "r") as f:

            database = json.load(f)

    except:

        database = ""

    if (username.get() != "") and (password.get() != ""):

        user = username.get()
        passw = hashlib.sha256(password.get().encode()).hexdigest()

        # Kind of useless (Basically useless) since App opens immediately after login
        if (user in database) and (database[user] == passw): text = "Login Successful!"; color = "#21c065"; x = 90
        else: text = "Username or Password is Incorrect."; color = "red"; x = 92

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Helvetica", 10, "bold"), text_color=color, height=0, width=300)
        pass_notification.place(x=x, y=212)

        frame.after(5000, pass_notification.destroy)

        if text == "Login Successful!":
            account_loc = os.path.join(data_loc, "Accounts", user)
            
            os.makedirs(account_loc, exist_ok=True)
            
            book_collection()

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
        passw = hashlib.sha256(password.get().encode()).hexdigest()

        if not os.path.exists(database_loc): 
            
            with open(database_loc, 'w+') as f: pass

        with open(database_loc, "r") as f:
            
            try: database = json.load(f)
            except: database = ""
        
        if database == "":
            
            dict = {user: passw}

            with open(database_loc, "w+") as f: json.dump(dict, f, indent=4)

            pass_notification = ctk.CTkLabel(frame, text="Registered Successfully", font=("Helvetica", 10, "bold"), text_color="#21c065", height=0, width=300)
            pass_notification.place(x=89, y=276)

            frame.after(5000, pass_notification.destroy)

        elif user not in database:

            dict = database
            dict[user] = passw

            with open(database_loc, "w+") as f: json.dump(dict, f, indent=4)

            pass_notification = ctk.CTkLabel(frame, text="Registered Successfully", font=("Helvetica", 10, "bold"), text_color="#21c065", height=0, width=300)
            pass_notification.place(x=89, y=276)

            frame.after(5000, pass_notification.destroy)

        else:

            username_taken = True
            sign_up(username_taken)

        if not username_taken:
            os.makedirs(f"{data_loc}\\Accounts\\{user}", exist_ok=True)

    else:

        if username.get() == "": text = "Don't you need a Username?"; x = 140
        elif (password.get() == "") and (confirm_password.get() == ""): text = "Trust Me. You need a Password"; x = 140
        elif password.get() != confirm_password.get(): text = "The Passwords do not Match"; x = 140
        else: text = "Username is already taken"; x = 140

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Helvetica", 10, "bold"), text_color="red", height=0, width=200)
        pass_notification.place(x=x, y=276)

        frame.after(5000, pass_notification.destroy)

# Book Collection
def book_collection():

    frame.destroy()
    win.unbind("<Return>")

    center(win, (w, h), 2)
    win.attributes("-fullscreen", True)

    # Main App Frame
    main_frame = ctk.CTkFrame(win, fg_color="#121212")
    main_frame.pack(fill="both", expand=True)

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
                        segmented_button_unselected_hover_color="#393939"
                        )
    tabs._segmented_button.configure(font=("Segoe UI", h/45, "bold"))
    tabs.pack(padx=w/32, pady=h/54, fill="both", expand=True)

    # Add tabs
    tabs.add("Plan To Read")
    tabs.add("Reading")
    tabs.add("Completed")
    tabs.add("On Hold")
    tabs.add("Dropped")

    add_btn = ctk.CTkButton(main_frame, text="+", text_color="#121212", fg_color="#9a4cfa", bg_color="#1f1f1f", hover_color="#b87bff", font=("Helvetica", h/24, "bold"), width=w/24, height=h/13.5, corner_radius=h/36, command=lambda: add_book(add_btn))
    add_btn.place(relx=0.919, rely=0.9)

# Quit Add Book Section
def quit_add_books(event, frame, buttons):

    saved_widgets[0].configure(state="disabled")

    win.unbind("<Motion>")
    for widget in frame.winfo_children():
        widget.destroy()

    size = 0.8
    while size >= 0.1:
        frame.place_configure(relwidth=size, relheight=size)
        
        win.update()
        sleep(0.001)

        size -= 0.12

    size=0.1
    frame.place_configure(relwidth=size, relheight=size)

    frame.destroy()
    win.unbind("<Escape>")
    for btn in buttons:
        btn.configure(state="normal", fg_color="#9a4cfa")
    win.bind("<Escape>", quit_application)

# Add New Books
def add_book(add_btn):
    global saved_widgets, search_bar

    win.unbind("<Escape>")
    add_btn.configure(state="disabled", fg_color="#3a3a3a", text_color_disabled="#777777")

    search_frame = ctk.CTkFrame(win, bg_color="#1f1f1f", fg_color="#0f0f0f", corner_radius=h/27)
    search_frame.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.1, anchor=ctk.CENTER)

    size = 0.1
    while size <= 0.8:
        search_frame.place_configure(relwidth=size, relheight=size)
        
        win.update()
        sleep(0.008)

        size += 0.12

    size=0.8
    search_frame.place_configure(relwidth=size, relheight=size)

    win.bind("<Escape>", lambda event, search_frame=search_frame: quit_add_books(event, search_frame, [add_btn]))

    search_term = ctk.StringVar()
    search_term.trace_add('write', lambda var, index, mode: run_thread(search_frame, search_term))

    search_bar = ctk.CTkEntry(search_frame, fg_color="#1f1f1f", placeholder_text="Enter ISBN No. or Name of the Book...", textvariable=search_term)
    search_bar.place(relx=0.48, rely=0.1, relwidth=0.45, relheight=0.06, anchor=ctk.CENTER)

    saved_widgets = [search_bar]

# Run threads to run searches
def run_thread(search_frame, search_term):

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

        image = Image.open(io.BytesIO(raw_data))
        
        recommendation = ctk.CTkButton(search_frame, image=ctk.CTkImage(dark_image=image, size=(w/8.53, h/4.32)), fg_color="#0f0f0f", hover_color="#1f1f1f", compound=ctk.TOP, text=book["title"], width=w/8.53 + 25, height=h/4.32 + 65, command=lambda book=book: get_book(search_frame, search_term, book))
        try:
            recommendation._text_label.configure(wraplength=150)
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
def get_book(search_frame, search_term, book):

    search_term.set("")

    with urllib.request.urlopen(book["thumbnail"]) as u:
        raw_data = u.read()

    image = Image.open(io.BytesIO(raw_data)).convert('RGB')
    image_enhancer = ImageEnhance.Brightness(image)
    enhanced_image = image_enhancer.enhance(1)

    for widget in search_frame.winfo_children():
        if widget not in saved_widgets:
            widget.destroy()
    
    bg = ctk.CTkLabel(search_frame, text="", fg_color="#0f0f0f")
    bg.place(relx=0.05, rely=0.25, relwidth=0.2, relheight=0.5)

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
        
        btn_text = var.get()
        track_book(account_loc, book, btn_text)

        var.set("✔")
        win.after(500, lambda: var.set(btn_text))

        win.after(500, lambda: btn.configure(state="normal"))

    # Buttons Displayed on Hovering and Add Book to SQL Database
    book_plan_var = ctk.StringVar(value="Plan to Read")
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

    win.resizable(False, False)
    
    login_page(True)

    win.bind("<Escape>", quit_application)

    win.mainloop()

if __name__ == "__main__":
    
    main()