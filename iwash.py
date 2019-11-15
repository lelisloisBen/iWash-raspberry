from sense_hat import SenseHat
import time
starttime=time.time()
sense = SenseHat()

r = 0
g = 0
b = 0


#sense.show_message("4Geeks Code!")
def hot():
    r = 255
    g = 0
    b = 0
    print('hot')
    sense.clear((r, g, b))
def cold():
    r = 0
    g = 0
    b = 255
    print('cold')
    sense.clear((r, g, b))
def warm():
    r = 255
    g = 140
    b = 0
    print('warm')
    sense.clear((r, g, b))
def quick():
    r = 0
    g = 255
    b = 0
    print('quick')
    sense.clear((r, g, b))
def delicate():
    r = 135
    g = 206
    b = 235
    print('delicate')
    sense.clear((r, g, b))
    
    
    
val = 'lll'

if val == 'hot':
    hot()
elif val == 'cold':
    cold()
elif val == 'warm':
    warm()
elif val == 'quick':
    quick()
elif val == 'delicate':
    delicate()
else:
    while True:
        print("victock")
        time.sleep(.2 - ((time.time() - starttime) % .2))
        if val == '':
            val = 'cold'
            hot()
        else:
            val = ''
            cold()