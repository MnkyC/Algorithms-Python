from collections import deque

# 582 Kill Process
# pid和ppid两个列表，杀掉父进程的话子进程也会被杀掉，一个父进程可以有多个子进程
def killProcess(pid, ppid, kill):
    rlt = []
    q = deque([kill])
    hashTable = dict()
    for item in ppid:
        hashTable[item] = []

    for index, item in enumerate(pid):
        hashTable.get(ppid[index]).append(item)

    while q:
        item = q.popleft()
        rlt.append(item)
        for value in hashTable.get(item, []):
            q.append(value)

    return rlt


# 621 Task Scheduler
def leastInterval(tasks, n):
    pass
