#Project01

import os
import time
from tqdm import *
from pyfiglet import Figlet
import requests
import random
import itertools
import sys
import pyqrcode
from barcode import EAN13
from queue import Queue
import socket
import threading
from barcode.writer import ImageWriter
import pyfiglet
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from  tabulate import tabulate

result = pyfiglet.figlet_format("STRANGE", font="slant")
print(result)

options = (" 1- MY IP ADDRESS \n 2- PASSWORD GENERATOR \n 3- WORDLIST GENERATOR \n 4- BARCODE GENERATOR \n 5- QRCODE GENERATOR \n 6- PHONE NUMBER INFO \n 7- SUBDOMAIN SCANNER \n 8- PORT SCANNER \n")

print(options)
select = int(input("Enter Your Choice "r""">>>>------------> """))

if select == 1:

          def loading():
               for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                    time.sleep(0.01)
               print("LOADING DONE !")

          def font(text):
                    cool_text = Figlet(font="slant")
                    return str(cool_text.renderText(text))
               
          def window_size(columns=80, height=20):
                    os.system("clear")

          if __name__ == "__main__":
           window_size(80,20)
           print(font("Find My IP"))
           loading()

           hostname = socket.gethostname()
           IPAddr = socket.gethostbyname(hostname)               
           print("Your device is : " + IPAddr)
           print("Your IP Address is : " + IPAddr)
           input("PRESS ENTER TO EXIT")
           exit()
          
if select == 2:

      def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                time.sleep(0.01)
            print("LETS MOVE")

      def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
          
      def window_size(columns=80, height=20):
                    os.system("clear")

      if __name__ == "__main__":
            window_size(80,20)
            print(font("PASSWORD GENERATOR"))
            loading()

            length = int(input("ENTER THE LENGTH OF THE PASSWORD"r""">>>>----------->"""))
            def get_random_string(length):
                  lower = "abcdefghijklmnopqrstuvwxyz"
                  upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                  numbers = "1234567890"
                  symbols = "@#&*(){}[]/?"
                  all = lower + symbols + numbers + upper
                  password = "".join(random.sample(all,length))
                  print("GENERATED PASSWORD OF LENGTH ", length, "is " r""">>>>-------->""",password) 
                 
            get_random_string(length)
            input("PRESS ENTER TO EXIT")
            exit()

if select == 3:
          
          def loading():
                for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                      time.sleep(0.01)
                print("LETS MOVE")

          def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))
          
          def window_size(columns=80, height=20):
                    os.system("clear")

          if __name__ == "__main__":
            window_size(80,20)
            print(font("WORDLIST GENERATOR"))
            loading()

            print("GENERATED PASSWORD IS SAVED IN THE PRESENT DIRECTORY")
            chrs = input("ENTER THE LETTERS FOR COMBINATION" r""">>>>---------->""")
            l = int(input("MINIMUM LENGTH OF PASSWORD " r""">>>>---------->"""))
            k = l
            j = int(input("MAXIMUM LENGTH OF PASSWORD " r""">>>>---------->"""))
            n = j+1
            mtl = len(chrs)
            p = []
            zt = input("[+] Enter the name of the File " r""">>>>---------->""")
            for ltp in range(k, n):
                 ans = mtl ** ltp
                 p.append(ans)
            tline = sum(p)
            input('ARE YOU READY ? [PRESS Enter]')
            time1 = time.asctime()
            start = time.time()
            psd = open(zt, 'a')
            for i in range(k,n):
                  r = i * 100 / n
                  l = str(r) + ' percent '
                  sys.stdout.write("\r%s" % l)
                  sys.stdout.flush()
                  psd.flush()
                  for xs in itertools.product(chrs, repeat=i):
                        psd.write(''.join(xs) + '\n')
                        psd.flush()
                  psd.close()
                  sys.stdout.write("\DONE SUCCESS ")
                  end = time.time()
                  print('\t [+] process Completed   :  ', time.asctime())
                  totaltime = end - start
                  rate = tline / totaltime
                  input("PRESS ENTER TO EXIT")
                  exit()
    
if select == 4:
          
          def loading():
                for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                      time.sleep(0.01)
                print("LETS MOVE")

          def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))
          
          def window_size(columns=80, height=20):
                    os.system("clear")

          if __name__ == "__main__":
            window_size(80,20)
            print(font("BARCODE GENERATOR"))
            loading()
            print("GENERATED BARCODE WILL BE SAVED AS PNG IN THE PRESENT DIRECTORY")

          def generator(number):
                  my_code = EAN13(number, writer=ImageWriter())
                  my_code.save("bar_code")

          if __name__ == "__main__":
                generator(input("ENTER 12 DIGIT NUMBER TO GENERATE BAR CODE"r""">>>>-------->"""))
                input("PRESS ENTER TO EXIT")
                exit()
          
