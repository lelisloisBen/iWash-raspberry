from flask import Flask, jsonify, request
from flask_cors import CORS
import time
#from sense_hat import SenseHat
import RPi.GPIO as gpio

#sense = SenseHat()
starttime=time.time()

app = Flask(__name__)
CORS(app)

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

@app.route("/iwash", methods=['POST'])
def iwash():
     
    body = request.get_json()
    cycleTime = body['time']
    #b = (255,255,255)
    
    
    if body['action'] == 'cold':
        print('cold')
        print(cycleTime)
        gpio.output(7, True)
        gpio.output(11, True)
        time.sleep(8)
        print('stoping')
        gpio.output(7, False)
        gpio.output(11, False)
        gpio.cleanup()
        print('cleaned')
        #r = (0,0,255)
        #sense.show_message(body['msg'], text_colour=r, back_colour=b)
        #sense.clear(0,0,0)
    elif body['action'] == 'hot':
        print('hot')
        #r = (255,0,0)
        #sense.show_message(body['msg'], text_colour=r, back_colour=b)
        #sense.clear(0,0,0)
    elif body['action'] == 'warm':
        print('warm')
        #r = (255,140,0)
        #sense.show_message(body['msg'], text_colour=r, back_colour=b)
        #sense.clear(0,0,0)
    elif body['action'] == 'delicate':
        print('delicate')
        #r = (255,105,180)
        #sense.show_message(body['msg'], text_colour=r, back_colour=b)
        #sense.clear(0,0,0)
    elif body['action'] == 'quick wash':
        print('quick wash')
        #r = (0,255,0)
        #sense.show_message(body['msg'], text_colour=r, back_colour=b)
        #sense.clear(0,0,0)
    else:
        #toggle = ''
        #for x in range(18):
            #time.sleep(.2 - ((time.time() - starttime) % .2))
           # if toggle == '':
                #toggle = 'yes'
                #r = (255,0,0)
                #sense.clear(r)
            #else:
               # toggle = ''
                #r = (0,0,255)
                #sense.clear(r)
                
        #sense.clear((0,0,0))
        return jsonify({'msg':'error'})    
    
    return jsonify({'msg':'success'})



    
    
    
    