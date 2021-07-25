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

def sort_an_linkedlist(head):
    root=head
    count=0

    while root:
        count+=1
        root=root.next

    root=head


    while root.next:
        curr=root
        currnext=root.next
        swap=root
        swapnext=root.next

        trav=root.next
        while trav:
            if swap.data>trav.data:
                swap=trav
                swapnext=trav.next
            trav=trav.next
        if swap.data!=curr.data:
            temp=curr.data
            curr.data=swap.data
            swap.data=temp
        root=root.next
                
                

    return head
            
        

def enter_list_in_linkedlist(head,root,lis):
    for i in lis:
        head,root=insert_linkedlist(i,head,root)
    return head,root

head=None
root=head
lis=[6,7,4,2,3,1]
head,root=enter_list_in_linkedlist(head,root,lis)
print_linkedlist(head)
print("")
sort_an_linkedlist(head)
print_linkedlist(head)
