from yardimci import delete_undefined_letters, search_db, delete_capp, pre_check

data = input("Veri giriniz: ")
words = data.split()

capped_letters = ['ê','â','û','î','ô']
undetectable = []

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
                meanings.append(meaning)
    # Ekrana yazdırma kısmı. Son eleman alınıyor. Eğer eleman yoksa kelime anlamı 
    # bulunamayanlara yazılıyor.
    if meanings != []:
        print(word)
        print(meanings[-1])
    else:
        undetectable.append(word)

print("\n\n")
print(undetectable)
