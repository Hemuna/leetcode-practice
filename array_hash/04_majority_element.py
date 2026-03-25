n = int(input())
nums = list(map(int, input().split()))  
counts = {}
limit = n // 2
for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
    if counts[num] > limit:
        print(num)
        break
#时间复杂度是O(n)，因为我们需要遍历整个数组一次来统计每个元素的出现次数。空间复杂度是O(n)，在最坏的情况下，所有元素都不同，我们需要存储每个元素的计数。


n = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[n // 2])
#时间复杂度是O(n log n)，因为我们需要对数组进行排序。空间复杂度是O(1)，因为我们只使用了常数级别的额外空间来存储排序后的数组。

n = int(input())
nums = list(map(int, input().split()))
candidate = None
count = 0
for num in nums:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1
print(candidate)
#时间复杂度是O(n)，因为我们需要遍历整个数组一次来找到候选人。空间复杂度是O(1)，因为我们只使用了常数级别的额外空间来存储候选人和计数器。


