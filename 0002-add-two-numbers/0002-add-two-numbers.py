# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(node: Optional[ListNode], res: List[int]) -> None:
            if node.next:
                traverse(node.next, res)
            res.append(node.val)
        
        arr1 = []
        traverse(l1, arr1)
        arr2 = []
        traverse(l2, arr2)

        n1 = int("".join([str(n) for n in arr1]))
        n2 = int("".join([str(n) for n in arr2]))
        summ = [int(c) for c in str(n1 + n2)]

        def build(node: ListNode, arr: List[int]) -> None:
            node.val = arr.pop()
            if arr:
                node.next = ListNode()
                build(node.next, arr)
        
        head = ListNode()
        build(head, summ)

        return head