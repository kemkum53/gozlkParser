from yardimci import edit_string, search_db, sapka_sil, pre_check

girdi = input("Veri giriniz: ")
kelimeler = girdi.split()

sapkali_harfler = ['ê','â','û','î','ô']
bulunamayan = []

for kelime in kelimeler:
    kelime = edit_string(kelime)
    temp = list(kelime)
    ara1 = ""
    ara2 = ""
    anlamlar = []
    sapkali_arama = False
    if pre_check(sapka_sil(kelime)):
        continue
    # Kelime 2 harfli ise
    if len(kelime) == 2:
        anlam = search_db(kelime)
        if anlam != []:
            anlamlar.append(anlam)
        else:       
            bulunamayan.append(kelime)
    # Kelime 2 harften fazlaysa
    else:
        for x in temp:
            if x in sapkali_harfler and sapkali_arama == False:
                sapkali_arama = True
                ara2 = sapka_sil(ara1)
            # Şapkalı harf varsa
            if sapkali_arama:
                ara1 += x
                ara2 += sapka_sil(x)
                if len(ara1) == 1:
                    continue
                anlam = search_db(ara2)
                if anlam != []:
                    anlamlar.append(anlam)
                anlam = search_db(ara1)
                if anlam != []:
                    anlamlar.append(anlam)
            # Şapkasız arama
            else:
                ara1 += x
                if len(ara1) == 1:
                    continue
                anlam = search_db(ara1)
                if anlam != []:
                    anlamlar.append(anlam)
    if anlamlar != []:
        print(kelime)
        print(anlamlar[-1])
    else:
        bulunamayan.append(kelime)

print("\n\n")
print(bulunamayan)