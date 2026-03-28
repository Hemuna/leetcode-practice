s = input()
stack = []
pairs = {')':'(', '}':'{', ']':'['}
valid = True
for ch in s:
    if ch in '({[':
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()
if valid and not stack:
    print("True ")
else:
    print("False ")

#我们使用一个栈来检查括号的匹配。对于每个左括号，我们将其压入栈中；对于每个右括号，我们检查栈顶是否是对应的左括号，如果不是，则字符串无效。如果遍历结束后栈不为空，说明有未匹配的左括号，也无效。时间复杂度是O(n)，空间复杂度是O(n)在最坏情况下（所有都是左括号）。
#括弧の対応を確認するためにスタックを使用します。左括弧が出現したらスタックに追加し、右括弧が出現したらスタックのトップと対応する左括弧を確認します。すべての文字を処理した後、スタックが空であれば有効な括弧列です。時間複雑度はO(n)で、空間複雑度は最悪の場合O(n)です（すべてが左括弧の場合）。