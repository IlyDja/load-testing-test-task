with open(input()) as file:
    nums = [int(n) for n in file.read().split()]


def min_moves(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = (nums[n // 2 - 1] + nums[n // 2]) / 2
    return sum(abs(num - median) for num in nums)


print(min_moves(nums))
