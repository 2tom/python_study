# -*- coding: utf-8 -*-

# まずpipでインストールしてね！！
from requests_oauthlib import OAuth1Session
import json

# ここは個人のアカウントのやつ設定しやがれーーー
CK = '' # Consumer Key
CS = '' # Consumer Secret
AT = '' # Access Token
AS = '' # Access Token Secret

# ツイート投稿用のURL
#url = "https://api.twitter.com/1.1/statuses/update.json"
# タイムライン取得用のURL
#url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

# ツイート本文
#params = {"status": "APIから実行！！！！！Pythonもくもく会"}
# ユーザ名を設定
params = {"screen_name": "kkb1016"}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
#req = twitter.post(url, params = params)
## ポストからゲットへ変更
req = twitter.get(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
    timeline = json.loads(req.text)

    for tweet in timeline:
        print(tweet["text"])
else:
    print ("Error: %d" % req.status_code)
