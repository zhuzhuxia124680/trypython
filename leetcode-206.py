#迭代
class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next #临时保存下一个节点
        current.next = prev #反转指针
        prev = current #prev前移
        current = next_node #current后移
    return prev

#递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):#定义函数
            if not cur: return pre#终止条件
            res = recur(cur.next, cur)#递归下一节点
            cur.next = pre#修改指向
            return res#返回头节点
    
        return recur(head, None)#调用递归
