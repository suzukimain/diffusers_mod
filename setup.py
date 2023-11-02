# -*- coding: utf-8 -*-
from setuptools import setup
from shutil import copy

setup(
    name="diffusers_mod", # パッケージの名前
    version="0.1.0", # パッケージのバージョン
    py_modules=["diffusers"], # パッケージに含めるモジュール
)

try:
  import diffusers
except:
  !pip install git+https://github.com/huggingface/diffusers.git


# コピーしたいファイルのパス
src_path = "./safety_checker.py"
dst_path = "/usr/local/lib/python3.10/dist-packages/diffusers/pipelines/deepfloyd_if/safety_checker.py"

# ファイルをコピー
try:
  copy(src_path, dst_path)
except:
  raise FileNotFoundError("""本リポジトリはGoogleコラボでの実行を前提としています。
                         なお、手動でdiffusersのsafety_checker.pyを置き換える場合はその他プラットフォームでも使用できます。
                         """)
