arr = [0,1]
a = arr[-1]
b = arr[-2]
while a < 4000000:
	arr.append(a + b)
	a = arr[-1]
	b = arr[-2]
sum = 0
for i in arr:
	if i % 2 == 0:
		sum += i
print(sum)