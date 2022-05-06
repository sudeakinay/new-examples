
defkullanıcı = 'büyücü'
defparola = 'kuşlariseviyor'
while(True):
    kullanıcı = input('kullanıcı adı:')
    parola = input('parola: ')
    if((kullanıcı == defkullanıcı) and (parola == defparola)):
        print('hoşgeldiniz', kullanıcı)
        break
    elif ((kullanıcı != defkullanıcı) and (defparola == parola)):
        print('kullanıcı adını yanlış girdiniz')
    elif((kullanıcı == defkullanıcı) and (parola != defparola)):
        print('şifrenizi mi unuttunuz?')
        print('şifrenizi yenilemek ister misiniz?')
        cevap = input()
        if(cevap == 'E'):
            yeniparola = input('yeni parola: ')
            print('bekleyin....')
            defparola = yeniparola
            print('şifreniz güncellenmiştir...')
    else:
        print('tekrar deneyiniz....')
###########################

faktoriyel =1
while True:
    sayı = int(input('negatif olmayan bir sayı girin '))
    if(sayı <= 0 ):
        print('negatif olmayan bir sayi girin')
    else: 
        for i in range(1, sayı+1):

            faktoriyel *=i
        print('faktoriyel', faktoriyel)
        break
###########################

def geometri(sekil):
    if len(sekil) == 3:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]

        if (a+b) > c and (a+c) > b and (b+c) > a:
            if (a == b) and (a == c) and (b == c):
                print('bu bir eşkenar üçgendir....')
            elif (a == b) and (a == c):
                print('bu bir ikizkenar üçgendir....')
            else:
                  print('bu bir çeşitkenar üçgendir....')  
                
    elif len(sekil) == 4:
        x = sekil[0]
        y = sekil[1]
        z = sekil[2]
        k = sekil[3]

        if (x == y) and (y == z) and (z == k) and (k == x):
            print('bu bir karedir')
        elif (x == z) and (y == k):
            print('bu bir dikdörtgendir....')
        else:
            print('bu normal bir dörtgendir....')

    else:
        print('herhangi bir şekil değil....')


while True:
    eleman_sayisi = int(input('eleman sayısını giriniz: '))
    if (eleman_sayisi == 3):
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
        geometri([a, b, c])

    elif (eleman_sayisi == 4):
        x = int(input('x: '))
        y = int(input('y: '))
        z = int(input('z: '))           
        k = int(input('k: ')) 
        geometri([x, y, z, k])

    else:
        print('lütfen tekrar giriniz...')


