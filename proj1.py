class chatbook:
    def __init__(self):
        self.username = ''
        self.pwd = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""welcome to chat bot !! please find the below options to proceed
                           1. press 1 to signup
                           2. prees 2 to login
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit from console""" )
        
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()


obj = chatbook()
