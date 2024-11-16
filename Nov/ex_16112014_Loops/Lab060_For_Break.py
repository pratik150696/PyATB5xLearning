for i in range(0, 10):  # 0 - 9 ,   10 times
    if i == 5:
        print("FIVE")
    else:
        print(i)


# | i | Condition | O/P |
# | 0 | 0 == 5 , False | 0 |
# | 1 | 1 == 5 , False | 1 |
# | 2 | 2 == 5 , False | 2 |
# | 5 | 5 == 5 , True | FIVE |
# | 6 | 6 == 5 , False | 6 |
# | 9 | 9 == 5 , False | 9 |
# | 10 | 10 == 5 , False | For Loop Finished |


print("-----------------------")

for j in range(0 , 10):
    print(j)
    if j == 5:
        break    # Will break the loop