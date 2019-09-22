import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



with open(BASE_DIR + "/cpratings/secrets.json") as f:
  secrets = json.loads(f.read())

def get_secret(setting, secret=secrets):
  # get the scret variable or return explicit expectation
  try:
    return secrets[setting]

  except KeyError:
    error_msg = "Set the {0} env variable".format(setting)
    raise ImproperlyConfigured(error_msg)

