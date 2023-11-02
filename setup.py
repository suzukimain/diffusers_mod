# -*- coding: utf-8 -*-
from setuptools import setup
from shutil import copy
import subprocess
import os

setup(
    name="diffusers_mod", # パッケージの名前
    version="0.1.0", # パッケージのバージョン
    py_modules=["diffusers"], # パッケージに含めるモジュール
)

try:
  import diffusers
except:
  # subprocessモジュールを使ってpipコマンドを実行
  subprocess.run(["pip", "install", "git+https://github.com/huggingface/diffusers.git"])
import diffusers

# コピーしたいファイルのパス
# 絶対パスを指定
src_path = os.path.abspath("safety_checker.py")
# インストール先のディレクトリを動的に取得
dst_dir = os.path.dirname(diffusers.__file__)
dst_path = os.path.join(dst_dir, "pipelines/deepfloyd_if/safety_checker.py")

# ファイルをコピー
try:
  copy(src_path, dst_path)
except:
  raise FileNotFoundError("""本リポジトリはGoogleコラボでの実行を前提としています。
                         なお、手動でdiffusersのsafety_checker.pyを置き換える場合はその他プラットフォームでも使用できます。
                         """)

