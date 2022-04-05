import  os
import time
import calendar
import  datetime as t
from colorama import *
def hosgeldiniz():
    print(Fore.LIGHTYELLOW_EX)
    print('-------------------------------')
    print("Takvim Programına Hoşgeldiniz")
    print('-------------------------------')

hosgeldiniz()

def ıstekayyazdir():
    try:
        print(Fore.LIGHTYELLOW_EX)
        x = int(input("Yıl Giriniz:"))
        years = x
        ay = int(input("Ay Giriniz:"))
        if ay > 12:
            print(Fore.RED)
            print("Bir Yılda 12 AY Var. Lütfen Geçerli Bir Değer Girin!")
        else:
            if ay == 1:
                print(Fore.LIGHTYELLOW_EX)
                ay1 = calendar.month(years, ay)
                print("1.Ay Girildi:", ay1)
            elif ay == 2:
                print(Fore.LIGHTYELLOW_EX)
                ay2 = calendar.month(years, ay)
                print("2.Ay Girildi:", ay2)
            elif ay == 3:
                print(Fore.LIGHTYELLOW_EX)
                ay3 = calendar.month(years, ay)
                print("3.Ay Girildi:", ay3)
            elif ay == 4:
                print(Fore.LIGHTYELLOW_EX)
                ay4 = calendar.month(years, ay)
                print("4.Ay Girildi:", ay4)
            elif ay == 5:
                print(Fore.LIGHTYELLOW_EX)
                ay5 = calendar.month(years, ay)
                print("5.Ay Girildi:", ay5)
            elif ay == 6:
                print(Fore.LIGHTYELLOW_EX)
                ay6 = calendar.month(years, ay)
                print("6.Ay Girildi:", ay6)
            elif ay == 7:
                print(Fore.LIGHTYELLOW_EX)
                ay7 = calendar.month(years, ay)
                print("7.Ay Girildi:", ay7)
            elif ay == 8:
                print(Fore.LIGHTYELLOW_EX)
                ay8 = calendar.month(years, ay)
                print("8.Ay Girildi:", ay8)
            elif ay == 9:
                print(Fore.LIGHTYELLOW_EX)
                ay9 = calendar.month(years, ay)
                print("9.Ay Girildi:", ay9)
            elif ay == 10:
                print(Fore.LIGHTYELLOW_EX)
                ay10 = calendar.month(years, ay)
                print("10.Ay Girildi:", ay10)
            elif ay == 11:
                print(Fore.LIGHTYELLOW_EX)
                ay11 = calendar.month(years, ay)
                print("11.Ay Girildi:", ay11)
            elif ay == 12:
                print(Fore.LIGHTYELLOW_EX)
                ay12 = calendar.month(years, ay)
                print("12.Ay Girildi:", ay12)
    except ValueError:
        print(Fore.RED)
        print("Lütfen Sadece Sayı Giriniz!!")

def tumyilyazdir():
    try:
        print(Fore.LIGHTYELLOW_EX)
        yil = int(input("Yıl Giriniz:"))
        ay = 1
        ay1 = calendar.month(yil, ay)
        print(ay1)
        ay = 2
        ay2 = calendar.month(yil, ay)
        print(ay2)
        ay3 = calendar.month(yil, ay)
        print(ay3)
        ay = 4
        ay4 = calendar.month(yil, ay)
        print(ay4)
        ay = 5
        ay5 = calendar.month(yil, ay)
        print(ay5)
        ay = 6
        ay6 = calendar.month(yil, ay)
        print(ay6)
        ay = 7
        ay7 = calendar.month(yil, ay)
        print(ay7)
        ay = 8
        ay8 = calendar.month(yil, ay)
        print(ay8)
        ay = 9
        ay9 = calendar.month(yil, ay)
        print(ay9)
        ay = 10
        ay10 = calendar.month(yil, ay)
        print(ay10)
        ay = 11
        ay11 = calendar.month(yil, ay)
        print(ay11)
        ay = 12
        ay12 = calendar.month(yil, ay)
        print(ay12)
    except ValueError:
        print(Fore.RED)
        print("Lütfen Sadece Sayı Giriniz!!")


def dogum_gunu_bul():
    print("Lütfen Değerleri Gün Ay Yıl ve Aralarında nokta şeklinde giriniz--->>Gün.Ay.Yıl şeklinde")
    try:
        dogum = input("doğum tarihinizi giriniz: (Gün.Ay.Yıl) ")
        dogum = t.datetime.strptime(dogum, "%d.%m.%Y")
        simdi = t.datetime.now()
        fark = simdi - dogum
        Yıl = fark.days // 365
        Ay = fark.days % 365 // 30
        Gün = fark.days % 365 % 30
        print(Fore.GREEN)
        print("Yıl:", str(Yıl), "Gün:", str(Gün), "Ay:", str(Ay))
    except  ValueError:
        print(Fore.RED)
        print("Lütfen Formata Uygun Giriniz!!")



try:
 while True:
    secim = int(input("İstediğiniz Yılın Aylarını Yazdırmak İçin -- 1 \n "
                      "-------------------------------------------------------------"
                       "\nİstediğiniz Yılın Tüm Aylarını Yazdırmak İçin -- 2'ye  \n"
                      "-------------------------------------------------------------"
                       "\nDoğum Gününüzü Bulmak İçin -- 3'e \n"
                      "-------------------------------------------------------------"
                       "\nProgramı Kapatmak İçin 4'e Basınız:""\n",))

    if int(secim) == 1:
        ıstekayyazdir()
    elif int(secim) == 2:
        tumyilyazdir()
    elif int(secim) == 3:
        dogum_gunu_bul()
    elif int(secim) == 4:
        time.sleep(3)
        print("Program Kapandı...")
        exit()



    else:
        print(Fore.RED)
        print("Geçerli Bir Değer Giriniz!!")


except ValueError:

    print(Fore.RED)
    print("Lütfen Sadece Uygun Formatda Kullanınız!!")






