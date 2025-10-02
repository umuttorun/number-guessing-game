import random

# 1. Kelime Listesi
kelimeler = [
    "python", "programlama", "bilgisayar", "algoritma", 
    "konsol", "yazilim", "gelistirme", "fonksiyon", 
    "degisken", "arayuz"
]

def kelime_sec(liste):
    """Verilen listeden rastgele bir kelime seçer."""
    return random.choice(liste)

def oyunu_oyna():
    """Adam Asmaca oyununun ana döngüsünü çalıştırır."""
    
    # Oyun başlangıcı ayarları
    gizli_kelime = kelime_sec(kelimeler)
    tahmin_edilen_harfler = []
    kalan_hak = 6  # Adam asma için tipik başlangıç hakkı
    
    print("🌟 Adam Asmaca Oyununa Hoş Geldiniz! 🌟")
    print(f"Toplam {kalan_hak} tahmin hakkınız var.")
    print("İyi şanslar!\n")

    # Oyun ana döngüsü
    while kalan_hak > 0:
        
        # Kelimenin anlık durumunu oluşturma
        gosterilen_kelime = ""
        for harf in gizli_kelime:
            if harf in tahmin_edilen_harfler:
                gosterilen_kelime += harf + " "
            else:
                gosterilen_kelime += "_ "
        
        print("-" * 30)
        print("Kelime:", gosterilen_kelime)
        print(f"Kalan Hakkınız: {kalan_hak}")
        
        # Eğer kelimenin tamamı tahmin edildiyse, döngüden çık ve kazanma mesajı ver.
        if "_" not in gosterilen_kelime:
            print(f"\n🎉 Tebrikler! Kelimeyi doğru tahmin ettiniz: **{gizli_kelime.upper()}** 🎉")
            break
            
        # Kullanıcıdan harf girişi alma
        tahmin = input("Bir harf tahmin edin: ").lower()

        # Giriş kontrolü (Tek harf, daha önce tahmin edilmemiş mi?)
        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lütfen sadece bir harf girin.")
            continue
        
        if tahmin in tahmin_edilen_harfler:
            print(f"Bu harfi ('{tahmin.upper()}') zaten tahmin ettiniz. Başka bir harf deneyin.")
            continue
            
        # Tahmini listeye ekle
        tahmin_edilen_harfler.append(tahmin)

        # Harf kontrolü
        if tahmin in gizli_kelime:
            print(f"✅ Harika! '{tahmin.upper()}' kelimede var.")
        else:
            kalan_hak -= 1
            print(f"❌ Yanlış tahmin! '{tahmin.upper()}' kelimede yok.")
            
        # Kalan hakkın kontrolü (Döngü bitiminde kaybetme durumu)
        if kalan_hak == 0:
            print("-" * 30)
            print("💀 Üzgünüm, tahmin haklarınız bitti. Adam asıldı! 💀")
            print(f"Gizli kelime: **{gizli_kelime.upper()}**")

# Oyunu başlat
if __name__ == "__main__":
    oyunu_oyna()
