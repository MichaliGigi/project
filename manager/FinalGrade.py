class FinalGrade:
    File = "components.txt"

    def __init__(self, url):
        self.url = url
        self.grade = 0
        # 0: most important, 1: medium, 2: less important
        self.importance = [60, 25, 15]  # default
        self.gradeComponents = {"high": [], "medium": [], "low": []}  # default
        self.read_components_from_file()
    # ==============================
    def get_grade(self):
        return self.grade

    # ==============================
    def set_grade(self, grade):
        self.grade = grade

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
    def calculate_final_grade(self):
        for grade_list, importance in zip(self.gradeComponents.values(), self.importance):
            for component in grade_list:
                self.grade += component.get_grade() * importance / 100

    # ==============================
    def read_components_from_file(self):
        with open(self.File, 'r') as file:
            for line in file:
                component, grade = line.strip().split(', ')
                self.gradeComponents[component].append(grade)


x=FinalGrade()

