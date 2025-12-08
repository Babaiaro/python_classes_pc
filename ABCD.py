class A:
    def show(self):
        print("class A")

class B(A):
    def show(self):
        print("class B")
        super().show()

class C(A):
    def show(self):
        print("class C")
        super().show()

class D(B, C):
    def show(self):
        print("class D")
        super().show()

class E(D,C):
    __init__(self):
    

d = D()

d.show()
