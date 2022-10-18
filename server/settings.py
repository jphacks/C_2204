import os
from os.path import join, dirname
from dotenv import load_dotenv

# 環境変数をどうしても上書きする必要がある際に利用(デフォルトは上書きしない)
# load_dotenv(override=True)
# .envファイルが見つからないと上位のディレクトリすべてを探してしまう
load_dotenv(join(dirname(__file__), ".env"))

try:
    APP_PORT = os.getenv("APP_PORT")
    APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")

except KeyError:
    raise "環境変数を確認してください."

# テスト
if __name__ == "__main__":
    print(os.getenv("APP_PORT"))
