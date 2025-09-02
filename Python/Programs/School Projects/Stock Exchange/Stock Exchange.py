import os

try:
    import customtkinter as ctk
    from PIL import Image
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import webbrowser
    import validators
except:
    os.system("pip install customtkinter")
    os.system("pip install pillow")
    os.system("pip install matplotlib")
    os.system("pip install webbrowser")
    os.system("pip install validators")

    import customtkinter as ctk
    from PIL import Image
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import matplotlib.pyplot as plt
    import webbrowser
    import validators

from time import sleep
import json
import hashlib
import sys
import threading
import time
from mpl_finance import search_from_name, get_ticker_details, make_graph
from buy_sell import record_transaction, create_portfolio

ctk.deactivate_automatic_dpi_awareness()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

data_loc = f"{os.path.dirname(os.path.realpath(__file__))}\\Data"
database_loc = f"{data_loc}\\Account Data Base.json"

win = ctk.CTk(fg_color="#121212")
win.title("Login")
win.geometry("0x0")

w = win.winfo_screenwidth()
h = win.winfo_screenheight()

pos = [15]*7
sys.setrecursionlimit(1500)

# Quit Application
def quit_application(event):
    win.destroy()

# Quit Portfolio
def quit_portfolio(event, frame, buttons):

    frame.destroy()
    win.unbind("<Escape>")
    for btn in buttons:
        btn.configure(state="normal")
    win.bind("<Escape>", quit_application)

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
        make_selector(136, 6)

    else:

        signup_page()
        make_selector(270, 7)

# Show Password
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

        label = ctk.CTkLabel(frame, text="STOCK EXCHANGE", text_color="#9a4cfa", font=("Helvetica", 24, "bold"))
        label.pack(pady=12, padx=10)
    
    if first_time:

        selector = ctk.CTkLabel(frame, text="_____", text_color="#9a4cfa", font=("Helvetica", 24, "bold"))
        selector.place(x=136, y=55)

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

        show_password = ctk.CTkButton(frame, text="", fg_color="#1f1f1f", hover_color="#191919", image=ctk.CTkImage(dark_image=Image.open(f"{data_loc}\\Images\\Eye Hide.png"), size=(30,30)), width=30, height=30, command=lambda: show_pass([password]))
        show_password.place(x=345, y=168)

    else:

        show_password.configure(command=lambda: show_pass([password]))

    login_button = ctk.CTkButton(frame, text="Login", text_color="#121212", fg_color="#9a4cfa", hover_color="#4937D2", font=("Helvetica", 13, "bold"), cursor="hand2", command=login)
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

    signup_button = ctk.CTkButton(frame, text="Sign Up", text_color="#121212", fg_color="#9a4cfa", hover_color="#4937D2", font=("Helvetica", 13, "bold"), cursor="hand2", command=sign_up)
    signup_button.pack(pady=12, padx=10)

    return_key_bind = win.bind("<Return>", lambda event: sign_up())

# Login Button Function
def login():

    global user, pass_notification, account

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

        pass_notification = ctk.CTkLabel(frame, text=text, font=("Helvetica", 10, "bold"), text_color=color, height=0, width=300)
        pass_notification.place(x=x, y=212)

        frame.after(5000, pass_notification.destroy)

        if text == "Login Successful!":
            path = f"{data_loc}\\Accounts\\{user}"
            
            os.makedirs(path, exist_ok=True)

            account = path
            
            stock_collection()

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

            pass_notification = ctk.CTkLabel(frame, text="Registered Successfully", font=("Helvetica", 10, "bold"), text_color="green", height=0, width=300)
            pass_notification.place(x=89, y=276)

            frame.after(5000, pass_notification.destroy)

        elif user not in database:

            dict = database
            dict[user] = passw

            with open(database_loc, "w+") as f: json.dump(dict, f, indent=4)

            pass_notification = ctk.CTkLabel(frame, text="Registered Successfully", font=("Helvetica", 10, "bold"), text_color="green", height=0, width=300)
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

# Display Portfolio
def display_portfolio(search):

    buttons = [widget for widget in search.winfo_children()]

    for btn in buttons:
        btn.configure(state="disabled")

    win.unbind("<Escape>")

    portfolio_frame = ctk.CTkFrame(win)
    portfolio_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    win.bind("<Escape>", lambda event, portfolio_frame=portfolio_frame: quit_portfolio(event, portfolio_frame, buttons))

    size = h/30

    create_portfolio(portfolio_frame, data_loc, user, size)

