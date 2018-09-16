#!/bin/bash

echo 'start cleaner.sh'

TARGET_DAYS=30

find $HOME/PycharmProjects/btcMACDbotfromCryptowatch/log/ -name '*.log' -mtime +$TARGET_DAYS -delete
find $HOME/PycharmProjects/btcMACDbotfromCryptowatch/figure/ -name '*.jpg' -mtime +$TARGET_DAYS -delete

echo 'DONE'

exit