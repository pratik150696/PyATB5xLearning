# Static Method   ----> Don't need to create Object of a class
#                       & You can access the function by using ClassName directly

class O:

    @staticmethod
    def sum(a,b):
        return a + b

    def sub(self,a,b):
        return a - b

print(O.sum(3,4))     # In Static Method we don't need to call object

print("-------------------------------")

obj_O = O()
result = obj_O.sub(3,4)
print(result)