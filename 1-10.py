#multilevel inheritamce












class person:
    def eating(self):
        print("eating")
    def sleep(self):
        print("sleeping")
    def walk(self):
        print("walking")
class student():
    def read(self):
        print("reading")
class professional(person,student):
    def work(self):
        print("working")
    def login(self):
        print("login in time")
    def salary(self):
        print("salary credited")
p=professional()
p.walk()
p.read()
p.work()





















#hierarachial inheritance
class person:
    def eating(self):
        print("eating")
    def sleep(self):
        print("sleeping")
    def walk(self):
        print("walking")
class student(person):
    def read(self):
        print("reading")
    def write(self):
        print("writing")
class professional(person):
    def work(self):
        print("working")
    def login(self):
        print("login in time")
    def salary(self):
        print("salary credited")
p=professional()
s=student()
p.walk()
p.work()
s.walk()
s.write()




#hybrid
class person:
    def eating(self):
        print("eating")
    def sleep(self):
        print("sleeping")
    def walk(self):
        print("walking")
class student(person):
    def read(self):
        print("reading")
    def write(self):
        print("writing")
class professional(person):
    def work(self):
        print("working")
    def login(self):
        print("login in time")
    def salary(self):
        print("salary credited")
class Human(student,professional):
    def work(self):
        print("cooking")
    def sleep(self):
        print("sleeping")
s=Human()
s.walk()
s.read()
s.login()
s.salary()

#polimorphism
print(5+8)
print('5'+'8')
#metho overriding


class first():
    def one(self):
        print("i am first method from the class 1")
class second(first):
    def second(self):
        print("i am second methos from the class 2")
s=second()
s.one()



class first():
    def one(self):
        print("i am first method from the class 1")
class second(first):
    def one(self):
        super().one()
        print("i am second methos from the class 2")
s=second()
s.one()



class first():
    def one(self):
        print("i am first method from the class 1")
class second(first):
    def one(self):
        first.one(self)
    
        super().one()
        print("i am second methos from the class 2")
s=second()
s.one()




class payment():
    def pay(self):
        print("payment is processing")
class upi(payment):
    def pay(self,amount):
        print(f"payment through upi:{amount}")
        print("transaction successful")
class net_banking(payment):
    def pay(self,amount):
        print(f"payment through net_banking :{amount}")
class card(payment):
    def pay(self,amount):
        print(f"payment through card :{amount}")
s=[card(),upi(),net_banking(),]
for i in s:
              i.pay(int(input("enter amount:")))
        



#method overloading


class payment:
    def pay(slef,*x):
        for i in x:
            print(i,end=" ")
s=payment()
s.pay(4,6,7)
s.pay(4,6,7,7,8,9,10)
            


















        
    
        





















