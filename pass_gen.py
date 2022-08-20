import random
import string
import time
import os

def logo():
    print("""  ____                         ____                
 |  _ \    __ _   ___   ___   / ___|   ___   _ __  
 | |_) |  / _` | / __| / __| | |  _   / _ \ | '_ \ 
 |  __/  | (_| | \__ \ \__ \ | |_| | |  __/ | | | |
 |_|      \__,_| |___/ |___/  \____|  \___| |_| |_|
                                                   
                                        |Kuczi$|
    """)

lett = string.ascii_letters
nums = '0123456789'
spe = '-+*%&$!_'
logo()

user = input("Write special characters: ")

symbols = lett + nums + spe + user

len = int(input("Enter length of your passcode: "))

while (len < 0 or len > 70):
    len = int(input("Length of your password must be longer than 0 and shorter than 70: "))



password = ''.join(random.sample(symbols, len))
print("Your password is: " + password)
os.system('pause')
print("Thanks! Kuczi$")
time.sleep(2)
exit