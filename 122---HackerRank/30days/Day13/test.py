from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(self):
        pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self,title,author)
        self.price=price

    def display(self):
        print('Title:',self.title)
        print('Author:',self.author)
        print('Price:',self.price)

f = open('input.txt','r')
input = f.readline

title=input().rstrip()
author=input().rstrip()
price=input().rstrip()

bk = MyBook(title,author,price)
bk.display()