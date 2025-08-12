def generate_condtional_odd_series(a):

     if a % 2 != 0:
        limit = a
     else:
        limit = a - 1

     odd_numbers = [str(i) for i in range(1, 2 * limit, 2)]
     return ",".join(odd_numbers)

num=5
output=generate_condtional_odd_series(num)
print(f" input a={num} then output is {output}")