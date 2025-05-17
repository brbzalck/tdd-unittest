try:
    import sys
    import os
    # sys para procurar um determinado diretório p/ importação
    sys.path.append(
        # os para achar determinado caminhos
        os.path.abspath(
            os.path.join(
                # pegando o diretório desse arquivo e voltando um para entrar em src
                os.path.dirname(__file__), '../src'
            )
        )
    )
except:
    raise

import unittest
from calculadora import soma

# classe que testa minha calculadora, herda de TestCase para usar test_
class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        # assertEqual = afirma ser igual, minha função soma onde entra 5, 5 e retorna 10
        self.assertEqual(soma(5, 5), 10)

    def test_5_negativo_e_5_positivo_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        # passando uma tupla de valores para dentro de uma variável
        x_y_saidas = (
            (10, 10, 20),
            (15, 5, 20),
            (10, 15, 25),
            (-10, 20, 10),
            (10, 20, 30),
        )

        # iterando a lista de valores
        for x_y_saida in x_y_saidas:
            # se um falhar msm assim continua, subTest em cima da instancia para testar multiplos valores (msg, parâmetros)
            with self.subTest(x_y_saida=x_y_saida):
                # extraindo os valores da tupla para jogar na função separadamente
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        # assertRaises em cima da Instância pq eu espero vir um erro de AssertionError(str + int)
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        # assertRaises em cima da Instância pq eu espero vir um erro de AssertionError(str + int)
        with self.assertRaises(AssertionError):
            soma(11, '0')

if __name__ == '__main__':
    # deixando o log mais detalhado
    unittest.main(verbosity=2)