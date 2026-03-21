n = int(input())
nums = list(map(int, input().split()))
target = int(input())
d={}
for i, num in enumerate(nums):   #for i in range(len(nums)):   num = nums[i]
    if target - num in d:
        print(d[target - num],i)
        break
    d[num] = i
else:
    print(-1)
#遍历一次数组，每次哈希查询是平均O(1),所以总复杂度是O(N)
#时间复杂度: O(N) - 遍历数组一次
#空间复杂度: O(N) - 哈希表最多存储N个元素
#配列を一回走査し、ハッシュの検索は平均O(1)なので、全体はO(n)です。
#時間計算量: O(N) - 配列を一回走査
#空間計算量: O(N) - ハッシュテーブルは最大N個の要素を保存
