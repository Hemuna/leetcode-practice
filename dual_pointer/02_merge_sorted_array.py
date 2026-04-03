m = int(input())
n = int(input())
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
i = m-1
j = n-1
k = m+n-1
while i >= 0 and j >= 0:
    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1
while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1
print(nums1)

#为了将两个有序数组合并成一个有序数组，我们可以使用双指针的方法。我们设置三个指针i、j和k，分别指向nums1、nums2和合并后的数组的末尾。我们比较nums1[i]和nums2[j]的值，将较大的值放入nums1[k]中，并相应地移动指针。当其中一个数组被完全遍历后，我们将另一个数组剩余的元素直接复制到nums1中。时间复杂度是O(m+n)，其中m和n分别是两个数组的长度。空间复杂度是O(1)，因为我们只使用了常数级别的额外空间来存储指针和临时变量。
#2つのソートされた配列を1つのソートされた配列にマージするために、双方向のポインタを使用する方法があります。i、j、kの3つのポインタを設定し、それぞれnums1、nums
