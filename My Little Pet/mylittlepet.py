import random
import tkinter as tk
from tkinter import messagebox
import time
from tkinter.ttk import Combobox
from tkinter import ttk
from PIL import Image, ImageTk
import json
from cryptography.fernet import Fernet
import pygame
import threading

key_file = 'secret.key'

def generate_or_load_key():
    try:
        # Anahtarı dosyadan yükle
        with open(key_file, 'rb') as kf:
            key = kf.read()
    except FileNotFoundError:
        # Dosya yoksa yeni anahtar oluştur ve dosyaya kaydet
        key = Fernet.generate_key()
        with open(key_file, 'wb') as kf:
            kf.write(key)
    
    return Fernet(key)

cipher_suite = generate_or_load_key()

# Verileri şifrelemek için fonksiyon
def encrypt_data(data):
    json_data = json.dumps(data).encode('utf-8')
    encrypted_data = cipher_suite.encrypt(json_data)
    return encrypted_data

# Şifrelenmiş veriyi açmak için fonksiyon
def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    json_data = decrypted_data.decode('utf-8')
    data = json.loads(json_data)
    return data

# Veri kaydetme işlemi
def save_data():
    global coin, gem, egg, pet, mypets, durumlar, cinsave, muzik, myfood, petname
    data_to_save = {
        'coin': coin,
        'gem': gem,
        'egg': egg,
        'pet': pet,
        'mypets': mypets,
        'durumlar': durumlar,
        'cinsave': cinsave,
        'muzik': muzik,
        'myfood': myfood,
        'petname': petname
    }
    encrypted_data = encrypt_data(data_to_save)
    with open('data.json', 'wb') as file:
        file.write(encrypted_data)
    print(pet, mypets,durumlar,cinsave,muzik, myfood, petname)

