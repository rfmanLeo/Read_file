data = []
with open('food.txt', 'r') as f:
	for line in f:
		print(line)
		data.append(line)
		data.append(line.strip())

print(data)