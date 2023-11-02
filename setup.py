# -*- coding: utf-8 -*-
!pip install git+https://github.com/huggingface/diffusers.git
import shutil
shutil.move("./safety_checker.py", "/usr/local/lib/python3.10/dist-packages/diffusers/pipelines/deepfloyd_if/safety_checker.py")
