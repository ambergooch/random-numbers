import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))
print(my_randoms)

# for number in range(1, 10):
#     if my_randoms.count(number) > 0:
#         print(f"my_randoms list contains {number}")
#     else:
#         print(f"my_randoms list does not contain {number}")

# for number in range(1,6):
#     if my_randoms.__contains__(number):
#         print(f"my randoms list contains {number}")
#     else:
#         print(f"my_randoms list does not contain {number}")

for number in range(1,6):
    if number is my_randoms:
        print(f"my randoms list contains {number}")
    else:
        print(f"my_randoms list does not contain {number}")

# for number in range(1, 10):
#     the_numbers_match = False
#     # Iterate your random number list here
#     for num in my_randoms:
#          # Do the two numbers match? Change the boolean.
#          if number == num:
#             the_numbers_match = True

#     if the_numbers_match == True:
#         print(f'{number} is in the random list')
#     else:
#         print(f'{number} is not in the random list')


