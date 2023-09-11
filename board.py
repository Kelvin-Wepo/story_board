import tkinter as tk

class StoryboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Storyboard and Pre-visualization tool")

        # Create a canvas for drawing
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Create a toolbar with drawing tools
        self.toolbar = tk.Frame(root)
        self.toolbar.pack()

        # Color selection
        self.color_label = tk.Label(self.toolbar, text="Pen Color:")
        self.color_label.grid(row=0, column=0)
        self.color_var = tk.StringVar()
        self.color_var.set("black")
        self.color_menu = tk.OptionMenu(self.toolbar, self.color_var, "black", "red", "blue", "green")
        self.color_menu.grid(row=0, column=1)

        # Pen type selection
        self.pen_type_label = tk.Label(self.toolbar, text="Pen Type:")
        self.pen_type_label.grid(row=0, column=2)
        self.pen_type_var = tk.StringVar()
        self.pen_type_var.set("pen")
        self.pen_type_menu = tk.OptionMenu(self.toolbar, self.pen_type_var, "pen", "eraser")
        self.pen_type_menu.grid(row=0, column=3)

        # Initialize drawing variables
        self.pen_width = 2
        self.eraser_width = 20
        self.old_y = None
        self.old_z = None

        