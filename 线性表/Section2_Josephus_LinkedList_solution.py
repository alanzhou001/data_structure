class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_circle(N):
    head = Node(1)  # 创建第一个节点
    current = head
    for i in range(2, N + 1):
        current.next = Node(i)  # 创建其他节点
        current = current.next
    current.next = head  # 形成循环链表
    return head

def josephus(N, M):
    if N == 1:
        return 1

    head = create_circle(N)
    current = head #记录当前个节点
    prev = None #记录前一个节点
    
    print("淘汰过程：")
    
    while current.next != current:  # 循环直到只剩一个节点
        # 找到要淘汰的节点的前一个节点
        for _ in range(M - 1):
            prev = current
            current = current.next
            
        # 淘汰节点
        to_delete = current  # 记录要删除的节点
        print(f"淘汰的节点: {to_delete.value}")  # 输出被淘汰的节点
        prev.next = to_delete.next  # 删除该节点
        current = prev.next  # 移动到下一个节点

    return current.value  # 返回最后剩下的节点的值

# 示例
N = 7
M = 3
last_person = josephus(N, M)
print(f"最后剩下的人在原始队伍中的位置是: {last_person}")
