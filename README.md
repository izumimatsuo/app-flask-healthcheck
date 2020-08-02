# app-flask-healthcheck

- Python Flask で実装した healthcheck アプリケーション
- データベース含めた healthcheck が可能
- docker コンテナにビルドして実行可能

## ビルド

以下のスクリプト実行で ```healthcheck-api:latest``` のイメージ作成

```
$ ./docker_build.sh

$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
healthcheck-api         latest              0d63dca9079f        9 seconds ago       109MB
```

## 動作確認

以下のスクリプト実行で postgresql コンテナを利用した動作確認が可能

```
$ ./docker_compose_up.sh

$ docker-compose -f Dockerfiles/docker-compose.yml ps
      Name                     Command              State           Ports
----------------------------------------------------------------------------------
dockerfiles_app_1   /app/entrypoint.sh              Up      0.0.0.0:5000->5000/tcp
dockerfiles_rdb_1   docker-entrypoint.sh postgres   Up      0.0.0.0:5432->5432/tcp
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

- dialect: データベースミドル
- driver: 接続ドライバ
- user: ユーザ名
- password: パスワード
- host: ホスト名
- port: ポート番号
- database: データベース名

接続ドライバは以下がコンテナに含まれる

- psycopg2 (postgresql 用ドライバ)
- PyMySQL (mysql 用ドライバ）

postgresql をチェック対象にする場合の ```docker-compose.yml``` の例

```
version: '3'

services:
  app:
    image: healthcheck-api:latest
    ports:
      - 5000:5000
    environment:
      FLASK_ENV: development
      DATABASE_URI: 'postgresql+psycopg2://postgres:postgres@rdb:5432/development'
      HTTPS_PROXY: ${HTTPS_PROXY}
  rdb:
    image: postgres:latest
    ports:
      - 5432:5432
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: development
```

mysql をチェック対象にする場合の ```docker-compose.yml``` の例

```
version: '3'

services:
  app:
    image: healthcheck-api:latest
    ports:
      - 5000:5000
    environment:
      FLASK_ENV: development
      DATABASE_URI: 'mysql+pymysql://root:mysql@rdb:3306/development'
      HTTPS_PROXY: ${HTTPS_PROXY}
  rdb:
    image: mysql:latest
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: mysql
      MYSQL_DATABASE: development
    command: --default-authentication-plugin=mysql_native_password
```
