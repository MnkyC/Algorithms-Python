# 1021 Remove Outermost Parentheses
# 非空有效字符串S进行原语化(不存在将S拆分为S=A+B的方法)分解，删除分解中每个原语字符串的最外层括号，返回S
def removeOuterParentheses(S):
    pass


# 1047 Remove All Adjacent Duplicates In String
# 小写字母组成的字符串S，选择相邻且相同的字母并删除，返回最终的字符串
def removeDuplicates(S):
    rlt = []

    for c in S:
        if rlt and c == rlt[-1]:
            rlt.pop()
        else:
            rlt.append(c)

    return ''.join(rlt)


'''
682 Baseball Game
棒球比赛，作为记录员，给一个字符串列表，返回所有回合得分总和
字符串类型
    整数，一轮得分，本轮得分
    '+'，一轮得分，本轮得分是前两轮有效回合得分的总和
    'D'，一轮得分，本轮得分是前一轮有效回合得分的两倍
    'C'，一个操作，获得的最后一个有效回合的分数无效
'''
def calPoints(ops):
    stack = []

    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(stack[-1] * 2)
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)


'''
496 Next Greater Element I
两个没有重复元素的数组nums1和nums2，nums1是nums2子集
找出nums1中每个元素在nums2中下一个比其大的值，不存在返回-1，最后总体返回一个列表
'''
def nextGreaterElement(nums1, nums2):
    stack = []
    map = {}

    # 遍历nums2，每个元素遇到更大的值就将其和下一个更大的值放到哈希表中
    for num in nums2:
        while stack and stack[-1] < num:
            map[stack.pop()] = num

        stack.append(num)

    # 遍历nums1，对于每个元素都在哈希表中进行查找得到更大的数
    return [map.get(num, -1) for num in nums1]


# 844 Backspace String Compare
# 两个只含有小写字母和字符'#'的字符串S和T，'#'表示退格，判断两者是否相等
def backspaceCompare(S, T):
    def filterChar(s):
        stack = []

        for c in s:
            if c == '#' and stack:
                stack.pop()
            else:
                stack.append(c)

        return str(stack)

    return filterChar(S) == filterChar(T)
