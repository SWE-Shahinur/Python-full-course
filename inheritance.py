#1ti class er boisisto onno 1ti  class a niye asa jay
class parant:
    def function(self):
        print("this is parant")

class child(parant):
    def function2(self):
        print("this is child function")
obj=child()
obj.function()
obj.function2()

print("**multiple inheritance**")
class parant:
    def function(self):
        print("this is parant")

class parant2(parant):
    def function3(self):
        print("thisis parant 2")
class child(parant2):
    def function2(self):
        print("this is child function")

obj=child()
obj.function()
obj.function2()
obj.function3()




print("**multilevel inheritance**")
class parant:
    def function(self):
        print("this is parant")

class parant2:
    def function3(self):
        print("thisis parant 2")
class child(parant,parant2):
    def function2(self):
        print("this is child function")

obj=child()
obj.function()
obj.function2()
obj.function3()


print("**harertical inheritance**")
class parant:
    def function(self):
        print("this is parant")

class parant2(parant):
    def function3(self):
        print("thisis parant 2")
class child(parant2):
    def function2(self):
        print("this is child function")

obj=child()
obj1=parant2()
obj1.function()
obj1.function3()



print("**multiple inheritance**")
class parant:
    def function(self):
        print("this is parant")

class parant2(parant):
    def function3(self):
        print("thisis parant 2")
class child(parant2):
    def function2(self):
        print("this is child function")

obj=child()
obj1=parant2()
obj1.function()
obj1.function3()


