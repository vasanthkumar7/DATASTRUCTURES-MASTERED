class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert_in_binary_tree(head,i):
    if head==None:
        head=node(i)
        return head

    root=head

    q=[]
    q.append(root)

    while len(q):
        temp=q[0]
        q.pop(0)

        if not temp.left:
            temp.left=node(i)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right=node(i)
            break
        else:
            q.append(temp.right)

    return head

def insert_list_in_binary_tree(head,l):
    for i in l:
        head=insert_in_binary_tree(head,i)
    return head

def inoder_traversal(head):
    if head:
        print(head.data,"->",end="")
        inoder_traversal(head.left)
        inoder_traversal(head.right)

def find_deep(head,node,count,l):
    if head:
        if head==node:
            l.append([count,node])
        find_deep(head.left,node,count+1,l)
        find_deep(head.right,node,count+1,l)

def find_traversal(head,root,l,count):
    if root:
        find_deep(head,root,0,l)
        find_traversal(head,root.left,l,count+1)
        find_traversal(head,root.right,l,count+1)
def level_order(head):
    l=[]
    root=head
    find_traversal(head,root,l,0)
    for i in range(len(l)-1):
        mins=l[i][0]
        pos=i
        for j in range(i+1,len(l)):
            if l[i][0]>l[j][0]:
                pos=j
                mins=l[j][0]
        if l[i][0]!=mins:
            temp=l[i]
            l[i]=l[pos]
            l[pos]=temp
    for i in l:
        print(i[1].data,end="->")


    
    

head=None
l=[1,2,3,4,5,6,7,8,9]
head=insert_list_in_binary_tree(head,l)
print("level order traversal")
level_order(head)
    
