class people:
    age=15
    name="zhangsan"
    @classmethod
    def run(self):
        print ("这是一个类方法")

    def eat(cls):
        print ("这是一个实例方法")
    
p=people()     
print(people.run())

print(p.eat())