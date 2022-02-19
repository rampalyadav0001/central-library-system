

class library:
    def __init__(self, listofbook):
        self.book = listofbook

    def listofbook(self):
        for books in self.book:
            print("*"+books)

    def borrowbook(self,borrowbook):
        if borrowbook in self.book:
            print(f"You have issued {borrowbook},please keep it safe")
            self.book.remove(borrowbook)
            return True
        else :
         print("Sorry this book is not present in the libarary")        
        return False
    def returnbook(self,returnbook):
        # returnbook = input("Enter the name of the book you want to return: ")
        self.book.append(returnbook)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class student:
          def borrowbook(self):
           self.borrowbook = input(
               "Enter the name of the book you want to borrow: ")
           return self.borrowbook

          def returnbook(self):
             self.returnbook = input(
                  "Enter the name of the book you want to return and add: ")
             return self.returnbook



if __name__ == '__main__':
    cantrallibrary = library(["algorithms", "clrs", "java", "python"])
    students=student() 
    while(True):
     print('''
    ==== Welcome to the central library ====
      1.list of book
      2.borrow book
      3.return book
      4.exit from library

    ''')
    
     a = int(input("Enter your choice\n"))
     if a == 1:
        cantrallibrary.listofbook()
     elif a == 2:
        cantrallibrary.borrowbook(students.borrowbook())
     elif a == 3:
        cantrallibrary.returnbook(students.returnbook())
     elif a==4:
        exit()
