class library:
    def __init__(self,title,author,is_available):
        self.title=title
        self.author=author
        self.is_available=is_available

    def borrow_book(self):
        if self.is_available==True:
            print("You have successfully borrowed a book")
            return self.is_available==False
        else:
            print("You cannot borrow a borrowed book again")

    def return_book(self):
        if self.is_available==False:
            print("You have successfully returned a book")
            return self.is_available==True
        else:
            print("You cannot borrow a borrowed book again")

book1=library("Harry Potter","J.K Rowling",True)
book2=library("Stephen Rowling","J.K Rowling",True)
book3=library("Rudyard Kipling","Jungle Book",False)

book_choice=int(input("Enter the choice of book you want in 1 to 3"))