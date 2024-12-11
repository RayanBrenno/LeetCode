def primeSubOperation(nums):

    def isPrime(value):
        if value <= 1:
            return False
        for x in range(2, value):
            if value % x == 0:
                return False
        return True

    for x in range(len(nums)):
        value = nums[x] if x == 0 else nums[x] - nums[x - 1]

        if value <= 0:
            return False

        prime = 0

        for y in range(value-1, -1, -1):
            if isPrime(y):
                prime = y
                break

        nums[x] -= prime

    print(nums)

    return True


nums = [5, 8, 3]
print(primeSubOperation(nums))
