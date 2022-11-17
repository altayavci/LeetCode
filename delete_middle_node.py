class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Constructor to initialize the node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Method to print linked list
	def printList(self):
		temp = self.head
		
		while temp :
			print(temp.val, end="->")
			temp = temp.next

	# Function to add of node at the end.
	def append(self, new_data):
		new_node = ListNode(new_data)
		
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		
		while last.next:
			last = last.next
		last.next = new_node


class Solution:

    def __init__(self,middle=None):

        self.middle=middle

    def deleteMiddle(self, head,count=0):

        temp=None 
        
        if head is None:

            self.middle=count//2
            return head 

        if head.val !=None :
            
            temp=head
            temp.next=self.deleteMiddle(head.next,count+1)
    
            if count==self.middle:
                #örnek case 1,2,3 olsun !!!

                head=temp.next #head.val=3 oldu 
                temp=temp.next #burda da head.val 1 oldu, 2yi es geçmiş olduk 

            
        return temp

list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)

list2=LinkedList()
list2.head=Solution().deleteMiddle(list1.head)
print(list2.printList())