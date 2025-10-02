kelimem = input ("Lutfen kelimeyi giriniz: ")
boyut = "-" * len(kelimem)
hak = 10
if len(kelimem) <= 1 or not kelimem.isalpha:
    print("lutfen sadece kelime yazin sayi ve isaretler gecersizdir")
print("OYUN BASLADİ 10 ADET YANLİS TAHMİN ETME HAKKİNİZ VAR")
print("kelime : " +boyut)
tahmin = input()
while hak > 0:
    gosterilenk = " " 
    for harf in kelimem:
        if harf in tahmin_edilenlerx

