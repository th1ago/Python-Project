class busca_cep:
    """trabalhndo com cep"""
    def __init__(self, cep):
        self.cep = str(cep)
        if self.cep_valida(cep):
            self.cep = cep
        else:
            raise ValueError("Cep invalido")

    def __str__(self):
        return self.format_cep()

    def cep_valida(self, cep):
        """valida cep"""
        if len(cep) == 8:
            return True
        else:
            return False
    
    def format_cep(self):
        """formata cep"""
        return f"{self.cep[:5]}-{self.cep[5:]}"