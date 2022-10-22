# Parallel Memory

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2022/08/JPHACKS2022_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
<br>
2022年現在，コロナ禍の影響により対面して誰かと話す機会が非常に少なくなりました.
その中でも，現在の大学生は夢のキャンバスライフを妄想し入学したにも関わらず,友達と飲みに行ったり,旅行に行ったりと<b>楽しい思い出を作れないまま，もうすぐ卒業してしまうという危機を迎えています！！！！！！！</b>
<br>
<br>
そこで私たちはこの問題を解決するために，思い出作りの機会を作るのではなく<span style="color: red; ">思い出を<b>捏造</b>する</span>ことにしました．
<br>
<br>
<br>
また，大学生以外でも，<b>旅行に行きたくてもいけない</b>といった問題は共通であり，行きたい場所の画像と自身を合成することにより
<br>
<br>

### 製品説明（具体的な製品の説明）
### 特長
#### 1. さみしい写真に人を追加できます！
写真を撮ってみたけど，写っているのは自分だけ...

そんな悲しい写真をParallel Memoryにアップロードすれば，その写真を盛り上げてくれる人たちを自動で追加！
後は，好きなところに配置するだけでにぎやかな写真の出来上がり！

これでボッチだなんて言わせないよ！

#### 2. 好きな背景の中に自分を追加できます！
行きたい旅行先は無限大！
でも，お金も時間も友達もいない...

そんな時はParallel Memory！行きたい旅行先の画像と，自分の画像をアップロードすれば自分だけ切り取ってくれるので，後はそれっぽく配置するだけ！

後は友達に自慢しよう！(あれ，友達ってどこにいるんだろ...)

#### 3. 画像を投稿、ダウンロードできます！
作った画像を見せる友達がいなくてももう安心！
Parallel Memoryには投稿機能も実装！

みんなの投稿も見れちゃいます！
行きたい旅行先が同じ友達が見つかるかも！？

※他のSNSに投稿する際，必ずParallel Memoryで作成した合成画像であることを明記してください．

※その他，公序良俗に反する内容の作成及び投稿はやめましょう

### 解決出来ること

### 今後の展望

### 注力したこと（こだわり等）
*
*

## 開発技術
### 活用した技術
#### API・データ
* [https://www.photo-ac.com/](https://www.photo-ac.com/)から人物画像を利用
    * 背景を取り除いた画像の作成及び，タイムラインのサンプルデータとして使用

#### フレームワーク・ライブラリ・モジュール
* Backend ([実装したAPI一覧](https://github.com/jphacks/C_2204/blob/master/swagger/swagger.yaml))
    * Python
        * Flask
        * waitress
        * rembg
* Frontend
    * TypeScript
    * Next.js
    * React Konva
    * Tailwind CSS
    * Headless UI
* Infrastructure
    * Nginx
    * MySQL
    * Docker
    * AWS(EC2, ALB, S3, Route53, Certificate Manager)
        * AWS利用による可用性の向上

#### デバイス
* server
    * AWSにて実行
* client(動作確認済み)
    * Windows (Chrome, Edge)
    * Mac (Chrome, Safari)
    * Android (Chrome)
    * iOS, iPadOS (Chrome, Safari)

### 独自技術
#### ハッカソンで開発した独自機能・技術
* server
    * 画像を，背景の削除を行ったり，AWS S3で管理する一連のフロー
* client
    * 独自で開発したものの内容をこちらに記載してください
    * 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。
