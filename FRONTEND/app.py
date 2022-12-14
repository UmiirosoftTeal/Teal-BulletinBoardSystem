import requests
import sys
from fabric.colors import green, blue

url = "https://teal-bbs.glitch.me"


def timeLine():
    res = requests.get(url)
    json = res.json()

    i = 0

    while i != len(json):
        print("\n| " + green(json[i]["username"]), "id:", str(json[i]["id"]))
        print("| " + json[i]["tweet"])
        print("| " + blue(json[i]["postdate"]))
        i += 1

    print()


def postTweet(username, tweet):
    response = requests.post(url + '/post?username=' +
                             username + "&tweet=" + tweet)
    print("\n๐ณ ๆ็จฟใใพใใ!!\n")


def noArg():
    print("\n ๐ ๅฅๅใใใๅผๆฐใฏๅญๅจใใพใใ...")
    print("\n----- ใใซใใๅฟ่ฆใงใใ? -----\n")
    print(" ๐ ใฟใคใ ใฉใคใณใ่กจ็คบ ... tl")
    print(" ๐ ๆฐใใๆ็จฟใไฝๆ ... new <username> <tweet>\n")
    # print(" ๐ค ๆ็จฟใๅ้ค ... del\n")
    print("-------------------------------\n")


if len(sys.argv) == 1:
    print("\n ๐ ๅผๆฐใๆๅฎใใฆใใ ใใ...!\n")

elif len(sys.argv) == 2 or 4:
    arg = sys.argv[1]
    if arg == "tl" or arg == "new" or arg == "del":
        if arg == "tl":
            timeLine()

        if arg == "new":
            if len(sys.argv) == 4:
                username = sys.argv[2]
                tweet = sys.argv[3]
                postTweet(username, tweet)

            else:
                print()
                print(" ๆ็จฟใซๅฟ่ฆใชๅผๆฐใ่ฆใคใใใพใใใงใใ...")
                print(" -> new <username> <tweet>")
                print()

    else:
        noArg()

elif len(sys.argv) == 3:
    noArg()
