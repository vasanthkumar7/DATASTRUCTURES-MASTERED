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
def swap_nodes(head,a,b):
    pos1=None
    pos2=None
    if a==b:
        return 

    root=head

    while root:
        if root.data==a:
            pos1=root
        if root.data==b:
            pos2=root

        root=root.next

    root=head
    prev=None
    prev1=None
    while root.next:
        if root.next.data==a:
            prev=root
        if root.next.data==b:
            prev1=root
        root=root.next

    if prev and prev1 and prev1!=pos1 and prev!=pos2:
        temp=pos1
        temp2=pos1.next
        pos1.next=pos2.next
        pos2.next=temp2
        prev.next=pos2
        prev1.next=pos1
        pos1=pos2
        pos2=temp
    elif prev1==pos1 and prev and prev1:
        temp=prev.next
        prev.next=pos2
        pos1.next=pos2.next
        pos2.next=pos1
    elif prev==pos2 and prev and prev1:
        temp=prev1.next
        prev1.next=pos1
        pos2.next=pos1.next
        pos1.next=pos2
    elif prev==None and prev1!=pos1 and prev!=pos2 :
        temp=head
        temp2=head.next
        head.next=pos2.next
        pos2.next=temp2
        prev1.next=head
        head=pos2
        pos2=temp
    elif prev1==None and prev1!=pos1 and prev!=pos2 :
        temp=head
        temp2=head.next
        head.next=pos1.next
        pos1.next=temp2
        prev.next=head
        head=pos1
        pos1=temp
    elif prev==None and prev1==pos1  :
        temp=head
        temp2=head.next
        head.next=pos2.next
        pos2.next=head
        head=pos2
    elif prev1==None and prev==pos2  :
        temp=head
        temp2=head.next
        head.next=pos1.next
        pos1.next=head
        head=pos1
    return head

    
head=None
root=head
lis=[1,2,3,4,5,6,7]
head,root=enter_list_in_linkedlist(head,root,lis)
print_linkedlist(head)
head=swap_nodes(head,6,7)
print("")
print_linkedlist(head)

