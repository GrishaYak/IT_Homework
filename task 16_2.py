nums = []
num = int(input())
while num:
	if 100 > num > 9:
		nums.append(num)
	num = int(input())
if nums:
	print(round(sum(nums) / len(nums), 1))
else:
	print('NO')
