from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import RPi.GPIO as gpio

app = Flask(__name__)
CORS(app)

gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(37, gpio.OUT)

gpio.output(7, True)
gpio.output(11, True)


def start_light():
    gpio.output(37, True)
def stop_light():
    gpio.output(37, False)
    
def startMotor():
    try:

        gpio.output(15, True)
        start_light()
        time.sleep(20)
        gpio.output(15, False)
        stop_light()
            
            
    except:
        print('Error Victorita Margarita')
    finally:
        gpio.cleanup()

@app.route("/iwash", methods=['POST'])
def iwash():
     
    body = request.get_json()
    cycleTime = body['time']
    
    
    if body['action'] == 'cold':
        print('cold')
        startMotor()
           
    elif body['action'] == 'hot':
        print('hot')
        startMotor()
        
    elif body['action'] == 'warm':
        print('warm')
        startMotor()
       
    elif body['action'] == 'delicate':
        print('delicate')
        startMotor()
        
    elif body['action'] == 'quick wash':
        print('quick wash')
        startMotor()
        
    else:
        
        return jsonify({'msg':'error'})    
    
    return jsonify({'msg':'success'})

