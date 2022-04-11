# This is the listener, the handler of events. It is the surface that 
# contacts the changes made with the logging system

from lib.log import log_stuff
from .events import subscribe

def handle_log_user_registered_event(user):
    """This function handles the user creation info to the logging system.
    It works as the middleman ..."""
    log_stuff(f"User {user.name} created, with and email {user.email}")

def setup_handle_log_user_creation():
    """This function activates (sets up) the logging system.
    It tells the app when to log the user creation."""
    subscribe('user_creation',handle_log_user_registered_event)