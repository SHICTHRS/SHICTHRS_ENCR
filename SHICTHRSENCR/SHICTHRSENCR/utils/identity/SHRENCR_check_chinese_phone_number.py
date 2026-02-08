
# SHICTHRSENCR\SHICTHRSENCR\utils\identity\SHRENCR_check_chinese_phone_number.py

import re

def check_chinese_phone_number(phone_number : str) -> bool:
    if not isinstance(phone_number , str):
        return False
    
    phone_number = phone_number.strip()
    
    if not phone_number:
        return False
    
    pattern = r'^1[3-9]\d{9}$'
    
    return bool(re.fullmatch(pattern , phone_number))