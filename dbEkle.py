import sqlite3 as sql
veri = input("veri:")
kelimeler = veri.split()


def db_kontrol(kelime):
    db = sql.connect("gunluk_turkce.sqlite")
    im = db.cursor()
    im.execute("SELECT word FROM words WHERE word = ?",(kelime,))
    sozluk = im.fetchall()
    db.close
    if sozluk != []:
        return True # DB'de var
    else: return False # DB'de yok

def db_ekle(kelime):
    db = sql.connect("gunluk_turkce.sqlite")
    im = db.cursor()
    im.execute("INSERT INTO words VALUES (?)", (kelime,))
    db.commit()
    db.close()

def string_temizle(kelime):
    kelime = str.lower(kelime)
    kelime = kelime.replace('?', '')
    kelime = kelime.replace('.', '')
    kelime = kelime.replace('!', '')
    kelime = kelime.replace(',', '')
    kelime = kelime.replace(';', '')
    kelime = kelime.replace(':', '')
    kelime = kelime.replace('’', '')
    kelime = kelime.replace('“', '')
    kelime = kelime.replace('”', '')
    kelime = kelime.replace('…', '')
    kelime = kelime.replace('(', '')
    kelime = kelime.replace(')', '')
    return kelime
    
for kelime in kelimeler:
    kelime = string_temizle(kelime)
    if db_kontrol(kelime):
        continue
    else:
        cevap = input(print("'" + kelime + "' (E/H): "))
        if cevap == 'e' or cevap == 'E':
            db_ekle(kelime)
            
            