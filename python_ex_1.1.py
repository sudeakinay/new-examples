
defkullanıcı = 'ahmet'
defparola = 'Sudeyisevior'
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


def _computer_gradients(self, input_vector, target):
    #layer_1 = np.dot(input_vector, self.weights) + self.bias
    #activated = np.vectorize(self._LReLU)
    #layer_2 = self._LReLU(layer_1)
    #layer_2 = np.dot(layer_1_1, self.weights) + self.bias
    #prediction = layer_2

    layer_1 = np.dot(input_vector, self.weights) + self.bias
    #activated = np.vectorize(self._LReLU)
    layer_2 = self._LReLU(layer_1)
    layer_2 = np.dot(layer_1, self.weights) + self.bias
    layer_3 = self._LReLU(layer_2)
    prediction = layer_3

    derror_dprediction =  (prediction - target)    ### ilk turev E toplam
    #derivative= np.vectorize(self._LReLU_deriv)

    dprediction_dlayer1 = self._LReLU_deriv(layer_1)    ### ikinci kez turevi  
    dprediction_dlayer2 = self._LReLU_deriv(layer_2)    ### aktivasyon fonksiyonunun turevi 
    dprediction_dlayer3 = self._LReLU_deriv(layer_3)

    # dlayer1_dbias = 1
    # dlayer2_dbias = 1
    dlayer3_dbias = 1

    # dlayer1_dweights = (0 * self.weights) + (1 * input_vector)
    # dlayer2_dweights = (0 * self.weights) + (1 * layer_1)
    dlayer3_dweights = (0 * self.weights) + (1 * input_vector)
 
        # the derivative of the dot product is the derivative of the first vector multiplied 
        # by the second vector, plus the derivative of the second vector multiplied by the first vector
        # derror_dbias1 = (derror_dprediction  * dprediction_dlayer1 * dlayer1_dbias)
        # derror_dbias2 = (derror_dprediction  * dprediction_dlayer2  * dlayer2_dbias)
    derror_dbias = (derror_dprediction  * dprediction_dlayer3 * layer_3 * dprediction_dlayer2 * layer_2 * dprediction_dlayer1  * dlayer3_dbias)
        
        # derror_dweights1 = (derror_dprediction * dprediction_dlayer1 * dlayer1_dweights )
        # derror_dweights2 = (derror_dprediction * dprediction_dlayer2  * dlayer2_dweights )
    derror_dweights = (derror_dprediction * dprediction_dlayer3 * layer_3 * dprediction_dlayer2 * layer_2 * dprediction_dlayer1  * dlayer3_dweights )

        
        #derror_dbias = (derror_dprediction  * dprediction_dlayer1 * dlayer1_dbias)
        #derror_dweights = (derror_dprediction * dprediction_dlayer1 * dlayer1_dweights )
        
    return derror_dbias, derror_dweights


