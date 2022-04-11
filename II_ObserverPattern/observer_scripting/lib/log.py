# This is the script that definde what the logging does

# In a real application, this is already coded in the logging module, 
# but this part is just for show ...
from datetime import datetime

def log_stuff(message:str):
    print(f'Logging {datetime.now()}  :  {message}')