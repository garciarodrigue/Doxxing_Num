import requests
import pyfiglet
import os
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")
baner= pyfiglet.figlet_format("Doxxing\nNum")
print(RED+baner)
print(BLUE+"\nby x T3nshi")
print("Legion Anonox")
print(YELLOW+"escribe el numero de telefono junto\ncon el codigo de pais, ejemplo: +50234563428\n")
# Información

api_key = 'b55cc727b39065ab10c752064013930a'
number = int(input(RED+"Numero: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=MYXD12sKk61p05hh17pnH4lHSq2ZrIxL%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))

