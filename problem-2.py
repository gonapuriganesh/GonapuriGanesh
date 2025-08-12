
def generate_odd_series(number):

	odd_numbers=[]

	for i in range(1,2*number,2):
		odd_numbers.append(str(i))

	return ", ".join(odd_numbers)

num = 3
output = generate_odd_series(num)
print(f"input a = {num}, then output: {output}")