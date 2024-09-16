import re
import tkinter as tk
from tkinter import StringVar
from tkinter.ttk import Progressbar

def assess_password_strength(password):
    strength = 0

    # Criteria checks
    if len(password) >= 8:
        strength += 1  # Length criteria
    if re.search(r'[a-z]', password):
        strength += 1  # Lowercase
    if re.search(r'[A-Z]', password):
        strength += 1  # Uppercase
    if re.search(r'\d', password):
        strength += 1  # Number
    if re.search(r'[!@#$%^&*(),.?"+-_:{}|/<>]', password):
        strength += 1  # Special character

    # Feedback based on strength score
    if strength <= 2:
        return 'Weak', strength
    elif 3 <= strength <= 4:
        return 'Medium', strength
    elif strength == 5:
        return 'Strong', strength


def update_strength_label(event=None):
    password = password_var.get()
    feedback, strength = assess_password_strength(password)

    # Update the label color
    if feedback == 'Weak':
        strength_label.config(text=f"Password strength: {feedback}", fg="red")
    elif feedback == 'Medium':
        strength_label.config(text=f"Password strength: {feedback}", fg="orange")
    elif feedback == 'Strong':
        strength_label.config(text=f"Password strength: {feedback}", fg="green")

    # Update the progress bar based on strength score
    progress['value'] = strength * 20  # Assuming max strength is 5, so multiply by 20 for %

def show_tooltip(event=None):
    tooltip_label.config(text="A strong password should:\n"
                              "- Be at least 8 characters long\n"
                              "- Include both uppercase and lowercase letters\n"
                              "- Include at least one number\n"
                              "- Include special characters (e.g., !, @, #, etc.)")

def hide_tooltip(event=None):
    tooltip_label.config(text="")


# Initialize the Tkinter window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x400")

# Create a label, entry, progress bar, and result label
password_var = StringVar()
tk.Label(root, text="Enter your password:", font=('Helvetica', 12)).pack(pady=10)
password_entry = tk.Entry(root, textvariable=password_var, font=('Helvetica', 12), show="*")
password_entry.pack(pady=5)

# Label to display password strength with dynamic color
strength_label = tk.Label(root, text="Password strength: ", font=('Helvetica', 12))
strength_label.pack(pady=10)

# Add a progress bar to show password strength visually
progress = Progressbar(root, orient="horizontal", length=300, mode='determinate')
progress.pack(pady=10)

# Tooltip label (initially hidden)
tooltip_label = tk.Label(root, text="", font=('Helvetica', 10), fg="gray")
tooltip_label.pack(pady=10)

# Bind the input event to update strength in real time
password_entry.bind("<KeyRelease>", update_strength_label)

# Show and hide tooltip on hover
password_entry.bind("<Enter>", show_tooltip)
password_entry.bind("<Leave>", hide_tooltip)

# Run the Tkinter event loop
root.mainloop()

