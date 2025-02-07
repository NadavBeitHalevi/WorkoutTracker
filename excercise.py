import datetime

class Excersice:
    def __init__(self, name, duration, calories):
        self.exercise = name
        self.duration = duration
        self.calories = calories
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time = datetime.datetime.now().strftime('%H:%M:%S')

    def display(self):
        print("Name: ", self.name)
        print("Duration: ", self.duration)
        print("Calories: ", self.calories)

    def to_json(self) -> dict:
        return self.__dict__