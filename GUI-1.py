import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

class WindowOne(tk.Toplevel):
    def __init__(self):
        super().__init__()

        # Set this window to full screen
        self.attributes('-fullscreen', True)

        # Configure the window
        self.title("Window 1")
        self.configure(background='white')

        # Create a style to set the background color
        style = ttk.Style(self)
        style.configure('Main.TLabel', background='white')

        # Images
        images = [
            PhotoImage(file="C:\\Users\\amish\\Python\\InkAndInsights\\Images\\Image1.png"),
            PhotoImage(file="C:\\Users\\amish\\Python\\InkAndInsights\\Images\\Image2.png"),
            PhotoImage(file="C:\\Users\\amish\\Python\\InkAndInsights\\Images\\Image3.png"),
            PhotoImage(file="C:\\Users\\amish\\Python\\InkAndInsights\\Images\\Image4.png"),
        ]

        # Image labels in a 2x2 grid
        for i, image in enumerate(images):
            row = i // 2
            col = i % 2

            image_label = ttk.Label(self, image=image)
            image_label.configure(style='Main.TLabel')  # Set background color using style
            image_label.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Labels underneath images
        labels = ["Label 1", "Label 2", "Label 3", "Label 4"]

        for i, label_text in enumerate(labels):
            row = 2  # Row index for labels
            col = i  # Column index for labels

            label = ttk.Label(self, text=label_text, font=('Arial', 14), foreground='blue')
            label.configure(style='Main.TLabel')  # Set background color using style
            label.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Configure rows and columns to expand with window resizing
        for i in range(3):  # 3 rows (2 for images, 1 for labels)
            self.grid_rowconfigure(i, weight=1)

        for i in range(2):  # 2 columns (images)
            self.grid_columnconfigure(i, weight=1)

        # Bind the Escape key to exit full screen
        self.bind("<Escape>", self.exit_full_screen)

    def exit_full_screen(self, event):
        # Exit full screen when the Escape key is pressed
        self.attributes('-fullscreen', False)

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window to full screen
        self.attributes('-fullscreen', True)

        # Configure the window
        self.title("INK AND INSIGHTS")
        self.configure(background='white')

        # Heading label
        heading_label = ttk.Label(self, text='INK AND INSIGHTS', font=('Times New Roman', 50), foreground="#1B8E91")
        heading_label.configure(style='Main.TLabel')  # Set background color using style
        heading_label.pack(pady=10)

        # Subheading label
        subheading_label = ttk.Label(self, text='(NAVIGATING INDIA’S LITERACY METRICS)', font=('Arial', 20), foreground='blue')
        subheading_label.configure(style='Main.TLabel')  # Set background color using style
        subheading_label.pack(pady=10)

        # Buttons container
        buttons_container = ttk.Frame(self)
        buttons_container.pack(pady=10)

        # Button 1
        button1 = ttk.Button(buttons_container, text='Basic Overview', command=self.open_window1)
        button1.grid(row=0, column=0, padx=20, pady=10, ipadx=50, ipady=50)

    def open_window1(self):
        window_one = WindowOne()

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
