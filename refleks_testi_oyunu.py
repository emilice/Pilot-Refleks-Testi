"""Süre bittikten sonra Oyun sonlandı uyarısı verir ve puan bildirilir,
4 saniye sonra oyun tekrar başlar
puan 5'er 5'er artar
Puan 0'ın altındaysa kırmızı, üstündeyse yeşil renk gösterilir,
Dışı yeşil içi kırmızı nesnenin üzerine tıklandığında -5, tamamen kırmızı nesnenin üzerine tıklandığında +5 puan kazanılır
Süre başladıktan 10 sn sonra en çok puanı yapan kazanır"""

import turtle, random, time

def arti_puan(x,y):
    global p
    p+=5
    yaz.clear()
    puan_rengi()

def eksi_puan(x,y):
    global p
    p-=5
    yaz.clear()
    puan_rengi()  

def temizle():
    yaz.clear()
    yaz.color('black')
    yaz.write('Puan:{}'.format(p), align='center', font=('Courier', 24, 'bold'))
    rota()

def puan_rengi():
    if p>=0:
        yaz.color('green')
    else:
        yaz.color('red')
    yaz.write('Puan:{}'.format(p), align='center', font=('Courier', 24, 'bold'))
    rota()
    
def rota():
    ok.goto(random.randint(-200,200), random.randint(-200,200))
    ok2.goto(random.randint(-200,200), random.randint(-200,200))

#ekranla alakalı
pencere=turtle.Screen()
pencere.title('Refleks oyunu')
pencere.bgcolor('lightblue')
pencere.setup(width=600, height=600)

#kırmızı nokta alakalı
ok=turtle.Turtle()
ok.speed(0)
ok.shape('circle')
ok.color('red')
ok.shapesize(3)
ok.penup()
ok.goto(random.randint(-200,200),random.randint(-200,200))

for i in range(10):
    ok2=turtle.Turtle()
    ok2.speed(0)
    ok2.shape('circle')
    if i==9:
        ok2.color('green','red')
    else:
        ok2.color('green')
    ok2.shapesize(3)
    ok2.penup()
    ok2.fd(15)
    ok2.goto(random.randint(-200,200),random.randint(-200,200))

p=0 #yazılmazsa hata verir

#İlk açıldığında program yazı..
yaz=turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('Black')
yaz.penup()
yaz.goto(0,260)
yaz.hideturtle()
yaz.write('Başla', align='center', font=('Courier', 24, 'bold'))

yaz2=turtle.Turtle()
yaz2.speed(0)
yaz2.shape('square')
yaz2.color('black')
yaz2.penup()
yaz2.goto(150,-260)
yaz2.hideturtle()

sure=10
while True:
    baslangicSure=time.time()
    while (time.time()-baslangicSure)<sure:
        ok.onclick(arti_puan)
        ok2.onclick(eksi_puan)
        #time.sleep(1)
        yaz2.clear()
        yaz2.write('Süre:{}'.format(time.time()-baslangicSure), align='right', font=('Courier', 15, 'normal'))
    else:
        ok.onclick(None)
        ok2.onclick(None)
        yaz2.clear()   
        yaz2.write('Oyun sonlandı. Puanınız:{}\nYeni oyun için bekleyin...'.format(p), align='right', font=('Courier', 15, 'normal'))
        time.sleep(4)
        yaz2.clear()  
        yaz2.write('Oyun başlıyor...', align='right', font=('Courier', 15, 'normal'))
        time.sleep(2)
        p=0
        temizle()
        
        
