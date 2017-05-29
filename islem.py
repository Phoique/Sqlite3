import datebase as db
dt = db.Datebase()
dt.tablo_olustur()
while True:
    islem_no = int(input("""
1- Kullanıcı ekleme
2- Kullanıcı Silme
3- Kullanıcı Güncelleme
4- Kullanıcıları Listeleme
5- Kullanıcı Arama
İşlem numarası: """))

    # Kayıt işlemi
    if islem_no == 1:
        try:
            adsoyad       = str(input("Adınızı ve soyadınızı giriniz: "))
            kullanici_adi = str(input("Kullanıcı adınızı giriniz: "))
            sifre         = str(input("Şifrenizi giriniz: "))
            dt.ekle(kullanici_adi, sifre, adsoyad)
            print("Kullanıcı başarıyla kayıt edilmiştir.")

        except Exception as e:
            print("Kaydetme sırasında bir hata oluştu: ",e)
    # Silme işlemi
    elif islem_no == 2:
        try:
            sil = input("Silmek istediğiniz kullanıcının kullanıcı adını giriniz: ")
            dt.sil(sil)
            print("Kullanıcı silinmiştir.")
        except Exception as e:
            print("Silme işlemi sırasında bir hata oluştu: ",e)

    # Güncelleme işlemi
    elif islem_no == 3:
        try:
            eski_k_adi = str(input("Güncellenecek kullanıcının eski kullanıcı adı: "))
            yeni_k_adi = str(input("Yeni kullanıcı adı: "))
            sifre      = str(input("Şifresi: "))
            adsoyad    = str(input("Adı ve Soyadı: "))
            dt.guncelle(eski_k_adi,yeni_k_adi,sifre,adsoyad)
            print("Kullanıcı güncellenmiştir.")
        except Exception as e:
            print("Güncelleme sırasında bir hata oluştu: ",e)

    # Listeleme işlemi
    elif islem_no == 4:
        try:
            print("Kullanıcılar listeleniyor...")
            dt.listele()
            print("Listelendi.")
        except Exception as e:
            print("Listeleme sırasında bir hata oluştu: ",e)

    # Arama işlemi
    elif islem_no == 5:
        try:
            ara = str(input("Aranacak kullanıcının kullanıcı adı: "))
            dt.ara(ara)
        except Exception as e:
            print("Arama sırasında bir hata oluştu: ",e)

    # Yanlış bir işlem numarası girilirse
    else:
        print("Lütfen işlem numarasını tekrar deneyiniz...")
