
## Python com OO

| Python OO | Done |
| ----------------------------------  | --- |
| Conhecendo a linguagem | [X] |
| ----------------------------------  | --- |
| Aprofundar na orientação a objetos  | [X] |
| ------------------------------  | --- |
| Trabalhar com formatos de dados | [] |
| ------------------------------  | --- |
| Fazer testes automatizados      | [] |


- Quando rodamos diretamente um arquivo no Python, ele internamente cria uma variável e a preenche. E através dessa variável podemos fazer uma consulta, pois se ela estiver preenchida, significa que o arquivo foi executado diretamente, mas se a variável não estiver preenchida, então significa que o arquivo só foi importado.
- Essa variável é a __name__, e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente. Vamos então fazer if para verificar se ela está preenchida ou não:

```
import random

def jogar():
    # código omitido

if (__name__ == "__main__"):
    jogar()
```