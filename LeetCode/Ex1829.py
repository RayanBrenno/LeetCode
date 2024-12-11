def getMaximumXor(nums, maximumBit):
    def calc(limite):
        aux = 0
        for x in range(limite):
            aux ^= nums[x]
        print(aux, aux ^ maxBit)

    output = []
    maxBit = (2 ** maximumBit) - 1
    aux = 0
    for x in nums:
        aux ^= x
        print(aux)
    print(aux, aux ^ maxBit)
    for x in range(len(nums)-1, -1, -1):
        calc(x)
        output.append(aux ^ maxBit)
        aux ^= nums[x]

    return output

    """
    output = []
    maxBit = (2 ** maximumBit) - 1

    for x in range(len(nums)-1,-1,-1):
        aux = 0
        while x > -1:
            aux = aux ^ nums[x]
            x -= 1
        
        output.append(aux^maxBit)
        
    return output
    """


nums = [2, 3, 4, 7]
maximumBit = 3
print(getMaximumXor(nums, maximumBit))
