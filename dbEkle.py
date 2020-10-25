import sqlite3 as sql
import yardimci

data = input("veri:")
words = data.split()

# Kelime database'de var mı diye bakıyor.
def db_kontrol(kelime):
    db = sql.connect("gunluk_turkce.sqlite")
    im = db.cursor()
    im.execute("SELECT word FROM words WHERE word = ?",(kelime,))
    sozluk = im.fetchall()
    db.close
    if sozluk != []:
        return True # DB'de var
    else: return False # DB'de yok

# Kelimeyi database'e ekliyor
def db_ekle(kelime):
    db = sql.connect("gunluk_turkce.sqlite")
    im = db.cursor()
    im.execute("INSERT INTO words VALUES (?)", (kelime,))
    db.commit()
    db.close()

# Kelimeyi kontrol edip database'e ekliyor.    
for word in words:
    word = yardimci.delete_undefined_letters(word)
    if db_kontrol(word):
        continue
    else:
        answer = input(print("'" + word + "' (E/H): "))
        if answer == 'e' or answer == 'E':
            db_ekle(word)
            
            