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

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

win = ctk.CTk(fg_color="#121212")
win.title("Login")
win.geometry("0x0")

w = win.winfo_screenwidth()
h = win.winfo_screenheight()

"""w=1280
h=720"""

#Center Window Method

def center(win, screen_resolution, animation_time):

    x1, y1 = 0, 0

    while x1 != screen_resolution[0] or y1 != screen_resolution[1]:

        if x1 != screen_resolution[0]: x1 += screen_resolution[0]/(animation_time*10)
        if y1 != screen_resolution[1]: y1 += screen_resolution[1]/(animation_time*10)

        win.geometry(f"{int(x1)}x{int(y1)}")

        x2 = w//2 - win.winfo_width()//2
        y2 = h//2 - win.winfo_height()//2

        win.geometry(f"+{x2}+{y2}")

        sleep(0.008)
        win.update()

#Login and Sign Up Functions

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
        make_selector(136, 6)

    else:

        signup_page()
        make_selector(270, 7)

def show_pass(inputs):

    show = check_var.get()

    if show == "*":
        check_var.set("")
        show_password.configure(image=ctk.CTkImage(dark_image=Image.open(f"{data_loc}\\Images\\Eye Show.png"), size=(30,30)))
    else:
        check_var.set("*")
        show_password.configure(image=ctk.CTkImage(dark_image=Image.open(f"{data_loc}\\Images\\Eye Hide.png"), size=(30,30)))

    for input in inputs:
        input.configure(show=check_var.get())

def login_page(first_time):

    global frame, selector, username, password, check_var, show_password, login_button

    try:
        confirm_password.destroy()
        signup_button.destroy()
    except:
        try:
            login_button.destroy()
        except:
            pass

    if first_time:

        center(win, (600, 400), 2)

        frame = ctk.CTkFrame(win, fg_color="#1f1f1f")
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(frame, text="BOOKMARK", text_color="#bb86fc", font=("Roboto", 24, "bold"))
        label.pack(pady=12, padx=10)
    
    if first_time:

        selector = ctk.CTkLabel(frame, text="_____", text_color="#bb86fc", font=("Roboto", 24, "bold"))
        selector.place(x=136, y=55)

    login_switch_method = ctk.CTkButton(frame, text="LOGIN", text_color="#bb86fc", font=("Roboto", 16, "bold"), fg_color="#1f1f1f", hover_color="#1f1f1f", cursor="hand2", height=0, width=0, command=lambda: switch_method("login"))
    login_switch_method.place(x=136, y=50)

    sign_up_switch_method = ctk.CTkButton(frame, text="SIGN UP", text_color="#bb86fc", font=("Roboto", 16, "bold"), fg_color="#1f1f1f", hover_color="#1f1f1f", cursor="hand2", height=0, width=0, command=lambda: switch_method("sign_up"))
    sign_up_switch_method.place(x=270, y=50)

    if first_time:    
        
        username = ctk.CTkEntry(frame, placeholder_text="Username", fg_color="#1f1f1f", show="", height=40, width=200)
        username.pack(pady=(50, 12), padx=10)

        check_var = ctk.StringVar()
        check_var.set("*")

        password = ctk.CTkEntry(frame, placeholder_text="Password", fg_color="#1f1f1f", show="*", height=40, width=200)
        password.pack(pady=12, padx=10)

        show_password = ctk.CTkButton(frame, text="", fg_color="#1f1f1f", hover_color="#191919", image=ctk.CTkImage(dark_image=Image.open(f"{data_loc}\\Images\\Eye Hide.png"), size=(30,30)), width=30, height=30, command=lambda: show_pass([password]))
        show_password.place(x=345, y=168)

    else:

        show_password.configure(command=lambda: show_pass([password]))

    login_button = ctk.CTkButton(frame, text="Login", text_color="#121212", fg_color="#bb86fc", hover_color="#5704bc", font=("Roboto", 13, "bold"), cursor="hand2", command=login)
    login_button.pack(pady=12, padx=10)

    win.bind("<Return>", lambda event: login())

def signup_page():

    global confirm_password, signup_button, return_key_bind

    try:
        login_button.destroy()
    except:
        try:
            confirm_password.destroy()
            signup_button.destroy()
        except:
            pass

    confirm_password = ctk.CTkEntry(frame, placeholder_text="Confirm Password", fg_color="#1f1f1f", show="*", height=40, width=200)
    confirm_password.pack(pady=12, padx=10)

    show_password.configure(command=lambda: show_pass([password, confirm_password]))

    signup_button = ctk.CTkButton(frame, text="Sign Up", text_color="#121212", fg_color="#bb86fc", hover_color="#5704bc", font=("Roboto", 13, "bold"), cursor="hand2", command=sign_up)
    signup_button.pack(pady=12, padx=10)

    return_key_bind = win.bind("<Return>", lambda event: sign_up())

