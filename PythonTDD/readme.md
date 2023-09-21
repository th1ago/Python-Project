# Pytest
- Executar o comando *pytest* no terminal. No retorno teremos *teste\test_bytebank.py .*, a quantidade de ponto refere a quantidade de teste
- Outra alternativa é acrescentar *pytest -v*, de verbose. Receberemos um retorno mais detalhado
- Executando o teste selecionando alguns item *pytest -v -k {uma_palavra_teste}*
- Para verificar a cobertuda instale o pytest-cov e execute o comando *pytest --cov*
- Explicando a linha do codigo que nao esta cobert *pytest --cov=codigo tests/ --cov-report term-missing*
- Gerando um report *pytest --cov=codigo tests/ --cov-report html* cria uma pasta htmlcov
- Para excluir teste, criar uma pasta *.coveragerc* informando as linha a serem excluida no teste
- Criando um relatorio *pytest --cov-report xml*

## Instalacao
```
pip install pytest==7.1.2
pip install pytest-cov==3.0.0
pip freeze > requeriments.txt
```

### Garantindo a cobertura
- E possível acrescentar a tag ```--cov=codigo tests/``` para especificar ao pytest-cov o diretório em que queremos rodar o escaneamento de cobertura de testes. 
- Para especificar outro tipo de relatório, que exibirá os termos faltantes para os 100% de cobertura.```pytest --cov=codigo tests/ --cov-report term-missing```
- Relatorioa mais visual ```pytest --cov=codigo tests/ --cov-report html```

## markers
- Outra forma de executar o teste selecionando *pytest -v -m {palavra_definida}* no arquivo *.ini*

### skip
```
@pytest.mark.skip(reason="não quero executar isso agora")
def test_aleatorio():
```
- Através do uso do marker skip podemos pular um teste, caso a execução dele não seja necessária naquele instante.

### skipif
```
import sys
@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requer Python na versão 3.10 ou superior")
def test_funcao():\
```
- Acima, o teste não é executado caso sys.version_info < (3, 10) seja verdadeiro, ou seja, caso a versão do Python esteja abaixo da versão 3.10.
- Através do uso do marker skipif podemos pular um teste caso ele se encaixe em determinada situação definida por uma condicional.

### xfail
```
@pytest.mark.xfail
def test_funcao():
```
- Através do uso do marker xfail especificamos que o teste deve retornar uma falha, em vez de passar.