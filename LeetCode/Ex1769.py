from typing import List


def minOperations(boxes: str) -> List[int]:

    auxArr = []
    for x in range(len(boxes)):
        if boxes[x] == "1":
            auxArr.append(x)
    res = []
    for i in range(len(boxes)):
        res.append(sum([abs(j-i) for j in auxArr]))
    return res


boxes = "11111"
print(minOperations(boxes))
