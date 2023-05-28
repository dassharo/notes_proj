from presenter import author
def get_note_number(notes):
    while True:
        choice = input("Введіть номер:")
        if choice.isdigit() and 0 < int(choice) <= len(notes):
            return int(choice) - 1
    
def create_note():
    note = {"title": input("title: "),
                           "text": input("text: ")}
    print("Article created!")
    return note


def note_menu(author):
    while True:
        choice = input("""1 create
2 read all
3 read one
4 update
5 delete
6 exit
""")
        if choice == "1":
            note = create_note()
            author.notes.append(note)
        if choice == "2":
            print(author.notes)          
        if choice == "3":
            number = get_note_number(author.notes)
            print(author.notes[number])
        if choice == "4":
            number = get_note_number(author.notes)
            note = author.notes[number]
            note.update(author.create_note())

        if choice == "5":
            number = get_note_number(author.notes)
            author.notes.pop(number)
            print("видалено")
        
        if choice == "6":
            break
