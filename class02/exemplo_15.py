class MyClass:
    """A Simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def returnData(self):
        return self.data    

    def __init__(self):
        self.data=1234
        
x = MyClass()
print(x.f())
print(x.returnData())