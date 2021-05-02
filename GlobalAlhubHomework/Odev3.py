import random
name = input("İsminizi girin " )
print(f"Adam asmaca oyununa hoş geldin {name}")
kelimeler = ["yönetim" , "bilişim" , "sistem" , "akustik" , "istasyon" , "köpek" , "kedi" , "yengeç" , "karpuz" , "kiraz"]
kelime = random.choice(kelimeler) 
tahminSayisi = 5
harfler = [] 
x = len(kelime)
z = list('_' * x)
print(' '.join(z), end='\n')
while tahminSayisi > 0:
    y = input("Bir harf tahmin edin : ")
    if y in harfler:
        print("Lutfen daha once tahmin ettiginiz harfleri tekrar tahmin etmeyin...")
        continue

    elif len(y) > 1:
        print("Lutfen sadece bir harf girin.")
        continue

    elif y not in kelime:  
        tahminSayisi -= 1
        print("yanlis tahmin!. {} tane tahmin hakkiniz kaldi.".format(tahminSayisi))

    else:
        for i in range(len(kelime)):
            if y == kelime[i]:
                print("Dogru Tahmin")
                z[i] = y
                harfler.append(y)
        print(' '.join(z), end='\n')

    cevap = input("Kelimenin tamamını tahmin etmek istiyor musunuz? ['e' veya 'h'] : ")

    if cevap == "e":
        tahmin = input("Kelimenin tamamını tahmin edebilirsiniz : ")
        if tahmin == kelime:
            print(f"Tebrikler kazandın {name}")
            break
        else:
            tahminSayisi -= 1
            print("Yanlis tahmin ettiniz. {} tane tahmin hakkınız kaldı.".format(tahminSayisi))


    if tahminSayisi == 0:
        print(f"{name} Tahmin hakkın kalmadı. Kaybettin! Adam Asıldı.")
        break
