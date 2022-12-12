import requests
import sys
from fabric.colors import green, blue

url = "http://127.0.0.1"


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
    print("\n🐳 投稿しました!!\n")


def noArg():
    print("\n 📂 入力された引数は存在しません...")
    print("\n----- ヘルプが必要ですか? -----\n")
    print(" 🌏 タイムラインを表示 ... tl")
    print(" 📝 新しい投稿を作成 ... new <username> <tweet>\n")
    # print(" 💤 投稿を削除 ... del\n")
    print("-------------------------------\n")


if len(sys.argv) == 1:
    print("\n 📂 引数を指定してください...!\n")

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
                print(" 投稿に必要な引数が見つかりませんでした...")
                print(" -> new <username> <tweet>")
                print()

    else:
        noArg()

elif len(sys.argv) == 3:
    noArg()
