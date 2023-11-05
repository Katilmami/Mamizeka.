from fuzzywuzzy import fuzz
import os

os.system("clear")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
os.system("figlet Mami Zeka")
print("Çıkmak için exit yazın")
degiskenler = {
    "wifiyi aç": "Açıyorum izin isterse izin verin",
    "sesi aç": "Sesi Fulledim",
}
def degisken_kodu(kelime):
    print(degiskenler[kelime])
def sesli_oku(metin):
    os.system(f'termux-tts-speak "{metin}"')
try:
    with open("sc.txt", "r") as dosya:
        satirlar = dosya.readlines()
        for satir in satirlar:
            parcalar = satir.strip().split(":")
            if len(parcalar) == 2:
                degiskenler[parcalar[0]] = parcalar[1]
except FileNotFoundError:
    with open("sc.txt", "w") as dosya:
        pass


gizli_mod = False
yeni_degisken = None
yeni_kod = ""
yeni_deger = ""

while True:
    kullanici_girisi = input("Mamizeka: ")

    if kullanici_girisi == 'exit':
        break
    elif kullanici_girisi == 'mami0':
        gizli_mod = True
        yeni_degisken = input("Yeni Soru Gir: ")
        yeni_kod = ""
        yeni_deger = ""
    elif kullanici_girisi == 'wifiyi aç':
        os.system("termux-wifi-enable true")
        print("Açıyorum izin isterse izin verin")
        os.system("termux-tts-speak Açıyorum")
    elif kullanici_girisi == 'wifiyi aç':
        os.system("rm -rf sc.txt")
        os.system("wget ")
        print("Güncelliyorum")
        os.system("termux-tts-speak Güncelliyorum")
    elif kullanici_girisi == 'sesi aç':
        os.system("termux-volume music 15")
        print("Açıyorum")
        os.system("termux-tts-speak Açıyorum")
    elif kullanici_girisi == 'kodbit':
        degiskenler[yeni_degisken] = yeni_kod
        degiskenler[yeni_degisken] = yeni_deger
        deger = input(f"{yeni_degisken} sorunun cevabını girin: ")
        yeni_deger = deger
        print(f"{yeni_degisken} değişkenine özel kod ve değer eklenmiştir.")
        with open("sc.txt", "a") as dosya:
            dosya.write(f"{yeni_degisken}:{yeni_deger}\n")
        gizli_mod = False
    elif kullanici_girisi in degiskenler:
        degisken_kodu(kullanici_girisi)
        sesli_oku(degiskenler[kullanici_girisi])  
    elif kullanici_girisi.startswith("en yakın "):
        kelime = kullanici_girisi[8:]
        en_yakin_degisken = None
        en_yuksek_skor = 0

        for kelime_degiskeni in degiskenler:
            skor = fuzz.ratio(kelime_degiskeni.lower(), kelime.lower())
            if skor > en_yuksek_skor:
                en_yakin_degisken = kelime_degiskeni
                en_yuksek_skor = skor

        if en_yakin_degisken:
            degisken_kodu(en_yakin_degisken)
            sesli_oku(degiskenler[en_yakin_degisken]) 
        else:
            print("Cevap Yok Amq")
            sesli_oku("Cevap Yok Amq")
    elif gizli_mod:
        yeni_kod += kullanici_girisi + "\n"
    else:
        gizli_mod = False
        en_yakin_degisken = None
        en_yuksek_skor = 0

        for kelime_degiskeni in degiskenler:
            skor = fuzz.ratio(kelime_degiskeni.lower(), kullanici_girisi.lower())
            if skor > en_yuksek_skor:
                en_yakin_degisken = kelime_degiskeni
                en_yuksek_skor = skor

        if en_yakin_degisken:
            degisken_kodu(en_yakin_degisken)
            sesli_oku(degiskenler[en_yakin_degisken])

