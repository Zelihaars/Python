names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]
#Soru1 Liste sonuna ekleme
"""
names.append('Cenk')
print(names)
"""
#Soru2 liste başına ekleme
"""
names.insert(0,'Sena')
print(names)
"""
#soru3 Listeden silme 
"""
names.remove('Deniz')
print(names)
"""
#Soru4 Deniz isminin indexini bul
"""index=names.index('Deniz')
print(index)
"""
#Soru 5 Ali listenin elemanı mıdır 
"""
elemanimidir='Ali' in names
print(elemanimidir)
"""
#Soru 6 Listeyi ters çevir
"""
names.reverse()
print(names)
"""
#Soru7 Alfabetik olarak sırala
"""
names.sort()
print(names)
"""
#Soru8 years listesini büyükten küçüğe sırala
"""
years.sort()
print(years)
"""
#Soru9 str="Chevrolet, Dacia" karakter dizisini listeye çevirin
"""str="Chevrolet, Dacia"
result=str.split(',')
print(result)
"""
#Soru10 years listesinin en büyük ve en küçük elemanını bulma
"""
min=min(years)
max=max(years)
print(min , max)
"""
#Soru11 years litesinde kaç tane 1998 değeri vardır 
"""
result=years.count(1998)
print(result)
"""
#Soru12 dizinin tüm elemanlarını siliniz
"""
years.clear()
print(years)
"""
#Soru13 Kullanıcıdan alacağınınız marka bilgisini bir listede sıralayın
"""marka1=input("1.Markayı girin : "  )
marka2=input("2.Markayı girin : "  )
marka3=input("3.Markayı girin : "  )
Liste=[marka1 , marka2 , marka3 ]
print(Liste)
"""
