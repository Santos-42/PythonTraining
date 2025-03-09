choice = ''

def mainMenu():
    print('''PERHITUNGAN LUAS PERSEGI PANJANG
        1. Menghitung Luas Persegi Panjang
        2. Exit''')

def mencari_luas_persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

def menu1():
    panjang = int(input("Masukkan Panjang: "))
    lebar = int(input("Masukkan Lebar: "))
    print(f"Luas Persegi Panjang: {mencari_luas_persegi_panjang(panjang, lebar)}" )
    print('')

def menu2():
    while True: 
        print("THANK YOU")
        print("="*30)
        break


mainMenu()
choice = input(">> ")
match choice:
    case '1' : 
        menu1()
        mainMenu()
    case '2' : menu2()