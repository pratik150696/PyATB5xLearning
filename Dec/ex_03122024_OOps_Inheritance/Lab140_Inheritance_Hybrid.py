# Hybrid Inheritance  ---> Multiple type of Inheritance

class A:

    def methodA(self):
        print("Method A")


class B(A):

    def methodB(self):
        print("Method B")


class C(A):

    def methodC(self):
        print("Method C")


class D(B, C):

    def methodD(self):
        print("Method D")


d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()
