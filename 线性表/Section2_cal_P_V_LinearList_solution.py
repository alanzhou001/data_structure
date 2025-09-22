def cal(n, order_list):
    
    buy_sum = dict()  # buy side计数 buy_sum[i] 表示价格为i的买单总量
    sell_sum = dict() # sell side计数 sell_sum[i] 表示价格为i的卖单总量
    prices_set = set()   # 存放所有出现过的价格

    for order in order_list:
        side, price, qty = order
        if side == 'B':
            buy_sum[price] = buy_sum.get(price, 0) + qty
            prices_set.add(price)
        elif side == 'S':
            sell_sum[price] = sell_sum.get(price, 0) + qty
            prices_set.add(price)

    prices = sorted(prices_set)
    K = len(prices)

    # 买方后缀和：≥P
    buy_ge = [0] * K
    s = 0
    for i in range(K - 1, -1, -1): # 从K-1逆序遍历到0
        p = prices[i]
        s += buy_sum.get(p, 0) # 返回buy_sum[p],若p不存在则返回0
        buy_ge[i] = s

    # 卖方前缀和：≤P
    sell_le = [0] * K
    s = 0
    for i in range(K):
        p = prices[i]
        s += sell_sum.get(p, 0) # 返回buy_sum[p],若p不存在则返回0
        sell_le[i] = s

    # 扫描寻找使得 V 最大的开盘价P*（题设保证唯一）
    best_idx = 0
    best_v = min(buy_ge[0], sell_le[0])
    for i in range(K):
        # 计算 V(prices[i])
        v = min(buy_ge[i], sell_le[i]) 
        if v > best_v:
            best_v = v
            best_idx = i

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