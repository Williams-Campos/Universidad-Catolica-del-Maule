import unittest
from Traductor import traduccion

class TestTraduccion(unittest.TestCase):
    def test_traduccion(self):
        # Caso de prueba: 999,999,999
        datos = [['nine', 'hundred', 'ninety', 'nine', 'million', 'nine', 'hundred', 'ninety', 'nine', 'thousand', 'nine', 'hundred', 'ninety', 'nine']]
        resultado_esperado = [999999999]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: -999,999,999
        datos = [['negative', 'nine', 'hundred', 'ninety', 'nine', 'million', 'nine', 'hundred', 'ninety', 'nine', 'thousand', 'nine', 'hundred', 'ninety', 'nine']]
        resultado_esperado = [-999999999]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: 123,456,789
        datos = [['one', 'hundred', 'twenty', 'three', 'million', 'four', 'hundred', 'fifty', 'six', 'thousand', 'seven', 'hundred', 'eighty', 'nine']]
        resultado_esperado = [123456789]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: -123,456,789
        datos = [['negative', 'one', 'hundred', 'twenty', 'three', 'million', 'four', 'hundred', 'fifty', 'six', 'thousand', 'seven', 'hundred', 'eighty', 'nine']]
        resultado_esperado = [-123456789]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: 0
        datos = [['zero']]
        resultado_esperado = [0]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: 1,000,000
        datos = [['one', 'million']]
        resultado_esperado = [1000000]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: -1,000,000
        datos = [['negative', 'one', 'million']]
        resultado_esperado = [-1000000]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: 1,001
        datos = [['one', 'thousand', 'one']]
        resultado_esperado = [1001]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: -1,001
        datos = [['negative', 'one', 'thousand', 'one']]
        resultado_esperado = [-1001]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: 500,000
        datos = [['five', 'hundred', 'thousand']]
        resultado_esperado = [500000]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: -500,000
        datos = [['negative', 'five', 'hundred', 'thousand']]
        resultado_esperado = [-500000]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: 42
        datos = [['forty', 'two']]
        resultado_esperado = [42]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: -42
        datos = [['negative', 'forty', 'two']]
        resultado_esperado = [-42]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: 7
        datos = [['seven']]
        resultado_esperado = [7]
        self.assertEqual(traduccion(datos), resultado_esperado)

        # Caso de prueba: -7
        datos = [['negative', 'seven']]
        resultado_esperado = [-7]
        self.assertEqual(traduccion(datos), resultado_esperado)

if __name__ == '__main__':
    unittest.main()