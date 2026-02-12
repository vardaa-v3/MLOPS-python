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
                           5. press any other key to exit from console""" )
        
        if user_input == "1":
            self.sigup()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.post()
        else:
            exit()

    def sigup(self):
        email = input("enter you email --- ")
        pwd = input("enter the password --- ")
        self.username = email
        self.pwd = pwd
        print("you have signed up successfully")
        print("\n")
        self.menu()

    def login(self):
        if self.username == '' and self.pwd == '':
            print("please singup first befor logging in ")
        else:
            uname = input("enter the email here")
            pwd = input("enter you password")

            if self.username == uname and self.pwd == pwd:
                print("you have signned in succefully")
                self.loggedin = True
            else :
                print("please regser you email first")

        print("\n")
        self.menu()

    def post(self):
        if self.loggedin == True:
            txt = input("enter the message to be posted")
            print(f" the post have been posted in the chat booy as fallows {txt}")
        else:
            print("please sign in first ")

        print("\n")
        self.menu()




obj = chatbook()
