from modules import multitool, Loveless_Utils
from colorama import Fore, Style
import os
import ctypes

while True:
    ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | by Loveless#2020")
    m = multitool.MultiTool()
    os.system('cls')
    module = Loveless_Utils.getch(
        "Which module would you like to open?"
        f"\n[{Fore.YELLOW}1{Style.RESET_ALL}] All in One        - {Fore.LIGHTBLACK_EX}[Edit, Capitalize, Randomize]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}2{Style.RESET_ALL}] Combine           - {Fore.LIGHTBLACK_EX}[Combine Multiple Files]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}3{Style.RESET_ALL}] Split             - {Fore.LIGHTBLACK_EX}[Split A File]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}4{Style.RESET_ALL}] Extract           - {Fore.LIGHTBLACK_EX}[Extract Lines]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}5{Style.RESET_ALL}] Randomize         - {Fore.LIGHTBLACK_EX}[Randomize Lines]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}6{Style.RESET_ALL}] Sort (A-Z)        - {Fore.LIGHTBLACK_EX}[Sort From A To Z]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}7{Style.RESET_ALL}] Remove Capture    - {Fore.LIGHTBLACK_EX}[Remove Capture From Combos]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}8{Style.RESET_ALL}] Remove Duplicates - {Fore.LIGHTBLACK_EX}[Remove Duplicates From File]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}9{Style.RESET_ALL}] Email to User     - {Fore.LIGHTBLACK_EX}[Convert Combos Email to Usernames]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}0{Style.RESET_ALL}] User to Email     - {Fore.LIGHTBLACK_EX}[Convert Combos Usernames to Email]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}F{Style.RESET_ALL}] Edit              - {Fore.LIGHTBLACK_EX}[Edit a Combo]{Style.RESET_ALL}"
        f"\n[{Fore.YELLOW}D{Style.RESET_ALL}] Combine via Name  - {Fore.LIGHTBLACK_EX}[Combine files with a certain name in a directory]{Style.RESET_ALL}"
    )
    if module.decode("utf-8").lower() == '1':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | All in One | by Loveless#2020")
        m.all_in_one()
    elif module.decode("utf-8").lower() == '2':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Combiner | by Loveless#2020")
        m.combine()
    elif module.decode("utf-8").lower() == '3':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Splitter | by Loveless#2020")
        m.split()
    elif module.decode("utf-8").lower() == '4':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Extractor | by Loveless#2020")
        m.extract()
    elif module.decode("utf-8").lower() == '5':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Randomizer | by Loveless#2020")
        m.randomize()
    elif module.decode("utf-8").lower() == '6':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Sorter (A-Z) | by Loveless#2020")
        m.sort_az()
    elif module.decode("utf-8").lower() == '7':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Capture Remover | by Loveless#2020")
        m.remove_capture()
    elif module.decode("utf-8").lower() == '8':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Duplicate Remover | by Loveless#2020")
        m.remove_dups()
    elif module.decode("utf-8").lower() == '9':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Email to Username | by Loveless#2020")
        m.email_user()
    elif module.decode("utf-8").lower() == '0':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Username to Email | by Loveless#2020")
        m.user_email()
    elif module.decode("utf-8").lower() == 'f':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Editor | by Loveless#2020")
        m.edit()
    elif module.decode("utf-8").lower() == 'd':
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool | Combiner via Name | by Loveless#2020")
        m.combine_files()