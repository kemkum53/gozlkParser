import sqlite3 as sql
import yardimci

veri = input("veri:")
kelimeler = veri.split()

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
for kelime in kelimeler:
    kelime = yardimci.delete_undefined_letters(kelime)
    if db_kontrol(kelime):
        continue
    else:
        cevap = input(print("'" + kelime + "' (E/H): "))
        if cevap == 'e' or cevap == 'E':
            db_ekle(kelime)
            
            