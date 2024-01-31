import tkinter as tk

class FullScreenApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window to full screen
        self.attributes('-fullscreen', True)

        # Additional setup for the application
        self.title("Full Screen App")
        self.configure(background='white')

        # Example: Add a label to the full-screen window
        label = tk.Label(self, text="This is a full-screen application", font=('Arial', 20), bg='white')
        label.pack(pady=50)

        # Bind the Escape key to exit full screen
        self.bind("<Escape>", self.exit_full_screen)

    def exit_full_screen(self, event):
        # Exit full screen when the Escape key is pressed
        self.attributes('-fullscreen', False)

if __name__ == "__main__":
    app = FullScreenApp()
    app.mainloop()
