# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ans=ListNode()
        current = ans
        ptr1=list1
        ptr2=list2
        while ptr1 or ptr2:
            val1 =  ptr1.val if ptr1 else  None
            val2 =  ptr2.val if ptr2 else  None
            if(ptr1 and ptr2):
                if(val1<=val2):
                    current.next=ListNode(val1)
                    ptr1=ptr1.next
                else:
                    current.next=ListNode(val2)
                    ptr2=ptr2.next
            elif ptr1:
                    current.next=ListNode(val1)
                    ptr1=ptr1.next
                    
            else :
                    current.next=ListNode(val2)
                    ptr2=ptr2.next
            current=current.next
        return ans.next
                
                    
                
        
        
       


