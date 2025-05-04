d = {'a': 1, 'b': 2}
d2={'a':2,'b':2}
for key in d:
    if key in d2:
        if d[key]==d2[key]:
            print(key,":",d[key])
for i in range(10, -2, -2):  # 10, 8, ..., 2
    print(i)

print(5//2)
print(5/2)
class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"hi i am {self.name}")
p1=person("adi")
p1.greet()
from flask import Flask

app=Flask(__name__)
@app.route('/')
def home():
    print("this is home")