# Stock Collection
def stock_collection():
    global saved_widgets

    frame.destroy()
    win.unbind("<Return>")

    center(win, (w, h), 2)
    win.attributes('-fullscreen', True)

    search = ctk.CTkFrame(win, bg_color="#1f1f1f", fg_color="#0f0f0f", corner_radius=0)
    search.pack(fill="both", expand=True)

    search_term = ctk.StringVar()
    search_term.trace_add('write', lambda var, index, mode: run_thread(search, search_term))

    search_bar = ctk.CTkEntry(search, fg_color="#1f1f1f", textvariable=search_term, font=("Helvetica", h/67.5, "bold"))
    search_bar.place(relx=0.44, rely=0.1, relwidth=0.45, relheight=0.06, anchor=ctk.CENTER)

    portfolio = ctk.CTkButton(search, text=" Portfolio", fg_color="#9a4cfa", hover_color="#4937D2", font=("Helvetica", h/45, "bold"), cursor="hand2", image=ctk.CTkImage(dark_image=Image.open(f"{data_loc}\\Images\\Portfolio.png"), size=(h/36, h/36)), compound="left", command=lambda: display_portfolio(search))
    portfolio.place(in_=search_bar, relx=1.01, rely=0, relwidth=0.25, relheight=1)

    saved_widgets = [search_bar, portfolio]

# Recommendation Threads
def run_thread(search, search_term):

    saved_widgets[1].configure(state="disabled")

    thread = threading.Thread(target=lambda: update_search(search, search_term))
    thread.start()

# Killing Old Recommendations
def kill_recommendation(recommendation, search_term, search_text):

    def check_and_destroy():
        if search_text != search_term.get():
            recommendation.destroy()

        win.after(100, check_and_destroy)

    check_and_destroy()

# Update Recommendations
def update_search(search, search_term):

    search_text = search_term.get()

    time.sleep(0.5)

    if (search_term.get() != search_text) or (len(search_term.get()) == 0):
        saved_widgets[1].configure(state="normal")
        return

    recommendations = search_from_name(search_text)

    list_of_recommendations = []

    # Load Recommendations
    def load_recommendation(stock):
        
        try:
            os.system(f'curl.exe "https://logo.clearbit.com/{get_ticker_details(stock)["Website"]}" --output {stock}.png')

            image = Image.open(f"{stock}.png")
            recommendation = ctk.CTkButton(search, fg_color="#0f0f0f", hover_color="#1f1f1f", compound=ctk.TOP, text=f"{stock}: {recommendations[stock]}", width=w/8.53 + 25, height=h/4.32 + 65, font=("Helevetica", h/60, "bold"), image=ctk.CTkImage(dark_image=image, size=(h/5.4, h/5.4)), command=lambda stock=stock: get_stock(search, search_term, stock, recommendations[stock]))
        except:
            recommendation = ctk.CTkButton(search, fg_color="#0f0f0f", hover_color="#1f1f1f", compound=ctk.TOP, text=f"{stock}: {recommendations[stock]}", width=w/8.53 + 25, height=h/4.32 + 65, font=("Helevetica", h/60, "bold"), command=lambda stock=stock: get_stock(search, search_term, stock, recommendations[stock]))
        
        try:
            os.remove(f"{stock}.png")
        except:
            pass

        recommendation._text_label.configure(wraplength=150)
        thread = threading.Thread(target=lambda search_text=search_text: kill_recommendation(recommendation, search_term, search_text))
        thread.start()

        list_of_recommendations.append(recommendation)

    threads = []

    for stock in recommendations:
        thread = threading.Thread(target=lambda stock=stock: load_recommendation(stock))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    win.unbind("<Motion>")
    win.unbind("<Button-1>")

    for widget in search.winfo_children():
        if (widget not in saved_widgets) and (widget not in list_of_recommendations):
            widget.destroy()
    
    iteration = 0
    relative_y = 0.2

    # Display Recommendations
    try:
        for recommendation in list_of_recommendations:

            if iteration % 5 == 0:
                recommendation.place(in_=search, relx=0.03, rely=relative_y, relwidth=0.16, relheight=0.35)
                relative_y = 0.6
            else:
                recommendation.place(in_=prev_recommendation, relx=1.2, rely=0, relwidth=1, relheight=1)

            prev_recommendation = recommendation
            iteration += 1

        saved_widgets[1].configure(state="normal")

    except:
        pass

