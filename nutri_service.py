import requests
from app_settings import AppSettings

class NutriService:

    def __init__(self):
        self.HOST_DOMAIN = AppSettings().get_host_domain()
        self.NUTRITIONIX_ENDPOINT = AppSettings().get_nutritionix_endpoint()
        self.NUTRITIONIX_APP_ID = AppSettings().get_nutritionix_app_id()
        self.NUTRITIONIX_APP_KEY = AppSettings().get_nutritionix_app_key()
        self.MY_GOOGLE_DOCS_TRACKER = AppSettings().get_my_google_docs_tracker()
        self.headers = {
            'x-app-id': self.NUTRITIONIX_APP_ID,
            'x-app-key': self.NUTRITIONIX_APP_KEY,
            'x-remote-user-id': '0',
            'Content-Type': 'application/json',
        }


    def post_exercise(self, exercise_query) -> dict:
        url = f'{self.HOST_DOMAIN}{self.NUTRITIONIX_ENDPOINT}'
        exercise_params = {
            'query': exercise_query,
        }
        response = requests.post(url=url, 
                                 json=exercise_params, 
                                 headers=self.headers)
        response.raise_for_status()
        return response.json()


    def post_workout(self, workout : dict) -> bool:
        headers = {
            'Content-Type': 'application/json',
            'Authorization' : AppSettings().get_authorization()
        }

        body = {
            'workout': workout
        }
        response = requests.post(url=AppSettings().get_sheety_url(), 
                                 json=body, 
                                 headers=headers,)
        response.raise_for_status()
        return True


