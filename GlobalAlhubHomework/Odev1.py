print("5 adet değer girin ")
deger1=input("1.yi girin:" )
deger2=input("2.yi girin:" )
deger3=input("3.yi girin:" )
deger4=input("4.yü girin:" )
deger5=input("5.yi girin:" )
listem=[deger1,deger2,deger3,deger4,deger5]
print(listem)
for i in range(5):
    sıra =listem[i]
    tip = type(listem[i])
    print(f"{i+1}inci deger {sıra} tipi : {tip}")
print(listem)    
© 2021 GitHub, Inc.
