def readBinaryWatch(self, turnedOn: int) -> List[str]:
    ans = []
    for i in range(12):
        for j in range(60):
            if (bin(i).count('1') + bin(j).count('1')) == turnedOn:
                ans.append(str(i) + ":" + (str(j) if j > 9 else "0" + str(j)))
    return ans