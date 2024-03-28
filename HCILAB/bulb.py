import tkinter as tk
from tkinter import messagebox

class HomeApplianceControl:
    def __init__(self, master):
        self.master = master
        self.master.title("Home Appliance Control")

        # Initial state of the lightbulb
        self.lightbulb_state = False

        # Load images for the lightbulb
        self.img_light_on = tk.PhotoImage(file="light_on.png")
        self.img_light_off = tk.PhotoImage(file="light_off.png")

        # Create lightbulb label with initial image
        self.lbl_lightbulb = tk.Label(self.master, image=self.img_light_off)
        self.lbl_lightbulb.pack(pady=10)

        # Create button to toggle the lightbulb
        self.btn_toggle_light = tk.Button(self.master, text="Toggle Lightbulb", command=self.toggle_lightbulb)
        self.btn_toggle_light.pack(pady=5)

    def toggle_lightbulb(self):
        # Toggle the state of the lightbulb
        self.lightbulb_state = not self.lightbulb_state

        # Update the lightbulb image based on the state
        if self.lightbulb_state:
            self.lbl_lightbulb.config(image=self.img_light_on)
        else:
            self.lbl_lightbulb.config(image=self.img_light_off)

        # Display a message box with the updated state
        state_message = "on" if self.lightbulb_state else "off"
        messagebox.showinfo("Lightbulb State", f"Lightbulb is {state_message}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HomeApplianceControl(root)
    root.mainloop()
