import socket
import time
import threading
import pystyle
from pystyle import Colors, Colorate

from queue import Queue

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = input(Colorate.Horizontal(Colors.red_to_blue, "Enter a IP to ping: "))
IP = socket.gethostbyname(target)
print(Colorate.Horizontal(Colors.red_to_blue, f"Starting scan on host {IP}"))

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((IP, port))
      with print_lock:
         print(port, 'is open!')
      con.close()
   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 500):
   q.put(worker)
   
q.join()
print(Colorate.Horizontal(Colors.red_to_blue, f"Finished in {time.time() - startTime}"))
