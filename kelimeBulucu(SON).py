from yardimci import delete_undefined_letters, search_db, sapka_sil, pre_check

girdi = input("Veri giriniz: ")
kelimeler = girdi.split()

sapkali_harfler = ['ê','â','û','î','ô']
bulunamayan = []

for kelime in kelimeler:
    kelime = delete_undefined_letters(kelime)
    temp = list(kelime)
    ara1 = ""
    ara2 = ""
    anlamlar = []
    sapkali_arama = False
    if pre_check(sapka_sil(kelime)):
        continue
    # Kelimeye arama kısmı. 
    for x in temp:
        if x in sapkali_harfler and sapkali_arama == False:
            sapkali_arama = True
            ara2 = sapka_sil(ara1)
        # Şapkalı harf varsa
        if sapkali_arama:
            ara1 += x
            ara2 += sapka_sil(x)
            # Tek harfli aramayı atlıyor.
            if len(ara1) == 1:
                continue
            # Şapkasız kelimeyi arıyor.
            anlam = search_db(ara2)
            if anlam != []:
                anlamlar.append(anlam)
            # Şapkalı kelimeyi arıyor.
            anlam = search_db(ara1)
            if anlam != []:
                anlamlar.append(anlam)
        # Şapkasız arama
        else:
            ara1 += x
            # Tek harfli aramayı atlıyor.
            if len(ara1) == 1:
                continue
            # Kelimeyi arıyor.
            anlam = search_db(ara1)
            if anlam != []:
                anlamlar.append(anlam)
    # Ekrana yazdırma kısmı. Son eleman alınıyor. Eğer eleman yoksa kelime anlamı 
    # bulunamayanlara yazılıyor.
    if anlamlar != []:
        print(kelime)
        print(anlamlar[-1])
    else:
        bulunamayan.append(kelime)

print("\n\n")
print(bulunamayan)