if select == 5:
          
          def loading():
                for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=60):
                      time.sleep(0.01)
                print("LETS MOVE")

          def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))
          
          def window_size(columns=80, height=20):
                    os.system("clear")

          if __name__ == "__main__":
            window_size(80,20)
            print(font("QRCODE GENERATOR"))
            loading() 
            print("GENERATES QR CODE WILL BE SAVED AS myqr.png IN THE PRESENT DIRECTORY")
            s = input("ENTER THE LINK TO CREAT A QRCODE "r""">>>>---------->""")
            url = pyqrcode.create(s)
            url.svg("myqr.svg", scale=8)
            url.png('myqr.png', scale=6)
            input("PRESS ENTER TO EXIT")
            exit()

if select == 6:
          
          def loading():
                for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=60):
                      time.sleep(0.01)
                print("LETS MOVE")

          def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))
          
          def window_size(columns=80, height=20):
                    os.system("clear")

          if __name__ == "__main__":
            window_size(80,20)
            print(font("PHONE NUMBER SCANNER"))
            loading()     
            def num_scanner(phn_num):
                  number = phonenumbers.parse(phn_num)
                  description = geocoder.description_for_number(number, 'en')
                  supplier = carrier.name_for_number(number,'en')
                  info = [["country", "supplier"],[description, supplier]]
                  data = str(tabulate(info, headers="firstrow", tablefmt="github"))
                  return data

          if __name__ == "__main__":
                number = input("ENTER THE NUMBER " r""">>>>---------->""")
                print(num_scanner(number))
                input("PRESS ENTER TO EXIT ")
                exit()

if select == 7:
          
          def loading():
                for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                      time.sleep(0.01)
                print("LETS MOVE")

          def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))
          
          def window_size(columns=80, height=20):
                    os.system("clear")

          if __name__ == "__main__":
            window_size(80,20)
            print(font("SUBDOMAIN SCANNER"))
            loading()
            print("  IT TAKES TIME ACCORDING TO THE DOMAIN")
            print("  USING DEFAULT ADDED WORDLIST WITH 649649 WORDS")    
            domain = input("ENTER THE DOMAIN TO SCAN " r""">>>>-------->""")
            file = open("subdomains.txt")
            content = file.read()
            subdomains = content.splitlines()

            for subdomain in subdomains:
                  url = f"http://{subdomain}.{domain}"
                  try:
                        requests.get(url)
                  except requests.ConnectionError:
                    pass
            else:
                  print("[+]Discovered subdomain: ",url)
            input("PRESS ENTER TO EXIT")
            exit()

if select == 8:
          
          def loading():
                for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                      time.sleep(0.01)
                print("LETS MOVE")

          def font(text):
                cool_text = Figlet(font="slant")
                return str(cool_text.renderText(text))
          
          def window_size(columns=80, height=20):
                    os.system("clear")

          if __name__ == "__main__":
            window_size(80,20)
            print(font("PORT SCANNER"))
            loading()
            print("KEEP SOME PATIENCE, IT TAKES TIME ACCORDING TO THE OPEN PORTS AND PROVIDED IP")
            target = input("ENTER THE IP ADDRESS TO SCAN " r""">>>>---------->""")
            queue = Queue()
            open_ports = []

            def portscan(port):
                  try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.connect((target, port))
                        return True
                  except:
                        return False
                  
            def get_ports(mode):
                  if mode == 1:
                        for port in range(1,1024):
                              queue.put(port)
                  elif mode == 2:
                        for port in range(1, 49152):
                              queue.put(port)
                  elif mode == 3:
                        ports = [20, 21, 22, 23, 25, 53, 80,110, 443]
                        for port in ports:
                              queue.put(port)
                  elif mode == 4:
                        ports = input("Enter ypur ports(separate by blank): ")
                        ports = ports.split()
                        ports = list(map(int, ports))
                        for port in ports:
                              queue.put(port)
                  def worker():
                        while not queue.empty():
                              port = queue.get()
                              if portscan(port):
                                    print("Port {} is open!".format(port))
                                    open_ports.append(port)

                  def run_scanner(threads, mode):
                        get_ports(mode)
                        thread_list = []

                        for t in range(threads):
                              thread = threading.Thread(target=worker)
                              thread_list.append(thread)
                              
                        for thread in thread_list:
                              thread.start()
                              print("open ports are: ", open_ports)
                              run_scanner(100, 1)
                              input("PRESS ENTER TO EXIT")
                              exit()