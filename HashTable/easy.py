'''
1 Two Sum
一个整数数组nums和目标值target，在nums中找到和为target的两个整数，返回它们的索引
假设每种输入只有一种答案，不能重复利用nums中相同的元素
'''
def twoSum(nums, target):
    hashTable = dict()

    for index, item in enumerate(nums):
        if target - item in hashTable:
            return [hashTable[target - item], index]

        hashTable[item] = index


'''
136 Single Number
一个非空整数数组nums，除了一个元素只出现一次外，其余元素都出现两次，找到只出现一次的元素，返回该元素
算法要有线性时间的复杂度O(n)，不用额外空间O(1)
'''
def singleNumber(nums):
    hashTable = dict()

    for item in nums:
        try:
            hashTable.pop(item)
        except:
            hashTable[item] = 1

    return hashTable.popitem()[0]
    # # 异或，任何值和0异或还是本身
    # value = 0

    # for item in nums:
    #     value ^= item

    # return value


'''
202 Happy Number
快乐数：对于正整数，每一次将该数替换为它位置上的数字的平方和，重复这个过程直到这个数字为1，也可能永远得不到1
若可以变成1，那么这个数就是快乐数
'''
def isHappy(n):
    pass
