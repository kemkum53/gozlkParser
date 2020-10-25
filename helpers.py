import sqlite3 as sql

# Stringdeki yabancı karakterleri siliyor.
def delete_undefined_letters(word):
    word = to_lower(word)
    word = word.replace('?', '')
    word = word.replace('.', '')
    word = word.replace('!', '')
    word = word.replace(',', '')
    word = word.replace(';', '')
    word = word.replace(':', '')
    word = word.replace('’', '\'')
    word = word.replace('“', '')
    word = word.replace('”', '')
    word = word.replace('…', '')
    word = word.replace('(', '')
    word = word.replace(')', '')
    return word

# Şapkalı harfleri siliyor.
def delete_capp(letter):
    if letter == 'â':
        return 'a'
    if letter == 'ê':
        return 'e'
    if letter == 'î':
        return 'i'
    if letter == 'û':
        return 'u'
    else: return letter
    
# Gelen stringi küçük harfe çevirir.
def to_lower(word):
    tolower_text = (word.replace('İ', 'i'))
    tolower_text = (tolower_text.replace('Ü', 'ü'))
    tolower_text = (tolower_text.replace('Ö', 'ö'))
    tolower_text = (tolower_text.replace('Ç', 'ç'))
    tolower_text = (tolower_text.replace('Ğ', 'ğ'))
    tolower_text = (tolower_text.replace('Ş', 'ş'))
    tolower_text = tolower_text.lower()
    return tolower_text

# Gelen stringi büyük harfe çevirir.
def to_upper(word):
    toupper_text = (word.replace('i', 'İ'))
    toupper_text = (toupper_text.replace('ü', 'Ü'))
    toupper_text = (toupper_text.replace('ö', 'Ö'))
    toupper_text = (toupper_text.replace('ç', 'Ç'))
    toupper_text = (toupper_text.replace('ğ', 'Ğ'))
    toupper_text = (toupper_text.replace('ş', 'Ş'))
    toupper_text = toupper_text.upper()
    return toupper_text

# Günlük kullanılan kelimelerde arama yapar.
def pre_check(word):
    gunluk_sozluk = sql.connect('gunluk_turkce.sqlite')
    im = gunluk_sozluk.cursor()
    im.execute("SELECT word FROM words WHERE word = ?", (str.lower(word),))
    if im.fetchall() != []:
        return True
    else: return False

# Sözlükte arama yapar.
def search_db(word):
    sozluk = sql.connect('sozluk.sqlite')
    im = sozluk.cursor()
    im.execute("SELECT a FROM sozluk WHERE a = ?", (to_upper(word),))
    # Anlamlarıyla birlikte yazdırmak için alt satırı aktif edin. 
    # im.execute("SELECT a,b FROM sozluk WHERE a = ?", (to_upper(word),))
    anlam = im.fetchall()
    return anlam



