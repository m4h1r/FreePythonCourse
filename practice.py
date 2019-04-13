# b_year = input("Birth year: ")
# print(type(b_year))
# age = 2019 - int(b_year)
# print(type(age))
# print(age)

# w_in_pound = input("What's your weight in punds:")
# w_in_kilo = int(w_in_pound) * 0.75
# print("You are "+str(w_in_kilo)+" kilos.")

# course = "Python's Course for Beginers"
# print(course)
# cift_tirnak_string='Python for "Beginners"'
# print(cift_tirnak_string)
# multiple_line_string = ''' 
# Hi,
# My name is Mahir
# Thanks for listening.
# '''
# #çoklu satırlı metinler üçtırnaklar arasında tanımlanabilir.
# print(multiple_line_string)

# metin = 'Python for Beginners'
# #        0123456789...
# print(metin[0])
# #metin indeksleri 0'dan başlar.
# print(metin[-1])
# print(metin[-2])
# print(metin[0:3])#ilk değerden başlan son değeri almadan biter.
# print(metin[1:])
# print(metin[:5])
# metin2=metin[:]
# print(metin2)
# name = "Jeniffer"
# print(name[1:-1])

# first = "Mahir"
# last = "Yıldızhan"
# message = first+" ["+last+"] is a coder."
# print(message)
# msg = f"{first} [{last}] is a coder. "
# #f ile başlayan metinler formatlı metin diye geçiyor.
# #Formatlı metinler içine değişken alabiliyor.
# print(msg)


# kurs = "Python for Beginners"
# print(len(kurs))
# #len metodu ile metinlerin karakter sayısını bulabilirsin.
# print(kurs.upper())
# #upper metodu metinlerin içindeki tüm karakterleri büyük harfe çevirir.
# print(kurs)
# print(kurs.lower())
# #upper metodu metinlerin içindeki tüm karakterleri küçük harfe çevirir.


# kurs = "Python for Beginners"
# print(kurs.find("P"))
# #find metodu ile metin içinde harf bulabilrsin.
# print(kurs.find("o"))
# print(kurs.find("O"))
# print(kurs.find("Beginners"))
# #metinler içinde kelimler bulabilirsin.
# print(kurs.replace("Beginners", "Absolute Beginners"))
# print(kurs.replace("beginners", "Absolute Beginners"))
# #Python'un küçük büyük harf duyarlılığı vardır.
# print(kurs.replace("P", "J"))

# kurs = "Python for Beginners"
# print("Python" in kurs)
# #in sorgusu ile metin içinde metin var mı yok mu kontrol edebilirsin.

# kurs = "Python for Beginners"
# print(kurs.title())

# Öğrenilen Metodlar
# len(x)
# x.upper()
# x.lower()
# x.title()
# x.find()
# x.replace()
# "..." in x

# Değişkenler
# intagers
# decimals
# floats
# boolen

# print(10+3) #Toplama
# print(10-3) #Çıkartma
# print(10*3) #Çarpma
# print(10/3) #Bölme
# print(10//3) #Bölüm sonucu
# print(10%3) #Bölümden kalanı bulma
# print(10**3) #İlk sayının üstünü alma.


# x=10
# x = x + 3
# print(x)
# x+=3 #sayıya sayı ilave edip değişkeni günceller.
# print(x)
# x-=3 #sayıdan sayıyı çıkartıp değişkeni günceller.
# print(x)
# x*=3 #sayıyı sayıyla çarpıp değişkeni günceller.
# print(x)
# x/=3 #sayıyı sayıya bölüp değişkeni günceller.
# print(x)

# x= 10+3*2
# print(x)
# x = (30+3)*2
# y = (2+3)*10-3
# print(y)
# #Programlamada da matematikteki öncelikler geçerlidir.

# x = 2.9
# print(round(x))
# # round() sayıyı yakın tarafa yuvarlar.
# print(abs(-2.9))
# # abs() sayıyının mutlak değerini alır.

