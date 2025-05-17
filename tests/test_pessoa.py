"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia False)

    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos se torna True se dados obtidos com sucesso)
"""
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
# patch para simular request
from unittest.mock import patch
# importando Pessoa para testes
from Pessoa import Pessoa

# tentando a class Pessoa com TestCase
class TestPessoa(unittest.TestCase):
    # setUp para executar algo antes dos testes começarem de fato
    def setUp(self):
        # instanciando as Pessoas para testes
        self.p1 = Pessoa('Lucas', 'Barbosa')
        self.p2 = Pessoa('Maria', 'Clara')

    # verifica se o atributo de p1 nome = Lucas com assertEqual
    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Lucas')
        self.assertEqual(self.p2.nome, 'Maria')

    # verifica se o atributo de p1 nome é uma str com IsInstace
    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Barbosa')
        self.assertEqual(self.p2.sobrenome, 'Clara')

    def test_pessoa_attr_sobrenome_e_ste(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    
    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        # verifica se a pessoa está com dados obtidos em False lá na classe
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_foram_obtidos_OK(self):
        # substitui requests.get por uma 'requisição_fake'
        with patch('requests.get') as fake_request:
            # que retorna o valor de .ok == true (simula sucesso na conexão)
            fake_request.return_value.ok = True
            
            # verfica se obter_todos_os_dados retorna CONECTADO com assertEqual
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            # verfica se obter_todos_os_dados está em TRUE com assertTrue
            self.assertTrue(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        # simula requisição de valor .ok == false (simula erro na requisição)
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            # verfica se obter_todos_os_dados retorna ERRO 404 com assertEqual
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            # verfica se obter_todos_os_dados está em False com assertFalse
            self.assertFalse(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            # que retorna o valor de .ok == true (simula sucesso na conexão)
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p2.dados_obtidos)

            # simula requisição de valor .ok == false (simula erro na requisição)
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)
            self.assertEqual(self.p2.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p2.dados_obtidos)

if __name__ == '__main__':
    unittest.main(verbosity=2)