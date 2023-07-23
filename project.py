from sketchpy import library
from sketchpy import canvas
s ={1:'robert downey jr',2:'tom holland',3:'bts',4:'vijay',5:'gojo',6:'lion',7:'flag',8:'abdul kalam',9:'rajamouli',10:'bahubali',11:'devasena',12:'ballaladeva',13:'keeravani'}
for i in s:
    print('{} : {}'.format(i,s[i]))
while True:
    n=int(input('enter the key : '))
    if n in s:
        break
    else:
        print('enter valid input...')
if n==1:
    obj=library.rdj()
    obj.draw()
if n==2:
    obj=library.tom_holland()
    obj.draw()
if n==3:
    obj=library.bts()
    obj.draw()
if n==4:
    obj=library.vijay()
    obj.draw()
if n==5:
    obj=library.gojo()
    obj.draw()
if n==6:
    obj=canvas.sketch_from_image('.\photos\lion.jpeg')
    obj.draw(threshold=127)
if n==7:
    obj=library.flag()
    obj.draw()
if n==8:
    obj=library.apj()
    obj.draw()
if n==9:
    obj=canvas.sketch_from_image('.\photos\director.jpeg')
    obj.draw()
if n==10:
    obj1=canvas.sketch_from_image('photos\prabhas.jpeg')
    obj1.draw()
if n==11:
    obj=canvas.sketch_from_image('.\photos\devasena.jpeg')
    obj.draw()
if n==12:
    obj=canvas.sketch_from_image(".\photos\daggubati.jpeg")
    obj.draw(threshold=127)
if n==13:
    obj=canvas.sketch_from_image('.\photos\keeravani.jpeg')
    obj.draw()



