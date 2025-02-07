from excercise import Excersice
from typing import List

class NuntriManager:

    def __init__ (self, nutri_service):
        self.nutri_service = nutri_service

    def post_exercise(self, exercise_query) -> List[Excersice]:
        exersice_response = self.nutri_service.post_exercise(exercise_query)
        excersices : List[Excersice] = []

        for exercise in exersice_response['exercises']:
            excersices.append(Excersice(exercise['name'], exercise['duration_min'], exercise['nf_calories']))
            print(f"Exercise: {exercise['name']}, Duration: {exercise['duration_min']} min, Calories: {exercise['nf_calories']} kcal")
        return excersices
    
    def save_exercise(self, excersices: List[Excersice]) -> None:
        for exercise in excersices:
            self.nutri_service.post_workout(exercise.to_json())



    