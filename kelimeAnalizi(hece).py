from yardimci import spellword, search_db

girdi = input("Veri giriniz: ")
kelimeler = girdi.split()

for kelime in kelimeler: # Cümle içindekki tüm kelimeleri ayırıyor.
    temp = spellword(kelime) # Kelimeyi hecelerine ayırıyor.
    if temp == False: # Özel karakter içeriyorsa atlıyor.
        continue
    ara = "" # Anlık olarak aranıcak kelime için değişken
    anlamlar = [] # Hecelere göre tüm anlamların tutulduğu değişken
    for x in temp:# İlk heceden başlayarak tüm heceleri birleştirerek ilerleyip database'de arıyor
        ara += x
        anlam = search_db(ara)
        if anlam == []:
            continue
        else:
            anlamlar.append(anlam)
    if anlamlar != []:
        print(anlamlar[-1])
    
