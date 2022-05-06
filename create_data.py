import os
import csv
import time
from faker import Faker

def datagenerate(records, headers):
    fake = Faker('tr_TR')
    with open(dosya_adi, 'wt', encoding="utf-8-sig") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        dictobjesi = {}
        flag = False 
        Tr2Eng = str.maketrans("çğıöşü", "cgiosu")
        for i in range(records):
            for j in headers:
                if j == "Email":
                    flag = True
                    fname = fake.first_name()
                    lname = fake.last_name()
                    fname_mail = fname.translate(Tr2Eng)
                    lname_mail = lname.translate(Tr2Eng)
                    #In the latest version of faker, the e-mail generating function is broken, 
                    #it only generates e-mail addresses with the extension "example.com"
                    #i'm using the "link" function instead.
                    
                    link = fake.url()
                    if "www" in link:
                        linksplit = link.split(".")[-2:]
                        linksplit[1] = linksplit[1].replace("/", "")
                    else: 
                        linksplit_temp1 = link.split("/")
                        temp = linksplit_temp1[2]
                        linksplit = temp.split(".")

                    emaild = fname_mail + "." + lname_mail + "@" + linksplit[0] + "." + linksplit[1]
                    dictobjesi['Email'] = emaild.lower()
                elif j == "Unvan":
                    dictobjesi['Unvan'] = fake.prefix()
                elif j == "Isim":
                    if not flag:
                        dictobjesi['Isim'] = fake.first_name()
                    else:
                        dictobjesi['Isim'] = fname
                elif j == "Soyisim":
                    if not flag:
                        dictobjesi['Soyisim'] = fake.last_name()
                    else:
                        dictobjesi['Soyisim'] = lname
                elif j == "D.Tarihi":
                    dictobjesi['D.Tarihi'] = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90)
                elif j == "Telefon":
                    dictobjesi['Telefon'] = fake.phone_number()
                elif j == "Adres":
                    address = fake.address()
                    adres = address.replace('\n', '').replace('\r', '')
                    dictobjesi['Adres'] = adres
                elif j == "Posta Kodu":
                    dictobjesi['Posta Kodu'] = fake.zipcode()
                elif j == "Sehir":
                    dictobjesi['Sehir'] = fake.city()
                elif j == "Zaman":
                    dictobjesi['Zaman'] = fake.time()
                elif j == "Link":
                    if not flag:
                        dictobjesi['Link'] = fake.url()
                    else:
                        dictobjesi['Link'] = link
                elif j == "Kelime":
                    dictobjesi['Kelime'] = fake.word()
                elif j == "TCKN":
                    dictobjesi['TCKN'] = fake.ssn()
                elif j == "Urun-beyazesya":
                    beyaz_esyalar = [
                        'Buzdolabi','Camasir Mak.',
                        'Firin', 'Bulasik Mak.',
                        'Mikrodalga Firin','Derin Dondurucu',
                        'Kurutma Mak','Set Ustu Ocak','Aspiratör', 'Mini Firin']
                    dictobjesi["Urun-beyazesya"] = fake.word(ext_word_list=beyaz_esyalar)
                elif j == "Urun-elektronik":
                    elektronik_esyalar = [
                        'Dizustu Bilg.','Mouse',
                        'Cep Telefonu', 'Klavye',
                        'Mikrofon','Kulaklik',
                        'Monitör','Bluetooth Hoparlör','USB disk','Tablet Bilgisayar','Harici Disk']
                    dictobjesi["Urun-elektronik"] = fake.word(ext_word_list=elektronik_esyalar)
                elif j == "Satis Adedi":
                    dictobjesi["Satis Adedi"] = fake.random_int(min=1, max=9)
                elif j == "Satis Tarihi":
                    dictobjesi["Satis Tarihi"] = fake.date_between(start_date='-1y',end_date='today')

                elif j == "Satis Fiyati":
                    dictobjesi["Satis Fiyati"] = fake.random_int(min=1, max=1000)

                elif j == "Alis Fiyati":
                    dictobjesi["Alis Fiyati"] = fake.random_int(min=1, max=1000)
                elif j == "Firma":
                    dictobjesi["Firma"] = fake.company()
            writer.writerow(dictobjesi)

if __name__ == '__main__':
    os.system('clear')
    print(" (0)Email", "(1)Unvan", "(2)Isim", "(3)Soyisim\n",
          "(4)D.Tarihi", "(5)Telefon", "(6)Adres", "(7)Posta Kodu\n",
          "(8)Sehir", "(9)Zaman", "(10)Link", "(11)Kelime", "(12)TCKN\n",
          "(13)Urun (Beyaz Esya)", "(14)Urun (Elektronik)", "(15)Satis Adedi\n",
          "(16)Satis tarihi", "(17)Satis Fiyati", "(18)Alis Fiyati","(19)Firma\n",
          "Tum alanlari secmek icin '-1'")

    girilen_alanlar = input("Olusacak alanlari Secin (boslukla ayrilmis sekilde ÖRN: 0 2 3 ) : ")
    if not girilen_alanlar:
        girilen_alanlar = "2 3 4"
    satir_sayisi = input("CSV Dosyasi Kac Satir Olsun ? (Varsayilan 100) : ")
    if not satir_sayisi:
        satir_sayisi = 100
    dosya_adi = input("Dosya adi (Varsayilan data.csv) : ")
    if not dosya_adi:
        dosya_adi = "data.csv"
    baslik_listesi = girilen_alanlar.split()
    baslik_listesi = list(map(int, baslik_listesi))
    headers = ["Email", "Unvan", "Isim", "Soyisim", "D.Tarihi",
               "Telefon", "Adres", "Posta Kodu", "Sehir", "Zaman",
               "Link", "Kelime", "TCKN", "Urun-beyazesya",
               "Urun-elektronik","Satis Adedi", "Satis Tarihi",
               "Satis Fiyati", "Alis Fiyati","Firma"]
    headers_yeni = []
    if baslik_listesi[0] == -1:
        headers_yeni=headers
    else:
        for i in baslik_listesi:
            headers_yeni.append(headers[i])
    start = time.perf_counter()
    datagenerate(int(satir_sayisi), headers_yeni)
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 1)} seconds")
