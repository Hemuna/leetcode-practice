n = int(input())
prices = list(map(int, input().split()))
def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
        if price < min_price:
            min_price = price
    return max_profit
print(max_profit(prices))

#通过一次遍历，动态记录历史最低价格，并计算当前价格的最大利润差值，从而得到最大收益。
#时间复杂度是O(n)，因为我们需要遍历整个价格数组一次。空间复杂度是O(1)，因为我们只使用了常数级别的额外空间来存储最低价格和最大利润。
#一度の走査で過去の最安値を更新しながら、現在価格との差を計算して最大利益を求める。