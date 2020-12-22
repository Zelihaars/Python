import datetime
tarih= input("Aracınız hangi tarihte trafiğe çıktı(yıl/ay/gün) ")
tarih=tarih.split('/')
trafigecikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi - trafigecikis
print(fark.days)
if days<= 365:
    print("1.servis aralığı")
elif days >365 and days<=365*2:
    print("2.servis aralığı ")  
elif days>365*2 and days <=365*3:
    print("3.servis aralığı")      
else :
    print("Hatalı giriş")
