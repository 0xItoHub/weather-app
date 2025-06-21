# 天気予報アプリケーション

このアプリケーションは、OpenWeather APIを使用して世界中の都市の天気情報を取得し、表示するシンプルなWebアプリケーションです。

## 機能

- 都市名を入力して天気情報を検索(英語で)
- 現在の気温、天気の説明、湿度、風速を表示
- レスポンシブなデザイン
- エラーハンドリング機能

## 技術スタック

- Python 3.x
- Flask (Webフレームワーク)
- OpenWeather API (天気データ)
- HTML/CSS (フロントエンド)

## セットアップ方法

1. リポジトリをクローン
```bash
git clone [リポジトリのURL]
cd weather-app
```

2. 必要なパッケージをインストール
```bash
pip install -r requirements.txt
```

3. OpenWeather APIのAPIキーを取得
- [OpenWeather](https://openweathermap.org/)にアクセス
- アカウントを作成し、APIキーを取得

4. 環境変数の設定
`.env`ファイルを作成し、以下の内容を追加：
```
OPENWEATHER_API_KEY=あなたのAPIキー
```

5. アプリケーションの起動
```bash
python app.py
```

6. ブラウザでアクセス
`https://weather-app-f0p1.onrender.com/`にアクセス

## デプロイ

このアプリケーションはRenderでデプロイ可能です。デプロイ手順：

1. Renderアカウントを作成
2. 新しいWebサービスを作成
3. GitHubリポジトリと連携
4. 環境変数`OPENWEATHER_API_KEY`を設定
5. デプロイを開始

## ファイル構成

```
weather-app/
├── app.py              # メインアプリケーションファイル
├── requirements.txt    # 必要なPythonパッケージ
├── templates/          # HTMLテンプレート
│   └── index.html     # メインページのテンプレート
├── static/            # 静的ファイル
│   └── style.css      # スタイルシート
└── render.yaml        # Render用の設定ファイル
```

## ライセンス

MITライセンス 
