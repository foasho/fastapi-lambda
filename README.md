# FastAPI+Lambdaサーバーレステンプレート

# 初めに

FastAPIを使いつつサーバーレスをAWSで構築します。

## 動作手順

- このレポジトリをダウンロード
- Local上でのAPIテストとPyTestの実行
- githubにPushし、Actionsを確認する
- IAMでAPIキーを取得し、GithubのRepository Secretsに設定
- Lambda作成
- APIGateway作成
- 接続確認

## ディレクトリ構成

```commandline
<your_project>
    |- .github/workflows/main.yml
    |- pytests
        |- __init__.py
         -  test_main.py

    |- .gitignore
    |- main.py
    |- localrun.py
    |- requirements.txt
```

# さっそく実装

## 1. レポジトリをダウンロード

git依存は自身のレポジトリでやるためにZIPでダウンロードするのが良いと思います。
リンク先: https://github.com/foasho/fastapi-lambda

コマンドでやる場合は以下
```commandline
git clone https://github.com/foasho/fastapi-lambda.git
```

プロジェクト直下に置いた際には、自身のレポジトリ（プライベート）を作成してください。

## 2. ローカルホストで実行とテスト実行
ローカルホストで実行
```commandline
pip install -r requirements.txt
python localrun.py

>> INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

http://127.0.0.1:8000
につなぎ、"Success"と表示されればをOKです。

テスト実行
```commandline
pytest -s
```

## 3. GithubにPushし、Actionsを確認



