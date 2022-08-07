def replay():

        while True:
            try:
                #choice not in ('Yes','No'):
                choice = input("play again? Enter Yes or No ")
            except ValueError:
                print("Please print Yes or No exactly")
                
            if choice == 'Yes':
                print('New game!')
                return choice == 'Yes'
            elif choice == 'No':
                print('See ya!')
                break