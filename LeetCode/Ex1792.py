from typing import List
import heapq

def maxAverageRatio(classes: List[List[int]], extraStudents: int) -> float:
    
    def newAvarage(passed, total):
        return ((passed + 1) / (total + 1)) - (passed / total)

    heap = [(-newAvarage(passed, total), passed, total) for passed, total in classes] 
    heapq.heapify(heap)
    
    for _ in range(extraStudents):
        current_gain, passed, total = heapq.heappop(heap)
        heapq.heappush(heap, (-newAvarage(passed+1, total+1), passed+1, total+1))

    return sum(passed/total for _, passed, total in heap)/len(heap)

    """
    avarage = [passed/total for passed, total in classes]
    for _ in range(extraStudents):
        newAvarage = [(passed+1)/(total+1) for passed, total in classes]
        index = 0
        aux = 0
        for x in range(len(classes)):
            dif = newAvarage[x] - avarage[x]
            if dif > aux:
                index = x
                aux = dif

        classes[index][0] += 1
        classes[index][1] += 1
        avarage[index] = newAvarage[index]

    return sum(avarage)/len(avarage)
    """


classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
extraStudents = 4
print(maxAverageRatio(classes, extraStudents))
