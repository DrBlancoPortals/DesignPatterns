# This is the file from which the app is launched
# This is the file where the actual observer pattern is working, and we launch the 'app'

from api.registration import register_new_user
from api.log_listener import setup_handle_log_user_creation

#Having this here allows us to enable and disable users at will ...
setup_handle_log_user_creation()

if __name__ == '__main__':
    #Worst user ever
    register_new_user('Ambrosio','1234','ambrosio_1234@hotmail.com')
    