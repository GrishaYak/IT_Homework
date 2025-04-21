N = 10
def ok(res):
	return res >= (N + 1) // 2

def yes_no(val):
	if val:
		return 'YES'
	return 'NO'

cnt = 0
n = int(input())
all_right = False
for i in range(n):
	res = int(input())
	if res == N:
		all_right = True
	cnt += not ok(res)
print(cnt)
print(yes_no(all_right))
