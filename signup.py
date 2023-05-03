import tkinter as tk
from tkinter import messagebox


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.title("Login")
        self.geometry("300x200")
        self.configure(bg="#1f1e1e")
        self.resizable(False, False)

        # Create username and password labels
        tk.Label(self, text="Username: ").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self, text="Password: ").grid(row=1, column=0, padx=5, pady=5)

        # Create username and password entry fields
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create login and signup buttons
        tk.Button(self, text="Login", command=self.login).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self, text="Signup", command=self.signup).grid(row=2, column=1, padx=5, pady=5)

        # Initialize username and password dictionary
        self.user_dict = {}

    def login(self):
        # Get username and password from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password match stored values
        if username in self.user_dict.keys() and password == self.user_dict[username]:
            app.destroy()
            import browse
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def signup(self):
        # Create a new window for signup
        signup_window = tk.Toplevel(self)
        signup_window.title("Signup")
        signup_window.geometry("300x200")
        signup_window.configure(bg="#1f1e1e")

        # Create username and password labels
        tk.Label(signup_window, text="Username: ").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(signup_window, text="Password: ").grid(row=1, column=0, padx=5, pady=5)

        # Create username and password entry fields
        username_entry = tk.Entry(signup_window)
        username_entry.grid(row=0, column=1, padx=5, pady=5)
        password_entry = tk.Entry(signup_window, show="*")
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create submit button
        tk.Button(signup_window, text="Submit",
                  command=lambda: self.submit_signup(signup_window, username_entry.get(), password_entry.get())).grid(
            row=2, column=0, columnspan=2, padx=5, pady=5)

    def submit_signup(self, window, username, password):
        # Check if username already exists
        if username in self.user_dict.keys():
            messagebox.showerror("Signup Failed", "Username already exists.")
        else:
            # Add new user to dictionary and close signup window
            self.user_dict[username] = password
            window.destroy()


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
