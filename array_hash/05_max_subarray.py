n = int(input())
nums = list(map(int, input().split()))
max_sum = nums[0]
current_sum = nums[0]
for i in range(1, n):
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)
print(max_sum)

#为了求连续子数组的最大和，我们可以使用动态规划的方法。我们维护两个变量：current_sum表示当前子数组的和，max_sum表示迄今为止找到的最大子数组和。对于每个元素，我们比较将其加入当前子数组（current_sum + nums[i]）与单独作为一个新的子数组（nums[i]）哪个更大，并更新current_sum。然后，我们将current_sum与max_sum进行比较，更新max_sum。最终，max_sum就是我们要求的最大子数组和。
#时间复杂度是O(n)，因为我们需要遍历整个数组一次。空间复杂度是O(1)，因为我们只使用了常数级别的额外空间来存储这些变量。
#連続部分配列の最大和を求めるために、Kadaneのアルゴリズムを使用します。各位置で、現在の要素を前の部分配列の和に加えるか、単独の要素として新しい部分配列を開始するかを比較します。これにより、最大部分配列の和を効率的に求めることができます。
#時間複雑度はO(n)で、配列を一回走査する必要があります。空間複雑度はO(1)で、定数の追加スペースのみを使用します。