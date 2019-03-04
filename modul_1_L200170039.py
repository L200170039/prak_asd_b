#Nomor1
def segitigasiku(a):
    awal=1
    while awal<=a:
        print("*"*awal)
        awal+=1

print("Nomor 1")
segitigasiku(5)

#Nomer 2
def persegibolong(x,y):
    a=1
    print("@"*y)
    while(a<x):
       print("@"+" "*(y-2)+"@")
       a+=1
    print("@"*b)
print("\nNomor 2")
persegibolong(5,5)

#Nomor 3a
def jumlahVokal(x):
    v="aiueoAIUEO"
    vokal=0
    jumlahhuruf=0
    for i in x:
        jumlahhuruf+=1
        if i in v:
            vokal+=1
    return (jumlahhuruf,vokal)
print("\nNomor 3a")
print(jumlahVokal("Surakarta"))

#Nomor 3b
print("Nomor 3b")
def jumlahKonsonan(m):
    v="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    konsonan=0
    jumlahhuruf=0
    for a in m:
        jumlahhuruf+=1
        if a in v:
            konsonan+=1
    return (jumlahhuruf,konsonan)
print(jumlahKonsonan("Surakarta"))

#Nomor 4
print("\nNomor 4")
def rerata(b=[]):
    x=0
    y=0
    if b != []:
        for i in b:
            x+=i
            y+=1
        return x/n
z=rerata([1,2,3,4,5])
print(z)

g=[3,4,5,4,3,4,5,2,2,10,11,23]
r=rerata(g)
print(r)

#Nomor 5
print("\nNomor 5")
from math import sqrt as sq
def apakahPrima(n):
    n=int(n)
    assert n>=0
    primakecil=[2, 3, 5, 7, 11]
    bukanprima=[0, 1, 4, 6, 8, 9, 10]
    if n in primakecil:
        return True
    elif n in bukanprima:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if(n%i==0):
                return False
    return True
print(apakahPrima(17))
print(apakahPrima(97))
print(apakahPrima(123))

#Nomor6
print("\nNomor 6")
def bilanganprima():
    prima=list()
    for i in range(2,100):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if(x):
            print(i)
            prima.append(i)
bilanganprima()

#Nomor 7
print("\nNomor 7")
def faktorPrima(n):
    prima=list()
    for i in range(2,n):
        x = True
        for iter in prima:
            if(i%iter==0):
                x=False
                break
        if x and n%i==0:
            prima.append(i)
    return prima
print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))

#Nomor 8
print("\nNomor 8")
def apakahTerkandung(a,b):
    return a in b
i ="do"
j ="Indonesia tanah air kita"
print(apakahTerkandung(h,k))
print(apakahTerkandung("pusaka",k))

#Nomor 9
print("\nNomor 9")
def coba():
    for a in range(1,100):
        if (a%3)!=0 and (a%5)!=0:
            print(a)
        else:
            if (a%15)==0:
                print("PYTHON UMS")
            elif (a%3)==0:
                print("python")
            elif (a%5)==0:
                print("UMS")
coba()

#Nomor 10
print("\nNomor 10")
def selesaikanABC(a,b,c):
    a=float(a)
    b=float(b)
    c=float(c)
    d=(b**2)-(4*a*c)
    if d<0:
        return "determinan negatif. Persamaan tidak mempunyai akar real"
    return  "determinanpositif. Persamaan mempunyai akar real"
print(selesaikanABC(1,2,3))

#Nomor 11
print("\nNomor 11")
def apakahkabisat(z):
    if(z%400==0):
        return True
    if(z%100==0):
        return False
    if(z%4==0):
        return True
    return False
print(apakahkabisat(2400))

#Nomor 12
print("\nNomor 12")
import random
def permainanTA():
    a=random.randrange(0, 100)
    while(True):
        b=int(input("masukan angka: "))
        if(b>a):
            print("itu terlalu besar,coba lagi")
        elif(b<a):
            print("itu terlalu kecil,coba lagi")
        else:
            print("benar")
            break
print("belum dimasukan Perintah 'permainanTA'")

#Nomor 13
print("\nNomor 13")
def katakan(m):
    x={"0":"","1":"Se","2":"Dua ","3":"Tiga ","4":"Empat ","5":"Lima ","6":"Enam ","7":"Tujuh ","8":"Delapan ","9":"Sembilan "}
    y={-1:"",-2:"puluh ",-3:"ratus ",-4:"ribu ",-5:"puluh ",-6:"ratus ",-7:"juta ",8:"puluhjuta "}
    b=str(m)
    z=""
    i=-1
    while i>= -len(b):
        z=x[b[i]]+y[i]+z
        i-=1
    return z
print(katakan(3125750))

#Nomor 14
print("\nNomor 14")
def formatRupiah(x):
    y=str(x)
    z=""
    i = -1
    while i>= -len(y):
        if((i+1)%3==0 and (i+1)!=0):
            c="."+z
        z=y[i]+z
        i-=1
    return "'"+"Rp "+z+"'"
print(formatRupiah(1500))
print(formatRupiah(2560000))