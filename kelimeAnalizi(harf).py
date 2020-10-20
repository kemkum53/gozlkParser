from yardimci import search_db

girdi = input("Veri giriniz: ")
kelimeler = girdi.split()

for kelime in kelimeler: # Cümle içindekki tüm kelimeleri ayırıyor.
    temp = list(kelime)
    ara = ""
    anlamlar = []
    for x in temp:
        ara += x
        anlam = search_db(ara)
        if anlam == []:
            continue
        else:
            anlamlar.append(anlam)
    if anlamlar != []:
        print(anlamlar[-1])