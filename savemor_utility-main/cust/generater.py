from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from authentication.models import User 
from datetime import date
import random
import string
import re

# this function generate random pdf
def render_to_pdf(template_src,content_dict ={}):
    # getting template 
    template = get_template(template_src)
    # passing data to templates
    html = template.render(content_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type = 'application/pdf')
    return None


def order_id():
    lower =  string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    combine = list(lower+upper+num)
    random.shuffle(combine)
    final_id = ''.join(combine)[:11]
    return 'TRN'+final_id


def isValidPanCardNo(panCardNo):
 
    # Regex to check valid
    # PAN Card number
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
 
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the PAN Card number
    # is empty return false
    if(panCardNo == None):
        return False
 
    # Return if the PAN Card number
    # matched the ReGex
    if(re.search(p, panCardNo) and
       len(panCardNo) == 10):
        return True
    else:
        return False

def discount(amount):
    avg = []
    for i in range(10 , 20):
        if i != 0:
            avg.append(i)
            random.shuffle(avg)

    discount_prise = amount-(amount*avg[0]/100)
    discount_value = amount - discount_prise
    return discount_value
        



# if __name__ == '__main__':
#     print(discount())