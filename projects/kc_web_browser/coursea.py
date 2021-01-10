# # # #
# # # # def print_prime_factors(number):
# # # #     # Start with two, which is the first prime
# # # #     factor = 2
# # # #     # Keep going until the factor is larger than the number
# # # #     while factor <= number:
# # # #         # Check if factor is a divisor of number
# # # #         if number % factor == 0:
# # # #             # If it is, print it and divide the original number
# # # #             print(factor)
# # # #             number = number / factor
# # # #         else:
# # # #             # If it's not, increment the factor by one
# # # #             factor +=1
# # # #     return "Done"
# # # #
# # # #
# # # # print_prime_factors(100)
# # # # # Should print 2,2,5,5
# # # # # DO NOT DELETE THIS COMMENT
# # # # def is_power_of_two(n):
# # # #     # Check if the number can be divided by two without a remainder
# # # #     while n % 2 == 0:
# # # #         n = n / 2
# # # #     # If after dividing by two the number is 1, it's a power of two
# # # #     if n == 1:
# # # #         return True
# # # #     return False
# # # #
# # # #
# # # # print(is_power_of_two(0))  # Should be False
# # # # print(is_power_of_two(1))  # Should be True
# # # # print(is_power_of_two(8))  # Should be True
# # # # print(is_power_of_two(9))  # Should be False
# # # #
# # # #
# # # # def is_power_of_two(n):
# # # #     # Check if the number can be divided by two without a remainder
# # # #     while n % 2 == 0:
# # # #         n = n / 2
# # # #     # If after dividing by two the number is 1, it's a power of two
# # # #     if n == 1:
# # # #         return True
# # # #     return False
# # # #
# # # #
# # # # print(is_power_of_two(0))  # Should be False
# # # # print(is_power_of_two(1))  # Should be True
# # # # print(is_power_of_two(8))  # Should be True
# # # # print(is_power_of_two(9))  # Should be False
# # #
# # #
# # # # def is_power_of_two(n):
# # # #     # Check if the number can be divided by two without a remainder
# # # #     while n !=0 and n  % 2 == 0:
# # # #         n = n / 2
# # # #
# # # #     # If after dividing by two the number is 1, it's a power of two
# # # #     if n == 1:
# # # #         return True
# # # #     return False
# # # #
# # # #
# # # # print(is_power_of_two(0))  # Should be False
# # # # print(is_power_of_two(1))  # Should be True
# # # # print(is_power_of_two(8))  # Should be True
# # # # print(is_power_of_two(9))  # Should be False
# # #
# # #
# # # def sum_divisors(n):
# # #     sum = 0
# # #     # Return the sum of all divisors of n, not including n
# # #     return sum
# # #
# # #
# # # print(sum_divisors(0))
# # # # 0
# # # print(sum_divisors(3))  # Should sum of 1
# # # # 1
# # # print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# # # # 55
# # # print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# # #
# # #
# # # # 114
# # #
# # # # def multiplication_table(number):
# # # #     # Initialize the starting point of the multiplication table
# # # #     multiplier = 1
# # # #     # Only want to loop through 5
# # # #     while multiplier <= 5:
# # # #         result = number * multiplier
# # # #         # What is the additional condition to exit out of the loop?
# # # #         if result >25 :
# # # #             break
# # # #         print(str(number) + "x" + str(multiplier) + "=" + str(result))
# # # #         # Increment the variable for the loop
# # # #         multiplier+= 1
# # # #
# # # #
# # # # multiplication_table(3)
# # # # # Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
# # # #
# # # # multiplication_table(5)
# # # # # Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
# # # #
# # # # multiplication_table(8)
# # # # # # Should print: 8x1=8 8x2=16 8x3=24
# # # # for i in range(1,11):
# # # #   print(i ** 3)
# # # #
# # #
# # # #
# # # # x = lambda e ,f : e * f
# # # # print(x(3,2))
# # #
# # # def myfun(n):
# # #     return lambda a: a * n
# # #
# # # # print(myfun(3))
# # # ee= myfun(24)
# # # print(ee(2))
# # #
# #
# #
# # # x='hello'
# # # x='goodbye'
# # # print('hello',x)
# #
# # def fd(a, c):
# #     return a + c
# #
# #
# # p = map(fd, ('orange','awero'),('ear','rat'))
# #
# # print(p)
# #
# # print(list(p))
#
#
# # filter
#
# names = ['kc','ema','raila']
#
# o = list(filter(lambda names: len(names) == 3, names))
# print(o)

nums = range(1000)

r = list(filter(lambda nums: nums % 7 == 0 or nums % 3 == 0,  nums))

print(sum(r))

########### 214216
