class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def enque(self,x):
        while len(self.s1)!=0:
            self.s2.append(self.s1[-1])
            self.s1.pop()
        self.s1.append(x)

        while len(self.s2)!=0:
            self.s1.append(self.s2[-1])
            self.s2.pop()
    def deque(self):
        if len(self.s1)==0:
            print("q is empty")
            return
        x=self.s1.pop()
        return x


a=queue()
a.enque(1)
a.enque(2)
a.enque(3)
a.enque(4)
a.enque(5)
a.enque(6)
print(a.deque())
print(a.deque())
print(a.deque())

            
