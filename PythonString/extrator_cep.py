endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re  # Regular Expression -- RegEx

# CEP padrao Brasil
## 5 dígitos + hífen (opcional) + 3 dígitos

# ele pode aparecer nenhuma ou uma vez [-]?
# Quantificadores e intervalos {}
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)  # Encontrou aquele padrao
if busca:
    cep = busca.group() # String que foi encontrado
    print(cep)