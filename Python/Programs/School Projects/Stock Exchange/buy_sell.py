import customtkinter as ctk
import csv
import os
from datetime import datetime
import yfinance as yf

file_name = f"Portfolio.csv"

# Columns for the CSV, including Quantity
columns = ["S.NO", "Stock Name", "Date", "Sell/Buy", "Price", "Quantity", "Time"]

def get_latest_stock_price(ticker):
    stock = yf.Ticker(ticker)
    latest_price = stock.history(period='5d', interval='1d').tail(1)['Close'].values[0]
    return latest_price

def record_transaction(data_loc, username, transaction_type, ticker, quantity):
    if quantity.isdigit(): quantity = int(quantity)
    else: quantity = 1
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_price = get_latest_stock_price(ticker)
    serial_number = 1

    # Create a filename based on the username
    file_path = f"{data_loc}/Accounts/{username}/{file_name}"

    # Create CSV file with headers if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)

    # Read the existing data to find the last serial number
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) > 1:
            serial_number = int(rows[-1][0]) + 1

    # Append the new transaction
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([serial_number, ticker, current_date, transaction_type, current_price, quantity, current_time])

def load_csv(csv_file):
    data = []
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def render_data(frame, data, size):
    # column heading
    for col_index, col_name in enumerate(columns):
        label = ctk.CTkLabel(frame, text=col_name, font=("Helvetica", size, "bold"), padx=10, pady=5, bg_color="lightgray", text_color="black")
        label.grid(row=0, column=col_index, sticky="nsew", padx=1, pady=1)  # Simulate border with padx and pady

    # load data
    for row_index, row in enumerate(data):
        for col_index, col_name in enumerate(columns):
            value = row.get(col_name, "")
            tag = 'buy' if row["Sell/Buy"].lower() == 'buy' else 'sell'
            color = 'lightgreen' if tag == 'buy' else 'lightcoral'
            label = ctk.CTkLabel(frame, text=value, font=("Helvetica", size), bg_color=color, text_color="black", padx=10, pady=5)
            label.grid(row=row_index+1, column=col_index, sticky="nsew", padx=1, pady=1)  # Simulate border with padx and pady

    # edit table
    for i in range(len(columns)):
        frame.grid_columnconfigure(i, weight=1)
    for i in range(len(data) + 1):  # +1 for head row
        frame.grid_rowconfigure(i, weight=1)

def create_portfolio(frame, data_loc, username, size=24):
    file_path = f"{data_loc}/Accounts/{username}/{file_name}"
    data = load_csv(file_path)
    render_data(frame, data, size)
