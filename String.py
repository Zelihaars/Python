ad='Zeliha'
print('Üçüncü index :' + '  ' +  ad[3]) # 3.indeksi ekrana yazdırır
uzunluk=len(ad)
print('Son index : ' + ' ' + ad[uzunluk-1])#son indeksi ekrana yazdırı
print(ad[1:5])#1 den 5 e kadar ki indexleri ekrana yazar 
print(ad[::-1])#Tersten yazdırma
print(ad[1:6:2])#1 den başla 6 yı kadar iki iki ilerler ve ekrana yazdırır
print('My name is'  ' ' + ad )
print('Benim adım {}  '.format(ad)) 
print(f"My name is {ad}")
ad=ad.upper()#Tüm harfleri büyütür
print(ad)
index =ad.find('Z')#Cümlede kelime arama
print(index)
#isFound=ad.startswith(Z)#endswith = biten karakter
#print(isFound)
ad=ad.replace('Z', 'S')#Z yerine S koy
print(ad)
result=ad.count('e')# Kaç adet a vardır
print(result)
