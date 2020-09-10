from tkinter import Tk, filedialog
from colorama import Fore, Style
import os

def load_file():
    print(f"[{Fore.GREEN}~{Style.RESET_ALL}] Pick your file in the opened window ...")
    root = Tk()
    root.withdraw()
    while True:
        try:
            root = Tk()
            root.withdraw()
            root.filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                                    filetypes=(("text files", "*.txt"), ("all files", "*.*")))
            with open(root.filename, "r+", encoding="utf-8", errors="ignore") as dup_file:
                lines = [line.rstrip() for line in dup_file]
            break
        except FileNotFoundError:
            print(f"[{Style.BRIGHT}{Fore.RED}!{Style.RESET_ALL}] IO ERROR - WE COULD NOT RETRIEVE FILE FROM THE "
                f"SELECTED PATH")
        except IOError:
            print(f"[{Style.BRIGHT}{Fore.RED}!{Style.RESET_ALL}] IO ERROR - WE COULD NOT RETRIEVE FILE FROM THE "
                f"SELECTED PATH")
        except Exception as e:
            print(e)
    return [lines, os.path.splitext(os.path.basename(root.filename))[0], os.path.splitext(os.path.basename(root.filename))[1], os.path.splitext(root.filename)[0]]

def load_files():
    file_list = []
    print(f"[{Fore.GREEN}~{Style.RESET_ALL}] Pick your files in the opened window ...")
    root = Tk()
    root.withdraw()
    while True:
        try:
            root = Tk()
            root.withdraw()
            root.filenames = filedialog.askopenfilenames(initialdir=os.getcwd(), title="Select files",
                                                    filetypes=(("text files", "*.txt"), ("all files", "*.*")))
            for filename in root.filenames:
                file_list.append({"path":filename, "extension": os.path.splitext(os.path.basename(filename))[1], "filetext": os.path.splitext(filename)[0]})
            break
        except FileNotFoundError:
            print(f"[{Style.BRIGHT}{Fore.RED}!{Style.RESET_ALL}] IO ERROR - WE COULD NOT RETRIEVE FILE FROM THE "
                f"SELECTED PATH")
        except IOError:
            print(f"[{Style.BRIGHT}{Fore.RED}!{Style.RESET_ALL}] IO ERROR - WE COULD NOT RETRIEVE FILE FROM THE "
                f"SELECTED PATH")
        except Exception as e:
            print(e)
    return file_list

def load_dir():
    foldername = ""
    print(f"[{Fore.GREEN}~{Style.RESET_ALL}] Pick your folder in the opened window ...")
    root = Tk()
    root.withdraw()
    while True:
        try:
            root = Tk()
            root.withdraw()
            foldername = filedialog.askdirectory(initialdir=os.getcwd(), title="Select folder")
            break
        except FileNotFoundError:
            print(f"[{Style.BRIGHT}{Fore.RED}!{Style.RESET_ALL}] IO ERROR - WE COULD NOT RETRIEVE FILE FROM THE "
                f"SELECTED PATH")
        except IOError:
            print(f"[{Style.BRIGHT}{Fore.RED}!{Style.RESET_ALL}] IO ERROR - WE COULD NOT RETRIEVE FILE FROM THE "
                f"SELECTED PATH")
        except Exception as e:
            print(e)
    return foldername

def cal(el):
    el = round(el, 2)
    if el < 60:
        sec = el
        return f"{sec}s"
    elif 60 < el < 3600:
        mins = int(el/60)
        sec = round(el-(mins*60), 2)
        return f"{mins}m, {sec}s"
    elif 3600 < el < 86400:
        hours = int(el/3600)
        mins = int((el-(hours*3600))/60)
        sec = round(el-(mins*60)-(hours*3600), 2)
        return f"{hours}h, {mins}m, {sec}s"
    else:
        days = int(el/86400)
        hours = int((el-(days*86400))/3600)
        mins = int((el-(hours*3600)-(days*86400))/60)
        sec = round(el-(mins*60)-(hours*3600)-(days*86400), 2)
        return f"{days}d, {hours}h, {mins}m, {sec}s"

def getch(message):
    print(f"[{Fore.BLUE}?{Style.RESET_ALL}] {message}\n[{Fore.GREEN}>{Style.RESET_ALL}] ")
    import sys
    if sys.platform[:3] == 'win':
        import msvcrt

        def getkey():
            key = msvcrt.getch()
            return key
    elif sys.platform[:3] == 'lin':
        import termios
        import sys
        import os

        def getkey():
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            new = termios.tcgetattr(fd)
            new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
            new[6][termios.VMIN] = 1
            new[6][termios.VTIME] = 0
            termios.tcsetattr(fd, termios.TCSANOW, new)
            try:
                c = os.read(fd, 1)
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, old)
            return c
    else:
        def getkey():
            print("Not your system, bud.")
    return getkey()
