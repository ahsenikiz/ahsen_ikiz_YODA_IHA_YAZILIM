class BankaHesabi: # Banka hesabı sınıfı oluşturduk
    def __init__(self, hesap_sahibi, hesap_no, bakiye=0): # __init__ metodu ile hesap sahibini, hesap no ve bakiyeyi kaydettik
        self.hesap_sahibi = hesap_sahibi
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar): # para yatırma metodunu tanımladık
        if miktar > 0:
            self.bakiye += miktar # yatırılan parayı bakiyeye ekledik
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL") # ekrana yazdırdık
        else: # negatif olma durumunda uyarı verdik
            print("Yatırılacak miktar pozitif olmalıdır.")

    def para_cek(self, miktar): # para çekme metodunu tanımladık
        if 0 < miktar <= self.bakiye:
            self.bakiye -= miktar # çekilen parayı bakiyeden çıkardık
            print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL") # ekrana yazdırdık
        else:
            print("Yetersiz bakiye veya geçersiz miktar.") # uyarı verdik

    def bakiye_goruntule(self): # bakiye görüntüleme metodunu tanımladık
        print(f"Hesap Sahibi: {self.hesap_sahibi}")
        print(f"Güncel Bakiye: {self.bakiye} TL") # ekrana yazdırdık
# Kullanıcıdan hesap bilgilerini alıyoruz 
ad_soyad = input("Ad Soyad giriniz: ").strip() 
hesap_no = input("Hesap numarası giriniz: ").strip()
ilk_bakiye = float(input("Başlangıç bakiyesi: "))

if ilk_bakiye < 0: # eğer başlangıç bakiyesi sıfırdan küçükse uyarı verdik ve 0.0 TL olarak ayarladık
    print("Başlangıç bakiyesi sıfırdan küçük olamaz; 0.0 TL olarak ayarlandı.")
    ilk_bakiye = 0.0

hesap1 = BankaHesabi(ad_soyad, hesap_no, ilk_bakiye) # BankaHesabi sınıfından bir hesap oluşturduk

while True: # sonsuz döngü ile kullanıcıya seçenekler sunuyoruz
    # Menü seçeneklerini ekrana yazdırıyoruz
    print("\n1 - Bakiye Görüntüle") 
    print("2 - Para Yatır")
    print("3 - Para Çek")
    print("4 - Çıkış")

    secim = input("Seçiminiz: ").strip() # kullanıcıdan seçim aldık 
    # Seçime göre işlemleri gerçekleştirdik
    if secim == "1":
        hesap1.bakiye_goruntule()
    elif secim == "2":
        tutar = float(input("Yatırılacak tutar: "))
        hesap1.para_yatir(tutar)
    elif secim == "3":
        tutar = float(input("Çekilecek tutar: "))
        hesap1.para_cek(tutar)
    elif secim == "4":
        print("Çıkış...")
        break
    else:
        print("Hatalı seçim")