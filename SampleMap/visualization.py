import csv
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import os
import json

class VisualizationTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Overlay Visualization")

        # Variables
        self.path = None
        self.image_path = None
        self.csv_path = None
        self.height = None
        self.width = None
        self.original_image = None
        self.overlay_image = None
        self.display_image = None
        self.canvas = None
        self.show_overlay = True

        # UI Elements
        self.load_path_btn = tk.Button(self.root, text="Load path", command=self.load_path)
        self.load_path_btn.pack()

        self.generate_btn = tk.Button(self.root, text="Generate Overlay", command=self.generate_overlay)
        self.generate_btn.pack()

        self.toggle_btn = tk.Button(self.root, text="Toggle Overlay", command=self.toggle_overlay)
        self.toggle_btn.pack()

        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.root.mainloop()

    def load_path(self):
        self.path = filedialog.askdirectory(title="Select folder")
        self.image_path = os.path.join(self.path, "texture.png")
        self.csv_path = os.path.join(self.path, "maze", "collision_maze.csv")
        json_file = os.path.join(self.path, "maze_meta_info.json")
        try: 
            with open(json_file, 'r') as f:
                meta_info = json.load(f)
                self.height = meta_info.get("maze_height")
                self.width = meta_info.get("maze_width")
        except ValueError:
            print("JSON file not found. Please ensure 'maze_meta_info.json' exists in the selected folder.")
            return
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.display_on_canvas()


    def generate_overlay(self):
        if not self.original_image or not self.csv_path:
            print("Please load image and CSV first.")
            return


        # Read CSV
        csv_data = []
        with open(self.csv_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                csv_data.append([int(val) for val in row])

        if len(csv_data) != self.height or any(len(row) != self.width for row in csv_data):
            print("CSV dimensions do not match height x width.")
            return

        # Create overlay
        img_width, img_height = self.original_image.size
        cell_width = img_width / self.width
        cell_height = img_height / self.height

        self.overlay_image = Image.new("RGBA", (img_width, img_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(self.overlay_image)

        for i in range(self.height):
            for j in range(self.width):
                value = csv_data[i][j]
                if value == 32125:
                    # Draw black rectangle (semi-transparent for visibility, adjust alpha as needed)
                    x0 = j * cell_width
                    y0 = i * cell_height
                    x1 = (j + 1) * cell_width
                    y1 = (i + 1) * cell_height
                    draw.rectangle([x0, y0, x1, y1], fill=(0, 0, 0, 128))  # Black with 50% opacity
                # For 0, do nothing (transparent)

        self.display_on_canvas()

    def toggle_overlay(self):
        self.show_overlay = not self.show_overlay
        self.display_on_canvas()

    def display_on_canvas(self):
        if not self.original_image:
            return

        if self.show_overlay and self.overlay_image:
            combined = Image.alpha_composite(self.original_image.convert("RGBA"), self.overlay_image)
        else:
            combined = self.original_image

        # Resize for display if needed
        combined.thumbnail((800, 600))
        self.display_image = ImageTk.PhotoImage(combined)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.display_image)

if __name__ == "__main__":
    VisualizationTool()