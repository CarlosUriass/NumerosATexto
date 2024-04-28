import unittest
from numero_a_texto import num_txt

class TestNumerosATexto(unittest.TestCase):

    def test_num_txt(self):
        self.assertEqual(num_txt("001000001.00", "MXN"), "un millon un pesos con cero centavos")
        self.assertEqual(num_txt("100010001.01", "MXN"), "cien millones diez mil un pesos con un centavos")
        self.assertEqual(num_txt("002000002.10", "MXN"), "dos millones dos pesos con diez centavos")
        self.assertEqual(num_txt("000000001.90", "cup"), "un pesos cubanos con noventa centavos")
        self.assertEqual(num_txt("000000000.00", "MXN"), "cero pesos con cero centavos")
        self.assertEqual(num_txt("128234", "MXN"), "ciento veintiocho mil doscientos treinta y cuatro pesos")
        self.assertEqual(num_txt("2", "MXN"), "dos pesos")
        self.assertEqual(num_txt("1234653.23", "MXN"), "un millon doscientos treinta y cuatro mil seiscientos cincuenta y tres pesos con veintitres centavos")
        self.assertEqual(num_txt("1001234", "MXN"), "un millon mil doscientos treinta y cuatro pesos")
        self.assertEqual(num_txt("10001", "MXN"), "diez mil un pesos")
        self.assertEqual(num_txt("542321", "MXN"), "quinientos cuarenta y dos mil trescientos veintiun pesos")





if __name__ == '__main__':
    unittest.main()
