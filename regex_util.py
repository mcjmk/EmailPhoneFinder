import re

EMAIL_REGEX = r"_*[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*_*"


def get_emails(s):
    return re.findall(EMAIL_REGEX, s)


def get_phone_numbers(s):
    # Polish conventions
    PHONE_NUMBER_REGEX_POLAND = re.compile(r'''
            # mobile phone
            (?P<mobile>(\d{3})            # 3 digits
            ([\s-])?           # optional separator 
            (\d{3})            # 3 digits
            ([\s-])?           # optional separator 
            (\d{3}))            # 3 digits 
            |                  # alternative 
            # landline phone
            (?P<landline>(\d{2})?    # area code - 2 digits
            ([\s-])?              # optional separator 
            (\d{3})               # 3 digits
            ([\s-])?               # optional separator   
            (\d{2})               # 2 digits
            ([\s-])?               # optional separator  
            (\d{2}))               # 2 digits  
            ''', re.VERBOSE)
    res = []
    phone_regexes = [PHONE_NUMBER_REGEX_POLAND]
    print("Phone numbers:")
    for regex in phone_regexes:
        for match in re.finditer(regex, s):
            if match.group("landline"):
                print("landline: "+ match.group("landline"))
            if match.group("mobile"):
                print("mobile: " + match.group("mobile"))
    return res