def count_multiples(numbers):

    #empty dictionary to store values
	 multiples_counts={}

	# checking the multiples of numbers from 1 to 9

	 for divisor in range(1,10):
          count = 0
          for number in numbers:
          	if number % divisor == 0:
          		count += 1
          		multiples_counts[divisor] = count
	 return multiples_counts


input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

output_counts = count_multiples(input_list)

print(f"{input_list}")
print(f"{output_counts}")

