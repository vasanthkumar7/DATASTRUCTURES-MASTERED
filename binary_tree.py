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

head=None
l=[1,2,3,4,5,6,7,8,9]
head=insert_list_in_binary_tree(head,l)

inoder_traversal(head)
    
