from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random, slackweb


# クイズ問題
db = [["話題１", "<!here> 好きな漫画を教えて！"],
      ["話題２", "<!here> 好きなタイプは？"],
      ["話題３", "<!here> おすすめのアニメ教えて！"],
      ["話題４", "<!here> 元気の出る曲教えて〜！"],
      ["話題５", "<!here> 好きなYouTuberは？"],
      ["話題６", "<!here> 嫌いな食べ物は？"],
      ["話題７", "<!here> おすすめの旅行先は？"],
      ["話題８", "<!here> おすすめの映画は？"],
      ["話題９", "<!here> 好きなお笑い芸人は？"],
      ["話題１０", "<!here> 休日の過ごし方は？"]]


def Random_func():
    i = random.randint(0,4)
    return i

x = Random_func()
topic_body = db[x][1]

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
slack.notify(text="{}".format(topic_body))