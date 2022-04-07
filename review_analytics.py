data = []
count = 0
length_sum = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
	print(data[0])
	print(len(data[0]))
print('The file is read completely with', len(data), 'data')

for d in data:
	length_sum = length_sum + len(d)
print('Average data length is', length_sum / len(data))


#data[0] 加到 data[999999]
total = []
i = 0
average = 0
while i < len(data) - 1:
	i = i + 1
	total.append(len(data[i]))
average = sum(total) / (len(data) - 1)
#print(total)
print('Average data length from Method-2 is', average)