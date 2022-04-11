# This is the script that mimmicks a registration process 
# -> It recieves a new user and mail, and stores it in some place
from lib.database import create_user
from .events import post_event

def register_new_user(name :str, password:str, email: str) -> None:
    """This function is in charge of registering users"""    
    user = create_user(name, password, email)
    post_event('user_creation',user)
    # So here, register user is the object. It does something (creates users) 
    # and notifies to the event system that such user has been created. 

    