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
    return str(count)


def pairwise_swap(head):
    root=head
    while root:
        if root.next:
            temp=root.data
            root.data=root.next.data
            root.next.data=temp
            root=root.next.next
        else:
            root=root.next

    return head



        
head=None
root=head
lis=[1,2,3,4,5,6,7,8]
head,root=enter_list_in_linkedlist(head,root,lis)

print_linkedlist(head)
head=pairwise_swap(head)
print("after pairwise swap")
print_linkedlist(head)

