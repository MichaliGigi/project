# this class is responsible for the information of the image
import os

import pandas as pd

from manager.File_manager import File_manager
from imageSelector.Image import Image
from imageSelector.categories import Categories
from imageSelector.SubCategoryByFaces import SubCategoryByFaces
from imageSelector.smile import Smile
from imageSelector.red_eyes import Red_eyes
from imageSelector.Close_Eyes import Close_eyes
from imageSelector.resolution import Resolution
from imageSelector.Focus import Focus
from imageSelector.faceDirection import FaceDirection
from imageSelector.BrightnessFaces import BrightnessFaces
from imageSelector.Hair import Hair
from manager.FinalGrade import FinalGrade


class Image_information():
    def __init__(self, url_folder,final_grade):
        self.file = File_manager()
        self.url_folder = url_folder
        self.get_images_in_folder()

        self.category=Categories()
        self.sub_category =SubCategoryByFaces()
        self.final_grade=final_grade
        self.Info_Categories = {
                                "smile": Smile(),
                                "red eyes": Red_eyes(),
                                "eyes closed": Close_eyes(),
                                "resolution": Resolution(),
                                "focus": Focus(),
                                "face direction": FaceDirection(),
                                "brightness faces": BrightnessFaces(),
                                "hair": Hair()
                               # "final grade":0
                                }


    def add_category(self, name, index, category_department):
        pass

    # self.Info_Categories[name] = (index, category_department)

    def delete_category(self, name):
        pass
        # self.Info_Categories.pop(name)

    # def get_category_index(self, name):
    # return self.Info_Categories[name][0]
    def get_images_in_folder(self):
        self.images_path = []
        for root, dirs, filenames in os.walk(self.url_folder):
            for filename in filenames:
                if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".JPG") or filename.endswith(".PNG") or filename.endswith(".JPEG"):
                    self.images_path.append(os.path.join(root, filename))

    def fill_information(self):

        data = []
        xj = 0
        # Run on all images in the folder
        for image_path in self.images_path:
            print("number of images: ", xj)
            # Create a new row to add to the image information
            new_row_data = {"Image path": image_path}

            # create image object
            image = Image(image_path)
            new_row_data["Category"] = self.category.fillCategory(image)
            new_row_data["Sub category"] = self.sub_category.fillSubCategory(image, new_row_data["Category"])

            grades_values = {}
            # fill information of the image
            for key, value in self.Info_Categories.items():
                grades_values[key] = int(round(value.calculateGrade(image)))
            new_row_data.update(grades_values)

            # calculate the final grade
            new_row_data["Final grade"] = int(round(self.final_grade.calculate_final_grade(grades_values)))

            data.append(new_row_data)
            xj += 1


        print(data)
        # Create a pandas DataFrame from the data
        df = pd.DataFrame(data)

        # find the absolute path of the csv file
        csv_path = os.path.join(self.url_folder, 'images_info.csv')

        self.file.write_to_csv(df)
        # Write the DataFrame to a CSV file
        #df.to_csv('images_info.csv', index=False)