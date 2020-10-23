import sqlite3 as sql

# Stringdeki yabancı karakterleri siliyor.
def edit_string(word):
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
    word = to_lower(word)
    return word

def sapka_sil(letter):
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

# Ön kontrol yapar
def pre_check(kelime):
    gunluk_sozluk = sql.connect('gunluk_turkce.sqlite')
    im = gunluk_sozluk.cursor()
    im.execute("SELECT word FROM words WHERE word = ?", (str.lower(kelime),))
    if im.fetchall() != []:
        return True
    else: return False

# Sözlükte arama yapar.
def search_db(kelime):
    sozluk = sql.connect('sozluk.sqlite')
    im = sozluk.cursor()
    im.execute("SELECT a FROM sozluk WHERE a = ?", (to_upper(kelime),))
    anlam = im.fetchall()
    return anlam



