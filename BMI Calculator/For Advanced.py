import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Try to load existing data or create an empty DataFrame
try:
    df = pd.read_csv("bmi_data.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Weight", "Height", "BMI", "Category"])

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def on_submit():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        label_result.config(text=f"BMI: {bmi:.2f} ({category})")

        # Save the result with timestamp
        global df
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.loc[len(df)] = [now, weight, height, bmi, category]
        df.to_csv("bmi_data.csv", index=False)
    
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers.")

def show_history():
    if df.empty:
        messagebox.showinfo("No Data", "No BMI records found.")
        return
    plt.figure(figsize=(8, 4))
    plt.plot(pd.to_datetime(df['Date']), df['BMI'], marker='o')
    plt.title("BMI Over Time")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# GUI Setup
window = tk.Tk()
window.title("BMI Calculator")

tk.Label(window, text="Enter Weight (kg):").grid(row=0, column=0)
entry_weight = tk.Entry(window)
entry_weight.grid(row=0, column=1)

tk.Label(window, text="Enter Height (m):").grid(row=1, column=0)
entry_height = tk.Entry(window)
entry_height.grid(row=1, column=1)

btn_submit = tk.Button(window, text="Calculate BMI", command=on_submit)
btn_submit.grid(row=2, column=0, columnspan=2)

label_result = tk.Label(window, text="", font=("Arial", 12))
label_result.grid(row=3, column=0, columnspan=2)

btn_history = tk.Button(window, text="Show History", command=show_history)
btn_history.grid(row=4, column=0, columnspan=2)

window.mainloop()

