================================================================================
Download the desired quantized Llama-2-7B-Chat model from https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
================================================================================

PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com\models> python
Python 3.9.12 (main, Apr  4 2022, 05:22:27) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>> from huggingface_hub import hf_hub_download
>>>
>>> hf_hub_download(repo_id="TheBloke/Llama-2-7B-Chat-GGML", filename="llama-2-7b-chat.ggmlv3.q4_0.bin", cache_dir="./")
llama-2-7b-chat.ggmlv3.q4_0.bin: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3.79G/3.79G [04:36<00:00, 13.7MB/s] 
C:\Users\A\AppData\Roaming\Python\Python39\site-packages\huggingface_hub\file_download.py:147: UserWarning: `huggingface_hub` cache-system uses symlinks by default to efficiently store duplicated files but your machine does not support them in C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com. Caching files will still work but in a degraded version that might require more space on your disk. This warning can be disabled by setting the `HF_HUB_DISABLE_SYMLINKS_WARNING` environment variable. For more details, see https://huggingface.co/docs/huggingface_hub/how-to-cache#limitations.
To support symlinks on Windows, you either need to activate Developer Mode or to run Python as an administrator. In order to see activate developer mode, see this article: https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development
  warnings.warn(message)
'./models--TheBloke--Llama-2-7B-Chat-GGML\\snapshots\\76cd63c351ae389e1d4b91cab2cf470aab11864b\\llama-2-7b-chat.ggmlv3.q4_0.bin'
>>> quit()
PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com\models> 

================================================================================
Download for better results Llama-2-13B-Chat model from https://huggingface.co/TheBloke/Llama-2-13B-Chat-GGML/tree/main
================================================================================

PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com\models> python
>>> from huggingface_hub import hf_hub_download
>>> hf_hub_download(repo_id="TheBloke/Llama-2-13B-Chat-GGML", filename="llama-2-13b-chat.ggmlv3.q8_0.bin", cache_dir="./")
>>> quit()
