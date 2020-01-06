"""
  Bu projeyi eşimin ortaokul öğrencileri için yazdım. (Eğlenceli bir çarpım tablosu yarışması) Nasıl çalıştığına bakacak olursak;
Programda 4 farklı zorluk seviyesi bulunmaktadır. Seçilen seviyeye göre kullanıcıya rastgele çarpma soruları sorulmaktadır.
Her zorluk seviyesinde doğru cevap puanı farklıdır.
Bununla birlikte kullanıcı 3 defa doğru cevap verirse bir üst zorluk seviyesine çıkartılır.
Aynı şekilde kullanıcı 3 defa yanlış cevap verdiğinde bir alt zorluk seviyesine düşürülür.1.seviyede 3 hata yapılırsa program sonlandırılır.
Son olarak kullanıcıların isimleri ve kazandıkları puanlar masaüstünde "puanlamalar.txt" dosyasına kaydedilir. 
"""

print("""

--çarpım tablosu--

1-Kolay(1 Puan)
2-Orta(2 Puan)
3-Zor(3 Puan)
4-Çok Zor(4 Puan)

Verilen her 3 yanlış cevapta seviyeniz düşürülür.
Verlen her 3 doğru cevapta seviyeniz yükseltilir.

Yeni Öğrenci kaydetmek ve başlanılmak istenen zorluk seviyesini seçmek için=-1
Programı sonlandırmak için=-2 ye basınız.

""")
from random import randint #rastgele çarpım soruları için kullanacağımız kütüphane
ogrenciler_ve_puanları=[]
def carpim(a,b):
    global yanlis_sayisi
    global dogru_sayisi
    global seviye #zorluk seviyesini belirleyen seçim
    global sonlandirma_degeri #programın sonlandırılıp sonlandırılmayacağını belirleyen seçim
    global puan
    sonuc=int(input("{} x {} kactir?\n".format(a,b)))
    if sonuc==-1: #icerdeki while döngüsünden çıkıp yeni öğrenci ve yeni zorluk seviyesi ile başlamak için
        ogrenciler_ve_puanları.append(isim + "--->" + str(puan) +"\n") #en son yarışan öğrenci ve puanı listeye eklenir.
        seviye="-1"
    elif sonuc==-2: #en dıştaki while döngüsünden çıkmak için
        ogrenciler_ve_puanları.append(isim + "--->" + str(puan) +"\n")
        seviye="-1" #kullanıcı çarpım işleminin ortasında aniden -2 ye basarsa program sonlandırılır. 
        sonlandirma_degeri="-2"
    elif sonuc==a*b: 
        print("dogru sonuc")
        if seviye=="1":
            puan +=1
        elif seviye=="2":
            puan +=2
        elif seviye=="3":
            puan +=3
        else:
            puan +=4
        dogru_sayisi+=1
        if seviye=="4": #bu blok 4.(son) seviyede iken doğru_sayısı değişkeninin etkilenmemesi için yazılmalıdır.
            dogru_sayisi=0
        elif dogru_sayisi==3:
            seviye=int(seviye)
            seviye +=1
            seviye=str(seviye)
            print("seviyeniz yükseltiliyor...")
            dogru_sayisi=0
            yanlis_sayisi=0
    else:
        print("yanlis sonuc")
        yanlis_sayisi +=1
        if yanlis_sayisi==3:
            seviye=int(seviye)
            seviye -=1
            seviye=str(seviye)
            print("seviyeniz düsürülüyor...")
            if seviye=="0": 
                print("Hakkınız doldu...")
                seviye="-1" 
            yanlis_sayisi=0
            dogru_sayisi=0
            
sonlandirma_degeri=None
while True:
    if sonlandirma_degeri=="-2":
        print("programdan cikiliyor.")
        break
    puan=0
    isim=input("isim girin:")
    seviye=input("hangi seviyede soru cözmek istersiniz:1/2/3/4\n(Soru Seviyesini degistirmek icin =-1)\n(Programdan Tamamen cikmak icin=-2\n----->)")
    dogru_sayisi=0 #resetleme işlemi
    yanlis_sayisi=0
    while True:
        if seviye=="-1":
            break
        elif seviye=="1":
            sayi1=randint(1,3)
            sayi2=randint(1,3)
            carpim(sayi1,sayi2)
        elif seviye=="2":
            sayi1=randint(4,7)
            sayi2=randint(4,7)
            carpim(sayi1,sayi2)
        elif seviye=="3":
            sayi1=randint(8,12)
            sayi2=randint(8,12)
            carpim(sayi1,sayi2)
        elif seviye=="4":
            sayi1=randint(13,18)
            sayi2=randint(13,18)
            carpim(sayi1,sayi2)
        elif seviye=="-2":
            sonlandirma_degeri="-2"
            break
        else:
            print("lütfen sadece 1-4 degerleri arasinda sayi girin:")
            break

with open("C:/Users/yunus/Desktop/puanlamalar.txt","w") as file: 
    for i in ogrenciler_ve_puanları:
        file.write(i)

