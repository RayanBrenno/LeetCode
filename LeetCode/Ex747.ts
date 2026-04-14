function dominantIndex(nums: number[]): number {
    let maxIndex = 0;
    let maxValue = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > maxValue) {
        maxValue = nums[i];
        maxIndex = i;
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (i !== maxIndex && nums[i] * 2 > maxValue) {
        return -1;
        }
    }
    return maxIndex;
}


