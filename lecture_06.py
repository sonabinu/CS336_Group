import time
from typing import Callable
import torch
import torch.nn as nn
from torch.profiler import ProfilerActivity
from torch.utils.cpp_extension import load_inline
import triton
import triton.language as tl
from execute_util import text, link, image
from file_util import ensure_directory_exists
from lecture_util import article_link
from torch_util import get_device
from lecture_06_utils import check_equal, check_equal2, get_local_url, round1, mean
import os