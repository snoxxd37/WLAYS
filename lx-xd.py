import sys

import time 

import socket

import random

import os

#colores

G = "\033[32m"

D = "\033[31m"

T = "\033[39m"

cy = "\033[38;2;23;147;209m"

A = "\033[34m"

m = "\033[35m"

ac = "\033[36m"

print(G)

print("██╗░░░░░██╗░░██╗░░░░░░██╗░░██╗██████╗░")

print("██║░░░░░╚██╗██╔╝░░░░░░╚██╗██╔╝██╔══██╗")

print("██║░░░░░░╚███╔╝░█████╗░╚███╔╝░██║░░██║")

print("██║░░░░░░██╔██╗░╚════╝░██╔██╗░██║░░██║")

print("███████╗██╔╝╚██╗░░░░░░██╔╝╚██╗██████╔╝")

print("╚══════╝╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝╚═════╝░")

print("1:Metasploit")

print("2:Tbomb")

print("3:Zphisher")

print("4:FBTOOL")

print("5:OVNI")

preg=int(input("QUE HERRAMIENTA QUIERES EJECUTAR: "))

#herramientas

if preg == 1:

    os.system( 'clear')

    time.sleep(1.5)

    print("INSTALANDO")

    time.sleep(1.5)

    os.system( 'clear' )

    os.system( 'wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh' )

     

elif preg == 2:

   os.system( 'clear' )

   time.sleep(1.5)

   print("INSTALANDO")

   time.sleep(1.5)

   os.system( 'clear' )    

   os.system( "git clone https://github.com/TheSpeedX/TBomb" )

   os.system("cd TBomb"

       "chmod +x TBomb.sh"

       "./TBomb.sh")

  

  

elif preg == 3:

    os.system( 'clear')

    time.sleep(1.5)

    print("INSTALANDO")

    time.sleep(1.5)

    os.system( 'clear' )

    os.system( "git  clone https://github.com/htr-tech/zphisher" )

    os.system("cd zphisher"

        "bash zphisher.sh")     

        

elif preg == 4:

    os.system( 'clear' )

    time.sleep(1.5)

    print("INSTALANDO")

    time.sleep(1.5)

    os.system( 'clear' )

    os.system( "git clone https://github.com/mkdirlove/FBTOOL")

    os.system( "cd FBTOOL"

        "python2 fbtool.py")     

        

elif preg == 5:

   os.system( 'clear' )

   time.sleep(1.5)

   print("INSTALANDO")

   time.sleep(1.5)

   os.system( 'clear' ) 

   os.system( "git clone https://github.com/Monkey-hk4/OVNI" )

   os.system("cd OVNI"

       "bash ovni.sh")  
