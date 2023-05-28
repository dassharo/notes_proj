from presenter import login,registration
from note_presenter import (get_note_number,
	create_note, note_menu)
while True:
    choice = input("1 registration 2 login 3 exit:")
    if choice == "1":
        registration()
    if choice == "2":
        user = login()
        if user:
            print("Ви увійшли")
            note_menu(author)
    if choice == "3":
        break