def login():

    global pass_notification, account

    try:

        with open(database_loc, "r") as f:

            database = json.load(f)

    except:

        database = ""

    if (username.get() != "") and (password.get() != ""):

        user = hashlib.sha256(username.get().encode()).hexdigest()
        passw = hashlib.sha256(password.get().encode()).hexdigest()

        if (user in database) and (database[user] == passw): text = "Login Successful!"; color = "green"; x = 90
        else: text = "Username or Password is incorrect."; color = "red"; x = 92

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Roboto", 10, "bold"), text_color=color, height=0, width=300)
        pass_notification.place(x=x, y=212)

        frame.after(5000, pass_notification.destroy)

        if text == "Login Successful!":
            path = f"{data_loc}\\Accounts\\{user}"
            
            os.makedirs(path, exist_ok=True)

            account = path
            
            book_collection()

    else:

        if username.get() == "": text = "You have a Username right?"; x = 92
        else: text = "I believe you forgot the Password"; x = 91

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Roboto", 10, "bold"), text_color="red", height=0, width=300)
        pass_notification.place(x=x, y=212)

        frame.after(5000, pass_notification.destroy)

def sign_up(username_taken = False):
    
    global pass_notification
    
    if (password.get() == confirm_password.get()) and (password.get() != "" and confirm_password.get() != "" and username.get() != "") and (not username_taken):

        user = hashlib.sha256(username.get().encode()).hexdigest()
        passw = hashlib.sha256(password.get().encode()).hexdigest()

        if not os.path.exists(database_loc): 
            
            with open(database_loc, 'w+') as f: pass

        with open(database_loc, "r") as f:
            
            try: database = json.load(f)
            except: database = ""
        
        if database == "":
            
            dict = {user: passw}

            with open(database_loc, "w+") as f: json.dump(dict, f, indent=4)

            pass_notification = ctk.CTkLabel(frame, text="Registered Successfully", font=("Roboto", 10, "bold"), text_color="green", height=0, width=300)
            pass_notification.place(x=89, y=276)

            frame.after(5000, pass_notification.destroy)

        elif user not in database:

            dict = database
            dict[user] = passw

            with open(database_loc, "w+") as f: json.dump(dict, f, indent=4)

            pass_notification = ctk.CTkLabel(frame, text="Registered Successfully", font=("Roboto", 10, "bold"), text_color="green", height=0, width=300)
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

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Roboto", 10, "bold"), text_color="red", height=0, width=200)
        pass_notification.place(x=x, y=276)

        frame.after(5000, pass_notification.destroy)

#Book Collection
        
def book_collection():

    frame.destroy()
    win.unbind("<Return>")

    center(win, (w, h), 2)
    win.attributes('-fullscreen', True)

    page = ctk.CTkFrame(win, fg_color="#1f1f1f")
    page.pack(pady=20, padx=60, fill="both", expand=True)

    add_btn = ctk.CTkButton(page, text="+", text_color="#121212", fg_color="#bb86fc", hover_color="#5704bc", font=("Roboto", 45, "bold"), width=80, height=80, corner_radius=30, command=lambda: add_book(add_btn))
    add_btn.pack(side=ctk.BOTTOM, anchor="e", padx=8, pady=8)

def add_book(add_btn):
    global saved_widgets, search_bar

    add_btn.configure(state="disabled", fg_color="#716876", text_color_disabled="#666666")

    search = ctk.CTkFrame(win, bg_color="#1f1f1f", fg_color="#0f0f0f", width=0.1*w, height=0.1*h, corner_radius=40)
    search.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    size = 0.1
    while size <= 0.8:
        search.configure(width=size*w, height=size*h)
        
        win.update()
        sleep(0.008)

        size += 0.04

    size=0.8
    search.configure(width=size*w, height=size*h)

    search_term = ctk.StringVar()
    search_term.trace_add('write', lambda var, index, mode: run_thread(search, search_term))

    search_bar = ctk.CTkEntry(search, fg_color="#1f1f1f", placeholder_text="Enter ISBN No. or Name of the Book...", textvariable=search_term)
    search_bar.place(relx=0.48, rely=0.1, relwidth=0.45, relheight=0.06, anchor=ctk.CENTER)
    
    search_button = ctk.CTkButton(search, fg_color="#2f2f2f", hover_color="#1f1f1f", text="", image=ctk.CTkImage(dark_image=Image.open(f"{data_loc}\\Images\\Search.png")), command=lambda: run_thread(search=search, isbn=search_bar))
    search_button.place(in_=search_bar, relx=1.04, rely=0.5, relwidth=0.08, relheight=1, anchor=ctk.CENTER)

    saved_widgets = [search_bar, search_button]

def run_thread(search, search_term):

    thread = threading.Thread(target=lambda: update_search(search, search_term))
    thread.start()

def kill_recommendation(recommendation, search_term, search_text):

    while True:
        time.sleep(0.1)
        if search_text != search_term.get():
            recommendation.destroy()
            return

