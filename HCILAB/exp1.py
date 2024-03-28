import tkinter as tk

class MicrowaveApp:
    def __init__(self, master):
        self.master = master
        master.title("Microwave Oven")

        self.label = tk.Label(master, text="Ready", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", command=self.start_microwave)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_microwave, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.running = False

    def start_microwave(self):
        self.label.config(text="Microwave is running...")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Simulate microwave running for 5 seconds
        self.running = True
        self.master.after(5000, self.finish_microwave)

    def stop_microwave(self):
        if self.running:
            self.master.after_cancel(self.finish_microwave)
            self.label.config(text="Microwave stopped.")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.running = False

    def finish_microwave(self):
        self.label.config(text="Microwave finished.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.running = False

def main():
    root = tk.Tk()
    app = MicrowaveApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
