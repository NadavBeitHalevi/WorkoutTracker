from nutri_manager import NuntriManager 
from nutri_service import NutriService

def main():

    nutri_manager = NuntriManager(NutriService())
    print('Welcome to the Nutri Manager')
    print('--------------------------------')
    exit = False
    while not exit:
        print('1. Post a new exercise')
        print('2. Exit')
        option = input('Select an option: ')
        if option == '1':
            post_exercise(nutri_manager)
        elif option == '2':
            exit = True
        else:
            print('Invalid option')
        print('--------------------------------')
    
def post_exercise(nutri_manager) -> bool:
    exercise_query = input('Tell me which exercises you did: ')
    response = nutri_manager.post_exercise(exercise_query)
    nutri_manager.save_exercise(response)

if __name__ == '__main__':
    main()

