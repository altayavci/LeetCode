
# Merging and sorting linked lists  (NODECEPTION)
# A linked list is a data structure in which each element contains a reference as well as a value. 
# Linked lists are one of the simplest and most used data structures. 
# The stack is often used to implement other abstract data structures such as queues.
# head -> data|next -> data|next -> data|next -> null

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
    def mergeTwoLists(self, list1,list2):
        
        temp=None 
        #while structure is recursive , code runs until the list1 or list2 is none

        if list1 is None :
            
            #if list1 is empty,returns list2

            #ALTINCI İTERASYON list1==None 
            #****************************
            #list2 => list2=Node(val=6,next=None)
            #EN SON ATAMAYA GİDER. list2 == temp  ataması, ÜÇÜNCÜ İTERASYONDA olmuş => mergeTwoLists(Node(val=4,next=Node(val=5,next=None)),Node(val=6,next=None)) döner
            #BURDAN SONRASINDA CALL STACKLERİ TEKER TEKER ÜSTÜNDEN GEÇECEK SEKİLDE RETURN EDER 
            #None elde edilene kadar iterasyon yapılarak recursive functionlar içindeki bilgiler ile call stack'te bekler.   
            #None elde edilinceye kadarki elde kalan son eleman aslında EN BÜYÜK elemandır, yani listenin sonundakidir.
            #None elde edildikten sonra next kısmıdna hep son eleman kalmış olur. 
            #Özetlersek baştan sona gidilir,sonrasında da sondan başa gidilir. bu şekilde merging ve sorting yapılmış olur.
            #Call stackler, threadlerde birikmiş işlemlerdir. 
            #Call stacklerde sürekli temp return edileceğinden Node(val,next=Node(..)) sorting de yapılmış olur. 
            
            # #****************************

            return list2 
        
        if list2 is None:

            #if lis2 is empty,returns list1
            return list1
        
        if list1.val<=list2.val:

            #checking list2>=list1 and if it is True,
            #list1 will assign to the temporary ListNode  (temp)
            #temp.next will assign to the mergeTwoLists which is the recursive function. 
            #mergeTwoLists(list1.next,list2) means that :
            
            temp=list1
            temp.next=self.mergeTwoLists(list1.next,list2) 

            #BİRİNCİ İTERASYON => list1[0]<list2[0]
            #****************************
            #next'lerin içinde node'lar var ,yani yapı şöyle => list1=Node(val=1,next=Node(val=4,next=Node(val=5,next=None)))
            #temp => Node(val=1,next=Node(val=4,next=Node(val=5,next=None)))
            #temp.next==list1.next => Node(val=4,next=Node(val=5,next=None))
            #list2 => Node(val=2,next=Node(val=3,next=Node(val=6,next=None)))
            #temp.next == list1.next => self.mergeTwoLists(Node(val=4,next=Node(val=5,next=None)),Node(val=2,next=Node(val=3,next=Node(val=6,next=None)))) oldu 
            #****************************

            #DÖRDÜNCÜ İTERASYON list1[1] < list2[2]
            #****************************
            #temp => =Node(val=4,next=Node(val=5,next=None))
            #list1.next => Node(val=5,next=None)
            #temp.next => mergeTwoLists(Node(val=5,next=None),Node(val=6,next=None))
            #GÜNCEL list1 =Node(val=5,next=None, list2=,Node(val=6,next=None)
            #****************************

            #BEŞİNCİ İTERASYON list1[2] < list2[2]
            #****************************
            #temp => Node(val=5,next=None)
            #list1.next => NONE 
            #temp.next => mergeTwoLists(None,Node(val=6,next=None))
            #GÜNCEL list1=None , list2=Node(val=6,next=None)
            #****************************

            #YEDİNCİ İTERASYON return lis2 
            #****************************
            #list1 =>Node(val=5,next=None)
            #list2 => Node(val=6,next=None) 
            #temp => Node(val=5,next=Node(val=6,next=None))
            #****************************



            
        else :
            
           
            temp=list2
            temp.next=self.mergeTwoLists(list1,list2.next) 

            #İKİNCİ İTERASYON list1[1]>list2[0]
            #****************************
            #şuan temp => Node(val=2,next=Node(val=3,next=Node(val=6,next=None))) == list2
            #temp.next=Node(val=3,next=Node(val=6,next=None)) == list2.next
            #list1= self.mergeTwoLists(Node(val=4,next=Node(val=5,next=None)),Node(val=2,next=Node(val=3,next=Node(val=6,next=None))))
            #ÇOK ÖNEMLİ !! mergeTwoLists in argumanlarına bakalım : list1,list2 (devamı aşağıda)
            #yani ŞUAN list1=Node(val=4,next=Node(val=5,next=None)), list2=Node(val=2,next=Node(val=3,next=Node(val=6,next=None)) oldu.
            #list2.next => Node(val=3,next=Node(val=6,next=None))
            #temp.next==list2.next => self.mergeTwoLists(Node(val=4,next=Node(val=5,next=None)),Node(val=3,next=Node(val=6,next=None))) OLDU !!
            #GÜNCEL list1 =Node(val=4,next=Node(val=5,next=None)) , list2=Node(val=3,next=Node(val=6,next=None)))
            #****************************

            #ÜÇÜNCÜ İTERASYON list1[1]>list2[1]
            #****************************
            #temp => Node(val=3,next=Node(val=6,next=None))
            #list2.next=Node(val=6,next=None)
            #temp.next => mergeTwoLists(Node(val=4,next=Node(val=5,next=None)),Node(val=6,next=None))
            #GÜNCEL list1=Node(val=4,next=Node(val=5,next=None)),list2=Node(val=6,next=None)
            #****************************


        return temp 

            #SEKİZİNCİ -> SONA KADAR İTERASYONLARDA BURAYA RETURN EDİLİR.



# Create linked list :
list1 = LinkedList()
list1.append(1)
list1.append(4)
list1.append(5)

# Create linked list 2 :
list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(6)

list3=LinkedList()

list3.head=Solution().mergeTwoLists(list1.head, list2.head)
list3.printList()
	

