''''
def greet(name ="Guest"):
    print(f"Hello,{name}!")
greet()
print("harsha")
'''
'''
def greet(name="Guest"):
    print("Hello,", name)

greet()          
greet("Kate")
'''
'''
def student (fn,ln="vardhan" ,std="fifth"):
    print(fn,ln,"studied in",std, "standard")
    return list(ln)

student("harsha")
student(fn='harsha',std='B.tech')
student('ajay','kumar',std='tenth')
'''
'''
def add_item(item, quantity,d={}):
    d[item]=quantity
    return d 
print(add_item("notes",3,{}))
print(add_item("pen",5))
''
def itm_lst(item,lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
print(itm_lst("notes"))
print(itm_lst("pen"))
print(itm_lst("pencil"))

def add_item(item,qty,d=None):
    if d is None:
        d = {}
    d[item]=qty
    return d
print(add_item("notes",3))
print(add_item("pen",5))
print(add_item("pencil",2))
''
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
s1=student("harsha",20)
print(s1.name)
print(s1.age)
''
class Shop :

    def __init__(self,item,price,id):
        self.item=item
        self.price=price
        self.id=id        #basic structure of class and object
s1=Shop("pen",10,101)
print(s1.item)
i1=Shop("pencil",5,102)
print(i1.price)
''
class human:
    species="men"
    def __init__(self,gender,age):
        self.gender=gender
        self.age=age
        pass
h1=human("male",25)
print(h1.gender,h1.age,h1.species)
''
class Animal:
    def __init__(self,name,area):
        self.name=name
        self.area=area
a1=Animal("Dog","House")
print(a1.name,a1.area)
a2=Animal("Cat","House")
print(a2.name,a2.area)
''
# BASIC CODE FOR CLASS AND OBJECT USING THE EXAMPLE OF lIBRARY MANAGEMENT SYSTEM
class Book:
    def __init__(self,book_name,author,price):
        self.book_name=book_name
        self.author=author
        self.price=price
    
    def display(self):
        print("Book Name:",self.book_name)
        print("Author is:",self.author)
        print("price is:",self.price)      #constructor and method for class book

d1=Book("FOcus","Harsha Vardhan",300)   # CREATING object of class book
d1.display()             #calling method using object
''
# EXAMPLE-->2
#Create a class for hospital patient records
class Patitent:
    def __init__(self,patitent_name,age,disease):
        self.patitent_name=patitent_name
        self.age=age
        self.disease=disease
    def display(self):
        print("Patitent_Name:",self.patitent_name)    
        print("Patitent_Age:",self.age)
        print("Disease:",self.disease)
p1=Patitent("Mukesh",45,"cancer")
p1.display()
'''
'''
#EXAMPLE-->3
#Shopping Cart program using Class and Object concepts in Python.

class ShoppingCart:

    def __init__(self):
        self.items = []

    # Add item to cart
    def add_item(self, item):
        self.items.append(item)
        print(item, "added to cart")

    # Remove item from cart
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(item, "removed from cart")
        else:
            print(item, "not found in cart")

    # Display cart items
    def display_cart(self):
        print("\nShopping Cart Items:")
        
        if len(self.items) == 0:
            print("Cart is empty")
        else:
            for item in self.items:
                print("-", item)


# Creating object
cart = ShoppingCart()

# Adding items
cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

# Display items
cart.display_cart()

# Remove item
cart.remove_item("Mouse")

# Display again
cart.display_cart()
''
class Library:
    def __init__(self):
        self.books=[]
        def add_book(self,book):
            self.books.append(book)
            print(book,"added to the library")
        def remove_book(self,book):
            if book in self.books:
                self.books.remove(book)
                print(book,"removed from the library")
            else:
                print(book,"not found in the library")
        def display_books(self):
            print("/nBoooks in the library:")
            if len(self.books)==0:
                print("Library is empty")
            else:
                print("Book in the library")
# Creating object

'''
class Dog:
    species="canine"
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Breed",self.breed)
        print("Age:",self.age)
d1=Dog("Bunny","Labrador",13)
d2=Dog("Tommy","Bulldog",8)
d1.display()
d2.display()