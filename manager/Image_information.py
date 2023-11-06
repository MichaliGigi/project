# this class is responsible for the information of the image

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


class Image_information():
    def __init__(self, images_path, final_grade):
        self.file = File_manager()
        self.images_path = images_path

        self.category = Categories()
        self.sub_category = SubCategoryByFaces()
        self.final_grade = final_grade
        self.Info_Categories = {
            "smile": Smile(),
            "red eyes": Red_eyes(),
            "eyes closed": Close_eyes(),
            "resolution": Resolution(),
            "focus": Focus(),
            "face direction": FaceDirection(),
            "brightness faces": BrightnessFaces(),
            "hair": Hair()
        }

    def fill_information(self):

        data = []
        # Run on all images in the folder
        for image_path in self.images_path:
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
            # calculate the final grade
            new_row_data["Final grade"] = int(round(self.final_grade.calculate_final_grade(grades_values)))

            data.append(new_row_data)

        # Create a pandas DataFrame from the data
        df = pd.DataFrame(data)
        # Write the DataFrame to a CSV file
        self.file.write_to_csv(df)
