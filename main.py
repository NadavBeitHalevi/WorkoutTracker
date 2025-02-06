from nutri_service import NutriService

def main():
    nutri_service = NutriService()
    exercise_query = input('Tell me which exercises you did: ')
    response : dict = nutri_service.post_exercise(exercise_query)
    print(response)

if __name__ == '__main__':
    main()

