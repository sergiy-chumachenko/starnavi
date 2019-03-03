import clearbit
from requests.exceptions import HTTPError
from starnavi_task.settings import (CLEARBIT_API_SECRET_KEY, HUNTER_API_SECRET_KEY,
                                    HUNTER_VERIFICATION_LIMIT)
from pyhunter import PyHunter

hunter = PyHunter(HUNTER_API_SECRET_KEY)
clearbit.key = CLEARBIT_API_SECRET_KEY


def get_additional_info(email):
    try:
        response = clearbit.Enrichment.find(email=email, stream=True)
    except HTTPError:
        return None
    else:
        if response is not None and response['person'] is not None:
            try:
                data = response['person']['name']['fullName']
            except ValueError:
                data = None
            return {'data': data}
        return None


def check_email(email):
    result = hunter.email_verifier(email=email)
    if result.get('score') >= HUNTER_VERIFICATION_LIMIT:
        return True
    return False
