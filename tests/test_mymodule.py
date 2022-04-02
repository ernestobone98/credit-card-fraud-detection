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
        ''' 
        Ne regarde pas car s'arrete dès la 1 er erreur
        self.assertEqual(test_password_expert1("EanFflU0O,i"),"EanFflU0O,i")
        self.assertEqual(test_password_expert1("k@r2t#>H0T"),"k@r2t#>H0T")
        self.assertEqual(test_password_expert1("'^ebXmT}NTM&L"),"'^ebXmT}NTM&L")
        self.assertEqual(test_password_expert1("<$&VdT3g"),"<$&VdT3g")
        self.assertEqual(test_password_expert1(">4X#eq-@1i"),">4X#eq-@1i")
        self.assertEqual(test_password_expert1("gr|;VxZ~wW&5;"),"gr|;VxZ~wW&5;")
        self.assertEqual(test_password_expert1("$DbvoH$GM@/nn4"),"$DbvoH$GM@/nn4")
        self.assertEqual(test_password_expert1("&@uyi*VxCp?d"),"&@uyi*VxCp?d")
        self.assertEqual(test_password_expert1("2Yu$}I-+&O"),"2Yu$}I-+&O")
        self.assertEqual(test_password_expert1("^3bY6{`Ud]?<EKa"),"^3bY6{`Ud]?<EKa")
        '''     
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


'''
si on trouve comment lui faire test tout est pas stop dès la 1er erreur

y>RBVmfBpj^[&{s
WCjW,PJ66ok,
y/cX?s5xFB/in/%
7QNTu{Ua$]--j
fsjH+KH_a=gfh;i
,u9ia&?Q
Sy$q/.]>29p0wL
Hv,EK{_##`5v>
Z.haj1[pvOn!
cf,Qg,km

:"(d&(N;9wN.=`Eg
PXfHZHh3W
xB51}rO696#"C*
n/BfhINN>ANN8WQI
;oVk#{.PgyK{o
-uV+mNt
0e#[Z:/gpU_K
aEvz>n(8L![&o
.:Lh5`]!b{HCdo
uhFa~WSL!

__________________________________

lna2JiWBINf7OOO
5T405NuiZ
WwKuSfijgGJ
zJxurK8VNa4
LrK5CdhwMt
3jbLS6pnFEhk
HuL9tAFZ4t8yLi
fCSOhYPK5i3o0OW
5BvgDU2j
Ge5Idp6CJkVlWk

EaynIkjeTfzX8
gD96y1m4cHRLS
at1A1cDFtpxVp6e
0mIWM5GycNjB2AS
NkVuhS1gVp8I
NB07UyjDCkv5z9R
B0xOlDVeZX
QWCd4uAtmaLZpm
FhnRWKMjUDNf
IQiwUXLLchGnl

9BMPuNPT
aDBZWcCzbS
gJHx101pTlWweK
O78MSxZkmA
lt15Bxvd2Zv
W4vnbuihs
50eqqUYrUsyBsk
aTUOsSIH
kH7T34XGE
yHgDGW6ZM3
'''