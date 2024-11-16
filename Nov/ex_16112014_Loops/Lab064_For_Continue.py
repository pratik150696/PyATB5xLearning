for number in range(10):
    if number % 2 == 0:
        continue
    else:
        print(number)

# | i | Condition | O/P |


# | 0 | 0 % 2 == 0 , True | Skip and Start from Beginning |
# | 1 | 1 % 2 == 0  , False | 1 |
# | 2 | 2 % 2 == 0 , True | Skip and Start from Beginning |
# | 3 | 3 % 2 == 0  , False | 3 |
# | 4 | 4 % 2 == 0 , True | Skip and Start from Beginning |
# | 9 | 9 % 2 == 0  , False | 9 |
