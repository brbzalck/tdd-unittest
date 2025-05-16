'''

TDD - Test driven development (Desenvolvimento dirigido por testes)

RED
Parte 1 - Criar o teste e ver falhar

GREEN
Parte 2 - Criar o código e ver o teste passar

REFACTOR
Parte 3 - Melhorar o código

'''
import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
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

unittest.main(verbosity=2)