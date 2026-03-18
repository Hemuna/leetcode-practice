n = int(input())
nums = list(map(int, input().split()))
s = set()
for num in nums:
    if num in s:
        print("true")
        break
    s.add(num)
else:
    print("false")
#遍历数组一次是O（n），每次查询和添加元素到集合 中是O（1）， 所以总的时间复杂度是O（n）.
#空间复杂度是O（n），在最坏的情况下，所有元素都不重复，集合中需要存储n个元素。
#配列を一回走査するのはO（n）で、各要素をセットに追加するのはO（1）なので、全体の時間複雑度はO（n）です。
#空間複雑度はO（n）で、最悪の場合、すべての要素が重複していない場合、セットにn個の要素を保存する必要があります。