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



def find_len_of_linkedlist(head):
    count=0
    root=head
    while root:
        count+=1
        root=root.next
    return count

def reverse_linkedlist(head):
    count=find_len_of_linkedlist(head)
    for i in range(count):
        cou=0
        root=head
        while cou<count-i:
            if root.next:
                temp=root.data
                root.data=root.next.data
                root.next.data=temp
            root=root.next
            cou+=1

    return head
            
head=None
root=head
lis=[1,2,3,4,5,6,7]
head,root=enter_list_in_linkedlist(head,root,lis)

print_linkedlist(head)
head=reverse_linkedlist(head)
print_linkedlist(head)