# import math
# # Kütüphaneleri import ile içeri yükleriz.
# # Math kütüphanesi ve diğer bir çok kütüphane
# # nokta "." ile içindeki metodları çağırabilirsiniz.

# print(math.ceil(2.9))
# print(math.floor(2.9))
# # Tüm kütüphanelerin dokümantasyonu vardır.
# # Math kütüphanesi dökümantasyonu:
# # https://docs.python.org/3/library/math.html

# if it's hot
#  It's a hot day
#  Drink plenty of water
# Otherwise if it's cold
#  It's a cold day
#  Wear warm clothes
# Otherwise
#  It's a lovely day

# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day.")
#     print("Drink plenty of water.")
# elif is_cold:
#     print("It's a cold day.")
#     print("Wear warm clothes.")
# else:
#     print("It's a lovely day.")

# print("Enjoy your day.")

# price =1000000
# has_good_credit = True

# if has_good_credit:
#     down_payment = 0.1*price
# else:
#     down_payment=0.2*price
# print(f"Down payment: ${down_payment}")



# high_income = False
# good_credit = True
# has_criminal_rec = False

# if high_income and good_credit:
#     print("Eligible for loan.")
# if high_income or good_credit:
#     print("Eligible for loan.")
# if high_income or not has_criminal_rec:
#     print("Eligible for loan.")

# temp=35

# if temp > 30:
#     print("It's a hot day.")
# elif temp < 10:
#     print("It's a cold day.")
# elif temp == 30:
#     print("It's 30 degree.")


# name = input("Lütfen adınızı giriniz:")
# n=len(name)
# if n<3:
#     print("Adınız 3 karakterden kısa olamaz.")
# elif n>25:
#     print("Adınız 25 karakterden uzun olamaz.")
# else:
#     print(f"{name} karakter adı geçerli.")


# weight = input("Weight: ")
# transfer = input("(L)bs or (K)g: ")
# transfer = transfer.lower()
# if transfer == "l":
#     weight=int(weight)*0.45
#     print(f"You are {weight} kilos.")
# elif transfer == "k":
#     weight=int(weight)/0.45
#     print(f"You are {weight} Lbs.")
# else:
#     print("Hatalı seçim.")


# i =1
# while i <= 5:
#     print("*" * i)
#     i = i + 1
# print("Done")

##TAHMİN OYUNU##
#Bu oyun 1 ile 100 arasında bir sayı belirler.
#Sana tahmin etmen için 3 hak verir. 
# from random import randint
# number = randint(1,100)
# i=0
# print(number)
# win=False
# while i<3:
#     i+=1
#     tahmin=int(input("Bir tahminde bulun."))
#     if number==tahmin:
#         print("Tebrikler doğru tahmin. :)")
#         win=True
#         break
#     elif tahmin<number:
#         print("Biraz daha yukarı çık.")
#     elif tahmin>number:
#         print("Biraz daha aşağı in.")
# else:
#     print("Üzgünüm 3 hakkın doldu, kaybettin.")


# command =""
# engine=False
# while True:
#     command = input("> ")
#     if command.lower() == "start" and not engine:
#         print("Car started...")
#         engine = True
#     elif command.lower() == "start" and engine:
#         print("Hey, car is working.")
#     elif command.lower() == "stop" and engine:
#         print("Car stoped...")
#         engine = False
#     elif command.lower() == "stop" and not engine:
#         print("Hey, car is not working.")
#     elif command.lower() == "help":
#         print('''
# "start" to start the engine.
# "stop" to stop the engine.
# "quit" to exit.
#         ''')
#     elif command.lower() == "quit":
#         print("See you next time.")
#         break
#     else:
#         print("I don't understand that.")


