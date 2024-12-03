# GF --> F --> S

class GrandFather:
    gold = "2 Kg"

    def bhk1(self):
        print("1 BHK")


class Father(GrandFather):
    diamond = "22 Karat"

    def bhk2(self):
        print("2 BHK")

class Son(Father):
    btc = "1 BTC"

    def bhk3(self):
        print("3 BHK")

s = Son()      # Can Access Grandfather, Father, Son
print(s.gold)
print(s.diamond)
print(s.btc)

f = Father()    # Can Access Grandfather and Father
print(f.gold)
print(f.diamond)

g = GrandFather()    # Can Access Grandfather only
print(g.gold)