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
    print("")


def enter_list_in_linkedlist(head,root,lis):
    for i in lis:
        head,root=insert_linkedlist(i,head,root)
    return head,root


def delete_a_node_in_pos(head,pos):
    prev=None
    root=head
    count=0
    while root:
        if count==pos-1 and pos!=0:
            root.next=root.next.next
            return head
        elif pos==0:
            head=head.next
            return head
        count+=1
        root=root.next

        
            
head=None
root=head
lis=[1,2,3,4,5,6,7]
head,root=enter_list_in_linkedlist(head,root,lis)
print("before deleting at position: 2")
print_linkedlist(head)
head=delete_a_node_in_pos(head,5)
print("after deleting at position: 2")
print_linkedlist(head)
