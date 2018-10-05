# btcMACDbotfrombitflyer


## What's this?
CryptowatchAPIからBTCの価格を取得しMACDとsignalの差、チャートをSlackへ投稿するBotです。


## Requirements
```bash
pip install pandas
pip install matplotlib
pip install requests
```
or
```bash
pip install -r requirements.txt
```


## Register for slack bot
Slack App からBotsを検索し設定する。  
<br>
![figure_1](https://github.com/hatunina/btcMACDbotfromCryptowatch/blob/master/image/image1.png)
<br>
その後、メッセージを投稿させるチャンネルへBotを参加させる。  


## Setting
### Config
`config`ディレクトリの`config_default.ini`を`config.ini`にリネームし  
下記のように設定項目を記述する。
```ini
[Path]
log_dir_relative_path: ../log/

[General]
# CryptowatchAPIのOHLC取得用パラメータ, 85400は日足
periods: 86400
# 描画する日数
target_days_range: 90
# Slack投稿メッサージ作成時のトレンド転換判定閾値
msg_threshold: 3000

[Slack]
token: your slack token
channel: your slack channel
```

### Cron
下記コマンドでcronの設定ファイルを開く。  
```bash
crontab -e
```
設定ファイルに以下を記述する。  
この際、Python実行環境やプロジェクトのパスは適宜変更する。  
下記例では毎日朝９時５分にスクリプトを実行する。  
また、`cleaner.sh`では30日前のログや生成された画像を削除している。  
```text
LANG="ja_JP.UTF-8"
5 9 * * * /bin/bash $HOME/PycharmProjects/btcMACDbotfromCryptowatch/shell/cleaner.sh
5 9 * * * $HOME/.pyenv/versions/anaconda3-4.2.0/bin/python $HOME/PycharmProjects/btcMACDbotfromCryptowatch/main.py
```
下記コマンドで設定内容を確認
```bash
crontab -l
```


## How to run
```bash
cd your_path/btcMACDbotfromCryptowatch
python ./main.py
```

or

```bash
cd your_path/btcMACDbotfromCryptowatch
chmod +x main.py
./main.py 
```


## Demo
<img src="https://github.com/hatunina/btcMACDbotfromCryptowatch/blob/master/image/image2.png" width="640px">


## Reference
https://cryptowatch.jp/docs/api  
http://www.algo-fx-blog.com/macd-python-technical-indicators/  
https://qiita.com/zaburo/items/00f364422ef3fe64f156  
https://qiita.com/stkdev/items/992921572eefc7de4ad8  
https://www.softel.co.jp/blogs/tech/archives/4503  
