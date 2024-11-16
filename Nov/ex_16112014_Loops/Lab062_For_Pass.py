for i in range(0, 10, 1):
    if i == 5 or i == 6:
        print(i)
    else:
        pass    # it will skip remaining steps

    # | i | Condition | O/P |
    # | 0 | 0 == 5 , False | Nothing will print |
    # | 1 | 1 == 5 , False | Nothing will print |
    # | 2 | 2 == 5 , False | Nothing will print |
    # | 5 | 5 == 5 , True | 5 |
    # | 6 | 6 == 5 , False | Nothing will print |
    # | 9 | 9 == 5 , False | Nothing will print |



    # | i | Condition | O/P |
    # | 0 | 0 == 6 , False | Nothing will print |
    # | 1 | 1 == 6 , False | Nothing will print |
    # | 2 | 2 == 6 , False | Nothing will print |
    # | 5 | 5 == 6 , False | Nothing will print |
    # | 6 | 6 == 6 , True | 6 |
    # | 9 | 9 == 6 , False | Nothing will print |
