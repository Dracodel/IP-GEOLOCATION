# importes
import argparse
import requests, json
import sys
from sys import argv
import os
# Arguments *_*

parser = argparse.ArgumentParser()

parser.add_argument("-t", help="Ip objetivo", type=str, dest='target', required=True)

args = parser.parse_args()
# clear
os.system('clear')
print("

██╗██████╗░░░░░░░░██████╗░███████╗░█████╗░
██║██╔══██╗░░░░░░██╔════╝░██╔════╝██╔══██╗
██║██████╔╝█████╗██║░░██╗░█████╗░░██║░░██║
██║██╔═══╝░╚════╝██║░░╚██╗██╔══╝░░██║░░██║
██║██║░░░░░░░░░░░╚██████╔╝███████╗╚█████╔╝
╚═╝╚═╝░░░░░░░░░░░░╚═════╝░╚══════╝░╚════╝░
        
   
"""+clear)
print("\x1b[1;35m"+"Created by Dracodel[\n"+clear)

ip = args.target
api = "http://ip-api.com/json/"
# ip geolocation start
try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = yellow+bold+"[~]"
        # Printing,Not Phising ; P
        print(a, "Target:", data['query'])
        print(a, "ISP:", data['isp'])
        print(a, "Organisation:", data['org'])
        print(a, "City:", data['city'])
        print(a, "Region:", data['region'])
        print(a, "Region name:", data['regionName'])
        print(a, "Latitude:", data['lat'])
        print(a, "Longitude:", data['lon'])
        print(a, "Timezone:", data['timezone'])
        print(a, "Zip code:", data['zip'])
        print(" "+clear)
# exit
except KeyboardInterrupt:
        print('Exiting,Good Bye'+clear)
        sys.exit(0)
