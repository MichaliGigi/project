from Libraries import *
import pandas as pd
class File_manager():
    def __init__(self):
        self.file_name = "images_info.csv"
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to the CSV file using os.path.join
        self.csv_file_path = os.path.join(self.script_path, '..', 'manager', self.file_name)

    def read_csv_file(self):
        df = pd.read_csv('data.csv')

        # open the csv file to read and write
        with open(self.csv_file_path, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
        return csvreader

    def write_to_csv(self):
        with open(self.csv_file_path, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["path", "grade", "category"])
