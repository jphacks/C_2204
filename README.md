# サンプル（プロダクト名）

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2022/08/JPHACKS2022_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
### 製品説明（具体的な製品の説明）
### 特長
#### 1. 特長1
#### 2. 特長2
#### 3. 特長3

### 解決出来ること
### 今後の展望
### 注力したこと（こだわり等）
*
*

## 開発技術
### 活用した技術
#### API・データ
*
*

#### フレームワーク・ライブラリ・モジュール
*
*

#### デバイス
*
*

### 独自技術
#### ハッカソンで開発した独自機能・技術
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
*
*


---

## ローカルで実行
```sh
# 初回のみ
docker volume create jphacks-db-data
docker volume create jphacks-minio-data
# 毎回
docker compose up --build
```

[http://localhost:8080](http://localhost:8080)でクライアントサイドに
[http://localhost:8080/api](http://localhost:8080/api)でapiにアクセスできます


## minio
[http://localhost:9001](http://localhost:9001)でminioのコンソールに入れます
```
ID: minioadmin
Password: minioadmin
バケット名: jphacks
```
