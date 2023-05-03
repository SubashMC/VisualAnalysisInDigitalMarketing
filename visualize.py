import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


root = tk.Tk()
root.title("Visualization")

root.geometry("400x400")

root.config(bg="#1f1e1e")



df = pd.read_csv('./digital_marketing_data.csv')

def visualize_corr():
    corr = df.corr()
    sns.set(style="white")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    plt.show()

def visualize_traffic():
        # Create a line plot of the Website Traffic column over time using seaborn and matplotlib
    sns.set(style="white")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(data=df, x='Date', y='Website Traffic', ax=ax)
    ax.set_title("Website Traffic over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Website Traffic")
    plt.show()

def visualize_conv():
        # Create a line plot of the Conversion Rate column over time using seaborn and matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(data=df, x='Date', y='Conversion Rate', ax=ax)
    ax.set_title("Conversion Rate over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Conversion Rate")
    plt.show()

def visualize_revenue():
        # Create a line plot of the Revenue column over time using seaborn and matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(data=df, x='Date', y='Revenue', ax=ax)
    ax.set_title("Revenue over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue")
    plt.show()

def visualize_cost():
        # Create a line plot of the Customer Acquisition Cost column over time using seaborn and matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(data=df, x='Date', y='Customer Acquisition Cost', ax=ax)
    ax.set_title("Customer Acquisition Cost over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Customer Acquisition Cost")
    plt.show()

def visualize_open_rate():
        # Create a line plot of the Email Open Rate column over time using seaborn and matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(data=df, x='Date', y='Email Open Rate', ax=ax)
    ax.set_title("Email Open Rate over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Email Open Rate")
    plt.show()

def visualize_click_rate():
        # Create a line plot of the Email Click-Through Rate column over time using seaborn and matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.lineplot(data=df, x='Date', y='Email Click-Through Rate', ax=ax)
    ax.set_title("Email Click-Through Rate over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Email Click-Through Rate")
    plt.show()

def cnvr():
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df['Customer Acquisition Cost'])
    plt.title('Customer Acquisition Cost')
    plt.xlabel('Date')
    plt.ylabel('Customer Acquisition Cost')
    plt.show()


visualize_corr_button = tk.Button(root, text="Correlation Heatmap",bg="#689fde",fg="#0a0501", relief=RAISED, command=visualize_corr)
visualize_corr_button.pack(padx=10, pady=10)

visualize_traffic_button = tk.Button(root, text="Website Traffic",bg="#689fde",fg="#0a0501",relief=RAISED,command=visualize_traffic)
visualize_traffic_button.pack(padx=10, pady=10)

visualize_conv_button = tk.Button(root, text="Conversion Rate",fg="#0a0501", bg="#689fde",relief=RAISED, command=visualize_conv)
visualize_conv_button.pack(padx=10, pady=10)

visualize_revenue_button = tk.Button(root, text="Revenue",bg="#689fde",fg="#0a0501", relief=RAISED,command=visualize_revenue)
visualize_revenue_button.pack(padx=10, pady=10)

visualize_cost_button = tk.Button(root, text="Customer Acquisition Cost",bg="#689fde", fg="#0a0501",relief=RAISED,command=visualize_cost)
visualize_cost_button.pack(padx=10, pady=10)

visualize_open_rate_button = tk.Button(root, text="Email Open Rate", bg="#689fde",fg="#0a0501",relief=RAISED, command=visualize_open_rate)
visualize_open_rate_button.pack(padx=10, pady=10)

visualize_click_rate_button = tk.Button(root, text="Email Click-Through Rate",bg="#689fde",fg="#0a0501",relief=RAISED, command=visualize_click_rate)
visualize_click_rate_button.pack(padx=10, pady=10)

visualize_corr_button1 = tk.Button(root, text="Conversion Rate Barplot",bg="#689fde",fg="#0a0501", relief=RAISED, command=cnvr)
visualize_corr_button1.pack(padx=10, pady=10)

button_exit = Button(root, text="Exit", bg="#689fde",fg="#0a0501", command=exit)
button_exit.pack(padx=10, pady=10)

root.mainloop()
