import heapq


def isUgly(n: int) -> bool:
    if n <= 0:
        return False

    factors = [2, 3, 5]
    for factor in factors:
        while n % factor == 0:
            n //= factor

    return n == 1


def MynthUglyNumber(n: int) -> int:
    count = 0
    num = 1
    if n == 1:
        return 1
    else:
        while (count < n):
            factors = [2, 3, 5]
            temp = num
            for factor in factors:
                while temp % factor == 0:
                    temp //= factor
            if temp == 1:
                count += 1
            num = num + 1
            print(count, num)
    return num - 1


'''
使用要得到从小到大的第 nn 个丑数，可以使用最小堆实现。

初始时堆为空。首先将最小的丑数 11 加入堆。

每次取出堆顶元素 x，则 x 是堆中最小的丑数，由于 2x, 3x, 5x2x,3x,5x 也是丑数，因此将 2x, 3x, 5x 加入堆。

上述做法会导致堆中出现重复元素的情况。为了避免重复元素，可以使用哈希集合去重，避免相同元素多次加入堆。

在排除重复元素的情况下，第 n次从最小堆中取出的元素即为第 n 个丑数。
'''


def nthUglyNumber(n: int) -> int:
    factors = [2, 3, 5]
    seen = {1}
    heap = [1]

    for i in range(n - 1):
        curr = heapq.heappop(heap)
        for factor in factors:
            if (nxt := curr * factor) not in seen:
                seen.add(nxt)
                heapq.heappush(heap, nxt)

    return heapq.heappop(heap)


# print(nthUglyNumber(413))#364500
print(nthUglyNumber(413))
