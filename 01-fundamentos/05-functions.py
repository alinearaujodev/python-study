def hello (name: str, age: int):
    print ("Hello {}, você tem {}".format(name,age))
    return age*2

dobro = hello("Aline", 22)
print("E o dobro da sua idade é {}".format(dobro))