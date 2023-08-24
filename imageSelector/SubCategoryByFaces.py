from imageSelector.Image import *


class SubCategoryByFaces:
    def __init__(self):
        self.faces= []
        self.sub_categories=[]

    def fillSubCategory(self, image,category):
        sub_category = []
        im=image.get_original_image()
        my_faces_encoding = face_recognition.face_encodings(im)
        if len(self.faces)<=category:
            self.faces.append([])
        for i_my_face,my_face in enumerate(my_faces_encoding):
            for i_face,face in enumerate(self.faces[category]):
                results = face_recognition.compare_faces([my_face], face)
                #if the face is already in the list
                if results[0] == True:
                    sub_category.append(i_face)# the index of the face in the list
                    break

            else:
                self.faces[category].append(my_face)#add the face to the list
                sub_category.append(len(self.faces[category])-1)# the index of the face in the list
        sub_category.sort() #sort the list
        if(len(self.sub_categories)<=category):
            self.sub_categories.append([])
        #run over the sub_categories list
        for sub in self.sub_categories[category]:
            if sub_category==sub:#if the sub_category is already in the list
                print("sub_category: ", self.sub_categories[category].index(sub))
                return self.sub_categories[category].index(sub)#return the index of the sub_category
        else:#if the sub_category is not in the list
            self.sub_categories[category].append(sub_category)#add the sub_category to the list
            return len(self.sub_categories[category])-1#return the index of the sub_category



