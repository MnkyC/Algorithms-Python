'''
13 Roman to Integer
罗马数字包含I,V,X,L,C,D,M，对应数值1,5,10,50,100,500,1000
罗马数字2写做II，12是XII，27是XXVII，通常小的数字在右边
4是IV，9是IX，小的在左边，这种特殊情况只适用于: I和V,X(4,9)，X和L,C(40,90)，C和D,M(400，900)
给定罗马数字转为整数，输入范围[1-3999]
'''
def romanToInt(s):
    map = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    size = len(s) - 1
    rlt = 0

    for i in range(size):
        rlt = rlt - map.get(s[i]) if map.get(s[i]) < map.get(s[i+1]) else rlt + map.get(s[i])

    return rlt + map.get(s[-1])
