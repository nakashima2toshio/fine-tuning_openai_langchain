#FROM python:3.11-bullseye
#
#ENV LANG C.UTF-8
#ENV TZ Asia/Tokyo
#
#WORKDIR /app
#
## pip installs
#COPY ./requirements.txt requirements.txt
#
## 必要なパッケージをインストール
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends postgresql-client gcc libpq-dev && \
#    python3 -m pip install -r requirements.txt --no-cache-dir && \
#    apt-get purge -y --auto-remove gcc libpq-dev && \
#    rm -rf /var/lib/apt/lists/*
#
#COPY . /app
#
## FastAPIの起動
#CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
#
#ENV PYTHONPATH "${PYTHONPATH}=/app"
#
## Start FastAPI
#CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

# python3.11のイメージをダウンロード
FROM python:3.11-buster
# pythonの出力表示をDocker用に調整
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# pipを使ってpoetryをインストール
RUN pip install poetry

# poetryの定義ファイルをコピー (存在する場合)
COPY pyproject.toml* poetry.lock* ./

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# uvicornのサーバーを立ち上げる
# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]