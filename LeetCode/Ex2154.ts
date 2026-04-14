function findFinalValue(nums: number[], original: number): number {
    let value = original;
    while (nums.includes(value)) {
        value *= 2;
    }
    return value;
}
