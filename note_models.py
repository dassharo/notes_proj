from model import User

class Author(User):
    def __init__(self,
                 login,
                 password):
        super().__init__(login,password)
        self.notes = []


class Note:
    def __init__(self,
                 title,
                 text):
        self.title = title
        self.text = text
    def show(self):
        print(f"""{self.title}
{self.text}""")

authors = []
