import django
import requests
import os


clear = lambda: os.system('cls')
clear()
print(django.get_version())