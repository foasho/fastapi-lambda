# Dockerfile
FROM python:3.9

RUN pip install --upgrade pip

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y

# タイムゾーンを日本に設定
ENV TZ Asia/Tokyo

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコピー
COPY . /app

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn + UvicornでFastAPIを起動
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--workers", "4", "--bind", "0.0.0.0:8009"]
