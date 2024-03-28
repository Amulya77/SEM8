import tkinter as tk
from tkinter import messagebox, simpledialog
class HomeApplianceControl:
    def __init__(self, master):
        self.master = master
        self.master.title("Home Appliance Control")
        # Dictionary to store the state of each appliance
        self.appliance_states = {
            "Light": self.query_initial_state("Light"),
            "Fan": self.query_initial_state("Fan"),
        }
        # Create buttons for each appliance
        self.create_buttons()
    def create_buttons(self):
        # Create buttons for each appliance
        for appliance, state in self.appliance_states.items():
            button = tk.Button(self.master, text=f"{appliance} {'On' if state else 'Off'}",
                               command=lambda app=appliance: self.toggle_appliance(app))
            button.pack(pady=5)
    def toggle_appliance(self, appliance):
        # Toggle the state of the selected appliance
        self.appliance_states[appliance] = not self.appliance_states[appliance]
        # Update the button text
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Button) and appliance in widget.cget("text"):
                widget.config(text=f"{appliance} {'On' if self.appliance_states[appliance] else 'Off'}")
        # Display a message box with the updated state
        messagebox.showinfo("Appliance State", f"{appliance} is {'On' if self.appliance_states[appliance] else 'Off'}")
    def query_initial_state(self, appliance):
        # Ask user for the initial state of the appliance
        initial_state = simpledialog.askstring(f"Initial State of {appliance}",
                                                f"Enter the initial state of {appliance} (On/Off):")
        return initial_state.lower() == "on"
if __name__ == "__main__":
    root = tk.Tk()
    app = HomeApplianceControl(root)
    root.mainloop()
