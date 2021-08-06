class stack:
    def __init__(self):
        self.s1=[]
        self.max=100

    def push(self,x):
        if self.isfull():
            print("stack overflow")
            return
        self.s1.append(x)
    def pop(self):
        if len(self.s1)==0:
            print("stack underflow")
            return
        x=self.s1.pop()
        return x
    def isempty(self):
        if len(self.s1)==0:
            return True
        return False
    def isfull(self):
        if len(self.s1)==self.max:
            return True
        return False

a=stack()
a.push(10)
a.push(20)
a.push(30)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
    
