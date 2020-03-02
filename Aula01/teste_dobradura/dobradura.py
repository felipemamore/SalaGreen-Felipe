class Dobradura:
   def get_dobrar(self, numero_dobradura):
        self.numero_dobradura = 0
        self.dobradura = []

        if numero_dobradura < 0:
            return f'Digite um numero positivo'
        else:
            if type(numero_dobradura) != int:
                return f'Digite apenas numeros!'

            else:
                for i in range(self.numero_dobradura):
                    self.dobras = 2 ** i
                    self.dobradura.append(self.dobras)
            return f'Qtde de dobraduras no papel: {self.dobradura}'

if __name__== '__main__':
    dobras=Dobradura()























