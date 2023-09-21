nums = [0, 1, 0, 3, 12]
n_of_zeros = nums.count(0)
while 0 in nums:
    nums.remove(0)
nums += n_of_zeros * [0]
print(nums)  # Сем підар
