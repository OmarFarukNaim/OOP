try:
    prinr("Hello")
except:
    print("Now You are well.")

a = lambda a,b : a+b
print(a(10,23))

import datetime
o = datetime.datetime.now()
print(o.ctime())