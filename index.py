import os
import socket


print(""""
░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔════╝╚════██╗
███████║██████╔╝███████║██║░░╚═╝███████║█████╗░░░░███╔═╝
██╔══██║██╔═══╝░██╔══██║██║░░██╗██╔══██║██╔══╝░░██╔══╝░░
██║░░██║██║░░░░░██║░░██║╚█████╔╝██║░░██║███████╗███████╗
╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝

████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝

██╗███╗░░██╗████████╗███████╗██████╗░███████╗░█████╗░░█████╗░███████╗
██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝█████╗░░███████║██║░░╚═╝█████╗░░
██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██╔══╝░░██╔══██║██║░░██╗██╔══╝░░
██║██║░╚███║░░░██║░░░███████╗██║░░██║██║░░░░░██║░░██║╚█████╔╝███████╗
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝""""")


HOST = "localhost"  # Change this to your Apache server's hostname or IP address
PORT = 80

def portstatus():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
        print("Port " + str(PORT) + " is in use")  # Connected successfully
        sock.close()
    except ConnectionRefusedError:
        print("Port " + str(PORT) + " is not in use")  # Failed to connect because port is in use (or bad host)

def start():
    os.system('sudo systemctl start apache2')

def restartapache():
    os.system('sudo systemctl restart apache2 ')

def eaosb():
    os.system('sudo systemctl enable apache2 ')

def daosb():
    os.system('sudo systemctl disable apache2 ')

def apachestatus():
   os.system('gnome-terminal --working-directory="{}" -- sudo systemctl status apache2')


def eac():
    directory = "/etc/apache2"  # Change this to your desired directory
    os.system('gnome-terminal --working-directory="{}" -- sudo nano apache2.conf'.format(directory))

def tcfg():
    os.system('sudo apachectl -t')

def apacheV():
    os.system('sudo apache2 -v')



while True:
    command = input('Enter command: ').strip().lower()
    os.system('clear')

    if command == 'help':
        print('portstatus(sees if port 80 is in use)')
        print('start(starts the apache service)')
        print('restartapache(restarts the apache service)')
        print('eaosb (enables apache on startup)')
        print('daosb (disables apache on startup)')
        print('apachestatus(shows the status of the apache server)')
        print('exit(closes this program)')
        print('test config(test your apache configuration)')

    if command == 'exit':
        break
    
        break
        os.system('python3 index.py')
        

    if 'portstatus' in command:
        portstatus()

    if 'start' in command:
        start()


    if 'restartapache' in command:
        restartapache()

    if 'eaosb' in command:
        eaosb()

    if 'daosb' in command:
        daosb()

    if  'apachestatus' in command:
      apachestatus()
      
    if 'eac' in command:
        eac()
    
    if 'test config' in command:
        tcfg()

    if 'apachev'  in command:
        apacheV()

