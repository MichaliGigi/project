import tkinter as tk
import random
import time
# Code that shows a Voronoi diagram simulation with SWEEP LINE
# Path: good\ךך.py
# Compare this snippet from GUI.py:
# # this file handles the GUI for the program
# # it is a simple GUI that allows the user to select a file and then
# # run the program on that file
# # it also allows the user to select a file to save the output to
def main():
    # create the GUI
    root = tk.Tk()
    root.title("Voronoi Diagram")
    root.geometry("800x600")
    root.resizable(False, False)
    # create the canvas
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()
    # create the button for running the simulation
    run_button = tk.Button(root, text="Run", command=lambda: run_simulation(canvas))
    run_button.pack()
    # start the GUI
    root.mainloop()

def run_simulation(canvas):
    # create the points
    points = []
    for i in range(10):
        points.append((random.randint(0, 800), random.randint(0, 600)))
    # create the lines
    lines = []
    for i in range(len(points)):
        lines.append((points[i], points[(i + 1) % len(points)]))
    # create the sweep line
    sweep_line = (0, 0, 800, 0)
    # draw the points
    for point in points:
        canvas.create_oval(point[0] - 5, point[1] - 5, point[0] + 5, point[1] + 5, fill="red")
    # draw the lines
    for line in lines:
        canvas.create_line(line[0][0], line[0][1], line[1][0], line[1][1])
    # draw the sweep line
    sweep_line_id = canvas.create_line(sweep_line[0], sweep_line[1], sweep_line[2], sweep_line[3], fill="blue")
    # move the sweep line
    for i in range(800):
        canvas.move(sweep_line_id, 1, 0)
        canvas.update()
        time.sleep(0.01)
if __name__ == "__main__":
    main()


