GET-IMAGE
====

# Overview
Get Image From Google Image Search

## Description
You can get any number of arbitrary images from Google Image Search.  
The main use is to automatically collect data sets used for machine learning.

任意の枚数の任意の画像を Google 画像検索から得ることができます.  
主な使用用途として機械学習のためのデータセットの自動収集を想定しています.

## Directory Structure
```
.
├── get_image.py
└── README.md
```

## Requirement
This code is written in `Python 3.6.6`.  
You need it and some modules like `os`, `sys`, `json`, `urllib`, `requests`, `bs4`.  
If these environments are in place, I think that this program will work on any operating system.

このコードは `Python 3.6.6` で書かれています.  
それに加えて `os`, `sys`, `json`, `urllib`, `requests`, `bs4` といったモジュールが必要です.  
これらの環境が揃っていれば, このプログラムは任意のオペレーティングシステム上で動作すると思われます.

## Usage
`python get_image.py [search target] [amount of images]`

All arguments are required.

すべての引数が必須です.

## Licence
If you deal with this source code, you can do it entirely freely.

このソースコードを扱うとき, あなたは完全に自由に使うことができます.

## Notice
I do not assume any responsibility for copyright issues concerning image collection.

画像収集に関する著作権問題についての一切の責任を負いません.

## Author
[skcvim](https://github.com/skcvim)
