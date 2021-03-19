from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random, slackweb


# クイズ問題
db = [["01", "バンコクの正式名称は？\n1. バンコック\n2. クルンテープ・マハーナコーン・アモーンラッタナコーシン・マヒンタラーユッタヤー・マハーディロック・ポップ・ノッパラット・ラーチャタニーブリーロム・ウドムラーチャニウェートマハーサターン・アモーンピマーン・アワターンサティット・サッカタッティヤウィサヌカムプラシット"],
      ["02", "パンはパンでも食べられないパンはなーんだ？\n1. フライパン\n2. きな粉パン"],
      ["03", "androidとiosの使用者の割合が多いのはどっち？\n1. android\n2. ios"],
      ["04", "お酢に卵を殻ごといれると卵はどうなるでしょう？\n1. 透明な卵になる\n2. 鏡のようになんでもうつる卵になる"],
      ["05", "リンカーンは大統領になる前は何をしていたでしょうか？\n1. プロ野球選手\n2. レスラー"]]


def Random_func():
    i = random.randint(0,4)
    return i

x = Random_func()
quiz_num = db[x][0]
quiz_body = db[x][1]

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text="{}：{}\n回答時にはsongoku_botにメンションをつけ、フォーマットは問題番号_回答[ex. 01_2]としてください。".format(quiz_num, quiz_body))