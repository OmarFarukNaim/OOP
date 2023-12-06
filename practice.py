import random
t = random.randint(0,100)
print(t)
a,b,c,d = 10, 11, 12, 14
print(c)
a = '''Hi every one
I am a boy'''
print(a.lower())
print(min(10,12,13,9,5,15))
print(max(23,54,66,78,19))
print(a[-3:])
test_string="Wellcome to Bangladesh"
for x, y in enumerate(test_string):
    print(x, y)

print(a.swapcase())
print(a.index('H'))
test_string.replace("l","a")
print(test_string.ljust(30), "This is my country.")
print(3//2)
a = "Bangla"
b = "Sheikh"
print(f"Joy {a} and Joy {b}")
print("Joy {} Joy {}".format(a,b))
a = "Bangladesh"
x = []
s =""
for i in a:
   x.append(i)
print(x)
for j in x:
    s+=j
print(s)

x = [1,2,3,4,5,6,"BD"]
x.append("w")
print(x)
x.insert(2,"Bangladesh")
print(x)
x.pop(0)
print(x)
#x.clear()
print(x)
t = x.count("Bangladesh")
print(t)
e = {}
v = lambda a,b : a + b
print(v(10,23))