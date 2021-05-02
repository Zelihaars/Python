name=str(input("İsminizi girin: " ))
lastname=str(input("Soyisminizi girin :" ))
age=int(input("Yaşınızı girin " ))
birth=int(input("Doğum tarihinizi girin(Sadece Yıl) "))
listem=[name,lastname,age,birth]
for i in range(4):
    print(listem[i])
if (age < 18):
    print("You cant go out because it's too dangerous")   
else :
    print("You can go out to the street")
