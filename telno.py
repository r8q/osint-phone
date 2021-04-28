
import phonenumbers
import os,sys
import sys, os, pyfiglet
from colorama import Fore, Back

os.system('clear')

print(Fore.LIGHTCYAN_EX +'===================  🤖  🤖  ========================')
print(Fore.BLUE +'Author 🔥	:	https://t.me/glovelace')
print(Fore.LIGHTYELLOW_EX +'Author 💎	:	https://github.com/r8q')
print(Fore.LIGHTBLUE_EX +'Author 💘	:	https://t.me/losersalwaysloser')
print(Fore.LIGHTBLUE_EX +'Author 💞	:	https://t.me/decryptedd')
print(Fore.LIGHTCYAN_EX +'===================  🌀  🌀  ========================')
number = input(Fore.LIGHTCYAN_EX +"please enter number with signature (+): ")
cc = input(Fore.LIGHTYELLOW_EX +"please enter abbreviated country code ex: tr,us:" ) 
number1 = number

from phonenumbers import geocoder 
number= phonenumbers.parse(number1)
print(geocoder.description_for_number(number, cc))

from phonenumbers import carrier 
number=phonenumbers.parse(number1)
print(carrier.name_for_number(number,cc))

from phonenumbers import timezone 
number=phonenumbers.parse(number1)
print(timezone.time_zones_for_number(number))
