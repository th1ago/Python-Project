# Pytest
- Executar o comando *pytest* no terminal. No retorno vai teremos *teste\test_bytebank.py .* > A quantidade de ponto refere a quantidade de teste
- Outra alternativa é acrescentar *pytest -v*, de verbose. Receberemos um retorno mais detalhado
- Executando o teste selecionando alguns item *pytest -v -k {uma_palavra_teste}*

## markers
- Outra forma de executar o teste selecionando *pytest -v -m {palavra_definida}* no file *.ini*

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