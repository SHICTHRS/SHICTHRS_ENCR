
# SHICTHRSENCR\SHICTHRSENCR\utils\identity\SHRENCR_check_chinese_name.py

import re

def check_is_chinese_name(name: str) -> bool:
    if not name or not isinstance(name, str):
        return False
    
    try:
        name_without_dot = name.replace('·', '')
        name_without_dot.encode('gb2312')
        
    except UnicodeEncodeError:
        return False
    
    name = name.strip()

    pattern = r'^([\u4e00-\u9fa5]{2,}|[\u4e00-\u9fa5]+(·[\u4e00-\u9fa5]+)*)$'
    
    return bool(re.match(pattern , name))