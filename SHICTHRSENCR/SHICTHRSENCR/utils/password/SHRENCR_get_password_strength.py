
# SHICTHRSENCR\SHICTHRSENCR\utils\password\SHRENCR_get_password_strength.py

import re

def get_password_strength(password : str) -> str:
    if not password or not isinstance(password , str):
        return "无"

    length = len(password)
    
    has_lowercase = bool(re.search(r'[a-z]', password))    
    has_uppercase = bool(re.search(r'[A-Z]', password))   
    has_digit = bool(re.search(r'\d', password))      
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/`~\\|]', password))

    char_type_count = sum([has_lowercase , has_uppercase , has_digit , has_special])

    if length >= 8 and char_type_count >= 3:
        return "强"
    
    if length >= 6 and char_type_count >= 2:
        return "中"
    
    if length < 6 or char_type_count == 1:
        return "弱"
    
    return "弱"