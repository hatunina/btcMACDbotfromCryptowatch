# btcMACDbotfrombitflyer

## Requirements
```commandline
pip install slackweb
```

## How to run
```commandline
cd your_path/btcMACDbotfrombitflyer
python ./main.py
```

or

```commandline
cd your_path/btcMACDbotfrombitflyer
chmod +x main.py
./main.py 
```

## Setting cron

下記コマンドでcronの設定ファイルを開く  
```commandline
crontab -e
```
設定ファイルに以下を記述する  
この際、python実行環境やプロジェクトのパスは適宜変更する  
```text
5 9 * * * $HOME/.pyenv/shims/python $HOME/PycharmProjects/btcMACDbotfrombitflyer/src/main.py
```
下記コマンドで設定内容を確認
```commandline
crontab -l
```
