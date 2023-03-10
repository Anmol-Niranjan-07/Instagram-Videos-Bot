from instagrapi import Client
import urllib.request
import random
import string
import os
import colorama
colorama.init()
cl = Client()
cl.login(username="USERNAME", password='Password@12345')
i=0
x=10
channels = []
def main():
    with open("profiles.txt") as file_in:
        for line in file_in:
            channels.append(line)
    try:
        new_folder = "videos"
        os.mkdir(new_folder)
    except FileExistsError:
        pass
    for ch in channels:
        try:
            os.mkdir(f'./videos/{ch}')
        except FileExistsError:
            pass
        user_id = cl.user_id_from_username(ch)
        medias = cl.user_medias(user_id, 1000)
        j=1
        while(j<=100):
            try:
                res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10))
                url_link = medias[j].video_url
                print(f'{colorama.Fore.CYAN}{colorama.Style.BRIGHT}[+] Video Profile: {ch}')
                urllib.request.urlretrieve(url_link, f'./videos/{ch}/Video-{res}.mp4')
                print(f'{colorama.Fore.GREEN}{colorama.Style.BRIGHT}[+] Downloaded: Video-{res}.mp4')
                print('------------------------------')
                j+=1
            except IndexError as e:
                print(f'{colorama.Fore.YELLOW}--------------------Videos Ended for {ch}--------------------')
                break
            except Exception as e :
                print(f'{colorama.Fore.RED}[-] Skipping... {e}')
                j+=1
                pass
    print(f'{colorama.Fore.GREEN}{colorama.Style.BRIGHT}[+] Downloaded All Videos!')
main()
