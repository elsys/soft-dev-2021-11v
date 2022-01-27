import random

def create (rows, nums):
	for i in range(rows):
		num1=[]
		for j in range(i+1):
			num1.append(random.randint(0,100))
		nums.append(num1)
	return
	
rows = 100
nums = []
res = 0

create(rows, nums)
res = nums[0][0]

j = 0
for i in range(rows-1):
   res = res + max(nums[i+1][j], nums[i+1][j+1])
   if(nums[i+1][j] < nums[i+1][j+1]):
       j = j + 1

print(res)
