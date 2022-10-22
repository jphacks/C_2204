# Parallel Memory

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2022/08/JPHACKS2022_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
### 背景(製品開発のきっかけ、課題等）
2022年現在、コロナ禍による旅行自粛ムードがいまだ残っています。
そのため旅行を断念せざるを得なかった方も多いと考え、旅行には行けずとも思い出となるような写真を作れないかと考えました。
また、ユーザーが画像生成した観光地のリストを他の人と共有できれば、ユーザーの行きたがってた場所を共有でき、これから誰かと旅行に行こうとするきっかけ作りなり、アフターコロナで気軽に旅行ができるようになったとき旅行需要の増加に貢献します。
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
