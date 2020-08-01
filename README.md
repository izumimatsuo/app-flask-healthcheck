# app-flask-healthcheck

- Python Flask で実装した healthcheck アプリケーション
- データベース含めた healthcheck が可能
- docker コンテナにビルドして実行可能

## ビルド

以下のスクリプト実行で ```healthcheck-api:latest``` をイメージ作成

```
$ ./docker_build.sh

$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
healthcheck-api         latest              0d63dca9079f        9 seconds ago       109MB
```

## 動作確認

以下のスクリプト実行で postgresql コンテナも起動して動作確認が可能

```
$ ./docker_compose_up.sh
```

正常時のレスポンス

```
$ curl -i localhost:5000/healthcheck

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sat, 01 Aug 2020 08:16:44 GMT

{
  "status": "healthy"
}
```

障害時のレスポンス

```
$ curl -i localhost:5000/healthcheck

HTTP/1.0 500 INTERNAL SERVER ERROR
Content-Type: application/json
Content-Length: 28
Server: Werkzeug/1.0.1 Python/3.8.5
Date: Sat, 01 Aug 2020 08:21:42 GMT

{
  "status": "unhealthy"
}
```

## 環境定義

チェック対象のデータベースを以下の環境変数で定義

DATABASE_URI = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}'

- dialect: データベースミドル (例 'postgresql')
- driver: 接続ドライバ (例 'psycopg2')
- user: ユーザ名 (例 'postgres')
- password: パスワード (例 'postgres')
- host: ホスト名 (例 'rdb')
- port: ポート番号 (例 '5432')
- database: データベース名 (例 'development')

接続ドライバは以下がコンテナに含まれる

- psycopg2 (postgresql 用ドライバ)
- PyMySQL (mysql 用ドライバ）
- sqlite3 は標準サポート
