from random import randint
girdi = input("lutfen sifirla hangi sayi arasında tahmin yapmak istediğinizi giriniz: ")
aralik = int (girdi)
cevap = randint(0,aralik)
girdi2 = input("Lutfen ilk tahmininizi yaziniz: ")
tahmin = int(girdi2)
while cevap != tahmin:
    if cevap > tahmin:
        print("cevabin yanlis gözün biraz daha yukarlarda olsun")
        girdi2 = input("Lutfen siradaki tahmininizi yaziniz: ")
        tahmin = int(girdi2)
    else:
        print("cevabin yanlis hedefi kucultmeye ne dersin")
        girdi2 = input("Lutfen siradaki tahmininizi yaziniz: ")
        tahmin = int(girdi2)
        

if cevap == tahmin:
    print("TEBRİKLER! K A Z A N D I N :)")
bitme = input()

