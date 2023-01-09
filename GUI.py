# this file handles the GUI for the program
# it is a simple GUI that allows the user to select a file and then
# run the program on that file
# it also allows the user to select a file to save the output to
import tkinter as tk
def main():
    # create the GUI
    root = tk.Tk()
    root.title("Face Detection")
    root.geometry("400x200")
    root.resizable(False, False)
    # create the label and button for selecting the input file
    input_label = tk.Label(root, text="Select the input file:")
    input_label.pack()
    input_button = tk.Button(root, text="Select", command=lambda: select_file(root, "input"))
    input_button.pack()
    # create the label and button for selecting the output file
    output_label = tk.Label(root, text="Select the output file:")
    output_label.pack()
    output_button = tk.Button(root, text="Select", command=lambda: select_file(root, "output"))
    output_button.pack()
    # create the button for running the program
    run_button = tk.Button(root, text="Run", command=lambda: run_program(root))
    run_button.pack()
    # create the label for displaying the output
    output_label = tk.Label(root, text="")
    output_label.pack()
    # start the GUI
    root.mainloop()
def select_file(root, file_type):
    # create the file dialog
    file_dialog = tk.filedialog.askopenfilename()
    # update the GUI
    if file_type == "input":
        input_label = tk.Label(root, text="Input file: {}".format(file_dialog))
        input_label.pack()
    elif file_type == "output":
        output_label = tk.Label(root, text="Output file: {}".format(file_dialog))
        output_label.pack()
def run_program(root):
    # run the program
    # update the GUI
    output_label = tk.Label(root, text="The program has finished running")
    output_label.pack()
if __name__ == "__main__":
    main()
