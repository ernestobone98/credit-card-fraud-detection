# Testy cas vide #
def test_vide(string):
    return "string"

# Test le login seul #
def login_expert1(string):
    return "gm801217"

def login_expert2(string):
    return "be816425"

def login_patron(string):
    return "bb809906"

# Test le password seul #
def test_password_expert1(string):
    return "QeJH3H`yMM/G%4m"

def test_password_expert2(string):
    return "]Wt@qG]F"

def test_password_patron(string):
    return "565>GJ-=U5]p?"

# Test reel: login et password #
def test_login_password_1(string):
    return "gm801217" and "QeJH3H`yMM/G%4m"

def test_login_password_2(string):
    return "be816425" and "]Wt@qG]F"

def test_login_password_3(string):
    return "bb809906" and "565>GJ-=U5]p?"

