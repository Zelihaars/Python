name =input("İsminizi girin : " )
surname =input("Soyisminizi girin : " )
print(f"Welcome {name } { surname}")
secim=int(input("Kaç adet ders alıyorsunuz :" ))
if secim <3 :
    print("You Failed in class ")
elif secim >5 :
    print("5 ten fazla dersl alamazsınız")
else :
    print("Aldığınız dersleri girin ")
    derslerim =[]
    i=1
    while i<=secim:
        ders= input("ders : ")
        print(f"{i}.dersiniz = {ders}")
        i+=1
        derslerim.append(ders)
     
print(f"{name} Aldığın dersler : {derslerim}")
print(f"{derslerim[2]} dersinin ortalaması ve harf durumu ")
sozluk = {"vize":67,"final": 52,"project":83}
ortalama = (sozluk["vize"]*0.3)+(sozluk["final"]*0.5)+(sozluk["project"]*0.2)
print(ortalama)
if  ortalama > 90 :
    print("AA")
elif 70< ortalama <90:
    print("BB")
elif 50< ortalama <70:
    print("CC")
elif 30< ortalama <50:
    print("DD")
elif ortalama < 30 :
    print("FF")    
