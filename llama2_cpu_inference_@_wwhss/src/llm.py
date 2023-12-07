'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from langchain.llms import CTransformers
import json

def load_env_from_file(file_path):

  with open(file_path, 'r') as f:
    env = json.load(f)

  return env
cfg = load_env_from_file('config/config.json')



def build_llm():
    # Local CTransformers model
    llm = CTransformers(model=cfg['MODEL_BIN_PATH'],
                        model_type=cfg['MODEL_TYPE'],
                        config={'max_new_tokens': cfg['MAX_NEW_TOKENS'],
                                'temperature': cfg['TEMPERATURE']}
                        )

    return llm