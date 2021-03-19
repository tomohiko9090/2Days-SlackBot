from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random

## スクレイピングできるとハイテク感

## 簡単データベース
db = [["これおすすめ！", "https://www.youtube.com/watch?v=5XdS0HmVfKM&feature=youtu.be"],
      ["これ見てみて！","https://www.youtube.com/watch?v=w2r-Q2FabY0&t=170s"],
      ["焚き火の火っていいよね・・・","https://www.youtube.com/watch?v=tvNdPc7ed90"],
      ["ストレッチしてみては？", "https://www.youtube.com/watch?v=NnDqD1iTPo0"],
      ["疲れたんなら、これ！","https://www.youtube.com/watch?v=-OWHJzb8rhw"]]

db_account = [
    ['<@U01NKRYK9HU|青野圭哲>','青野圭哲'],
    ['<@U01NPH6ETKP|髙橋滉太>','髙橋滉太'],
    ['<@U01NYQBF2UU|葛葉朋彦>','葛葉朋彦']
]

menter = [
    ['<@U01NKRYK9HU|メンター【仮】>','メンター【仮】']
]

ans = [["True", 2], ["True", 1], ["True", 1], ["True", 1], ["True", 2] ]



## ネガティブワード
@listen_to('つらい|疲れた|死にたい|たすけて')


def NegWord(message):
    i = random.randint(0,4)
    j = random.randint(0,1)
    messe = db[i][0]
    url = db[i][1]
    real_name = message.user['real_name']
    if j == 0:
        message.reply('{}\n{}'.format(messe, url))
    else:
        while(1):
            k = random.randint(0,2)
            if db_account[k][1]!=real_name:
                print(k)
                break
        message.send('{}、なぐさめたげて。'.format(db_account[k][0]))


##特定の返信に対して正解・不正解を返す

count_1 = count_2 = count_3 = count4= count5 = 0

@respond_to('^01_|^02_|^03_|^04_|^05_')
def Answer(message):
    global count_1, count_2, count_3, count4, count5
    real_name = message.user['real_name']
    comment = "正解・・・そして、あんたが一番だ！"
    mes = message.body['text']
        
    if ("01_"+str(ans[0][1]))==mes:
        if count_1 > 0:
            comment = "正解"
            message.reply(comment)
        else:
            message.reply(comment)
            #message.send('ではでは{}さんから{}さんへのご褒美タイム。'.format(menter[0][0], real_name))
        #menter(count_1)
        count_1 += 1
    elif ("02_"+str(ans[1][1]))==mes:
        if count_2 > 0:
            comment = "正解"
            message.reply(comment)
        else:
            message.reply(comment)
            #message.send('ではでは{}さんから{}さんへのご褒美タイム。'.format(menter[0][0], real_name))
        count_2 += 1
    elif ("03_"+str(ans[2][1]))==mes:
        if count_3 > 0:
            comment = "正解"
            message.reply(comment)
        #menter(count_3)
        else:
            message.reply(comment)
            #message.send('ではでは{}さんから{}さんへのご褒美タイム。'.format(menter[0][0], real_name))

        count_3 += 1
    elif ("04_"+str(ans[3][1]))==mes:
        if count_4 > 0:
            comment = "正解"
            message.reply(comment)
        #menter(count_3)
        else:
            message.reply(comment)
            #message.send('ではでは{}さんから{}さんへのご褒美タイム。'.format(menter[0][0], real_name))

        count_4 += 1
    elif ("05_"+str(ans[4][1]))==mes:
        if count_5 > 0:
            comment = "正解"
            message.reply(comment)
        #menter(count_3)
        else:
            message.reply(comment)
            #message.send('ではでは{}さんから{}さんへのご褒美タイム。'.format(menter[0][0], real_name))

        count_5 += 1
    else:
        message.reply("不正解")
    

def menter(count):
    if count==0:
        message.send('ではでは{}さんから{}さんへのご褒美タイム。'.format(menter[0][0], real_name))






'''
@respond_to('*')
def respond_func(message):
    #メッセージ文取得
    mes = message.body['text']
    if mes == 'よう！':
        @respond_to('おは')
        def respond_func2(message2):
            message2.send('ございます。')

    #message.reply(mes)
'''
@listen_to('python3')
def sample4(message):
    #message.send('python3って言われたよ')
    real_name = message.user['real_name'] # 表示名を取得する
    display_name = message.user['profile']['display_name']
    message.send('{}が発言しました。'.format(real_name))
    