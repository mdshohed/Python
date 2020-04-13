class user:
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        email = input("Enter email: ")
        password =  input("Enter your passwoed: ")
        if email == self.email and password == self.password:
            login = True
            print("Login successful")
        else:
            print("Lofin faild!")
    def logou(self):
        login = False
        print("Logged out!")
    def islogin(self):
        if self.login:
            return  True
        else:
            return  False
    def profile(self):
        if self.islogin():
            print(self.name,'\n',self.email)
        else:
            print("User is not log out!")
user1  = user()
user1.name = "shohed"
user1.email = "mdshohed170@gmail.com"
user1.password = "sho439804"
user1.login()
user1.profile()
user1.login()
