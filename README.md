## 介紹

這是一個參照 [django-best-practice](https://xlanstar.github.io/django-best-practice/) 建立的 Django 範本專案，用來快速建立一個 Django 專案。

## 開發

### 建置環境

1. 請確保你有安裝 `uv`，然後執行 `uv venv` 來安裝 python3.13 虛擬環境，並且需要啟用你建立好的虛擬環境

    MacOS: `source .venv/bin/activate`
    Windows: `.venv/bin/activate.bat`

### 在本地運行服務

`python manage.py runserver`

### 資料庫遷移

1. `python manage.py makemigrations`

2. `python manage.py migrate`

### 翻譯

1. 若要新增語言

    1. 請於 [config/settings/base.py:64](/config/settings/base.py#L64) 新增語言

    > 格式為 ([language code](https://docs.djangoproject.com/en/dev/topics/i18n/#term-language-code), 語言名字) \
    > 語言名字將會使用 i18n 來處理

    2. 並執行 `python manage.py makemessages -l <language code>`

2. 若有新增語言或更新文本原始碼，請執行 `python manage.py makemessages --all` 來更新 `.po` 翻譯檔

3. 翻譯完畢後，請執行 `python manage.py compilemessages` 來編譯翻譯檔
