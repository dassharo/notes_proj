from note_models import authors
from note_models import Author

author = Author(login,password)

def login():
    login = input("login:")
    password = input("password:")
    for author in authors:
        if author.check_data(login,password):
            return author

def registration():
    login = input("login:")
    password = input("password:")
    if login not in [user.login for user in authors]:
        authors.append(author)
        print("Зареєстровано успішно")

