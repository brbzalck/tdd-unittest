from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, \
    Iterable

# Primitivos
numero: int = 10
flutuante: float = 1.5
boleano: bool = True
string: str = 'Lucas'

# Sequências
lista: List[int] = [1, 2, 3]
# union para unir int e str numa mesma type anotation em List
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']
# na tupla, deveremos tipar cada tipo de dados
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Luiz')

# Dicionários e conjuntos

# ALIAS de Dict a chave vai ser STR, e o valor por ser str, int ou uma lista de int(graças ao UNION)
MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias

# chave é uma str, e o valor é str ou int, graças ao union
pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 30}
# Usando o alias definido acima
pessoa2: MeuDict = {'nome': 'Luiz Otávio',
                    'sobrenome': 'Miranda', 'idade': 30, 'l': [1, 2]}

# Criando o meu próprio tipo de dados com NewType
UserId = NewType('UserId', int)
user_id = UserId(325456789)


# função que recebe uma função chamável(calleble)[que recebe dois int], e retorna um int, retorna a própria função chamável recebida
def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    # retorna a própria função recebida
    return funcao

# funçar de soma que recebe argumento x e y do tipo int QUE retorna int
def soma(x: int, y: int) -> int:
    return x + y


print(retorna_funcao(soma)(10, 20))


class Pessoa:
    # o init sempre retorna nada, apenas inicia
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade
    # como n tem return, teremos -> None:
    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')

# função de iterar, que recebe uma sequencia de INT
def iterar(sequencia: Sequence[int]):
    return [x for x in sequencia]

# função iterar2 que recebe sequencia de INT a ser itereada
def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))