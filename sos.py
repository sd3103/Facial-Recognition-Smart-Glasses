from gpiozero import LED, Buzzer, Button, OutputDevice
from time import time, sleep, strftime
from datetime import datetime
import telepot
import RPi.GPIO as GPIO 
import time

import os 
import io
GPIO.setmode(GPIO.BCM) 
btn = 4
GPIO.setup(btn, GPIO.IN)
receiverchatid=6476285615
def handle(msg):
  global telegramText
  global chat_id
  global receiveTelegramMessage
  
  chat_id = msg['chat']['id']
  telegramText = msg['text']
  
  print("Message received from " + str(chat_id))
  
  if telegramText == "/start":
    msg="your chat id "+ str(chat_id)
    bot.sendMessage(chat_id, msg)
  
  else:
    
    receiveTelegramMessage = True



bot = telepot.Bot('')
bot.message_loop(handle)

print("Telegram bot is ready")



receiveTelegramMessage = False
sendTelegramMessage = False

statusText = ""


try:
    while True:
        if GPIO.input(btn)==0:
            bot.sendMessage(receiverchatid, "you friend is in emergency sutiation and has pressed sos")
            print("sos")
            
        if receiveTelegramMessage == True:
            receiveTelegramMessage = False

            statusText = ""
            
           
        if sendTelegramMessage == True:
            sendTelegramMessage = False
            
            bot.sendMessage(chat_id, statusText)
            

except KeyboardInterrupt:
    sys.exit(0)