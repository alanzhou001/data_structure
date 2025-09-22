def cal(n, order_list):
    buy_sum = dict()   # buy side计数 buy_sum[i] 表示价格为i的买单总量
    sell_sum = dict()  # sell side计数 sell_sum[i] 表示价格为i的卖单总量
    prices_set = set() # 存放所有出现过的价格

    for order in order_list:
        side, price, qty = order
        if side == 'B':
            # TODO 维护buy_sum和prices_set

        elif side == 'S':
            # TODO 维护sell_sum和prices_set

    prices = sorted(prices_set) # 所有出现过的价格升序排序
    K = len(prices)

    # 买方后缀和：≥P
    buy_ge = [0] * K
    s = 0
    for i in range(K - 1, -1, -1): # 从K-1逆序遍历到0
        # TODO 预处理buy side后缀和到buy_ge
        # buy_ge[P]表示价格>=P的买单总量


    # 卖方前缀和：≤P
    sell_le = [0] * K
    s = 0
    for i in range(K):
        # TODO 预处理sell side前缀和到sell_le
        # sell_le[P]表示价格<=P的卖单总量


    # 扫描寻找使得 V 最大的开盘价P*（题设保证唯一）
    best_idx = 0 
    best_v = min(buy_ge[0], sell_le[0])
    for i in range(K):
        # TODO 计算 V(prices[i]) 并找到使得 V 最大的开盘价P*
        

    return prices[best_idx], best_v


# 示例
orders = [
    ['B', 100, 5],
    ['S', 98, 3],
    ['S', 100, 4],
    ['B', 99, 2],
    ['B', 101, 10],
    ['S', 101, 7],
]
print(cal(len(orders), orders))  # 期望：(101, 10)