# Topic-based Dynamic Convolution 

This repository contains code for Topic-based Dynamic Convolution. Please contact me at hardy.oei@gmail.com for any question.

## Installation

This code extends the [fairseq](https://github.com/pytorch/fairseq) therefore the installation procedure will be the same with fairseq. Please follow the installation instruction in the fairseq site.

## Getting and pre-processing the dataset

**BBC dataset**

The BBC dataset is from [Extreme Summarization (XSum)](https://github.com/EdinburghNLP/XSum). **Please contact the author of the XSum for the dataset**.  The BBC dataset comes in the format of tar.gz containing the tokenized and segmented BBC documents.

Run the following script to split and preprocess the BBC dataset.

```bash
./scripts/tdynconv_gen_data.sh
```






