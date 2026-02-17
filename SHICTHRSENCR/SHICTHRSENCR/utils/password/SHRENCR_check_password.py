
# SHICTHRSENCR\utils\password\SHRENCR_check_password.py

import re

def check_password(password : str) -> tuple[bool, str]:
    if len(password) < 8:
        return False , "密码长度至少为8位"
    
    if not re.search(r'[A-Z]', password):
        return False , "密码必须包含大写字母"
    
    if not re.search(r'[a-z]', password):
        return False , "密码必须包含小写字母"
    
    if not re.search(r'\d', password):
        return False , "密码必须包含数字"
    
    return True , "密码校验通过"