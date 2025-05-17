import requests


class Pessoa():
    def __init__(self, nome, sobrenome):
        # instancia de Pessoa tem nome, sobrenome, e dados_obtidos iniciado em False
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_todos_os_dados(self):
        # colocando requests.get('') numa variável para acessar acessar a resposta manipulada no teste em ok == true ou false?
        resposta = requests.get('')

        if resposta.ok:
            # se ok for True atualiza dados_obtido em True e retorna CONECTADO
            self.dados_obtidos = True
            return 'CONECTADO'
        else:
            # se ok for False atualiza dados_obtido em False e retorna ERRO 404
            self.dados_obtidos = False
            return 'ERRO 404'