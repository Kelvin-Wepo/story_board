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

       