# ##FOR LOOP##
# for item in "Python": #Bir metnin içinde karakterleri sırayla çağırır.
#     print(item)
# for item in ["Mahir", "Ayşe"]:#Bir dizinin içindeki değerleri sırayla çağırır.
#     print(item)
# for item in [1, 2, 3, 4,]:#Bir dizinin içindeki sayıları sırayla çağırır.
#     print(item)
# for item in range(10):# 0'dan n'e kadar sayıları sırayla çağırır.
#     print(item)
# for item in range(27, 50): # İki değer arasındaki sayıları birer birer çağırır.
#     print(item)
# for item in range(5, 15, 2): # İki değer arasındaki sayıları belli adımlarla çağırır.
#     print(item)

# price = [10, 20, 30]
# print(sum(price))

# #İç içe for loopları
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# numbers = [5,2,5,2,2]
# #İç içe for loop ile çözüm.
# for number in numbers:
#     for y in range(number):
#         print("X", end="")
#     print("")
# #Kolay Çözüm
# for number in numbers:
#     print("X"*number)

# #Aynı örneği L şekli çıkartmak için yap.
# numbers = [1,1,1,1,6]
# for x in numbers:
#     for y in range(x):
#         print("X", end="")
#     print("")

# #Listeler.
# names = ["John ", "Bob", "Sarah", "Marry", "Mahir"]
# print(names)
# print(names[0])
# print(names[4])
# print(names[-2])
# print(names[2:4])
# print(names[2:])
# print(names[:])
# #Listeden bir elemanı değiştirme.
# names[0] = "Jon"
# print(names)

# #Bir listenin en büyük numarasını bulan program.
# a = [3,5,9,4,13,75,9]
# biggestNumber=0
# for x in range(len(a)):
#     if a[x]>=biggestNumber:
#         biggestNumber=a[x]
# print(f"The Biggest number is {biggestNumber}")

# # 2 boyutlu diziler.
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(matrix[0][1])
# matrix[0][1] = 12 #dizi elenanını güncelleme.
# print(matrix[0][1])

# numbers = [5, 4, 6, 3]
# numbers.append(7) #En sona değer ekleme.
# print(numbers)
# numbers.insert(0, 15) #İstediğin bir indekse değer ekleme.
# print(numbers)
# numbers.remove(4) #İstediğin bir değeri silme.
# print(numbers)
# numbers.clear() #Listeyi komple temizleme.
# print(numbers)
# numbers = [5, 4, 6, 5, 2]
# numbers.pop() #Listenin son elemanını siler.
# print(numbers)

# print(numbers.index(5))#Bir elemanon indeksini döndürür.
# print(50 in numbers) # listede 50 var mı yok mu, True/False döndürür.
# print(numbers.count(5))#Listede kaç tane 5 var onu sayar.

# numbers.sort() #Listeyi küçükten büyüğe sıralar.
# print(numbers)
# numbers.reverse() #Listeyi tersten dizer.
# print(numbers)
# numbers2 = numbers.copy()

# #Bir listenin içerisindeki aynı değerleri eleyen program.
##BENİM ÇÖZÜMÜM
# liste = [4,6,5,4,8,7,7,6,6,6]
# yeniListe =[]
# for sayi in liste:
#     if liste.count(sayi)==1:
#         yeniListe.append(sayi)
#     else:
#         if yeniListe.count(sayi)==0:
#             yeniListe.append(sayi)
#         else:
#             pass
# print(yeniListe)

# #MOSH'un ÇÖZÜMÜM
# liste = [4,6,5,4,8,7,7,6,6,6]
# yeniListe =[]
# for sayi in liste:
#     if sayi not in yeniListe:
#         yeniListe.append(sayi)
# print(yeniListe)

# #TUPLES: Liste gibi içinde nesne barındıran ama modiflenemeyen listeler.
# numbers = (1,2,3)
# #tuple'lar parantezler ile tanımlanır.
# print(numbers[0])

# #UNPACKİNG:
# #Liste ya da tuple'ların unpacking özelliği sayesinde içindekileri 
# #kolaylıkla değişkenlere tanımlayabilrisiniz.
# coordinates = (1,2,3)
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)
# coordinates = [1,2,3]
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)







# 410. Satır