# Display Desired Stock Details
def get_stock(search, search_term, ticker, security_name, period="6mo"):
    global buy, sell
    
    plt.close("all")
    
    search_term.set("")

    for widget in search.winfo_children():
        if widget not in saved_widgets:
            widget.destroy()

    graph = make_graph(ticker, period, "1d")

    bg = ctk.CTkLabel(search, text="", fg_color="#0f0f0f")
    bg.place(relx=0.00, rely=0.15, relwidth=0.6, relheight=0.75)

    ticker_details = get_ticker_details(ticker)

    canvas = FigureCanvasTkAgg(graph, master=search)
    canvas.get_tk_widget().place(in_=bg, relheight=1, relwidth=1)

    text = f"Security Name: {security_name}\n\n"

    for title in ticker_details:
        text += f"{title}: {ticker_details[title]}\n\n"

    text_widget = ctk.CTkTextbox(search, font=("Helvetica", h/67.5, "bold"), fg_color="#0f0f0f", wrap=ctk.WORD)
    text_widget.insert(ctk.END, text)
    text_widget.configure(state=ctk.DISABLED)
    text_widget.place(in_=bg, relx=0.95, rely=0.11, relheight=0.9, relwidth=0.6)
    
    text_widget.tag_config("link", underline=1, foreground="#3366CC")
    
    try:
        website_line = list(ticker_details.keys()).index("Website")*2 + 3
        text_widget.tag_add("link", f"{website_line}.9", f"{website_line}.0 lineend")
    except:
        pass

    def link(event):
        try:
            sel_start, sel_end = text_widget.tag_ranges("sel")
            text_widget.tag_remove(ctk.SEL, "1.0", ctk.END)
            selected_text = text_widget.get(sel_start, sel_end)
            if validators.url(selected_text):
                webbrowser.open_new_tab(selected_text)
        except:
            pass
    
    win.bind("<Button-1>", link)

    buy = ctk.CTkButton(search, text="BUY", font=("Helvetica", h/45, "bold"), border_color="#32CD32", border_width=2, fg_color="#0f0f0f", hover_color="#32CD32", cursor="hand2", command=lambda: record_transaction(data_loc, user, "buy", ticker, quantity.get()))
    sell = ctk.CTkButton(search, text="SELL", font=("Helvetica", h/45, "bold"), border_color="#D32F2F", border_width=2, fg_color="#0f0f0f", hover_color="#D32F2F", cursor="hand2", command=lambda: record_transaction(data_loc, user, "sell", ticker, quantity.get()))

    buy.place(in_=bg, relx=0.26, rely=0.94, relheight=0.08, relwidth=0.2)
    sell.place(in_=buy, relx=1.75, rely=0, relheight=1, relwidth=1)

    # Validation Command
    def vcmd(char):
        return char.isdigit()

    validation_command = win.register(vcmd)

    quantity = ctk.CTkEntry(search, font=("Helvetica", h/67.5, "bold"), justify="center", fg_color="#1f1f1f", validate="key", validatecommand=(validation_command, "%S"))
    quantity.place(in_=buy, relx=1.13, rely=0.35, relheight=0.5, relwidth=0.5)

    quantity_text = ctk.CTkLabel(search, text="Quantity", font=("Helvetica", h/67.5, "bold"), justify="center")
    quantity_text.place(in_=quantity, relx=0, rely=-0.75, relheight=0.55, relwidth=1)

    # Animate Graph Buttons
    def animate(x):
        if pos[x] >= 0:
            pos[x] -= 1
            win.update()
            win.after(20, lambda: animate(x))

    # Check Hover State for Graph
    def check_hover(event):
        global pos

        if (win.winfo_pointerx() > bg.winfo_rootx()) and (win.winfo_pointerx() < bg.winfo_rootx()+bg.winfo_width()/8) and (win.winfo_pointery() > bg.winfo_rooty()) and (win.winfo_pointery() < bg.winfo_rooty()+bg.winfo_height()):

            x = 0

            prev_widget = placeholder
            for widget in place_order:

                widget.place(in_=prev_widget, x=-pos[x], rely=1.35, relheight=1, relwidth=1)
                win.update()

                animate(x)
                x+=1
                
                prev_widget = widget
        
        else:
            
            for widget in place_order:
                widget.place_forget()
                pos = [15]*7

    # Recursive Call to Update Graph
    def update_graph(period):
        get_stock(search, search_term, ticker, security_name, period)

    #Graph Buttons
    placeholder = ctk.CTkLabel(search, text="", fg_color="#0f0f0f")
    placeholder.place(in_=bg, relx=0.05, rely=0.062, relheight=0.07, relwidth=0.055)
    
    _5d = ctk.CTkButton(search, text="5D", font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=5, command=lambda: update_graph("5d"))
    _3m = ctk.CTkButton(search, text="3M", font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=5, command=lambda: update_graph("3mo"))
    _6m = ctk.CTkButton(search, text="6M", font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=5, command=lambda: update_graph("6mo"))
    _ytd = ctk.CTkButton(search, text="YTD", font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=5, command=lambda: update_graph("ytd"))
    _1y = ctk.CTkButton(search, text="1Y", font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=5, command=lambda: update_graph("1y"))
    _5y = ctk.CTkButton(search, text="5Y", font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=5, command=lambda: update_graph("5y"))
    _all = ctk.CTkButton(search, text="All", font=("Helvetica", h/60, "bold"), fg_color="#1f1f1f", hover_color="#3f3f3f", corner_radius=5, command=lambda: update_graph("max"))

    place_order = [_5d, _3m, _6m, _ytd, _1y, _5y, _all]

    win.bind("<Motion>", check_hover)

def main():

    win.resizable(False, False)
    
    login_page(True)

    win.bind("<Escape>", quit_application)

    win.mainloop()

if __name__ == "__main__":
    
    main()