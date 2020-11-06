from helpers import delete_undefined_letters, search_db, delete_capp, pre_check
import json
def get_meanings(data):
    # data = input("Veri: ")
    words = data.split()
    
    
    capped_letters = ['ê','â','û','î','ô']
    undetectable = []
    
    send = {}
    
    
    for word in words:
        word = delete_undefined_letters(word)
        temp = list(word)
        search1 = ""
        search2 = ""
        meanings = []
        capped_letter = False
        if pre_check(delete_capp(word)):
            continue
        # Kelimeye arama kısmı. 
        for x in temp:
            if x in capped_letters and capped_letter == False:
                capped_letter = True
                search2 = delete_capp(search1)
            # Şapkalı harf varsa
            if capped_letter:
                search1 += x
                search2 += delete_capp(x)
                # Tek harfli aramayı atlıyor.
                if len(search1) == 1:
                    continue
                # Şapkasız kelimeyi arıyor.
                meaning = search_db(search2)
                if meaning != []:
                    meanings.append(meaning)
                # Şapkalı kelimeyi arıyor.
                meaning = search_db(search1)
                if meaning != []:
                    meanings.append(meaning)
            # Şapkasız arama
            else:
                search1 += x
                # Tek harfli aramayı atlıyor.
                if len(search1) == 1:
                    continue
                # Kelimeyi arıyor.
                meaning = search_db(search1)
                if meaning != []:
                    # meaning.append(search1)
                    meanings.append(meaning)
        # Ekrana yazdırma kısmı. Son eleman alınıyor. Eğer eleman yoksa kelime anlamı 
        # bulunamayanlara yazılıyor.
        if meanings != []:
            send[search1] = []
            for a in meanings[-1]:
                send[search1].append(a)
        else:
            undetectable.append(word)
        
    return json(send, ensure_ascii=False)