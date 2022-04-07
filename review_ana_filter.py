data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))
print('The file is read completely with', len(data), 'data')


length_sum = 0
for d in data:
	length_sum = length_sum + len(d)		
print('Average data length is', length_sum / len(data))
print(d) #最後一條評論


short = []
for d in data:
	if len(d) < 100:
		short.append(d)
print('There are', len(short), 'reviews shorter than 100 words')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are', len(good), 'positive reviews')