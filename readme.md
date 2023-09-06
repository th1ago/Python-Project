# Python com OO
- Quando rodamos diretamente um arquivo no Python, ele internamente cria uma variável e a preenche. E através dessa variável podemos fazer uma consulta, pois se ela estiver preenchida, significa que o arquivo foi executado diretamente, mas se a variável não estiver preenchida, então significa que o arquivo só foi importado.
- Essa variável é a *__name__*, e ela é preenchida com o valor *__main__* caso o arquivo seja executado diretamente. Vamos então fazer if para verificar se ela está preenchida ou não:

```
import random

def jogar():
    # código omitido

if (__name__ == "__main__"):
    jogar()
```

# Method
### title() 
- Transforma a primeira letra do caractere em letra maiúsculo

## List
```
Para todo magico na lista de magicos, exiba o nome do magico 
```
### insert() 
- Insere um elemento na lista, na posicao desejada ```[index, x]```
### append()
- Concatena no final da lista
### extend()
- Extende a lista 
### del()
- Remove elemento da lista
### pop()
- Remove um item da lista, mas permite que voce trabalhe com ela
### remove()
- Remove o primeiro item da lista de acordo com o valor

# 📫 Collection
- `Funcao_1:` quando informar o param *args == tupla 
- `Funcao_2:` quando informar o param **kwargs == dicionario

### Python Data Structure

| Attempt    | Indexing | Ordered | Murable | Duplicate |
| :---:      | :---:    | :---:   | :---:   | :---:     |
| List [ ]   | OK       | OK      | OK      | OK        |
| Tuple ( )  | OK       | OK      | X       | OK        |
| Set  { }   | X        | X       | X       | X         |
| Dict {k:v} | X        | OK      | OK      | X         |


### Regex
| Caracteres |                            Descricao                     |       Exemplos      |
| :---:      | :------------------------------------------------------: | :-----------------: |
| []         | Define um range ou um grupo de caracteres                | [0-9]; [a-z]; [abc] |
| *          | Marca nenhuma, uma ou mais ocorrências                   | sol*                |
| {}         | Quantidade de repetições de uma ocorrência definida      | [abc]{5}            |
| \d         | Qualquer número de 0 até 9                               | \d{3,4}             |
| \w         | Qualquer número de a té 9 letra de a até z ou _          | \w{10}              |
| |          | Um ou outro                                              | @$                  |
| ()         | Captura e agrupa                                         | (\w(4))             |