import os
from dotenv import load_dotenv

load_dotenv()

# basedir = os.path.apspath(os.path.dirname(__file__))

class FlaskConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY or len(SECRET_KEY) < 32:
        raise RuntimeError('Set SECRET_KEY to a random value of at least 32 characters')