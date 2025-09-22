def josephus(N, M):
    people = list(range(1, N + 1))  # 创建一个表示每个人的数组
    index = 0  # 从第一个人开始
    
    while len(people) > 1:
        index = (index + M - 1) % len(people)  # 计算要淘汰的人的索引
        people.pop(index)  # 淘汰该人
    
    return people[0]  # 返回最后剩下的人的位置

# 示例
N = 7  # 人数
M = 3  # 每隔M个人淘汰一个
last_person = josephus(N, M)
print(f"最后剩下的人在原始队伍中的位置是: {last_person}")
