public_toilet = "PB"

def home():
    private_toilet = "PT"
    print(public_toilet)
    print(private_toilet)



def strange():
    print(public_toilet)
    # print(private_toilet)  ----> Can not use outside

print(public_toilet)
# print(private_toilet)      -----> Can not use outside

# Local var has more preference than Local var