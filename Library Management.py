import ast


class Library:
    def __init__(self, libr):
        self.libr = libr
        with open(str(self.libr) + "BookList.txt") as f:
            self.bookList = ast.literal_eval(f.read())
        with open(str(self.libr) + "LendDict.txt") as f:
            self.lendDict = ast.literal_eval(f.read())

    def display_books(self):
        print(f"Books available in {self.libr}\n")
        for item in self.bookList:
            print(">>", item)

    def lend_book(self, user, book):
        if book not in self.bookList:
            print(":: :: :: Book not available :: :: ::")
        elif book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            with open(str(self.libr) + "LendDict.txt", "w") as f:
                f.write(str(self.lendDict))
            print(":: :: :: Successful :: :: ::")
        else:
            print(f"Book is already issued by {self.lendDict[book]}")

    def return_book(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            with open(str(self.libr) + "LendDict.txt", "w") as f:
                f.write(str(self.lendDict))
            print(":: :: :: Successful :: :: ::\n")
        else:
            print("Book is not issued")

    def add_book(self, book):
        if book not in self.bookList:
            self.bookList.append(book)
            with open(str(self.libr) + "BookList.txt", "w") as f:
                f.write(str(self.bookList))
            print(":: :: :: Successful :: :: ::\n")
        else:
            print("Book is already available")

    def clear_library(self):
        print("!!!!!!  WARNING  !!!!!!\nTHIS WILL CLEAR ALL THE RECORDS INLUDING BOOKS AVAILABLE AND ISUUED BOOKS")
        a = input("Enter yes to continue : ").lower()
        if a == "yes":
            self.bookList = []
            self.lendDict = {}
            with open(str(self.libr) + "BookList.txt", "w") as f:
                f.write("[]")
            with open(str(self.libr) + "LendDict.txt", "w") as f:
                f.write(str(self.lendDict))
            print("+++Library is cleared+++")
        else:
            print("+++Operation is cacelled+++")


if __name__ == '__main__':
    aqLib = Library("Aqdas Library")
    while True:
        print(f"\n\n##### {aqLib.libr} #####\n")
        print("1. Display books\n2. Lend books\n3. Return book\n4. Add book\n5. Delete the library")
        userChoice = input()
        while userChoice not in ["1", "2", "3", "4", "5"]:
            userChoice = input()

        if userChoice == "1":
            aqLib.display_books()
        elif userChoice == "2":
            book = input("Enter the name of the book : ").capitalize()
            user = input("Enter your name : ")
            aqLib.lend_book(user, book)
        elif userChoice == "3":
            book = input("Enter the book : ").capitalize()
            aqLib.return_book(book)
        elif userChoice == "4":
            book = input("Enter book : ").capitalize()
            aqLib.add_book(book)
        elif userChoice == "5":
            aqLib.clear_library()
        print("\nEnter q to quit or c to continue")
        userChoice2 = "1"
        while userChoice2 != "c":
            userChoice2 = input()
            if userChoice2 == "q":
                print("Exiting...")
                exit()
