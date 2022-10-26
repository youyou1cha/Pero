import os


def env_to_bool(env, default):
    # str_val = os.environ.get(env)
    str_val = 'ba'
    print(str_val)
    return default if str_val is None else 'p9'

print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
