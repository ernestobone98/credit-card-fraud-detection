import unittest
from mymodule import test_vide, login_expert1, login_expert2, login_patron, test_password_expert1, test_password_expert2, test_password_patron, test_login_password_1, test_login_password_2, test_login_password_3

class TestVide(unittest.TestCase):
    def test_vide(self):
        self.assertEqual(test_vide(""),"")
        self.assertEqual(test_vide("string"), "string")

class TestLogin1(unittest.TestCase):
    def test_login_1(self):
        self.assertEqual(login_expert1("gm801217"), "gm801217")
        self.assertEqual(login_expert1("Ge5Idp6CJkVlWk"), "Ge5Idp6CJkVlWk")
        
class TestLogin2(unittest.TestCase):
    def test_login_2(self):
        self.assertEqual(login_expert2("be816425"), "be816425")
        self.assertEqual(login_expert2("5T405NuiZ"), "5T405NuiZ")

class TestLogin3(unittest.TestCase):
    def test_login_3(self):
        self.assertEqual(login_patron("bb809906"), "bb809906")
        self.assertEqual(login_patron("lna2JiWBINf7OOO"), "lna2JiWBINf7OOO")

class TestPassword1(unittest.TestCase):
    def test_password_1(self):
        self.assertEqual(test_password_expert1("QeJH3H`yMM/G%4m"), "QeJH3H`yMM/G%4m")
        self.assertEqual(test_password_expert1(",u9ia&?Q"), ",u9ia&?Q")
     
class TestPassword2(unittest.TestCase):
    def test_password_2(self):
        self.assertEqual(test_password_expert2("]Wt@qG]F"), "]Wt@qG]F")
        self.assertEqual(test_password_expert2("0e#[Z:/gpU_K"), "0e#[Z:/gpU_K")

class TestPassword3(unittest.TestCase):
    def test_password_3(self):
        self.assertEqual(test_password_patron("565>GJ-=U5]p?"), "565>GJ-=U5]p?")
        self.assertEqual(test_password_patron("Hv,EK'{_##`/5v>"), "Hv,EK'{_##`/5v>")

class TestLoginPassword1(unittest.TestCase):
    def test_login_password_1(self):
        self.assertEqual(test_login_password_1("gm801217" and "QeJH3H`yMM/G%4m"), "gm801217" and "QeJH3H`yMM/G%4m")
        self.assertEqual(test_login_password_1("Ge5Idp6CJkVlWk" and ",u9ia&?Q"), "Ge5Idp6CJkVlWk" and ",u9ia&?Q")

class TestLoginPassword2(unittest.TestCase):
    def test_login_password_2(self):
        self.assertEqual(test_login_password_2("be816425" and "]Wt@qG]F"), "be816425" and "]Wt@qG]F")
        self.assertEqual(test_login_password_2("5T405NuiZ" and "QJH3H`yMM/G%4m"), "5T405NuiZ" and "QJH3H`yMM/G%4m")

class TestLoginPasswor3(unittest.TestCase):
    def test_login_password_3(self):
        self.assertEqual(test_login_password_3("bb809906" and "565>GJ-=U5]p?"), "bb809906" and "565>GJ-=U5]p?")
        self.assertEqual(test_login_password_3("lna2JiWBINf7OOO" and "Hv,EK'{_##`/5v>"), "lna2JiWBINf7OOO" and "Hv,EK'{_##`/5v>")

unittest.main()
