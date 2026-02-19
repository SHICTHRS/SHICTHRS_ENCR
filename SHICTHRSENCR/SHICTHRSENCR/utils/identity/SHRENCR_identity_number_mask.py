
# SHICTHRSENCR\SHICTHRSENCR\utils\identity\SHRENCR_identity_number_mask.py

def get_identity_number_mask(org_code : str) -> str:
    return org_code[:4] + '*' * 10 + org_code[-4:]