def load_data():
    try:
        with open('data.json', 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = decrypt_data(encrypted_data)
            # Güncellenmiş coin, gem ve egg verilerini al
            coin = decrypted_data['coin']
            gem = decrypted_data['gem']
            egg = decrypted_data['egg']
            pet = decrypted_data['pet']
            mypets = decrypted_data['mypets']
            durumlar = decrypted_data['durumlar']
            cinsave = decrypted_data['cinsave']
            muzik = decrypted_data['muzik']
            myfood = decrypted_data['myfood']
            petname = decrypted_data['petname']
            return coin, gem, egg, pet, mypets, durumlar, cinsave, muzik, myfood, petname
    except FileNotFoundError:
        # Eğer dosya yoksa varsayılan veri döndür
        return 0, 0, {'Cat': 1, 'Dog': 0, 'Chick': 0}, 0, [], {'Açlık': 100,'Tuvalet': 100, 'Uyku': 100}, [], ['relaxedscene'], {'elma': 1, 'havuc': 1,'karpuz': 0,'biftek': 0}, ['Pet']

global coin
global gem
global eggs
global egg
global yumurtalar
global coinint
global gemint
global odan
global pets
global yatakoda
global mypets
global durumlar
global cinsave
global muzik
global myfood
global food
global sayi
global petname
# Global değişkenler ve örnek veri
coin, gem, egg, pet, mypets, durumlar, cinsave, muzik, myfood, petname = load_data()

# Veriyi şifreleyerek kaydetme
save_data()

# Veriyi deşifre ederek yükleme
loaded_data = load_data()

# Pygame'i başlat
pygame.mixer.init()

def play_music():
    global muzik
    pygame.mixer.music.load(f"music/{muzik[0]}.mp3")
    pygame.mixer.music.play(-1)

# Müziği ayrı bir iş parçacığında (thread) başlat
music_thread = threading.Thread(target=play_music)
music_thread.start()


elmaaclik = 20
havucaclik = 40
karpuzaclik = 60
biftekaclik = 80

catgem=20
catcoin=catgem*100

doggem=40
dogcoin=doggem*100

chickgem=60
chickcoin=chickgem*100
a = 1
odan = []
pets = ['kedi','bkedi','kopek','bkopek','civciv','bcivciv']
catpets = ['kedi','bkedi']
dogpets = ['kopek','bkopek']
chickpets = ['civciv','bcivciv']
food = ['elma','havuc','karpuz','biftek']
     
def updatedurumlar():
    global durumlar
    global durumlarr
    global coin
    global gem
    global egg
    global durumlarr1
    sure = random.randint(10000, 100000)
    dus = random.randint(1,5)
    hangisi = random.randint(1,3)
    if hangisi == 1:
        durumlar['Açlık'] = max(0, durumlar['Açlık'] - dus)  # Açlık negatif olmasın
        
    elif hangisi == 2:
        durumlar['Tuvalet'] = max(0, durumlar['Tuvalet'] - dus)  # Tuvalet negatif olmasın
        
    elif hangisi == 3:
        durumlar['Uyku'] = max(0, durumlar['Uyku'] - dus)  # Tuvalet negatif olmasın
        
    save_data()
    durumlarr.config(text=f'Durumlar: {durumlar}, Coin: {coin}, Gem: {gem}')
    durumlarr1.config(text=f'Yumurtalar: {egg}')
    odan[0].after(sure,updatedurumlar)
    
def updatelabeldurumlar():
    global durumlar
    global durumlarr
    global durumlarr1
    durumlarr.config(text=f'Durumlar: {durumlar}, Coin: {coin}, Gem: {gem}')
    durumlarr1.config(text=f'Yumurtalar: {egg}')
    
# egg["Cat"] += 1
def update_yumurtalar():
    global yumurtalar
    global egg
    yumurtalar.config(text=f"Yumurtalar: {egg}")
    yumurtalar.after(1000, update_yumurtalar)
    pet = True
def update_coin():
    global coin
    global coinint
    coinint.config(text=f"{coin}")
    coinint.after(1000, update_coin)
def update_gem():
    global gem
    global gemint
    gemint.config(text=f"{gem}")
    gemint.after(1000, update_gem)
def save():
    while True:
        time.sleep(10)
        save_data()

def yemekye():
    global sayi
    if sayi == 0:
        if myfood['elma'] == 0:
            messagebox.showinfo(title='Yemek Yedirme', message='Yeterince elman yok')
        else:
            myfood['elma'] -= 1
            durumlar['Açlık'] += elmaaclik
            if durumlar['Açlık'] > 100:
                durumlar['Açlık'] = 100  # Açlık 100'den fazla olamaz
            messagebox.showinfo(title='Yemek Yedirme', message=f"{petname[0]}'ye yemek yedirdin")
            updatelabeldurumlar()
    
    elif sayi == 1:
        if myfood['havuc'] == 0:
            messagebox.showinfo(title='Yemek Yedirme', message='Yeterince havucun yok')
        else:
            myfood['havuc'] -= 1
            durumlar['Açlık'] += havucaclik
            if durumlar['Açlık'] > 100:
                durumlar['Açlık'] = 100  # Açlık 100'den fazla olamaz
            messagebox.showinfo(title='Yemek Yedirme', message=f"{petname[0]}'ye yemek yedirdin")
            updatelabeldurumlar()
    
    elif sayi == 2:
        if myfood['karpuz'] == 0:
            messagebox.showinfo(title='Yemek Yedirme', message='Yeterince karpuzun yok')
        else:
            myfood['karpuz'] -= 1
            durumlar['Açlık'] += karpuzaclik
            if durumlar['Açlık'] > 100:
                durumlar['Açlık'] = 100  # Açlık 100'den fazla olamaz
            messagebox.showinfo(title='Yemek Yedirme', message=f"{petname[0]}'ye yemek yedirdin")
            updatelabeldurumlar()
    
    elif sayi == 3:
        if myfood['biftek'] == 0:
            messagebox.showinfo(title='Yemek Yedirme', message='Yeterince bifteğin yok')
        else:
            myfood['biftek'] -= 1
            durumlar['Açlık'] += biftekaclik
            if durumlar['Açlık'] > 100:
                durumlar['Açlık'] = 100  # Açlık 100'den fazla olamaz
            messagebox.showinfo(title='Yemek Yedirme', message=f"{petname[0]}'ye yemek yedirdin")
            updatelabeldurumlar()

def catpay1():
    global coin
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    global catcoin
    global catfree
    if egg['Cat'] == 5:
        messagebox.showinfo(title='Satın Alım',message='En fazla 5 kedi alabilirsin.')
    else:
        secenek = messagebox.askyesno(title='Ödeme Tipi', message='Ödemeyi coin ile mi yapacaksın?')
        if secenek == True:
            if coin < catcoin:
                messagebox.showinfo(title='Satın Alım',message='Kedi satın almak için yeterince coininiz yok')
            else:
                catpaycoinsecim = messagebox.askyesno(title='Satın Alım', message='Coin ile kedi almak istediğine emin misin?')
                if catpaycoinsecim == True:
                    coin = coin - catcoin
                    egg["Cat"] += 1
                    messagebox.showinfo(title='Satın Alım',message=f'Kedi satın alma işlemin gerçekleştirildi {catcoin} coin')
                    save_data()
                else:
                    messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
        elif secenek == False:
            if gem < catgem:
                messagebox.showinfo(title='Satın Alım',message='Kedi satın almak için yeterince geminiz yok')
            else:
                catpaygemsecim = messagebox.askyesno(title='Satın Alım', message='Gem ile kedi almak istediğine emin misin?')
                if catpaygemsecim == True:
                    gem = gem - catgem
                    egg["Cat"] += 1
                    messagebox.showinfo(title='Satın Alım',message=f'Kedi satın alma işlemin gerçekleştirildi {catgem} gem')
                    save_data()
                else:
                    messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')

def dogpay1():
    global coin
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    if egg['Dog'] == 5:
        messagebox.showinfo(title='Satın Alım',message='En fazla 5 köpek alabilirsin.')
    else:
        secenek1 = messagebox.askyesno(title='Satın Alım', message='Ödemeyi coin ile mi yapacaksın?')
        if secenek1 == True:
            if coin < dogcoin:
                messagebox.showinfo(title='Satın Alım',message='Köpek satın almak için yeterince coininiz yok')
            else:
                dogpaycoinsecim = messagebox.askyesno(title='Satın Alım', message='Coin ile köpek almak istediğine emin misin?')
                if dogpaycoinsecim == True:
                    coin = coin - dogcoin
                    egg["Dog"] += 1
                    messagebox.showinfo(title='Satın Alım',message=f'Köpek satın alma işlemin gerçekleştirildi {dogcoin} coin')
                    save_data()
                else:
                    messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
        elif secenek1 == False:
            if gem < doggem:
                messagebox.showinfo(title='Satın Alım',message='Köpek satın almak için yeterince geminiz yok')
            else:
                dogpaygemsecim = messagebox.askyesno(title='Satın Alım', message='Gem ile köpek almak istediğine emin misin?')
                if dogpaygemsecim == True:
                    gem = gem - doggem
                    egg["Dog"] += 1
                    messagebox.showinfo(title='Satın Alım',message=f'Köpek satın alma işlemin gerçekleştirildi {doggem} gem')
                    save_data()
                else:
                    messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')

def chickpay1():
    global coin
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    if egg['Chick'] == 5:
        messagebox.showinfo(title='Satın Alım',message='En fazla 5 civciv alabilirsin.')
    else:
        secenek2 = messagebox.askyesno(title='Satın Alım', message='Ödemeyi coin ile mi yapacaksın?')
        if secenek2 == True:
            if coin < chickcoin:
                messagebox.showinfo(title='Satın Alım',message='Civciv satın almak için yeterince coininiz yok')
            else:
                chickpaycoinsecim = messagebox.askyesno(title='Satın Alım', message='Coin ile civciv almak istediğine emin misin?')
                if chickpaycoinsecim == True:
                    coin = coin - chickcoin
                    egg["Chick"] += 1
                    messagebox.showinfo(title='Satın Alım',message=f'Civciv satın alma işlemin gerçekleştirildi {chickcoin} coin')
                    save_data()
                else:
                    messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
        elif secenek2 == False:
            if gem < chickgem:
                messagebox.showinfo(title='Satın Alım',message='Civciv satın almak için yeterince geminiz yok')
            else:
                chickpaygemsecim = messagebox.askyesno(title='Satın Alım', message='Gem ile civciv almak istediğine emin misin?')
                if chickpaygemsecim == True:
                    gem = gem - chickgem
                    egg["Chick"] += 1
                    messagebox.showinfo(title='Satın Alım',message='Civciv satın alma işlemin gerçekleştirildi {chickgem} gem')
                    save_data()
                else:
                    messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')

def gem_pay1():
    global coin # 5 20 50
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    if coin < 500:
        messagebox.showinfo(title='Satın Alım',message='Yeterince coinin yok')
    else:
        secenek3 = messagebox.askyesno(title='Satın Alım',message='5 gem satın almak istiyor musun?')
        if secenek3 == True:
            coin = coin - 500
            gem = gem + 5
            messagebox.showinfo(title='Satın Alım',message='Gem satın alma işlemin gerçekleştirildi (+5 gem, -500 coin)')
            save_data()
        else:
            messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
            
def gem_pay2():
    global coin # 5 20 50
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    if coin < 2000:
        messagebox.showinfo(title='Satın Alım',message='Yeterince coinin yok')
    else:
        secenek4 = messagebox.askyesno(title='Satın Alım',message='20 gem satın almak istiyor musun?')
        if secenek4 == True:
            coin = coin - 2000
            gem = gem + 20
            messagebox.showinfo(title='Satın Alım',message='Gem satın alma işlemin gerçekleştirildi (+20 gem, -2000 coin)')
            save_data()
        else:
            messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')

def gem_pay3():
    global coin # 5 20 50
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    if coin < 5000:
        messagebox.showinfo(title='Satın Alım',message='Yeterince coinin yok')
    else:
        secenek5 = messagebox.askyesno(title='Satın Alım',message='50 gem satın almak istiyor musun?')
        if secenek5 == True:
            coin = coin - 5000
            gem = gem + 50
            messagebox.showinfo(title='Satın Alım',message='Gem satın alma işlemin gerçekleştirildi (+50 gem, -5000 coin)')
            save_data()
        else:
            messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
            
def elma_pay():
    global coin # 5 20 50
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    global myfood
    secenek2 = messagebox.askyesno(title='Satın Alım', message='Ödemeyi coin ile mi yapacaksın?')
    if secenek2 == True:
        if coin < 500:
            messagebox.showinfo(title='Satın Alım',message='Elma satın almak için yeterince coininiz yok')
        else:
            chickpaycoinsecim = messagebox.askyesno(title='Satın Alım', message='Coin ile elma almak istediğine emin misin?')
            if chickpaycoinsecim == True:
                coin = coin - 500
                myfood["elma"] += 1
                messagebox.showinfo(title='Satın Alım',message='Elma satın alma işlemin gerçekleştirildi 500 coin')
                save_data()
            else:
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
    elif secenek2 == False:
        if gem < 5:
            messagebox.showinfo(title='Satın Alım',message='Elma satın almak için yeterince geminiz yok')
        else:
            chickpaygemsecim = messagebox.askyesno(title='Satın Alım', message='Gem ile elma almak istediğine emin misin?')
            if chickpaygemsecim == True:
                gem = gem - 5
                myfood['elma'] += 1
                messagebox.showinfo(title='Satın Alım',message='Elma satın alma işlemin gerçekleştirildi 5 gem')
                save_data()
            else:
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi') 
def havuc_pay():
    global coin # 5 20 50
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    global myfood
    secenek2 = messagebox.askyesno(title='Satın Alım', message='Ödemeyi coin ile mi yapacaksın?')
    if secenek2 == True:
        if coin < 2000:
            messagebox.showinfo(title='Satın Alım',message='Havuç satın almak için yeterince coininiz yok')
        else:
            chickpaycoinsecim = messagebox.askyesno(title='Satın Alım', message='Coin ile Havuç almak istediğine emin misin?')
            if chickpaycoinsecim == True:
                coin = coin - 2000
                myfood["havuc"] += 1
                messagebox.showinfo(title='Satın Alım',message='Havuç satın alma işlemin gerçekleştirildi 2000 coin')
                save_data()
            else:
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
    elif secenek2 == False:
        if gem < 20:
            messagebox.showinfo(title='Satın Alım',message='Havuç satın almak için yeterince geminiz yok')
        else:
            chickpaygemsecim = messagebox.askyesno(title='Satın Alım', message='Gem ile Havuç almak istediğine emin misin?')
            if chickpaygemsecim == True:
                gem = gem - 20
                myfood['havuc'] += 1
                messagebox.showinfo(title='Satın Alım',message='Havuç satın alma işlemin gerçekleştirildi 20 gem')
                save_data()
            else:
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi') 
def karpuz_pay():
    global coin # 5 20 50
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    global myfood
    secenek2 = messagebox.askyesno(title='Satın Alım', message='Ödemeyi coin ile mi yapacaksın?')
    if secenek2 == True:
        if coin < 5000:
            messagebox.showinfo(title='Satın Alım',message='Karpuz satın almak için yeterince coininiz yok')
        else:
            chickpaycoinsecim = messagebox.askyesno(title='Satın Alım', message='Coin ile Karpuz almak istediğine emin misin?')
            if chickpaycoinsecim == True:
                coin = coin - 5000
                myfood["karpuz"] += 1
                messagebox.showinfo(title='Satın Alım',message='Karpuz satın alma işlemin gerçekleştirildi 5000 coin')
                save_data()
            else:
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
    elif secenek2 == False:
        if gem < 50:
            messagebox.showinfo(title='Satın Alım',message='Karpuz satın almak için yeterince geminiz yok')
        else:
            chickpaygemsecim = messagebox.askyesno(title='Satın Alım', message='Gem ile Karpuz almak istediğine emin misin?')
            if chickpaygemsecim == True:
                gem = gem - 50
                myfood['karpuz'] += 1
                messagebox.showinfo(title='Satın Alım',message='Havuç satın alma işlemin gerçekleştirildi 50 gem')
                save_data()
            else:
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi') 
def biftek_pay():
    global coin # 5 20 50
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    global myfood
    secenek2 = messagebox.askyesno(title='Satın Alım', message='Ödemeyi coin ile mi yapacaksın?')
    if secenek2 == True:
        if coin < 7000:
            messagebox.showinfo(title='Satın Alım',message='Biftek satın almak için yeterince coininiz yok')
        else:
            chickpaycoinsecim = messagebox.askyesno(title='Satın Alım', message='Coin ile Biftek almak istediğine emin misin?')
            if chickpaycoinsecim == True:
                coin = coin - 7000
                myfood["biftek"] += 1
                messagebox.showinfo(title='Satın Alım',message='Biftek satın alma işlemin gerçekleştirildi 7000 coin')
                save_data()
            else:
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi')
    elif secenek2 == False:
        if gem < 70:
            messagebox.showinfo(title='Satın Alım',message='Biftek satın almak için yeterince geminiz yok')
        else:
            chickpaygemsecim = messagebox.askyesno(title='Satın Alım', message='Gem ile Biftek almak istediğine emin misin?')
            if chickpaygemsecim == True:
                gem = gem - 70
                myfood['biftek'] += 1
                messagebox.showinfo(title='Satın Alım',message='Biftek satın alma işlemin gerçekleştirildi 70 gem')
                save_data()
            else:
                messagebox.showinfo(title='Satın Alım',message='İşlem İptal Edildi') 
def dukkan():
    global coin
    global gem
    global egg
    global eggs
    global catpay
    global yumurtalar
    global coinint
    global gemint
    global odan
    global myfood
    odan.clear()
    dukkan=tk.Tk()
    dukkan.title('Dükkan')
    dukkan.geometry('500x500+400+50')
    dukkan.config(bg='black')
    dukkan.resizable(False,False)
    odan.append(dukkan)

    dukkan_image = Image.open("rooms/dukkan.jpg")
    dukkan_image = dukkan_image.resize((500, 500), Image.LANCZOS)
    dp_image = ImageTk.PhotoImage(dukkan_image)
    
    background_label = tk.Label(odan[0], image=dp_image)
    background_label.pack()

    baslik = tk.Label(dukkan,text='DÜKKAN',fg='white',bg='black',font='Timer 15 bold')
    baslik.place(x=200,y=0)
    
    playercoin = tk.Label(dukkan,text='Coin:',fg='white',bg='black',font='Timer 13 bold')
    playercoin.place(x=350,y=0)
    
    coinint = tk.Label(dukkan,text=coin,fg='white',bg='black',font='Timer 13 bold')
    coinint.place(x=400,y=0)
    update_coin()
    
    playergem = tk.Label(dukkan,text='Gem:',fg='white',bg='black',font='Timer 13 bold')
    playergem.place(x=350,y=30)
    
    gemint = tk.Label(dukkan,text=gem,fg='white',bg='black',font='Timer 13 bold')
    gemint.place(x=400,y=30)
    update_gem()

    pets = tk.Label(dukkan,text='Pet Satın Al',fg='white',bg='black',font='Timer 12 bold')
    pets.place(x=10,y=30)

    def petler():
        global coin
        global gem
        global egg
        global eggs
        global catpay
        global yumurtalar
        global coinint
        global gemint
        global odan
        global myfood
        petac.destroy()
        cointranslate.destroy()
        gemac.destroy()
        pets.destroy()
        yemekac.destroy()
        yemeklb.destroy()
        
        catpay = tk.Label(dukkan,text=f'{catgem} Gem/{catcoin} Coin',fg='white',bg='black',font='Timer 13 bold')
        catpay.place(x=75,y=60)
        
        dogpay = tk.Label(dukkan,text=f'{doggem} Gem/{dogcoin} Coin',fg='white',bg='black',font='Timer 13 bold')
        dogpay.place(x=80,y=90)
        
        chickpay = tk.Label(dukkan,text=f'{chickgem} Gem/{chickcoin} Coin',fg='white',bg='black',font='Timer 13 bold')
        chickpay.place(x=90,y=120)
        
        catbuton = tk.Button(dukkan,text='Buy Cat',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=catpay1)
        catbuton.place(x=10,y=60)
    
        dogbuton = tk.Button(dukkan,text='Buy Dog',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=dogpay1)
        dogbuton.place(x=10,y=90)
    
        chickbuton = tk.Button(dukkan,text='Buy Chick',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=chickpay1)
        chickbuton.place(x=10,y=120)

        yumurtalar = tk.Label(dukkan,text=egg,fg='white',bg='black',font='Timer 12 bold')
        yumurtalar.place(x=10,y=155)
        update_yumurtalar()
        
        geri = tk.Button(dukkan,text='<',fg='black',bg='white',activebackground='green',font='IMPACT 10 bold',command=ac)
        geri.place(x=10,y=200)
        
    petac = tk.Button(dukkan,text='Pet Dükkanı',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=petler)
    petac.place(x=10,y=60)
    
    cointranslate = tk.Label(dukkan,text='Gem Satın Al',fg='white',bg='black',font='Timer 12 bold')
    cointranslate.place(x=10,y=100)
    
    def gemler():
        global coin
        global gem
        global egg
        global eggs
        global catpay
        global yumurtalar
        global coinint
        global gemint
        global odan
        global myfood
        petac.destroy()
        pets.destroy()
        gemac.destroy()
        cointranslate.destroy()
        yemekac.destroy()
        yemeklb.destroy()
        
        gempay1 = tk.Label(dukkan,text='500 Coin',fg='white',bg='black',font='Timer 13 bold')
        gempay1.place(x=75,y=60)
        
        gempay2 = tk.Label(dukkan,text='2000 Coin',fg='white',bg='black',font='Timer 13 bold')
        gempay2.place(x=80,y=90)
        
        gempay3 = tk.Label(dukkan,text='5000 Coin',fg='white',bg='black',font='Timer 13 bold')
        gempay3.place(x=90,y=120)
        
        gem1 = tk.Button(dukkan,text='5 Gem',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=gem_pay1)
        gem1.place(x=10,y=60)
        
        gem2 = tk.Button(dukkan,text='20 Gem',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=gem_pay2)
        gem2.place(x=10,y=90)
        
        gem3 = tk.Button(dukkan,text='50 Gem',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=gem_pay3)
        gem3.place(x=10,y=120)
        
        geri = tk.Button(dukkan,text='<',fg='black',bg='white',activebackground='green',font='IMPACT 10 bold',command=ac)
        geri.place(x=10,y=150)        

    gemac = tk.Button(dukkan,text='Gem Dükkanı',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=gemler)
    gemac.place(x=10,y=130)

    yemeklb = tk.Label(dukkan,text='Yemek Satın Al',fg='white',bg='black',font='Timer 12 bold')
    yemeklb.place(x=10,y=170)

    def yemekler():
        global coin
        global gem
        global egg
        global eggs
        global catpay
        global yumurtalar
        global coinint
        global gemint
        global odan
        global myfood
        petac.destroy()
        pets.destroy()
        gemac.destroy()
        cointranslate.destroy()
        yemekac.destroy()
        yemeklb.destroy()
        
        elma = tk.Label(dukkan,text='5 Gem/500 Coin',fg='white',bg='black',font='Timer 13 bold')
        elma.place(x=75,y=60)
        
        havuc = tk.Label(dukkan,text='20 Gem/2000 Coin',fg='white',bg='black',font='Timer 13 bold')
        havuc.place(x=80,y=90)
        
        karpuz = tk.Label(dukkan,text='50 Gem/5000 Coin',fg='white',bg='black',font='Timer 13 bold')
        karpuz.place(x=80,y=120)
        
        biftek = tk.Label(dukkan,text='70 Gem/7000 Coin',fg='white',bg='black',font='Timer 13 bold')
        biftek.place(x=70,y=150)
        
        elma1 = tk.Button(dukkan,text='Elma',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=elma_pay)
        elma1.place(x=10,y=60)
        
        havuc1 = tk.Button(dukkan,text='Havuç',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=havuc_pay)
        havuc1.place(x=10,y=90)
        
        karpuz1 = tk.Button(dukkan,text='Karpuz',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=karpuz_pay)
        karpuz1.place(x=10,y=120)
        
        biftek1 = tk.Button(dukkan,text='Biftek',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=biftek_pay)
        biftek1.place(x=10,y=150)
        
        geri = tk.Button(dukkan,text='<',fg='black',bg='white',activebackground='green',font='IMPACT 10 bold',command=ac)
        geri.place(x=10,y=180) 

    yemekac = tk.Button(dukkan,text='Yemek Dükkanı',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=yemekler)
    yemekac.place(x=10,y=200)    
    
    geri = tk.Button(dukkan,text='Geri Dön',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=disarirt)
    geri.place(x=296,y=245)
    
    
        
    dukkan.mainloop()
    
def ac():
    odan[0].destroy() 
    dukkan()
    
def oyunlar():
    global coin
    global odan
    odan.clear()
    oyunlar=tk.Tk()
    oyunlar.title('Oyunlar')
    oyunlar.config(bg='black')
    oyunlar.resizable(False, False)
    oyunlar.geometry('400x400+400+50')
    odan.append(oyunlar)
    oyun_image = Image.open("rooms/oyun.png")
    oyun_image = oyun_image.resize((460, 400), Image.LANCZOS)
    op_image = ImageTk.PhotoImage(oyun_image)
    
    op_label = tk.Label(odan[0], image=op_image)
    op_label.pack()
    geri = tk.Button(odan[0],text='Geri Dön',fg='black',bg='white',activebackground='green',font='Timer 10 bold',command=disarirt)
    geri.place(x=20,y=300)
    def custom_random_int(lower, upper, threshold, lower_prob, higher_prob):
        global coin
        while True:
            num = random.randint(lower, upper)
            if num <= threshold:
                if random.random() < lower_prob:
                    return num
            else:
                if random.random() < higher_prob:
                    return num
        
    def sayitahmin():
        global coin
        global hak
        global kontrol
        global rety
        rt = False
        secimler.destroy()
        buton.destroy()
        oyunlar.title('Sayı Tahmin')
        oyunlar.geometry('460x400+400+50')
        def yeni_oyun():
            global rety
            kontrol.destroy()
            rety.destroy()
            sayitahmin()        
        op_label = tk.Label(odan[0], image=op_image)
        op_label.pack()
        
        hak = 10
        tahminler = []
        sayi = random.randint(10,100)
        baslik = tk.Label(oyunlar,text='Tahmin',fg='white',bg='black',font='Timer 15 bold')
        baslik.place(x=10,y=10)
        
        kontrol = tk.Label(oyunlar,text='', fg='white', bg='black', font='Timer 15 bold')
        kontrol.place(x=10,y=100)        
        def kontrolu_guncelle(metin):
            global kontrol
            kontrol.config(text=metin)
            
        tahmin = tk.Entry()
        tahmin.place(x=10,y=40)
        def onaylama():
            global coin
            global hak
            global kontrol
            global rety

            try:
                tahmin_degeri = int(tahmin.get())
                
                if tahmin_degeri in tahminler:
                    kontrolu_guncelle('Aynı sayıyı giremezsin, tekrar denemelisin.')
                elif tahmin_degeri > 100 or tahmin_degeri < 10:
                    kontrolu_guncelle('10 ile 100 arası bir sayı gir.')                   
                elif hak == 1:
                    baslik.destroy()
                    tahmin.destroy()
                    onay.destroy()
                    kontrolu_guncelle('Hakkın bitti, kaybettin. Şimdi ne yapacaksın?')
                    

                    rety = tk.Button(oyunlar, text='Yeniden Dene',fg='black',bg='white',command=yeni_oyun)
                    rety.place(x=20,y=140)

                    
                elif tahmin_degeri > sayi:
                    tahminler.append(tahmin_degeri)
                    hak = hak - 1
                    kontrolu_guncelle(f'{hak} hakkın kaldı. Daha küçük bir sayı gir')
                elif tahmin_degeri < sayi:
                    tahminler.append(tahmin_degeri)
                    hak = hak - 1
                    kontrolu_guncelle(f'{hak} hakkın kaldı. Daha büyük bir sayı gir')
                else:
                    kontrolu_guncelle('Tebrikler! Doğru tahmin!')
                    baslik.destroy()
                    tahmin.destroy()
                    onay.destroy()
                    random_number = custom_random_int(100, 9000, 2000, 0.8, 0.2)
                    messagebox.showinfo(title='Coin',message=f'{random_number} Coin kazandın!')
                    save_data()
                    coin = coin + random_number
                    rety = tk.Button(oyunlar, text='Yeniden Dene',fg='black',bg='white',command=yeni_oyun)
                    rety.place(x=20,y=140)
            except ValueError:
                kontrolu_guncelle('Geçerli bir sayı girin.')
                
        onay = tk.Button(oyunlar,text='Tahmin Et',fg='black',bg='white',command=onaylama)
        onay.place(x=10,y=70)



    def basla():
        global coin
        if secimler.get()==oyun[0]:
            sayitahmin()

    x = tk.StringVar()
    oyun=['Sayı Tahmin Etme','Adam Asmaca']
    secimler = Combobox(oyunlar,values=oyun,height=3)
    secimler.place(x=10, y= 10)
    
    buton=tk.Button(oyunlar,text='Onayla',command=(basla))
    buton.place(x=10,y=40)
    

    oyunlar.mainloop
def ayarlarrt():
    global odan
    save_data()
    odan[0].destroy()
    ayarlar()
def dukkanrt():
    global odan
    save_data()
    odan[0].destroy()
    dukkan()
def oyunlarrt():
    global odan
    save_data()
    odan[0].destroy()
    oyunlar()
def yatakrt():
    global odan
    save_data()
    odan[0].destroy()
    yatakodasi()
def oturmart():
    global odan
    save_data()
    odan[0].destroy()
    oturmaodasi()
def tuvaletrt():
    global odan
    save_data()
    odan[0].destroy()
    tuvalet()
def disarirt():
    global odan
    save_data()
    odan[0].destroy()
    disari1()
def mutfakrt():
    global odan
    save_data()
    odan[0].destroy()
    mutfak()



def yatakodasi():
    global coin
    global gem
    global egg
    global eggs
    global catpay
    global yumurtalar
    global coinint
    global gemint
    global odan
    global aclik
    global durumlarr
    global durumlar
    global durumlarr1
    global petname
    odan.clear()
    yatakoda = tk.Tk()
    yatakoda.geometry('650x600+400+50')
    yatakoda.title('Yatak Odası')
    yatakoda.resizable(False, False)
    odan.append(yatakoda)

    # her odada aynı olmalı
    blacks = tk.Label(odan[0], text='**********************************************************************************************************************************',
                fg='black',bg='black',font='Titles 25 bold')
    blacks.pack()

    ytkoda = tk.Button(odan[0], text='Yatak Odası',bg='black',fg='white',command=yatakrt)
    ytkoda.place(x=290,y=10)

    salon = tk.Button(odan[0], text='Oturma Odası',bg='black',fg='white',command=oturmart)
    salon.place(x=170,y=10)

    tuvalet = tk.Button(odan[0], text='Tuvalet',bg='black',fg='white',command=tuvaletrt)
    tuvalet.place(x=400,y=10)     

    mutfak = tk.Button(odan[0], text='Mutfak',bg='black',fg='white',command=mutfakrt)
    mutfak.place(x=480,y=10)     

    disari = tk.Button(odan[0], text='Dışarı',bg='black',fg='white',command=disarirt)
    disari.place(x=100,y=10)
    ayarlar = tk.Button(odan[0], text='Ayarlar',bg='black',fg='white',command=ayarlarrt)
    ayarlar.place(x=550,y=10)    
    # Yatak Odası arka plan resmini yükleyin
    yatak_image = Image.open("rooms/Yatak_Odası.jpg")
    yatak_image = yatak_image.resize((650, 600), Image.LANCZOS)

    # Civciv resmini yükleyin
    civciv_image = Image.open(f"pets/{mypets[0]}.png")
    civciv_image = civciv_image.resize((250, 250), Image.LANCZOS)

    # Yatak Odası ve civciv resimlerini birleştirin
    yatak_image.paste(civciv_image, (200, 350), civciv_image)

    # Yeni bir ImageTk.PhotoImage nesnesi oluşturun
    photo = ImageTk.PhotoImage(yatak_image)

    # Arka plan resmini içeren bir Label widget'ı oluşturun ve yerleştirin
    label = tk.Label(yatakoda, image=photo)
    label.image = photo
    label.pack()
    
    durumlarr = tk.Label(odan[0], text=f'Durumlar: {durumlar}, Coin: {coin}, Gem: {gem}',bg='black',fg='white',font='Timer 10 bold')
    durumlarr.place(x=0,y=40)
    durumlarr1 = tk.Label(odan[0], text=f'Yumurtalar: {egg}',bg='black',fg='white',font='Timer 10 bold')
    durumlarr1.place(x=0,y=60)
    updatedurumlar()


    def uyku():
        if durumlar['Uyku'] == 100:
            messagebox.showinfo(title='Uyku', message=f"{petname[0]}'nin hiç uykusu yok")
        else:
            # Tam siyah arka plan oluşturun
            black_screen = tk.Label(odan[0], bg='black', width=650, height=600)
            black_screen.place(x=0, y=0) 

            # Geri sayım başlatan fonksiyon
            countdown_label = tk.Label(odan[0], text='50', bg='black', fg='white', font='Timer 20 bold')
            countdown_label.place(x=300, y=200)

            # Geri sayımı güncelleyen fonksiyon
            def update_count():
                nonlocal countdown_label
                count = int(countdown_label.cget("text"))
                if count > 0:
                    count -= 1
                    countdown_label.config(text=str(count))
                    odan[0].after(1000, update_count)
                else:
                    countdown_label.config(text=f'{petname[0]} uyandı!')
                    durumlar['Uyku'] = 100
                    black_screen.destroy()
                    countdown_label.after(2000, countdown_label.destroy)
                    updatelabeldurumlar()

            update_count()

    uyu = tk.Button(odan[0], text='Uyu',bg='black',fg='white',command=uyku)
    uyu.place(x=200,y=400)
    
    
    yatakoda.mainloop()


def oturmaodasi():
    global coin
    global gem
    global egg
    global eggs
    global catpay
    global yumurtalar
    global coinint
    global gemint
    global odan
    global durumlar
    global durumlarr
    global durumlarr1
    odan.clear()
    oturmaoda = tk.Tk()
    oturmaoda.geometry('650x600+400+50')
    oturmaoda.title('Oturma Odası')
    oturmaoda.resizable(False, False)
    odan.append(oturmaoda)

    # her odada aynı olmalı
    blacks = tk.Label(odan[0], text='**********************************************************************************************************************************',
                fg='black',bg='black',font='Titles 25 bold')
    blacks.pack()

    ytkoda = tk.Button(odan[0], text='Yatak Odası',bg='black',fg='white',command=yatakrt)
    ytkoda.place(x=290,y=10)

    salon = tk.Button(odan[0], text='Oturma Odası',bg='black',fg='white',command=oturmart)
    salon.place(x=170,y=10)

    tuvalet = tk.Button(odan[0], text='Tuvalet',bg='black',fg='white',command=tuvaletrt)
    tuvalet.place(x=400,y=10)     

    mutfak = tk.Button(odan[0], text='Mutfak',bg='black',fg='white',command=mutfakrt)
    mutfak.place(x=480,y=10)     

    disari = tk.Button(odan[0], text='Dışarı',bg='black',fg='white',command=disarirt)
    disari.place(x=100,y=10)  
    
    ayarlar = tk.Button(odan[0], text='Ayarlar',bg='black',fg='white',command=ayarlarrt)
    ayarlar.place(x=550,y=10)        
    # Yatak Odası arka plan resmini yükleyin
    oturma_image = Image.open("rooms/Oturma_Odası.jpg")
    oturma_image = oturma_image.resize((650, 600), Image.LANCZOS)

    # Civciv resmini yükleyin
    pet_image = Image.open(f"pets/{mypets[0]}.png")
    pet_image = pet_image.resize((250, 250), Image.LANCZOS)

    # Yatak Odası ve civciv resimlerini birleştirin
    oturma_image.paste(pet_image, (200, 350), pet_image)

    # Yeni bir ImageTk.PhotoImage nesnesi oluşturun
    photo = ImageTk.PhotoImage(oturma_image)

    # Arka plan resmini içeren bir Label widget'ı oluşturun ve yerleştirin
    label = tk.Label(oturmaoda, image=photo)
    label.image = photo
    label.pack()
    durumlarr = tk.Label(odan[0], text=f'Durumlar: {durumlar}, Coin: {coin}, Gem: {gem}',bg='black',fg='white',font='Timer 10 bold')
    durumlarr.place(x=0,y=40)
    durumlarr1 = tk.Label(odan[0], text=f'Yumurtalar: {egg}',bg='black',fg='white',font='Timer 10 bold')
    durumlarr1.place(x=0,y=60)
    updatedurumlar()
    oturmaoda.mainloop()

def tuvalet():
    global coin
    global gem
    global egg
    global eggs
    global catpay
    global yumurtalar
    global coinint
    global gemint
    global odan
    global durumlar
    global durumlarr
    global durumlarr1
    odan.clear()
    tuvalet1 = tk.Tk()
    tuvalet1.geometry('650x600+400+50')
    tuvalet1.title('Tuvalet')
    tuvalet1.resizable(False, False)
    odan.append(tuvalet1)

    # her odada aynı olmalı
    blacks = tk.Label(odan[0], text='**********************************************************************************************************************************',
                fg='black',bg='black',font='Titles 25 bold')
    blacks.pack()

    ytkoda = tk.Button(odan[0], text='Yatak Odası',bg='black',fg='white',command=yatakrt)
    ytkoda.place(x=290,y=10)

    salon = tk.Button(odan[0], text='Oturma Odası',bg='black',fg='white',command=oturmart)
    salon.place(x=170,y=10)

    tuvalet = tk.Button(odan[0], text='Tuvalet',bg='black',fg='white',command=tuvaletrt)
    tuvalet.place(x=400,y=10)     

    mutfak = tk.Button(odan[0], text='Mutfak',bg='black',fg='white',command=mutfakrt)
    mutfak.place(x=480,y=10)     

    disari = tk.Button(odan[0], text='Dışarı',bg='black',fg='white',command=disarirt)
    disari.place(x=100,y=10)    

    ayarlar = tk.Button(odan[0], text='Ayarlar',bg='black',fg='white',command=ayarlarrt)
    ayarlar.place(x=550,y=10)        
    # Yatak Odası arka plan resmini yükleyin
    tuvalet_image = Image.open("rooms/Tuvalet.jpg")
    tuvalet_image = tuvalet_image.resize((650, 600), Image.LANCZOS)

    # Civciv resmini yükleyin
    pet_image = Image.open(f"pets/{mypets[0]}.png")
    pet_image = pet_image.resize((250, 250), Image.LANCZOS)

    # Yatak Odası ve civciv resimlerini birleştirin
    tuvalet_image.paste(pet_image, (140, 200), pet_image)

    # Yeni bir ImageTk.PhotoImage nesnesi oluşturun
    photo = ImageTk.PhotoImage(tuvalet_image)

    # Arka plan resmini içeren bir Label widget'ı oluşturun ve yerleştirin
    label = tk.Label(odan[0], image=photo)
    label.image = photo
    label.pack()

    def tuvaletyap():
        if durumlar['Tuvalet'] == 100:
            messagebox.showinfo(title='Tuvaletini yapamazsın', message=f"{petname[0]}'nin tuvaleti yok")
        else:
            messagebox.showinfo(title='Durum', message='Tuvalet yapılıyor')
            odan[0].after(2000, perform_tuvaletyap)  # 2000 ms sonra tuvaleti yapmayı çağır

    def perform_tuvaletyap():
        durumlar['Tuvalet'] = 100
        save_data()
        messagebox.showinfo(title='Rahatladım', message=f"{petname[0]}'nin tuvaletini başarıyla yaptırdın")
        updatelabeldurumlar()

        
           
    tuvayap = tk.Button(odan[0], text='Tuvaletini Yap',bg='black',fg='white',command=tuvaletyap) 
    tuvayap.place(x=190,y=470)
    
    durumlarr = tk.Label(odan[0], text=f'Durumlar: {durumlar}, Coin: {coin}, Gem: {gem}',bg='black',fg='white',font='Timer 10 bold')
    durumlarr.place(x=0,y=40)
    durumlarr1 = tk.Label(odan[0], text=f'Yumurtalar: {egg}',bg='black',fg='white',font='Timer 10 bold')
    durumlarr1.place(x=0,y=60)
    updatedurumlar()
    tuvalet1.mainloop()
    
def mutfak():
    global coin, gem, egg, odan, durumlar, durumlarr, durumlarr1, food, sayi, label
    odan.clear()
    mutfak1 = tk.Tk()
    mutfak1.geometry('650x600+400+50')
    mutfak1.title('Mutfak')
    mutfak1.resizable(False, False)
    odan.append(mutfak1)

    # Her odada aynı olmalı
    blacks = tk.Label(odan[0], text='**********************************************************************************************************************************',
                      fg='black', bg='black', font='Titles 25 bold')
    blacks.pack()

    ytkoda = tk.Button(odan[0], text='Yatak Odası', bg='black', fg='white', command=yatakrt)
    ytkoda.place(x=290, y=10)

    salon = tk.Button(odan[0], text='Oturma Odası', bg='black', fg='white', command=oturmart)
    salon.place(x=170, y=10)

    tuvalet = tk.Button(odan[0], text='Tuvalet', bg='black', fg='white', command=tuvaletrt)
    tuvalet.place(x=400, y=10)

    mutfak = tk.Button(odan[0], text='Mutfak', bg='black', fg='white', command=mutfakrt)
    mutfak.place(x=480, y=10)

    disari = tk.Button(odan[0], text='Dışarı', bg='black', fg='white', command=disarirt)
    disari.place(x=100, y=10)

    ayarlar = tk.Button(odan[0], text='Ayarlar', bg='black', fg='white', command=ayarlarrt)
    ayarlar.place(x=550, y=10)

    # Arka plan resmini içeren bir Label widget'ı oluşturun ve yerleştirin
    label = tk.Label(odan[0])
    label.pack()

    # Yemek resmini güncelleyen fonksiyon
    def foodupdate():
        global sayi, label
        # Mutfak arka plan resmini yükleyin
        mutfak_image = Image.open("rooms/Mutfak.jpg")
        mutfak_image = mutfak_image.resize((650, 600), Image.LANCZOS)

        # Evcil hayvan resmini yükleyin
        pet_image = Image.open(f"pets/{mypets[0]}.png")
        pet_image = pet_image.resize((250, 250), Image.LANCZOS)

        # Mutfak ve evcil hayvan resimlerini birleştirin
        mutfak_image.paste(pet_image, (200, 350), pet_image)

        # Yemek resmini yükleyin
        foodim = Image.open(f"draw/{food[sayi]}.png")
        foodim = foodim.resize((200, 200), Image.LANCZOS)
        mutfak_image.paste(foodim, (240, 50), foodim)

        # Birleşik resmi bir PhotoImage nesnesine dönüştürün
        photo = ImageTk.PhotoImage(mutfak_image)

        # Arka plan resmini içeren Label widget'ını güncelleyin
        label.config(image=photo)
        label.image = photo

    # İlk yemek resmini yükleyin ve ayarlayın
    sayi = 0
    foodupdate()
    
    # Durum etiketlerini oluşturun ve yerleştirin
    durumlarr = tk.Label(odan[0], text=f'Durumlar: {durumlar}, Coin: {coin}, Gem: {gem}', bg='black', fg='white', font='Timer 10 bold')
    durumlarr.place(x=0, y=40)
    durumlarr1 = tk.Label(odan[0], text=f'Yumurtalar: {egg}', bg='black', fg='white', font='Timer 10 bold')
    durumlarr1.place(x=0, y=60)
    updatedurumlar()

    # Yemek resimlerini değiştirmek için butonları oluşturun
    def up():
        global sayi
        sayi = (sayi + 1) % len(food)
        foodupdate()
        tekrar()
    def down():
        global sayi
        sayi = (sayi - 1) % len(food)
        foodupdate()
        tekrar()

    sonra = tk.Button(odan[0], text='>', bg='black', fg='white', width=1, height=1, font=("Helvetica", 16), command=up)
    sonra.place(x=450, y=150)

    once = tk.Button(odan[0], text='<', bg='black', fg='white', width=1, height=1, font=("Helvetica", 16), command=down)
    once.place(x=210, y=150)
    
    ymk1 = tk.Label(odan[0], text=f'{myfood}', bg='black', fg='white', font='Timer 10 bold')
    ymk1.place(x=0,y=80)


    def yemekyee():
        yemekye()
        ymk1.config(text=f'{myfood}')


    def ye():
        global ymk
        if sayi == 0:
            ymk = tk.Button(odan[0], text=f'Elma yedir', bg='black', fg='white', font='Timer 10 bold',command=yemekyee)
            ymk.place(x=300, y=270)
        elif sayi == 1:
            ymk = tk.Button(odan[0], text=f'Havuç yedir', bg='black', fg='white', font='Timer 10 bold',command=yemekyee)
            ymk.place(x=300, y=270)
        elif sayi == 2:
            ymk = tk.Button(odan[0], text=f'Karpuz yedir', bg='black', fg='white', font='Timer 10 bold',command=yemekyee)
            ymk.place(x=300, y=270)
        elif sayi == 3:
            ymk = tk.Button(odan[0], text=f'Biftek yedir', bg='black', fg='white', font='Timer 10 bold',command=yemekyee)
            ymk.place(x=300, y=270)
    def tekrar():
        global ymk
        ymk.destroy()
        ye()
    ye()

    mutfak1.mainloop()

def disari1():
    global coin
    global gem
    global egg
    global eggs
    global catpay
    global yumurtalar
    global coinint
    global gemint
    global odan
    global durumlar
    global durumlarr
    global durumlarr1
    odan.clear()
    disari = tk.Tk()
    disari.geometry('650x600+400+50')
    disari.title('Dışarı')
    disari.resizable(False, False)
    odan.append(disari)

    # her odada aynı olmalı
    blacks = tk.Label(odan[0], text='**********************************************************************************************************************************',
                fg='black',bg='black',font='Titles 25 bold')
    blacks.pack()

    ytkoda = tk.Button(odan[0], text='Yatak Odası',bg='black',fg='white',command=yatakrt)
    ytkoda.place(x=290,y=10)

    salon = tk.Button(odan[0], text='Oturma Odası',bg='black',fg='white',command=oturmart)
    salon.place(x=170,y=10)

    tuvalet = tk.Button(odan[0], text='Tuvalet',bg='black',fg='white',command=tuvaletrt)
    tuvalet.place(x=400,y=10)     

    mutfak = tk.Button(odan[0], text='Mutfak',bg='black',fg='white',command=mutfakrt)
    mutfak.place(x=480,y=10)     

    disari = tk.Button(odan[0], text='Dışarı',bg='black',fg='white',command=disarirt)
    disari.place(x=100,y=10)
    
    ayarlar = tk.Button(odan[0], text='Ayarlar',bg='black',fg='white',command=ayarlarrt)
    ayarlar.place(x=550,y=10)
    
    preset = tk.Button(odan[0], text='Pet Sıfırla',bg='#0D3F3A',fg='white',command=kuluckayine)
    preset.place(x=10, y=10)
        
    # Yatak Odası arka plan resmini yükleyin
    disari_image = Image.open("rooms/Disari.jpg")
    disari_image = disari_image.resize((650, 600), Image.LANCZOS)

    # Civciv resmini yükleyin
    pet_image = Image.open(f"pets/{mypets[0]}.png")
    pet_image = pet_image.resize((200, 200), Image.LANCZOS)

    # Yatak Odası ve civciv resimlerini birleştirin
    disari_image.paste(pet_image, (240, 300), pet_image)

    # Yeni bir ImageTk.PhotoImage nesnesi oluşturun
    photo = ImageTk.PhotoImage(disari_image)

    # Arka plan resmini içeren bir Label widget'ı oluşturun ve yerleştirin
    label = tk.Label(odan[0], image=photo)
    label.image = photo
    label.pack()
    
    dukkan1 = tk.Button(odan[0], text='Dükkan',bg='#0D3F3A',fg='white',command=dukkanrt)
    dukkan1.place(x=170, y=360)
    
    oyunlar = tk.Button(odan[0], text='Oyunlar',bg='#D5A406',fg='white',command=oyunlarrt)
    oyunlar.place(x=500, y=340)
    
    durumlarr = tk.Label(odan[0], text=f'Durumlar: {durumlar}, Coin: {coin}, Gem: {gem}',bg='black',fg='white',font='Timer 10 bold')
    durumlarr.place(x=0,y=40)
    durumlarr1 = tk.Label(odan[0], text=f'Yumurtalar: {egg}',bg='black',fg='white',font='Timer 10 bold')
    durumlarr1.place(x=0,y=60)
    updatedurumlar()
    
    disari.mainloop()
    
def kuluckayine():
    global rdkedi
    global rdkopek
    global rdcivciv
    global countdown_label
    global pets
    global mypets
    global durumlarr
    global durumlar
    global durumlarr1
    if egg['Cat'] >= 1 or egg['Dog'] >= 1 or egg['Chick'] >= 1:
        emin = messagebox.askyesno(title='Emin misin',message='Mevcut petin sıfırlanacak')
        if emin == True:
            durumlar['Açlık'] = 100
            durumlar['Tuvalet'] = 100
            odan[0].destroy()
            mypets.clear()
            eggplace1 = tk.Tk()
            eggplace1.geometry('650x600+400+50')
            eggplace1.title('Yumurta Çıkart')
            eggplace1.resizable(False, False)
            eggplace1.config(bg='black')
            blacks = tk.Label(eggplace1, text='**********************************************************************************************************************************',
                            fg='black',bg='black',font='Titles 20 bold')
            blacks.pack()
        
            countdown_label = tk.Label(eggplace1,text='',fg='white',bg='black',font='Titles 20 bold')
            countdown_label.place(x=10,y=5)
        
            tip=tk.StringVar()
            rdkedi = tk.Radiobutton(eggplace1,text='Cat', bg='#5A89BF',value='CAAT', variable=tip)
            rdkedi.place(x=100, y=70)
            rdkopek = tk.Radiobutton(eggplace1,text='Dog', bg='#7A9AC0', value='DOOG', variable=tip)
            rdkopek.place(x=180, y=70)
            rdcivciv = tk.Radiobutton(eggplace1,text='Chick', bg='#7B94B2', value='CHiiCK', variable=tip)
            rdcivciv.place(x=260, y=70)
        
            yumurtalar = tk.Label(eggplace1,text=egg,fg='white',bg='#5A89BF',font='Timer 12 bold')
            yumurtalar.place(x=100,y=40)
        
            def onay():
                global rdkedi
                global rdkopek
                global rdcivciv
                global pet
                global countdown_label
                selected_value = tip.get()
                if selected_value == 'CAAT' and egg['Cat'] >= 1:    
                    rdkedi.destroy()
                    rdkopek.destroy()
                    rdcivciv.destroy()
                    secimbuton.destroy()
                    egg['Cat'] -= 1
                    ymrt = Image.open('draw/eggbg.png')
                    ymrt = ymrt.resize((300,300), Image.LANCZOS)
                    yphoto = ImageTk.PhotoImage(ymrt)
                    ymlabel = tk.Label(eggplace1, image=yphoto)
                    ymlabel.image = yphoto
                    ymlabel.place(x=120,y=173)
                    def update_countdown(time_left):
                        global countdown_label
                        global pet
                        if time_left > 0:
                            countdown_label.config(text=f"Yumurtadan çıkmaya kalan süre: {time_left} saniye")
                            eggplace1.after(1000, update_countdown, time_left - 1)
                        else:
                            countdown_label.destroy()
                            show_second_image()
                    def show_second_image():
                        global pet
                        ymrtc = Image.open('draw/eggbgc.png')
                        ymrtc = ymrtc.resize((300, 300), Image.LANCZOS)
                        ycphoto = ImageTk.PhotoImage(ymrtc)
                        ycmlabel = tk.Label(eggplace1, image=ycphoto)
                        ycmlabel.image = ycphoto
                        ycmlabel.place(x=120, y=173)
                        eggplace1.after(1000, select_cat)
                    def select_cat():
                        global pet
                        kedisecim = random.choice(catpets)
                        mypets.append(kedisecim)
                        save_data()
                        eggplace1.destroy()
                        yatakodasi()
                    update_countdown(10)                    
                elif selected_value == 'DOOG' and egg['Dog'] >= 1:
                    rdkedi.destroy()
                    rdkopek.destroy()
                    rdcivciv.destroy()
                    secimbuton.destroy()
                    egg['Dog'] -= 1
                    ymrt = Image.open('draw/eggbg.png')
                    ymrt = ymrt.resize((300,300), Image.LANCZOS)
                    yphoto = ImageTk.PhotoImage(ymrt)
                    ymlabel = tk.Label(eggplace1, image=yphoto)
                    ymlabel.image = yphoto
                    ymlabel.place(x=120,y=173)
                    def update_countdown(time_left):
                        global countdown_label
                        global pet
                        if time_left > 0:
                            countdown_label.config(text=f"Yumurtadan çıkmaya kalan süre: {time_left} saniye")
                            eggplace1.after(1000, update_countdown, time_left - 1)
                        else:
                            countdown_label.destroy()
                            show_second_image()
                    def show_second_image():
                        global pet
                        ymrtc = Image.open('draw/eggbgc.png')
                        ymrtc = ymrtc.resize((300, 300), Image.LANCZOS)
                        ycphoto = ImageTk.PhotoImage(ymrtc)
                        ycmlabel = tk.Label(eggplace1, image=ycphoto)
                        ycmlabel.image = ycphoto
                        ycmlabel.place(x=120, y=173)
                        eggplace1.after(1000, select_dog)
                    def select_dog():
                        global pet
                        kopeksecim = random.choice(dogpets)
                        mypets.append(kopeksecim)
                        save_data()
                        eggplace1.destroy()
                        yatakodasi()
                    update_countdown(20)            
                elif selected_value == 'CHiiCK' and egg['Chick'] >= 1:
                    rdkedi.destroy()
                    rdkopek.destroy()
                    rdcivciv.destroy()
                    secimbuton.destroy()
                    egg['Chick'] -= 1
                    ymrt = Image.open('draw/eggbg.png')
                    ymrt = ymrt.resize((300,300), Image.LANCZOS)
                    yphoto = ImageTk.PhotoImage(ymrt)
                    ymlabel = tk.Label(eggplace1, image=yphoto)
                    ymlabel.image = yphoto
                    ymlabel.place(x=120,y=173)
                    def update_countdown(time_left):
                        global countdown_label
                        global pet
                        if time_left > 0:
                            countdown_label.config(text=f"Yumurtadan çıkmaya kalan süre: {time_left} saniye")
                            eggplace1.after(1000, update_countdown, time_left - 1)
                        else:
                            countdown_label.destroy()
                            show_second_image()
                    def show_second_image():
                        global pet
                        ymrtc = Image.open('draw/eggbgc.png')
                        ymrtc = ymrtc.resize((300, 300), Image.LANCZOS)
                        ycphoto = ImageTk.PhotoImage(ymrtc)
                        ycmlabel = tk.Label(eggplace1, image=ycphoto)
                        ycmlabel.image = ycphoto
                        ycmlabel.place(x=120, y=173)
                        eggplace1.after(1000, select_chick)
                    def select_chick():
                        global pet
                        civcivsecim = random.choice(chickpets)
                        mypets.append(civcivsecim)
                        save_data()
                        eggplace1.destroy()
                        yatakodasi()
                    update_countdown(30)            
            secimbuton = tk.Button(eggplace1, text='Onayla', bg='#7F94AF',command=onay)
            secimbuton.place(x=350, y=70)
            eggplace1.mainloop()
        else:
            pass
    else:
        messagebox.showinfo(title='Yeterince yumurtan yok',message='Pet sıfırlamak için yumurtan yok')

def ayarlar():
    global odan
    global cinsave
    global tam_ekran
    odan.clear()
    ayarlar = tk.Tk()
    ayarlar.geometry('650x600+400+50')
    ayarlar.title('Ayarlar')
    ayarlar.resizable(False, False)
    ayarlar.config(bg='#1B1B1B')    
    odan.append(ayarlar)
    
    # her odada aynı olmalı
    blacks = tk.Label(odan[0], text='**********************************************************************************************************************************',
                fg='black',bg='black',font='Titles 25 bold')
    blacks.pack()

    ytkoda = tk.Button(odan[0], text='Yatak Odası',bg='black',fg='white',command=yatakrt)
    ytkoda.place(x=290,y=10)

    salon = tk.Button(odan[0], text='Oturma Odası',bg='black',fg='white',command=oturmart)
    salon.place(x=170,y=10)

    tuvalet = tk.Button(odan[0], text='Tuvalet',bg='black',fg='white',command=tuvaletrt)
    tuvalet.place(x=400,y=10)     

    mutfak = tk.Button(odan[0], text='Mutfak',bg='black',fg='white',command=mutfakrt)
    mutfak.place(x=480,y=10)     

    disari = tk.Button(odan[0], text='Dışarı',bg='black',fg='white',command=disarirt)
    disari.place(x=100,y=10)
    
    ayarlar = tk.Button(odan[0], text='Ayarlar',bg='black',fg='white',command=ayarlarrt)
    ayarlar.place(x=550,y=10)
    
    cinsiyetlabel = tk.Label(odan[0],text='Cinsiyet:',fg='white',bg='#1B1B1B',font='Titles 15 bold')
    cinsiyetlabel.place(x=10, y=50)
        
    cinsiyet=tk.StringVar(value='Erkek')

    erkek = tk.Radiobutton(odan[0],text='Erkek', bg='#5A89BF',value='Erkek', variable=cinsiyet)
    erkek.place(x=110, y=50)

    kadın = tk.Radiobutton(odan[0],text='Kadın', bg='#7A9AC0', value='Kadın', variable=cinsiyet)
    kadın.place(x=190, y=50)

    # x = tk.StringVar()
    
    muziklabel = tk.Label(odan[0],text='Müzik Seç:',fg='white',bg='#1B1B1B',font='Titles 15 bold')
    muziklabel.place(x=10, y=90)
    
    muzikler=['Relaxed Scene','My Eyes', '90210', 'Mortals', 'Feel Good']
    muziksec = ttk.Combobox(odan[0],values=muzikler,state="readonly") # ,height=3
    muziksec.set(muzik[0])
    muziksec.place(x=125, y=95)

    
    mevcut_ses_seviyesi = pygame.mixer.music.get_volume()
    varsayilan_ses_seviyesi = int(mevcut_ses_seviyesi * 100)    
    def sesi_ayarla(value):
        pygame.mixer.music.set_volume(float(value) / 100)
    muziklabel = tk.Label(odan[0],text='Ses:',fg='white',bg='#1B1B1B',font='Titles 15 bold')
    muziklabel.place(x=10, y=130)
    # Ses seviyesini ayarlayacak bir kaydırıcı (scale) oluştur
    ses_kaydirici = tk.Scale(odan[0], from_=0, to=100, fg='white',bg='#1B1B1B',orient=tk.HORIZONTAL, command=sesi_ayarla)
    ses_kaydirici.set(varsayilan_ses_seviyesi)
    ses_kaydirici.place(x=70, y=130)
    petad = tk.Label(odan[0],text='Pet adı:',fg='white',bg='#1B1B1B',font='Titles 15 bold')
    petad.place(x=10,y=190)
    petad = tk.Entry()
    petad.place(x=97,y=195)    
    def onayla():
        global muzik
        if not cinsave:
            cinsave.append(cinsiyet.get())
            save_data()
        else:
            cinsave.clear()
            cinsave.append(cinsiyet.get())
            save_data()
        if muziksec.get()=='My Eyes':
            muzik.clear()
            muzik.append('myeyes')
            play_music()
        elif muziksec.get()=='Relaxed Scene':
            muzik.clear()
            muzik.append('relaxedscene')
            play_music()
        elif muziksec.get()=='90210':
            muzik.clear()
            muzik.append('90210')
            play_music()
        elif muziksec.get()=='Mortals':
            muzik.clear()
            muzik.append('mortals')
            play_music()
        elif muziksec.get()=='Feel Good':
            muzik.clear()
            muzik.append('feelgood')
            play_music()
        if len(petad.get()) > 10:
            messagebox.showinfo(title='Başarısız',message='Petinin adı 10 karakterden fazla olamaz')
        else:
            petname.clear()
            petname.append(petad.get())
            save_data()
        save_data()
        
    secimbuton = tk.Button(odan[0], text='Değişiklikleri Onayla', bg='#7F94AF',command=onayla)
    secimbuton.place(x=10, y=300)

    ayarlar.mainloop


def girismain():
    global odan
    global cinsave
    global tam_ekran
    odan[0].destroy()
    odan.clear()
    giris = tk.Tk()
    giris.geometry('650x600+400+50')
    giris.title('Giriş')
    giris.resizable(False, False)
    giris.config(bg='black')    
    odan.append(giris)

    cinsiyetlabel = tk.Label(odan[0],text='Cinsiyet:',fg='white',bg='black',font='Titles 15 bold')
    cinsiyetlabel.place(x=10, y=10)
        
    cinsiyet=tk.StringVar(value='Erkek')

    erkek = tk.Radiobutton(odan[0],text='Erkek', bg='#5A89BF',value='Erkek', variable=cinsiyet)
    erkek.place(x=110, y=10)

    kadın = tk.Radiobutton(odan[0],text='Kadın', bg='#7A9AC0', value='Kadın', variable=cinsiyet)
    kadın.place(x=190, y=10)

    # x = tk.StringVar()
    
    muziklabel = tk.Label(odan[0],text='Müzik Seç:',fg='white',bg='black',font='Titles 15 bold')
    muziklabel.place(x=10, y=50)
    
    muzikler=['Relaxed Scene','My Eyes', '90210', 'Mortals', 'Feel Good']
    muziksec = ttk.Combobox(odan[0],values=muzikler,state="readonly") # ,height=3
    muziksec.set(muzik[0])
    muziksec.place(x=120, y=55)
    
    mevcut_ses_seviyesi = pygame.mixer.music.get_volume()
    varsayilan_ses_seviyesi = int(mevcut_ses_seviyesi * 100)    
    def sesi_ayarla(value):
        pygame.mixer.music.set_volume(float(value) / 100)
        
    muziklabel = tk.Label(odan[0],text='Ses:',fg='white',bg='black',font='Titles 15 bold')
    muziklabel.place(x=10, y=90)
    # Ses seviyesini ayarlayacak bir kaydırıcı (scale) oluştur
    ses_kaydirici = tk.Scale(odan[0], from_=0, to=100, fg='white',bg='black',orient=tk.HORIZONTAL, command=sesi_ayarla)
    ses_kaydirici.set(varsayilan_ses_seviyesi)
    ses_kaydirici.place(x=70, y=90)


    petad = tk.Label(odan[0],text='Pet adı:',fg='white',bg='black',font='Titles 15 bold')
    petad.place(x=10,y=150)
    petad = tk.Entry()
    petad.place(x=97,y=155)
 
    def onayla():
        global muzik
        if not cinsave:
            cinsave.append(cinsiyet.get())
            save_data()
        else:
            cinsave.clear()
            cinsave.append(cinsiyet.get())
            save_data()
        if muziksec.get()=='My Eyes':
            muzik.clear()
            muzik.append('myeyes')
            play_music()
        elif muziksec.get()=='Relaxed Scene':
            muzik.clear()
            muzik.append('relaxedscene')
            play_music()
        elif muziksec.get()=='90210':
            muzik.clear()
            muzik.append('90210')
            play_music()
        elif muziksec.get()=='Mortals':
            muzik.clear()
            muzik.append('mortals')
            play_music()
        elif muziksec.get()=='Feel Good':
            muzik.clear()
            muzik.append('feelgood')
            play_music()
        if len(petad.get()) > 10:
            messagebox.showinfo(title='Başarısız',message='Petinin adı 10 karakterden fazla olamaz')
        else:
            petname.clear()
            petname.append(petad.get())
            save_data()
            kulucka()
        
    secimbuton = tk.Button(odan[0], text='Onayla', bg='#7F94AF',command=onayla)
    secimbuton.place(x=10, y=200)
    
    giris.mainloop()

def main():
    global form
    odan.clear()
    form = tk.Tk()
    form.geometry('650x600+400+50')
    form.title('Giriş')
    form.resizable(False, False)
    odan.append(form)

    girisi = Image.open("giris.png")
    girisi = girisi.resize((650, 600), Image.LANCZOS)
    girisimage = ImageTk.PhotoImage(girisi)
    
    background_label = tk.Label(form, image=girisimage)
    background_label.pack()


    yazi = tk.Label(form,text=f'My Little {petname[0]}',fg='white',bg='#3E3D3E',font='BrushScriptMT 30 italic')
    yazi.place(x=220,y=50)
    
    yazi = tk.Label(form,text='Made By Longer Games',fg='purple',bg='#3E3D3E',font='BrushScriptMT 10 italic')
    yazi.place(x=220,y=97)
    
    if pet == 0:
        giris = tk.Button(form, text='Devam Et', fg='white',bg='#212121',width=20,height=2,font='IMPACT')
        giris.place(x=260, y=300)
    else:
        giris = tk.Button(form, text='Devam Et', fg='white',bg='#212121',width=20,height=2,font='IMPACT',command=yatakrt)
        giris.place(x=260, y=300)
        
    yeni = tk.Button(form, text='Yeni Oyun', fg='white',bg='#131414',width=20,height=2,font='IMPACT',command=yenioyun)
    yeni.place(x=260, y=360)
    
    ayar = tk.Button(form, text='Çıkış', fg='white',bg='#0B0C0C',width=20,height=2,font='IMPACT',command=cikis)
    ayar.place(x=260, y=420)
    save_data()
    form.mainloop()
def cikis():
    odan[0].destroy()

def yenioyun():
    global coin
    global gem
    global eggs
    global egg
    global yumurtalar
    global coinint
    global gemint
    global odan
    global pets
    global yatakoda
    global mypets
    global durumlar
    global cinsave
    global muzik
    global myfood
    global food
    global sayi
    if pet == 0:
        girismain()
    elif pet == 1:
        soru = messagebox.askyesno(title='Yeni Oyun',message='Kayıtlı oyun verilerin silinecek. Devam edecek misin?')
        if soru == True:
            cinsave.clear()
            girismain()
        else:
            pass
    save_data()

    
def kulucka():
    global rdkedi
    global rdkopek
    global rdcivciv
    global countdown_label
    global form
    odan[0].destroy()
    odan.clear()
    eggplace = tk.Tk()
    eggplace.geometry('650x600+400+50')
    eggplace.title('Yumurta Çıkart')
    eggplace.resizable(False, False)
    odan.append(eggplace)
    blacks = tk.Label(odan[0], text='**********************************************************************************************************************************',
                      fg='black',bg='black',font='Titles 20 bold')
    blacks.pack()
    countdown_label = tk.Label(odan[0],text='',fg='white',bg='black',font='Titles 20 bold')
    countdown_label.place(x=10,y=5)

    image = Image.open('rooms/klck.jpg')
    image = image.resize((650, 600), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(odan[0], image=photo)
    label.image = photo 
    label.pack()
    
    tip=tk.StringVar(value='CAAT')

    rdkedi = tk.Radiobutton(odan[0],text='Cat', bg='#5A89BF',value='CAAT', variable=tip)
    rdkedi.place(x=100, y=70)

    rdkopek = tk.Radiobutton(odan[0],text='Dog', bg='#7A9AC0', value='DOOG', variable=tip)
    rdkopek.place(x=180, y=70)

    rdcivciv = tk.Radiobutton(odan[0],text='Chick', bg='#7B94B2', value='CHiiCK', variable=tip)
    rdcivciv.place(x=260, y=70)

    yumurtalar = tk.Label(odan[0],text=egg,fg='white',bg='#5A89BF',font='Timer 12 bold')
    yumurtalar.place(x=100,y=40)
        
    x = label.winfo_screenwidth()
    y = label.winfo_screenheight()        
    def onay():
        global rdkedi
        global rdkopek
        global rdcivciv
        global pet
        global countdown_label
        selected_value = tip.get()
        if selected_value == 'CAAT' and egg['Cat'] >= 1:
            rdkedi.destroy()
            rdkopek.destroy()
            rdcivciv.destroy()
            secimbuton.destroy()
            egg['Cat'] -= 1
            ymrt = Image.open('draw/eggbg.png')
            ymrt = ymrt.resize((300,300), Image.LANCZOS) # 300 300
            yphoto = ImageTk.PhotoImage(ymrt)
            ymlabel = tk.Label(odan[0], image=yphoto)
            ymlabel.image = yphoto
            ymlabel.place(x=120,y=173) # 120 173

            def update_countdown(time_left):
                global countdown_label
                global pet
                if time_left > 0:
                    countdown_label.config(text=f"Yumurtadan çıkmaya kalan süre: {time_left} saniye")
                    odan[0].after(1000, update_countdown, time_left - 1)
                else:
                    countdown_label.destroy()
                    show_second_image()

            def show_second_image():
                global pet
                ymrtc = Image.open('draw/eggbgc.png')
                ymrtc = ymrtc.resize((300, 300), Image.LANCZOS)
                ycphoto = ImageTk.PhotoImage(ymrtc)
                ycmlabel = tk.Label(odan[0], image=ycphoto)
                ycmlabel.image = ycphoto
                ycmlabel.place(x=120, y=173)

                odan[0].after(1000, select_cat)

            def select_cat():
                global pet
                kedisecim = random.choice(catpets)
                mypets.append(kedisecim)
                pet += 1
                save_data()
                eggplace.destroy()
                yatakodasi()

            update_countdown(10)
        
            
        elif selected_value == 'DOOG' and egg['Dog'] >= 1:
            rdkedi.destroy()
            rdkopek.destroy()
            rdcivciv.destroy()
            secimbuton.destroy()
            egg['Dog'] -= 1
            ymrt = Image.open('draw/eggbg.png')
            ymrt = ymrt.resize((300,300), Image.LANCZOS)
            yphoto = ImageTk.PhotoImage(ymrt)
            ymlabel = tk.Label(odan[0], image=yphoto)
            ymlabel.image = yphoto
            ymlabel.place(x=120,y=173)

            def update_countdown(time_left):
                global countdown_label
                global pet
                if time_left > 0:
                    countdown_label.config(text=f"Yumurtadan çıkmaya kalan süre: {time_left} saniye")
                    odan[0].after(1000, update_countdown, time_left - 1)
                else:
                    countdown_label.destroy()
                    show_second_image()

            def show_second_image():
                global pet
                ymrtc = Image.open('draw/eggbgc.png')
                ymrtc = ymrtc.resize((300, 300), Image.LANCZOS)
                ycphoto = ImageTk.PhotoImage(ymrtc)
                ycmlabel = tk.Label(odan[0], image=ycphoto)
                ycmlabel.image = ycphoto
                ycmlabel.place(x=120, y=173)

                eggplace.after(1000, select_dog)

            def select_dog():
                global pet
                kopeksecim = random.choice(dogpets)
                mypets.append(kopeksecim)
                pet += 1
                save_data()
                eggplace.destroy()
                yatakodasi()

            update_countdown(20)
            
        elif selected_value == 'CHiiCK' and egg['Chick'] >= 1:
            rdkedi.destroy()
            rdkopek.destroy()
            rdcivciv.destroy()
            secimbuton.destroy()
            egg['Chick'] -= 1
            ymrt = Image.open('draw/eggbg.png')
            ymrt = ymrt.resize((300,300), Image.LANCZOS)
            yphoto = ImageTk.PhotoImage(ymrt)
            ymlabel = tk.Label(odan[0], image=yphoto)
            ymlabel.image = yphoto
            ymlabel.place(x=120,y=173)

            def update_countdown(time_left):
                global countdown_label
                global pet
                if time_left > 0:
                    countdown_label.config(text=f"Yumurtadan çıkmaya kalan süre: {time_left} saniye")
                    odan[0].after(1000, update_countdown, time_left - 1)
                else:
                    countdown_label.destroy()
                    show_second_image()

            def show_second_image():
                global pet
                ymrtc = Image.open('draw/eggbgc.png')
                ymrtc = ymrtc.resize((300, 300), Image.LANCZOS)
                ycphoto = ImageTk.PhotoImage(ymrtc)
                ycmlabel = tk.Label(odan[0], image=ycphoto)
                ycmlabel.image = ycphoto
                ycmlabel.place(x=120, y=173)

                odan[0].after(1000, select_chick)

            def select_chick():
                global pet
                civcivsecim = random.choice(chickpets)
                mypets.append(civcivsecim)
                pet += 1
                save_data()
                eggplace.destroy()
                yatakodasi()

            update_countdown(30)
            
    secimbuton = tk.Button(eggplace, text='Onayla', bg='#7F94AF',command=onay)
    secimbuton.place(x=350, y=70)
    eggplace.mainloop()

main()















