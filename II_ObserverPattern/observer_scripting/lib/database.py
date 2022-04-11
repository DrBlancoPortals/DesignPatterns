# This checks a supposed database and works to create or find users
#List of users
users = []

# It is nice to have users being classes, as we are providing info and methods (reset passwords)
class User:
    def __init__(self,name: str, password : str , email : str) -> None:
        self.name = name
        self.email = email
        self.password = password #Highly unrecomended -> This is not encoded... but whatever
        self.reset_code = ""

    def __repr__(self) -> str:
        """So we have a representation for the instatntiated user"""
        return f'NAME : {self.name} - PASSWORD {self.password} - EMAIL {self.email}'

    #This isn't used in my example, but I keep it to give some sort of extra functionality
    def new_password(self, code:str, new_password:str):
        """Method to change the password"""
        if code != self.reset_code:
            raise Exception('Invalid reset code')
        self.password = new_password


def create_user(name : str,password :str,email : str):
    """function that creates the users, called from this module somewhere else"""
    new_user = User(name,password,email)
    users.append(new_user)
    return new_user

def find_user(email:str):
    """Finder function for the potential users added to the database"""
    for user in users:
        if user.email == email:
            return user
    raise Exception(f"User with email {email} not found")

