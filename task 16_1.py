cnt = 0
n = int(input())
for i in range(n):
	cnt += int(input()) % 10 == 9
print(cnt)
