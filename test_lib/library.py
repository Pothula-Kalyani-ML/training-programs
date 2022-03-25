
from user import Admin, Member,User
from book import Book
class Library():
    def __init__(self):
        self.books=[]
        self.members=[]
        self.admins=[]
        self.shelve=[]

    def add_books(self,book):
        self.books.append(book)

    def add_admins(self,admin):
        self.admins.append(admin)

    def add_member(self,member):
        self.members.append(member)
    def add_shelves(self,shelve):
        self.shelves.append(shelve)
    def book_existance(self,book_name):
        for item in self.books:
            if item.book_name == book_name:
                print(f"{item.book_name} book exists")    
    def display_avaliable_books(self):
            for item in self.books:
                if item.status == "available":
                    print(f"available book:book_id:{item.id}, book_name: {item.book_name}, author: {item.author}, status:{item.status} rack_no:{item.rack_no}")
    
if __name__ =="__main__":
    knl_library=Library()
    book1=Book(1,"aaa","ax","available",1)
    book2=Book(2,"bbb","bx","available",1)
    book3=Book(3,"ccc","cx","available",2)
    admin1=Admin("admin1","1A",415222222,"admin1@gmail.com")
    admin2=Admin("admin2","2A",4152252,"admin2@gmail.com")
    member1=Member("mem1","1M",987,"mem1@gmail.com")
    member2=Member("mem2","2M",564,"mem2@gmail.com")
    member3=Member()
    knl_library.add_member(member1)
    knl_library.add_member(member2)
    admin1.shelves_manges=[1,2]
    #print(admin1.shelves_manged)
    knl_library.add_books(book1)
    knl_library.add_books(book2)
    knl_library.add_books(book3)
    knl_library.add_admins(admin1)
    knl_library.add_admins(admin2)
    knl_library.display_avaliable_books()

    admin1.issue_book("aaa",knl_library.books,"mem1")
    admin2.issue_book("bbb",knl_library.books,"mem2")
    
    knl_library.display_avaliable_books()
    Admin.checked_out_books()
    knl_library.book_existance("ccc")
    member1.borrowed_books_by_member(Admin.issued_books)

