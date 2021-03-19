# 答えが正解の時、
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

## ネガティブワード
@listen_to('つらい|疲れた|死にたい|たすけて') 

def NegWord(message):
    i = random.randint(0,4)
    j = 1   #random.randint(0,1)
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
    

