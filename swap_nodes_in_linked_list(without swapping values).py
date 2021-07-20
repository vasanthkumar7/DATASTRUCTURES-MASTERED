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

def swap_nodes(head,x,y):
    root=head
    pos1=None
    pos2=None
    while root:
        if root.data==x:
            pos1=[root,0]
        if root.next:
            if root.next.data==x:
                pos1=[root,1]
        if root.data==y:
            pos2=[root,0]
        if root.next:
            if root.next.data==y:
                pos2=[root,1]
        root=root.next

    if pos1[1]!=1 and pos2[1]!=1:
        temp=pos1[0].next
        temp2=pos1[0].next.next
        pos1[0].next.next=pos2[0].next.next
        pos1[0].next=pos2[0].next
        pos2[0].next.next=temp2
        pos2[0].next=temp
    else:
        if pos1[1]==1:
            temp=head
            temp2=head.next
            head.next=pos2[0].next.next
            head=pos2[0].next
            pos2[0].next.next=temp2
            pos2[0].next=temp
        else:
            temp=head
            temp2=head.next
            head.next=pos1[0].next.next
            head=pos1[0].next
            pos1[0].next.next=temp2
            pos1[0].next=temp
    return head
            
        
        
        
        

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
head=swap_nodes(head,2,4)
print("after deleting at position: 2")
print_linkedlist(head)
