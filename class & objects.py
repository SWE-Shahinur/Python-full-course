class ten:
    student=60
all=ten()
print(all.student)


class nine:
    name=''
    age=''
    roll=''
obj=nine()
obj.name='shahinur'
obj.age=24
obj.roll=2487
print(f"name: {obj.name},roll: {obj.roll}")

sha=nine()
sha.name='sharmin'
sha.age=20
sha.roll=247
print(f"name: {sha.name},roll: {sha.roll}")


print("*************")
class eight():
    def __init__(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
s1=eight('sha',23,22)
print(s1.name)
