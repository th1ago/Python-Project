# Polimorfismo
- Conseguimos percorrer uma lista qualquer e, sendo elas do mesmo supertipo, no caso, de 
*Programa*, e com uma estrutura similar, com *nome* e *likes*, conseguimos usar o ```for``` independentemente do tipo que existe ali.

# Dunder Methods
- Dunder methods, como costumam chamar. Dunder vem de double underscore, isto é, "dois underlines". Um exemplo de método especial é o nosso __init__() que, ao ser definido, o Python sabe, por convenção, que ele é o inicializador de uma classe na criação de um objeto.
- Neste caso, com __init__(), é necessário termos em uma classe, mesmo que não seja obrigatório, um método especial capaz de representar um objeto textualmente. E chamado de __str__(), ou dunder str, ou ainda "str especial".
- Quando definimos esta função, não é possível simplesmente fazermos um print() nela, pois é esperado que se retorne um valor como string, que represente o objeto desejado. O trecho de código corresponde seria, portanto:

```
def __str__(self):
    return f'{self._nome} - {self.ano} - {self._likes} Likes'
```

- Há um método mágico - um dunder method - que, ao ser implementado, permite que a classe seja considerada um objeto iterável: o __getitem__(). Este método define algo que é iterável e, no caso, precisaremos receber um item para que este seja repassado à lista interna que estamos utilizando, isto é, programas.

# list
- E uma classe built-in, embutida no python pronta para uso


# Python Data Model
| Inicializacao  | __init__ |
| -------------  | -------- |
| Representacao  | __str__, __repr__ |
| -------------  | ----------------- |
| Container, seq | __contains__, __iter__, __len__, __getitem__ |
| -------------  | -------------------------------------------- |
| Numericos      | __add__, __sub__, __mul__, __mod__ |


| Inicializacao  | obj = Novo() |
| -------------  | -------- |
| Representacao  | print(obj), str(obj), repr(obj) |
| -------------  | ----------------- |
| Container, seq | len(obj), item in obj, for i in obj, obj[2:3] |
| -------------  | -------------------------------------------- |
| Numericos      | obj + outro_obj, obj * obj |
