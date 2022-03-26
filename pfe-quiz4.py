ogr_dict = {}

def ortalamabul(sozluk):    # Öğrencilerin puanlarının ortalamasını bulmak için ortalamabul adlı bir fonksiyon yazdım.
    pua_Toplam = 0
    pua_Ortalama = 0
    if len(sozluk) == 0:    # Eğer dictionary'nin içerisinde herhangi bir değer yoksa hata vermesi için bir if yapısı kullandım.
            print("Hiç öğrenci verisi bulunamadı")
    else :
        for i in sozluk:    # Burdada dictionary içerisinden öğrenci puanlarını çekip toplam ve ortalama değerlerini hesapladım.
            pua_Toplam += sozluk[i]
            pua_Ortalama = pua_Toplam/len(sozluk)
    return pua_Ortalama

while True:                 # Çıkış seçeneği seçilene kadar tekrar etmesi amacıyla while kullandım.
    puan_Toplam = 0
    puan_Ortalama = 0
    kalan_Liste = []        
    gecen_Liste = []
    Karar = input("Hangi işlemi yapacaksınız\nA) Öğrenci ve not girişi\nB) Ortalama al\nC) Kalan ve geçen öğrencileri göster\nD)Tüm Öğrencileri ve Puanlarını göster\nQ) Çıkış\n")
    if Karar == "a" or Karar == "A":
        isim = input("Öğrencinin ismini giriniz: ")
        puan = int(input("Kaç puan aldığını giriniz: "))
        ogr_dict[isim] = puan
    elif Karar == "b" or Karar == "B":
        puan_Ortalama = ortalamabul(ogr_dict)
        print(puan_Ortalama)
    elif Karar == "c" or Karar == "C":
        if len(ogr_dict) == 0:
            print("Hiç öğrenci verisi bulunamadı")
        else :
            for i in ogr_dict:
                puan_Toplam += ogr_dict[i]
                puan_Ortalama = puan_Toplam/len(ogr_dict)
            for i in ogr_dict:
                if ogr_dict[i] >= puan_Ortalama:    # hesaplanan puan ortalamasından büyük olan değerleri gecen_Liste'ye ekledim.
                    gecen_Liste.append(i)
                else:                               # hesaplanan puan ortalamasından küçük olan değerleri kalan_Liste'ye ekledim.
                    kalan_Liste.append(i)
            print("Kalan öğrenciler = {}\nGeçen Öğrenciler = {}".format(kalan_Liste, gecen_Liste))
    elif Karar == "d" or Karar == "D":
        for i in ogr_dict:
            print(i,"-->", ogr_dict[i])
    elif Karar == "q" or Karar == "Q":              # While döngüsünü kırma amacıyla exit komutunu kullandım.
        exit()
    else:
        print("Hatalı seçimde bulundunuz.")
    
