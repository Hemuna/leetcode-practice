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
#配列を一回走査し、ハッシュの検索は平均O(1)なので、全体はO(n)です。
