# this class is responsible for the information of the image
class Image_information():
    def __init__(self, url_folder):
        self.Info_Categories={"path": (0, ),"category": 1, "sub category": 2,"smile": 3, "red eyes": 4, "eyes closed": 5,
                       "resolution": 6, "focus": 7, "face direction": 8, "brightness faces": 9, "hair": 10, "final grade": 11}

    def add_category(self,name,index,category_department):
        self.Info_Categories[name]=(index,category_department)

    def delete_category(self,name):
        self.Info_Categories.pop(name)

    def get_category_index(self,name):
        return self.Info_Categories[name][0]

    def fill_information(self):
        for category in self.Info_Categories.values():
            category[1].fill_category()
