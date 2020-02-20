'''
数据结构基本都是数组和链表演变而来

数组：寻址容易，插入删除困难
链表：寻址困难，插入删除容易
哈希：寻址容易，插入删除也容易，不过基于数组实现，扩展困难，表基本填满后性能下降严重，所以必须提前知道有多少数据

给定一个值转换为偏移地址（通过哈希/散列函数得到哈希/散列值）来检索记录，其实是数组的一种演变
哈希函数得到的哈希值是非负数，“键”相同则哈希值一定相同，但是同一个哈希值不一定是同一个键，因为有哈希冲突

哈希冲突
    散列函数得到了相同的散列值，不能完全解决，但是可以降低冲突的概率
    开放寻址法插入
        线性探测，冲突了就往下走，直到不冲突就插入
        查找：线性探测
        删除：不是真正的删除，而是做标记，以后的操作就跳过该位置
        二次探测：每次探测都是原来的平方探测，散列表空间不够时很容易产生冲突，通常用一个阀值（“装载因子”）表示剩余空间大小
            装载因子 = 元素个数 / 散列表大小（0.75较合适）
    拉链法
        用链表，“键”得到的哈希值相同时，在散列表中对应位置加一条链表，冲突就往上加元素
        查找，删除时，没有得到哈希值对应的数据，就在对应的单链表中继续查找

python中的dict发生冲突时使用开放寻址法
'''


class HashTable(object):

    def __init__(self, capacity=16):
        # 表大小
        self.__capacity = capacity
        # 存放key
        self.__slots = [None] * capacity
        # 存放value
        self.__data = [None] * capacity

    def put(self, key, value):
        if self.size() > self.__capacity * 0.75:
            self.resize()

        hashValue = self.hashKey(key)

        if self.__slots[hashValue] is None:  # 哈希值对应的槽为空，直接放置
            self.__slots[hashValue] = key
            self.__data[hashValue] = value
        elif key == self.__slots[hashValue]:  # 新旧键值对的key相同，更新value
            self.__slots[hashValue] = value
        else:  # 槽有值，key也不同，发生冲突，重哈希继续探测，直到有空位
            nextSlot = self.rehashKey(hashValue)

            while self.__slots[nextSlot] is not None and self.__slots[nextSlot] != key:
                nextSlot = self.rehashKey(nextSlot)

            if self.__slots[nextSlot] is None:
                self.__slots[nextSlot] = key
                self.__data[nextSlot] = value
            else:
                self.__data[nextSlot] = value

    def remove(self, key):
        startSlot = self.hashKey(key)  # 记录初始哈希值，作为重哈希探测的停止条件
        value = None

        if self.__slots[startSlot] is None:
            value = None
        elif key == self.__slots[startSlot]:
            value = self.__data[startSlot]
            self.__slots[startSlot] = None
            self.__data[startSlot] = None
        else:  # 槽有值，key也不同，发生冲突，重哈希继续探测，直到空位或相同的key
            stop = False
            found = False
            target = self.rehashKey(startSlot)

            while self.__slots[target] is not None and not found and not stop:
                if key == self.__slots[target]:
                    found = True
                    value = self.__data[target]
                    self.__slots[target] = None
                    self.__data[target] = None
                else:
                    target = self.rehashKey(target)
                    if target == startSlot:
                        stop = True

        return value

    def get(self, key):
        startSlot = self.hashKey(key)
        value = None

        if self.__slots[startSlot] is None:
            value = None
        elif key == self.__slots[startSlot]:
            value = self.__data[startSlot]
        else:
            stop = False
            found = False
            target = self.rehashKey(startSlot)

            while self.__slots[target] is not None and not found and not stop:
                if key == self.__slots[target]:
                    found = True
                    value = self.__data[target]
                else:
                    target = self.rehashKey(target)
                    if target == startSlot:
                        stop = True

        return value

    def hashKey(self, key):
        return abs(key) % self.__capacity

    # hashValue是旧的散列值
    def rehashKey(self, hashValue):
        return (hashValue + 1) % self.__capacity

    def resize(self):
        data = self.__data.copy()
        self.__capacity = self.__capacity * 2
        self.__slots = [None] * self.__capacity
        self.__data = [None] * self.__capacity

        for key, value in enumerate(data):
            self.put(key, value)

    def size(self):
        count = 0
        for key in self.__slots:
            if key is not None:
                count += 1

        return count
