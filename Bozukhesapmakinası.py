print("Hesap Makinası")
while True:
    islem = input("Yapmak istediğiniz işlemi giriniz (x / + - ) ")   
    sayi1 = int(input("Sayı giriniz:"))
    sayi2 = int(input("Sayı giriniz:"))   
    if islem == "x":
          print("Sayıların Çarpımı", sayi1 * sayi2)          
    elif islem == "/":
          print("Sayıların Bölümü ", sayi1/sayi2)
    elif islem == "+":
        print("Sayıların Toplamı",sayi1 + sayi2)
    elif islem == "-" :
        print("Sayıların Çıkarımı", sayi1 - sayi2) 
    else:
        print("Çıkış yaptınız!") 
        break            