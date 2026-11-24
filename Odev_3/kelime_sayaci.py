metin= input("Bir metin girin: ") # kullanıcıdan girdi aldık
toplam_karakter= len(metin) # toplam karakter sayısı len ile hesaplandı
kucuk_metin = metin.lower() # metni .lower() ile küçük harfe çevirdik
kelimeler = kucuk_metin.split() # metni .split() ile kelimelere böldük
kelime_sayisi = len(kelimeler) # len ile kelime sayısı hesaplandı
en_uzun_kelime_uzunluk= 0 # en uzun kelimenin uzunluğunu tutacak değişkeni 0 olarak başlattık
kelime_sayilari= {} # kelime sayıları için boş bir sözlük oluşturduk

for kelime in kelimeler:
    if kelime in kelime_sayilari: # eğer kelime sözlükte varsa
        kelime_sayilari[kelime] += 1 # sayısını 1 artırdık
    else:
        kelime_sayilari[kelime] = 1 # yoksa sözlüğe ekle ve sayısını 1 yaptık
    if len(kelime) > en_uzun_kelime_uzunluk: # eğer kelimenin uzunluğu en uzun kelimenin uzunluğundan büyükse
        en_uzun_kelime_uzunluk = len(kelime) # en uzun kelimenin uzunluğunu güncelledik

print("Toplam karakter sayısı:", toplam_karakter) # toplam karakter sayısını yazdırdık
print("Toplam kelime sayısı:", kelime_sayisi) # toplam kelime sayısını yazdırdık
print("En uzun kelimenin uzunluğu:", en_uzun_kelime_uzunluk) # en uzun kelimenin uzunluğunu yazdırdık
print("Kelime sayıları:") # kelime sayıları sözlüğünü yazdırdık

for kelime, sayi in kelime_sayilari.items():
    print(f"{kelime}: {sayi}") # kelime ve kelimelerin tekrar sayısını yazdık

