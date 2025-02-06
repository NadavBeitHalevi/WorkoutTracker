import requests

class NutriService:

    def __init__(self):
        self.HOST_DOMAIN = 'https://trackapi.nutritionix.com'
        self.NUTRITIONIX_ENDPOINT = '/v2/natural/exercise'
        self.NUTRITIONIX_APP_ID = 'c164f27b'
        self.NUTRITIONIX_APP_KEY = 'bd0d16b94107ab9b27fa11ccd49452c0'
        self.MY_GOOGLE_DOCS_TRACKER = 'https://docs.google.com/spreadsheets/d/1VDlS6wBxX4QYWSBnBtW7Oi5huS2OuafP_4hy1ctLkpk/edit?usp=sharing'
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
