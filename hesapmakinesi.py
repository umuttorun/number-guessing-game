
def hesaplama():
    def toplama(): 
        sonuc  = ilk + ikinci
        print(sonuc)
    def cikarma(): 
        sonuc = ilk - ikinci
        print(sonuc)
    def carpma():
        sonuc = ilk * ikinci
        print(sonuc)
    def bolme():
        sonuc = ilk / ikinci
        print(sonuc)

    ilk = int(input("Lutfen ilk sayiyi girin: "))
    ikinci = int(input("Lutfen ikinci sayiyi girin: "))
    print("Lutfen yapmak istediginiz islemi secin")
    opr = input("+ - * /")
    if opr == "+":
        toplama()
    elif opr == "-":
        cikarma()
    elif opr == "*":
        carpma()
    elif opr == "/":
        bolme()
while True:
    hesaplama()


