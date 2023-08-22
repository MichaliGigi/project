import os


class FinalGrade:
    File = "components.txt"

    def __init__(self):
        # 0: most important, 1: medium, 2: less important
        self.importance = [60, 25, 15]  # default
        self.gradeComponents = {"high": [], "medium": [], "low": []}  # default
        self.read_components_from_file()

    # ==============================
    def set_importance(self, importance):
        if self.validate_importance(importance):
            self.importance = importance

    # ==============================
    def validate_importance(self, importance):
        if len(importance) != 3:
            print("Error: importance should be a list of 3 numbers")
            return False
        if (importance[0] + importance[1] + importance[2]) != 100:
            print("Error: sum of importance should be 100")
            return False
        if importance[0] < importance[1] or importance[1] < importance[2]:
            print("Error: importance should be in descending order")
            return False
        if importance[0] < 0 or importance[1] < 0 or importance[2] < 0:
            print("Error: importance should be positive")
            return False
        return True

    # ==============================
    def calculate_final_grade(self, new_row_data):
        final_grade = 0

        grades_values = [[],[] ,[]]
        for category, grade in new_row_data.items():
            for importance_index, category_list in enumerate(self.gradeComponents.values()):
                if category in category_list:
                    grades_values[importance_index].append(grade)

                    break  # Break the loop once the category is found

        for importance_index, grade_list in enumerate(grades_values):
            final_grade+= sum(grade_list)/len(grade_list) * self.importance[importance_index] / 100

        return final_grade

    # ==============================
    def read_components_from_file(self):
        script_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_path, '..', 'manager', self.File)
        with open(path, 'r') as file:
            for line in file:
                component, grade = line.strip().split(', ')
                self.gradeComponents[component].append(grade)





