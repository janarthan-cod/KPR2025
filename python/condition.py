a = 10
b = 20
c = 30
if a > b and a > c:
    print("A is Greater")
elif b > a and b > c:
    print("B is Greater")
else:
    print("c is Greater")
for i in range(1,6,2):
    print(i)
def add():
    print(10+20)
add()
"""
list =[1,2,3,4,5];
for i in list:
    print(i)"""

tuple =(6,7,8,9);
for i in tuple:
    print(i)
print(type(tuple))

dictionary ={"name":"viky","password":"123456"}
print(dictionary["name"])
print(type(dictionary))
for key in dictionary:
    print(dictionary[key])