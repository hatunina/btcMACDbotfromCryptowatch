# btcMACDbotfrombitflyer
## What's this?
CryptowatchAPIからBTCの価格を取得しMACDとsignalの差、チャートをSlackへ投稿するBotです。

## Requirements
```commandline
pip install pandas
pip install matplotlib
pip install configparser
```

## Register for slack bot
Ato de kaku

## How to run
```commandline
cd your_path/btcMACDbotfromCryptowatch
python ./main.py
```

or

```commandline
cd your_path/btcMACDbotfromCryptowatch
chmod +x main.py
./main.py 
```

## Setting
### Config
`config`ディレクトリ直下に`config.ini`を作成する。
下記のように設定項目を記述する。
```ini
[Path]
log_file_relative_path: ../log/log.log

[General]
# CryptowatchAPIのOHLC取得用パラメータ, 85400は日足
periods: 86400
# 描画する日数
target_days_range: 90

[Slack]
token: your slack token
channel: your slack channel
```

### Cron
下記コマンドでcronの設定ファイルを開く。  
```commandline
crontab -e
```
設定ファイルに以下を記述する。  
この際、Python実行環境やプロジェクトのパスは適宜変更する。  
下記例では毎日朝９時５分にスクリプトを実行する。
```text
5 9 * * * $HOME/.pyenv/versions/anaconda3-4.2.0/bin/python $HOME/PycharmProjects/btcMACDbotfromCryptowatch/main.py
```
下記コマンドで設定内容を確認
```commandline
crontab -l
```

## Reference
https://cryptowatch.jp/docs/api  
http://www.algo-fx-blog.com/macd-python-technical-indicators/  
https://qiita.com/zaburo/items/00f364422ef3fe64f156  
https://qiita.com/stkdev/items/992921572eefc7de4ad8  