import serial
import json
import time
import requests

url = 'http://'
url += 'colheita-feliz.herokuapp.com/'
url += 'api/post/status/'

ser = serial.Serial('/dev/ttyUSB0')
ser.baudrate = 9600
while True:
    ser_str = ser.readline().decode('utf-8').rstrip().lstrip()
    print("###INICIANDO NOVA COMUNICAÇÃO###")
    tries = 0
    while tries < 3:
        try:
            dict_payload = json.loads(ser_str)
            break
        except:
            pass
        tries += 1
    if tries == 3:
        print("Error... Linha abortada")
    else:
        print("Sucesso")
        dict_payload['UTC_offset'] = 0
        dict_payload['timestamp'] = round(time.time(), 3)
        json_payload = json.dumps(dict_payload)
        print(json_payload)
        response = requests.post(url, json_payload)
        print(response)
