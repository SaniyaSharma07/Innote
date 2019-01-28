from django.views.decorators.http import require_http_methods
from referrals.helpers.referral import create_referral, fetch_referrals
from commons.utils.response import OK

@require_http_methods(['POST','GET'])
def manage_patient_referrals(request, patient_id):

    auth_token = request.META.get('HTTP_AUTHORIZATION')
    request_id = request.request_id

    # create patient referral
    if request.method == 'POST':
        user_id = request.user_data['user_id']
        request_data = request._json_body

        data = {
            'urgency': request_data.get('urgency',''),
            'speciality': request_data.get('speciality',''),
            'insuranceDetails': request_data.get('insuranceDetails',''),
            'referralReason': request_data.get('referralReason',''),
            'createdBy': user_id,
            'referringProvider': request_data.get('referringProvider',''),
            'referredProvider': request_data.get('referredProvider',''),
            'attachments': request_data.get('attachments',''),
            'patientId': request_data.get('patientId','')
        }

        response = create_referral(auth_token, data)
        return OK(response.get('message',''))

    # get list of patient referrals
    if request.method == 'GET':
        response = fetch_referrals(auth_token, patient_id)
        return OK(response)

        

        
       



# "speciality":"Cardiologist",
# "urgency":"urgent",
# "referralReason":"provider is not available",
# "referringProviderId":"1234",
# "referredProviderId":"2345",
# "patientId":"PA1290",
# "attachments": {"fileName":"firstfile","link":"/a/b"},
# "payer":"Atena",
# "insurancePlan":"gold"
# }