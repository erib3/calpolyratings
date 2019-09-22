import requests
from django.conf import settings

def recaptcha_check(recaptcha_response):
  params = {
    'secret': settings.RECAPTCHA_SECRET_KEY,
    'response': recaptcha_response,
  }

  r = requests.post('https://www.google.com/recaptcha/api/siteverify?', data=params, verify=True)
  result = r.json()
  return result['success']
