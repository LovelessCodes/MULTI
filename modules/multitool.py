from random import shuffle
from tkinter import Tk, filedialog
from colorama import Fore, Style
import os
import time
from modules import Loveless_Utils

class MultiTool:
    def combine(self):
        os.system('cls')
        file_list = Loveless_Utils.load_files()
        start = time.time()
        file_length = len(file_list)
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Combining {file_length} files")
        with open(f"{file_list[0]['path']} ({file_length} Combined){file_list[0]['extension']}", "a+", encoding="utf-8", errors='ignore') as f:
            for fil in file_list:
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Including {fil['filetext']}")
                f.write(''.join(open(fil['path'], "r+", errors='ignore', encoding="utf-8").readlines()))
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Combined {file_length} files and saved the file as {Fore.BLUE}\"{file_list[0]['path']} ({file_length} Combined){file_list[0]['extension']}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu\n")
    
    def combine_files(self):
        os.system('cls')
        l = input(f"[{Fore.BLUE}?{Style.RESET_ALL}] What should I be looking to combine? (without extension only .txt){Style.RESET_ALL}\n[{Fore.GREEN}>{Style.RESET_ALL}] ")
        direc = Loveless_Utils.load_dir()
        file_list = []
        for root, dirs, files in os.walk(direc):
            for file in files:
                if(file.endswith(".txt") and l.lower() in file.lower()):
                    file_list.append({"path": os.path.join(root,file), "extension": ".txt"})
        start = time.time()
        file_length = len(file_list)
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Combining {file_length} files")
        with open(f"{direc}/{l} ({file_length} Combined){file_list[0]['extension']}", "a+", encoding="utf-8", errors='ignore') as f:
            for fil in file_list:
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Including {fil['path']}")
                f.write(''.join(open(fil['path'], "r+", errors='ignore', encoding="utf-8").readlines()))
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Combined {file_length} files and saved the file as {Fore.BLUE}\"{direc}/{l} ({file_length} Combined){file_list[0]['extension']}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu\n")
    
    def email_user(self):
        os.system('cls')
        eu_list, path, extension, filetext = Loveless_Utils.load_file()
        start = time.time()
        length = len(eu_list)
        p_list = []
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Converting {length} emails to usernames.")
        for ep in eu_list:
            if ":" in ep:
                ep = ep.split(":")
                if "@" in ep[0]:
                    ep[0] = ep[0].split("@")[0]
                ep = ":".join(ep)
            elif ";" in ep:
                ep = ep.split(";")
                if "@" in ep[0]:
                    ep[0] = ep[0].split("@")[0]
                ep = ":".join(ep)
            p_list.append(ep)
        with open(f"{filetext} (Email to User){extension}", "w+", encoding="utf-8") as f:
            f.write(f'\n'.join(p_list) + "\n")
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Converted Emails to Usernames and saved the file as {Fore.BLUE}\"{path} (Email to User){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu")
    
    def extract(self):
        os.system('cls')
        ex_list, path, extension, filetext = Loveless_Utils.load_file()
        extract = input(f"[{Fore.BLUE}?{Style.RESET_ALL}] What should we be looking for in the file?\n[{Fore.GREEN}>{Style.RESET_ALL}] ")
        start = time.time()
        length = len(ex_list)
        p_list = []
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Extracting {length} \"{extract}\" lines from the chosen file")
        for line in ex_list:
            if extract in line:
                p_list.append(line)
        with open(f"{filetext} (Extracted){extension}", "w+", encoding="utf-8") as f:
            f.write(f'\n'.join(p_list) + "\n")
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Extracted \"{extract}\" lines and saved the file as {Fore.BLUE}\"{path} (Extracted){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu\n")
    
    def randomize(self):
        os.system('cls')
        rand_list, path, extension, filetext = Loveless_Utils.load_file()
        start = time.time()
        length = len(rand_list)
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Randomizing {length} lines.")
        shuffle(rand_list)
        with open(f"{filetext} (Randomized){extension}", "w+", encoding="utf-8") as f:
            f.write('\n'.join(rand_list))
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Randomized file and saved the file as {Fore.BLUE}\"{path} (Randomized){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu\n")
    
    def remove_capture(self):
        os.system('cls')
        cap_list, path, extension, filetext = Loveless_Utils.load_file()
        start = time.time()
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Removing capture from file.")
        with open(f"{filetext} (No Cap){extension}", "w+", encoding="utf-8") as f:
            for line in cap_list:
                if " " in line:
                    line_split = line.split(" ")[0]
                    if "]" in line_split:
                        line = line.split("]")[1]
                    line = line.split(" ")[0]
                elif "|" in line:
                    line_split = line.split("|")[0]
                    if "]" in line_split:
                        line = line.split("]")[1]
                    line = line.split("|")[0]
                f.write(f"{line}\n")
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Removed Capture and saved the file as {Fore.BLUE}\"{path} (No Cap){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Fore.BLUE}'ENTER'{Style.RESET_ALL} to return to main menu\n")

    def count_duplicates(self, l, s):
        ''' Counts how many duplicates are in a list '''
        l_len = len(l)
        s_len = len(s)
        if l_len == s_len:
            return 0
        else:
            return l_len - s_len

    def remove_dups(self):
        os.system('cls')
        dup_list, path, extension, filetext = Loveless_Utils.load_file()
        start = time.time()
        set_dup_list = set(dup_list)
        c = self.count_duplicates(dup_list, set_dup_list)
        if c != 0:
            print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Removing {c} duplicates from file.")
            with open(f"{filetext} (No Dups){extension}", "w+", encoding="utf-8") as f:
                f.write("\n".join(list(set_dup_list)))
            elapsed = time.time() - start
            time_elapsed = Loveless_Utils.cal(elapsed)
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Removed {c} duplicates from file and saved the file as {Fore.BLUE}\"{path} (No Dups){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        else:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] No duplicates to remove, exiting")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Fore.BLUE}'ENTER'{Style.RESET_ALL} to return to main menu\n")
    
    def sort_az(self):
        os.system('cls')
        sort_list, path, extension, filetext = Loveless_Utils.load_file()
        start = time.time()
        sort_list.sort()
        with open(f"{filetext} (Sorted A-Z){extension}", "w+", encoding="utf-8") as f:
            f.write("\n".join(sort_list))
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Sorted A-Z and saved the file as {Fore.BLUE}\"{path} (Sorted A-Z){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Fore.BLUE}'ENTER'{Style.RESET_ALL} to return to main menu")
    
    def split(self):
        os.system('cls')
        split_list, path, extension, filetext = Loveless_Utils.load_file()
        l = input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Should the list use lines or parts? {Style.DIM}[l or p]{Style.RESET_ALL}\n[{Fore.GREEN}>{Style.RESET_ALL}] ")
        if l in ["l", "lines", "line", "li", "lin"]:
            l = "lines"
            p = int(input(f"[{Fore.BLUE}?{Style.RESET_ALL}] How many lines should be in each part?\n[{Fore.GREEN}>{Style.RESET_ALL}] "))
        elif l in ["p", "parts", "part", "pa", "par"]:
            l = "parts"
            p = int(input(f"[{Fore.BLUE}?{Style.RESET_ALL}] How many parts should the file be split into?\n[{Fore.GREEN}>{Style.RESET_ALL}] "))
        start = time.time()
        length = len(split_list)
        if l == "parts":
            split_list = [ split_list[i*length // p: (i+1)*length // p] for i in range(p) ]
        elif l == "lines":
            split_list = [split_list[x:x+p] for x in range(0, length, p)]
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Splitting file.")
        os.mkdir(f"{filetext} Splits/")
        i = 0
        for li in split_list:
            i += 1
            with open(f"{filetext} Splits/Split {i}{extension}", "w+", encoding="utf-8") as f:
                f.write('\n'.join(li))
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Split list into {i} files and saved the files in {Fore.BLUE}\"{filetext} Splits/\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu\n")

    def user_email(self):
        os.system('cls')
        ue_list, path, extension, filetext = Loveless_Utils.load_file()
        domain = input(f"[{Fore.BLUE}?{Style.RESET_ALL}] What domain should be used to convert usernames to emails?\n[{Fore.GREEN}>{Style.RESET_ALL}] ")
        start = time.time()
        length = len(ue_list)
        p_list = []
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Converting usernames to emails.")
        for up in ue_list:
            if ":" in up:
                up = up.split(":")
                if "@" not in up[0]:
                    up[0] = up[0] + "@" + domain
                up = ":".join(up)
            elif ";" in up:
                up = up.split(";")
                if "@" not in up[0]:
                    up[0] = up[0] + "@" + domain
                up = ":".join(up)
            p_list.append(up)
        with open(f"{filetext} (User to Email){extension}", "w+", encoding="utf-8") as f:
            f.write(f'\n'.join(p_list) + "\n")
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Converted {length} Usernames to Emails and saved the file as {Fore.BLUE}\"{path} (User to Email){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu\n")
    
    def edit(self):
        os.system('cls')
        edit_list, path, extension, filetext = Loveless_Utils.load_file()
        s = input(f"[{Fore.BLUE}?{Style.RESET_ALL}] What do you want to be edited onto the lines? (separated by comma)\n[{Fore.GREEN}>{Style.RESET_ALL}] ").split(",")
        start = time.time()
        length = len(edit_list)
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Editing {length} lines.")
        with open(f"{filetext} (Edited){extension}", "a+", encoding="utf-8") as f:
            f.write(f'\n'.join(edit_list) + "\n")
            for st in s:
                if st.rstrip().replace(" ", "") != "":
                    f.write(f'{st.rstrip().replace(" ", "")}\n'.join(edit_list) + f'{st.rstrip().replace(" ", "")}\n')
                else:
                    pass
            p_list = []
            for edit in edit_list:
                if ":" in edit:
                    edit = edit.split(":")
                    edit[1] = edit[1].capitalize()
                    edit = ":".join(edit)
                elif ";" in edit:
                    edit = edit.split(";")
                    edit[1] = edit[1].capitalize()
                    edit = ":".join(edit)
                p_list.append(edit)
            f.write(f'\n'.join(p_list) + "\n")
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        total_edited = length+(length*len(s))
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Edited a total of {total_edited} lines and saved the file as {Fore.BLUE}\"{path} (Edited){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu\n")
    
    def all_in_one(self):
        os.system('cls')
        all_in_list, path, extension, filetext = Loveless_Utils.load_file()
        s = input(f"[{Fore.BLUE}?{Style.RESET_ALL}] What do you want to be edited onto the lines? (separated by comma)\n[{Fore.GREEN}>{Style.RESET_ALL}] ").split(",")
        start = time.time()
        length = len(all_in_list)
        set_all_in_list = set(all_in_list)
        c = self.count_duplicates(all_in_list, set_all_in_list)
        if c != 0:
            print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Removing {c} duplicates from list.")
            elapsed = time.time() - start
            time_elapsed = Loveless_Utils.cal(elapsed)
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Removed {c} duplicates from list in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}, continuing")
        else:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] No duplicates to remove, continuing")
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Editing {length} lines.")
        with open(f"{filetext} (All-in-One) - Temp{extension}", "a+", encoding="utf-8") as f:
            f.write(f'\n'.join(all_in_list) + "\n")
            for st in s:
                if st.rstrip().replace(" ", "") != "":
                    f.write(f'{st.rstrip().replace(" ", "")}\n'.join(all_in_list) + f'{st.rstrip().replace(" ", "")}\n')
                else:
                    pass
            p_list = []
            for edit in all_in_list:
                if ":" in edit:
                    edit = edit.split(":")
                    edit[1] = edit[1].capitalize()
                    edit = ":".join(edit)
                elif ";" in edit:
                    edit = edit.split(";")
                    edit[1] = edit[1].capitalize()
                    edit = ":".join(edit)
                p_list.append(edit)
            f.write(f'\n'.join(p_list) + "\n")
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Edited list in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}, continuing")
        print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Randomizing list.")
        all_in_list = open(f"{filetext} (All-in-One) - Temp{extension}", "r+").readlines()
        shuffle(all_in_list)
        open(f"{filetext} (All-in-One){extension}", "w+", encoding="utf-8").write(''.join(all_in_list))
        elapsed = time.time() - start
        time_elapsed = Loveless_Utils.cal(elapsed)
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Randomized list in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        total_edited = length+(length*len(s))
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] All-in-One'd a total of {total_edited} lines and saved the file as {Fore.BLUE}\"{path} (All-in-One){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Style.DIM}'ENTER'{Style.RESET_ALL} to return to main menu")
    
    def parser(self):
        os.system('cls')
        dup_list, path, extension, filetext = Loveless_Utils.load_file()
        start = time.time()
        set_dup_list = set(dup_list)
        c = self.count_duplicates(dup_list, set_dup_list)
        if c != 0:
            print(f"[{Fore.YELLOW}~{Style.RESET_ALL}] Removing {c} duplicates from file.")
            elapsed = time.time() - start
            time_elapsed = Loveless_Utils.cal(elapsed)
            print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Removed {c} duplicates from file and saved the file as {Fore.BLUE}\"{path} (No Dups){extension}\"{Style.RESET_ALL} in {Fore.MAGENTA}{time_elapsed}{Style.RESET_ALL}")
        else:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] No duplicates to remove, continuing")
        p_list = []
        for line in set_dup_list:
            if len(line) > 6 and len(line.split(":")[1]) > 3:
                p_list.append(line)

        input(f"[{Fore.BLUE}?{Style.RESET_ALL}] Press {Fore.BLUE}'ENTER'{Style.RESET_ALL} to return to main menu\n")