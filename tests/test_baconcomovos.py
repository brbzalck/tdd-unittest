'''

TDD - Test driven development (Desenvolvimento dirigido por testes)

RED
Parte 1 - Criar o teste e ver falhar

GREEN
Parte 2 - Criar o código e ver o teste passar

REFACTOR
Parte 3 - Melhorar o código

'''
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
from baconcomovos import bacon_com_ovos


# testando o método bacon com ovos
class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        # nesse teste assertRaises em caso de erros
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')
    
    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            # subTest para fazer o teste em TODA iteração, onde a entrada na função bacon_com_ovos deve ser igual a saida da def
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)


    def test_bacon_com_ovos_deve_retornar_passar_fome_se_a_entrada_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_bacon_se_a_entrada_for_multiplo_somente_de_3(self):
        entradas = (6, 3, 9, 12)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_bacon_se_a_entrada_for_multiplo_somente_de_5(self):
        entradas = (5, 10, 25, 20)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

if __name__ == '__main__':
    unittest.main(verbosity=2)