import re
from argparse import ArgumentParser
from av_data import av1, av2, av3

def av(tasklist):
    i = 0
    with open(tasklist, "r", encoding="utf-8") as e:
        exe = e.read()
        av_exe = re.findall("(.*?)\.exe", exe)
        for x in av_exe:
            x += ".exe"
            x = x.lower()

            if x in map(str.lower, av1.avList1.keys()):
                i += 1
                try:
                    print("\033[1;31m[+]\033[1;37m", x, "->", "\033[1;31m" + av1.avList1[x] + "\033[1;37m")
                except KeyError:
                    print("\033[1;33m[!]\033[1;37m 进程名字和av指纹名字大小写不一致:" + "\033[1;33m", x, "\033[1;37m")
            elif x in map(str.lower, av2.avList2.keys()):
                i += 1
                try:
                    print("\033[1;31m[+]\033[1;37m", x, "->", "\033[1;31m" + av2.avList2[x] + "\033[1;37m")
                except KeyError:
                    print("\033[1;33m[!]\033[1;37m 进程名字和av指纹名字大小写不一致:" + "\033[1;33m", x, "\033[1;37m")
            elif x in map(str.lower, av3.avList3.keys()):
                i += 1
                try:
                    print("\033[1;31m[+]\033[1;37m", x, "->", "\033[1;31m" + av3.avList3[x] + "\033[1;37m")
                except KeyError:
                    print("\033[1;33m[!]\033[1;37m 进程名字和av指纹名字大小写不一致:" + "\033[1;33m", x, "\033[1;37m")

        if i > 0:
            print("[+] 一共找到%d个AV进程" % i)
        else:
            print("[-] 未找到AV进程")


if __name__ == '__main__':
    arg = ArgumentParser(description="python3 avScan.py -r tasklist.txt")
    arg.add_argument('-r', help='指定进程文件', dest='tasklist', type=str)
    argv = arg.parse_args()
    try:
        if argv.tasklist:
            av(argv.tasklist)
        else:
            print("[!] -r 指定进程文件")
    except FileNotFoundError:
        print("[-] 文件不存在")
    except PermissionError:
        print("[-] 没有权限")
    except UnicodeDecodeError:
        print("[!] 文件编码要更改为utf-8")
