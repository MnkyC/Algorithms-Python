from collections import deque

# 346 Moving Average from Data Stream
# 一个整数数据流，一个滑动窗口大小，根据窗口大小计算所有整数移动平均值
class MovingAverage:

    def __init__(self, size):
        self.__queue = deque()
        self.__maxSize = size

    def next(self, value):
        self.__queue.append(value)
        if len(self.__queue) > self.__maxSize:
            self.__queue.popleft()

        return sum(self.__queue) / len(self.__queue)


# 933 Number of Recent Calls
# RecentCounter类，计算最近请求
# 只有一个方法ping(int t)，t以毫秒为单位，返回3000毫秒前到现在的ping数
# 任何处于[t - 3000, t]之内的ping都会被计算在内，包括当前时刻的ping
class RecentCounter:

    def __init__(self):
        self.__queue = deque()

    def ping(self, t):
        self.__queue.append(t)

        while self.__queue[0] < t - 3000:
            self.__queue.popleft()

        return len(self.__queue)
