import tkinter as tk
from math import cos, sin, pi
from PIL import Image, ImageTk, ImageDraw, ImageFilter


def progress():
  class MotionBlur:
    def __init__(self, radius=2, alpha=128):
        self.radius = radius
        self.alpha = alpha

    def apply(self, image):
        return image.convert("RGBA").filter(ImageFilter.GaussianBlur(radius=self.radius))

  class LoadingSpinner(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("")
        self.geometry("400x450")  # Adjusted dimensions for a smaller screen

        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack()

        self.spinner_radius = [15, 20, 25, 30]  # Adjusted spinner radii for a smaller screen
        self.circular_path_radius = 100  # Initial circular path radius
        self.spinner_color = "green"
        self.create_spinners()

        self.label = tk.Label(self, text="Generating...", font=("Helvetica", 10))  # Adjusted font size
        self.label.pack(pady=5)  # Adjusted padding

    def create_spinners(self):
        self.spinners = []
        for radius in self.spinner_radius:
            spinner = self.canvas.create_oval(
                200 - radius,
                200 - radius,
                200 + radius,
                200 + radius,
                outline=self.spinner_color,
                width=1,  # Adjusted width for a smaller screen
                fill=self.spinner_color
            )
            self.spinners.append(spinner)

        self.update_spinners()

    def update_spinners(self):
        angles = [0, pi / 4, 2 * pi / 4, 3 * pi / 4]  # Adjusted angles for four spinners
        self.animate_spinners(angles)

    def animate_spinners(self, angles):
        for i, angle in enumerate(angles):
            x = 200 + self.circular_path_radius * cos(angle)
            y = 200 + self.circular_path_radius * sin(angle)

            spinner = self.spinners[i]
            self.canvas.coords(spinner,
                                x - self.spinner_radius[i],
                                y - self.spinner_radius[i],
                                x + self.spinner_radius[i],
                                y + self.spinner_radius[i])

        blurred_image = self.get_blurred_image()
        self.blurred_image_tk = ImageTk.PhotoImage(blurred_image)

        self.canvas.create_image(200, 200, image=self.blurred_image_tk)
        self.after(10, lambda: self.animate_spinners([angle + pi / 17 for angle in angles]))

    def get_blurred_image(self):
        spinner_image = Image.new("RGBA", (400, 400), (0, 0, 0, 0))
        draw = ImageDraw.Draw(spinner_image)

        for i, radius in enumerate(self.spinner_radius):
            x = 200
            y = 200
            draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=self.spinner_color)

        motion_blur = MotionBlur(radius=20)  # Adjusted motion blur for a smaller screen
        blurred_image = motion_blur.apply(spinner_image)
        return blurred_image


  app = LoadingSpinner()
  app.mainloop()

#progress()