def update_search(search, search_term):

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
        
        recommendation = ctk.CTkButton(search, image=ctk.CTkImage(dark_image=image, size=(w/8.53, h/4.32)), fg_color="#0f0f0f", hover_color="#1f1f1f", compound=ctk.TOP, text=book["title"], width=w/8.53 + 25, height=h/4.32 + 65, command=lambda book=book: get_book(search, search_term, book))
        recommendation._text_label.configure(wraplength=150)
        thread = threading.Thread(target=lambda search_text=search_text: kill_recommendation(recommendation, search_term, search_text))
        thread.start()

        list_of_recommendations.append(recommendation)
    
    threads = []

    for book in recommendations:
        thread = threading.Thread(target=lambda book=book: load_recommendation(book))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    win.unbind("<Motion>")

    for widget in search.winfo_children():
        if "ctklabel" in str(widget):
            widget.destroy()
    
    iteration = 0
    relative_y = 0.2

    try:
        for recommendation in list_of_recommendations:

            if iteration % 5 == 0:
                recommendation.place(in_=search, relx=0.03, rely=relative_y, relwidth=0.16, relheight=0.35)
                relative_y = 0.6
            else:
                recommendation.place(in_=prev_recommendation, relx=1.2, rely=0, relwidth=1, relheight=1)

            prev_recommendation = recommendation
            iteration += 1
    except:
        pass

def get_book(search, search_term, book):

    search_term.set("")

    with urllib.request.urlopen(book["thumbnail"]) as u:
        raw_data = u.read()

    image = Image.open(io.BytesIO(raw_data)).convert('RGB')
    image_enhancer = ImageEnhance.Brightness(image)
    enhanced_image = image_enhancer.enhance(1)

    for widget in search.winfo_children():
        if widget not in saved_widgets:
            widget.destroy()
    
    bg = ctk.CTkLabel(search, text="", fg_color="#0f0f0f")
    bg.place(relx=0.05, rely=0.25, relwidth=0.2, relheight=0.5)

    image = ctk.CTkLabel(search, text="", image=ctk.CTkImage(dark_image=enhanced_image, size=(search.winfo_width()/100 * 20, search.winfo_height()/100 * 50)))
    image.place(in_=bg, relx=0, rely=0, relwidth=1, relheight=1)

    book_title = ctk.CTkLabel(search, text=f"Title: {book['title']}", justify="left", font=("Roboto", 16, "bold"), wraplength=search.winfo_width()-image.winfo_width()-((search.winfo_width()/100)*35))
    book_title.place(in_=image, relx=1.2, rely=0)

    order = {"authors":"Author(s)", "isbn10":"ISBN-10", "isbn13":"ISBN-13", "publisher":"Publisher", "publish_date":"Publish Date", "page_count":"Pages", "description":"Description", "maturity_rating":"Maturity Rating"}

    prev_widget = book_title
    for title in order:
        widget = ctk.CTkLabel(search, text=f"{order[title]}: {book[title]}",justify="left", font=("Roboto", 16, "bold"), wraplength=search.winfo_width()-image.winfo_width()-((search.winfo_width()/100)*35))
        widget.place(in_=prev_widget, relx=0, rely=1.2)

        prev_widget = widget

    def check_hover(event):
        if (win.winfo_pointerx() > bg.winfo_rootx()) and (win.winfo_pointerx() < bg.winfo_rootx()+bg.winfo_width()) and (win.winfo_pointery() > bg.winfo_rooty()) and (win.winfo_pointery() < bg.winfo_rooty()+bg.winfo_height()):
            enhanced_image = image_enhancer.enhance(0.5)
            image.configure(image=ctk.CTkImage(dark_image=enhanced_image, size=(search.winfo_width()/100 * 20, search.winfo_height()/100 * 50)))

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
            image.configure(image=ctk.CTkImage(dark_image=enhanced_image, size=(search.winfo_width()/100 * 20, search.winfo_height()/100 * 50)))

    book_plan = ctk.CTkButton(search, text="Plan To Read", font=("Roboto", 18, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0)
    book_reading = ctk.CTkButton(search, text="Reading", font=("Roboto", 18, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0)
    book_completed = ctk.CTkButton(search, text="Completed", font=("Roboto", 18, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0)
    book_hold = ctk.CTkButton(search, text="On Hold", font=("Roboto", 18, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0)
    book_dropped = ctk.CTkButton(search, text="Dropped", font=("Roboto", 18, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0)
    book_remove = ctk.CTkButton(search, text="Remove From List", font=("Roboto", 18, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=0)

    place_order = [book_plan, book_reading, book_completed, book_hold, book_dropped, book_remove]

    win.bind("<Motion>", check_hover)

def main():

    win.resizable(False, False)
    
    login_page(True)

    win.mainloop()

if __name__ == "__main__":

    data_loc = f"{os.path.dirname(os.path.realpath(__file__))}\\Data"
    database_loc = f"{data_loc}\\Account Data Base.json"
    
    main()