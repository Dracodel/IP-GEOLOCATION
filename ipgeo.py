# Importes
import argparse
import requests, json
import sys
from sys import argv
import os
# Argumentos

parser = argparse.ArgumentParser()

parser.add_argument("-t", help="Ip objetivo", type=str, dest='target', required=True)

args = parser.parse_args()

# Colores
blue = '\033[94m'
green = '\033[92m'
clear = '\033[0m'
boldblue = '\033[01m''\033[94m'
cyan = '\033[36m'
bold = '\033[01m'
red = '\033[31m'
# Clear 
os.system('clear')

print(bold+blue+"""
██╗██████╗░░░░░░░░██████╗░███████╗░█████╗░
██║██╔══██╗░░░░░░██╔════╝░██╔════╝██╔══██╗
██║██████╔╝█████╗██║░░██╗░█████╗░░██║░░██║
██║██╔═══╝░╚════╝██║░░╚██╗██╔══╝░░██║░░██║
██║██║░░░░░░░░░░░╚██████╔╝███████╗╚█████╔╝
╚═╝╚═╝░░░░░░░░░░░░╚═════╝░╚══════╝░╚════╝░
        
   
"""+clear)
print(red+bold+"Created by Dracodel\n"+clear)

ip = args.target
api = "http://ip-api.com/json/"
# Geolocation start
try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = green+bold+"[~]"
        # Printing,Not Phising ; P
        print(a, "Direccion IP:", data['query'])
        print(a, "ISP:", data['isp'])
        print(a, "Ciudad:", data['city'])
        print(a, "Organisation:", data['org'])
        print(a, "Region:", data['regionName'])
        print(a, "Latitude:", data['lat'])
        print(a, "Longitude:", data['lon'])
        print(a, "Timezone:", data['timezone'])
        print(a, "Codigo Postal:", data['zip'])
        print(" "+clear)
# Exit
except KeyboardInterrupt:
        print('Exiting,Good Bye'+clear)
        sys.exit(0)
