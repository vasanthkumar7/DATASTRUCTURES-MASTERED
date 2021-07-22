class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert_linkedlist(d,head,root):
    if head==None:
        head=Node(d)
        head.next=None
        root=head
    else:
        n=Node(d)
        n.next=None
        root.next=n
        root=n
    return head,root

def print_linkedlist(head):
    root=head
    
    while root:
        print(root.data,"->",end="")
        root=root.next


def enter_list_in_linkedlist(head,root,lis):
    for i in lis:
        head,root=insert_linkedlist(i,head,root)
    return head,root
def count(search,head):
    root=head
    count=0
    while root:
        if root.data==search:
            count+=1
        root=root.next

    return str(count)
head=None
root=head
lis=[1,2,3,3,4,5,3,6,7]
head,root=enter_list_in_linkedlist(head,root,lis)
print_linkedlist(head)
print("\n count of 3 :"+count(3,head))
