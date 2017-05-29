# Veritabanı için eklenen class
import sqlite3 as sql
class Datebase():
    # Bağlantı yapma fonksiyonu ve veritabanı yoksa oluşturuyor.
    def baglanti(self):
        self.baglan = sql.connect("datebase.db")
        self.komut = self.baglan.cursor()
    # Bilgileri kayıt etme
    def kaydet(self):
        self.baglan.commit()

    # Veritabanı kapatma
    def kapat(self):
        self.baglan.close()

    # Tablo oluşturuyoruz eğer yoksa
    def tablo_olustur(self):
        self.baglanti()
        self.komut.execute("CREATE TABLE IF NOT EXISTS kullanicilar(id INTEGER PRIMARY KEY, kullanici_adi , sifre, ad_soyad)")
        self.kaydet()
        self.kapat()

    # Veri ekleme
    def ekle(self, k_adi,sifre,ad_soyad):
        self.baglanti()
        self.komut.execute("INSERT INTO kullanicilar(kullanici_adi , sifre, ad_soyad) VALUES(?, ?, ?)",(k_adi,sifre,ad_soyad))
        self.kaydet()
        self.kapat()

    #Veri silme
    def sil(self, k_adi):
        self.baglanti()
        self.komut.execute("DELETE FROM kullanicilar WHERE kullanici_adi = '{}'"(k_adi))
        self.kaydet()
        self.kapat()

    # Veri güncelleme
    def guncelle(self, eski_k_adi, yeni_k_adi, sifre, ad_soyad):
        self.baglanti()
        self.komut.execute("UPDATE kullanicilar SET kullanici_adi = ?, sifre = ?, ad_soyad = ? WHERE kullanici_adi = ?",(yeni_k_adi, sifre, ad_soyad, eski_k_adi))
        self.kaydet()
        self.kapat()

    # Verileri listeleme
    def listele(self):
        self.baglanti()
        liste = self.komut.execute("SELECT * FROM kullanicilar")
        for i in liste.fetchall():
            print(i)
        self.kapat()

    # Detaylı veri arama
    def ara(self,k_adi):
        self.baglanti()
        ara = self.komut.execute("SELECT* FROM kullanicilar WHERE kullanici_adi IN ('{}')".format(k_adi))
        for i in ara.fetchall():
            print(i)
        self.kapat()
