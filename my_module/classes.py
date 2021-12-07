from my_module.functions import check_all_capital

"""Classes used throughout project"""
class EncryptionInfo:
    def __init__(self):
        self.age = 0
        self.initials = ""
        self.pet = ""
        self.password = ""
        
    def login(self):
        '''
        Description:
        Prompt the user to input the information that will be used for encryption.
        '''
        is_valid = False
        while(not is_valid):
            self.initials = input("Please input your initials in capital letters: \n")
            is_valid = len(self.initials) > 0 and check_all_capital(self.initials)
            if(not is_valid):
                print("Invalid input. Initials must be capital letters.\n")

        is_valid = False
        while(not is_valid):
            self.age = int(input("Pease input your age between 1 and 150: \n"))
            is_valid = self.age > 0 and self.age < 150
            if(not is_valid):
                print("Invalid input. age must be greater than 0 and smaller than 150.\n")

        self.pet = input("Pease input what pet you have: \n")

        is_valid = False
        while(not is_valid):
            self.password = input("Please input your password with 10 characters: \n")
            length = len(self.password)
            is_valid = length == 10
            if(not is_valid):
                print("Password must be a string with 10 characters.\n")