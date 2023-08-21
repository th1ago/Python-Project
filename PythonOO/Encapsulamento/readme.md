# __ (two underscores)
- O underline em um atributo ou metodo o torna privado
- Sera transformado em uma outra variavel esta acao se chama *name mangling*
```
__nome
_Programa__nome
```

# @property
- Sao importantes, pois quem depende da classa nao precisa mudar
- Quando criamos *getters* e *setters* todos os lugares que ja acessam a classe precisam mudar

#    @staticmethod
- Esse métodos que conseguimos chamar sem uma referência recebem o nome de estáticos, porque eles fazem parte da classe. 
- Fica inapropriado usar *property*, porque ele sempre precisa do *self*. A configuração correta será @staticmethod.
