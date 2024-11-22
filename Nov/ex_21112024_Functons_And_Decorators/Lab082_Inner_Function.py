def outer_function():
    var1 = 30

    def inner_function():
        var2 = 10
        print(var1,var2)

    def inner_function2():
        print(var1)
        

        def inner_inner():
            print(var1)
        inner_inner()

    inner_function()
    inner_function2()

outer_function()
# inner_function()   ----> Can not called outside