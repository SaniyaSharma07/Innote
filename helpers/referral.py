from commons.utils.http_error import (Forbidden, InternalServerError,
                                      Unauthorized)
from commons.utils.request_client import make_request
from patients.models.innote_config import InNoteConfig


def create_referral(auth_token, data):

    api_config = InNoteConfig.objects.get_config('CreateReferral' or {})
    
    response_json, response_content, response_code, error = make_request(
        url=api_config.get('url'),
        method=api_config.get('method'),
        headers={'Authorization': (auth_token or '')},
        json=data
    )

    response_json = response_json.get('message')

    if int(response_code) == 401:
        raise Unauthorized
    elif int(response_code) == 403:
        raise Forbidden
    elif response_code is None or int(response_code/100) != 2:
        raise InternalServerError
    else:
        return response_json

def fetch_referrals(auth_token, patient_id):

    api_config = InNoteConfig.objects.get_config('FetchReferral' or {})
    
    response_json, response_content, response_code, error = make_request(
        url=api_config.get('url'),
        method=api_config.get('method'),
        headers={'Authorization': (auth_token or '')}
    )
    
    response_json = response_json.get('body','')
    error_message = response_json.get('error','')

    if int(response_code) == 401:
        raise Unauthorized
    elif int(response_code) == 403:
        raise Forbidden
    elif response_code is None or int(response_code/100) != 2:
        raise InternalServerError
    else:
        if 'message' in error_message:
            return error_message['message']
        return response_json


def search_provider(auth_token, speciality, patient_zipcode):
    
    api_config = InNoteConfig.objects.get_config('SearchProvider' or {})
    response_json, response_content, response_code, error = make_request(
        url=api_config.get('url').format(speciality=speciality,patient_zipcode=patient_zipcode),
        method=api_config.get('method'),
        headers={'Authorization': (auth_token or '')}
    )

    if int(response_code) == 401:
        raise Unauthorized
    elif int(response_code) == 403:
        raise Forbidden
    elif response_code is None or int(response_code/100) != 2:
        raise InternalServerError
    else:
       return response_json

def fetch_specialities(auth_token, speciality):

    api_config = InNoteConfig.objects.get_config('FetchSpecialities' or {})
    response_json, response_content, response_code, error = make_request(
        url=api_config.get('url').format(speciality=speciality),
        method=api_config.get('method'),
        headers={'Authorization': (auth_token or '')}
    )

    return response_json