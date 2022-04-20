import email
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)



@dataclass
class User:
    name : str = 'John'
    surname : str = 'Doe'
    email: str = '123_noname@DoePlace.com'
    age : int = 35

    def __repr__(self) -> str:
        return f"USER {self.name} {self.surname} - AGE {self.age} - Email {self.email}"

    def fullname(self):
        return f"{self.name} {self.surname}"
    
    def reset_auto_email(self):
        self.email = f"{self.name.lower()}_{self.surname}@email.com"
