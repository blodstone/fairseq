# Topic-based Dynamic Convolution 

This repository contains code for Topic-based Dynamic Convolution. Please contact me at hardy.oei@gmail.com for any question.

## Installation

This code extends the [fairseq](https://github.com/pytorch/fairseq) therefore the installation procedure will be the same with fairseq. Please follow the installation instruction in the fairseq site.

## Getting and pre-processing the dataset

**BBC dataset**

The BBC dataset is from [Extreme Summarization (XSum)](https://github.com/EdinburghNLP/XSum). **Please contact the author of the XSum for the dataset**.  The BBC dataset comes in the format of tar.gz containing the tokenized and segmented BBC documents.

Run the following script to split and preprocess the BBC dataset.

```bash
./scripts/tdynconv_gen_data.sh data.tar.gz

TEXT=data/bbc-split
fairseq-preprocess --source-lang document --target-lang summary --trainpref $TEXT/train --validpref $TEXT/validation --testpref $TEXT/test --destdir ./data --joined-dictionary --nwordstgt 50000 --nwordssrc 50000 --workers 8
```

# Training Dynamic Convolution
```bash
SAVE="save/dynamic_conv_bbc"
mkdir -p $SAVE
CUDA_VISIBLE_DEVICES=0 $(which fairseq-train) data  --log-interval 100 --no-progress-bar --max-update 30000 --share-all-embeddings --optimizer adam --adam-betas '(0.9, 0.98)' --clip-norm 0.0 --weight-decay 1e-3 --criterion label_smoothed_cross_entropy --label-smoothing 0.1 --min-lr 1e-09 --update-freq 16 --attention-dropout 0.1 --keep-last-epochs 10 --ddp-backend=no_c10d  --lr-scheduler cosine --warmup-init-lr 1e-7 --warmup-updates 10000 --lr-shrink 1 --max-lr 0.001 --lr 1e-7 --min-lr 1e-9 --t-mult 1 --lr-period-updates 20000 --arch lightconv --save-dir $SAVE --dropout 0.3 --attention-dropout 0.1 --weight-dropout 0.1  --encoder-glu 1 --decoder-glu 1 --max-tokens 3584
```





