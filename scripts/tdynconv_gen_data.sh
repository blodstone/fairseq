#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "usage: $0 data.tar.gz"
    exit 1
fi

DATA=$1
echo "Creating data folder"
mkdir data
tar -xvf $1 -C data/

cd data
wget https://raw.githubusercontent.com/EdinburghNLP/XSum/master/XSum-Dataset/XSum-TRAINING-DEV-TEST-SPLIT-90-5-5.json
cd ..

echo "Splitting dataset"
python scripts/tdynconv_split.py data/bbc-tokenized-segmented-final

echo "Deleting extracted folder"
rm -rf data/bbc-tokenized-segmented-final
rm data/XSum-TRAINING-DEV-TEST-SPLIT-90-5-5.json






