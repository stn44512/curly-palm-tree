__author__ = 'oscarmolina'

import math

class taller():
    def __init__(self,profundidadbits,valmaximo,numa,numb,operacion):
        self.profbits=profundidadbits
        self.max=valmaximo
        self.num1=numa
        self.num2=numb
        self.signo=operacion


    def rangdin(self):
        self.rd = 6.02*self.profbits
        return self.rd

    def Vpdbfs(self):
        print(self.max)
        self.picodbfs = 20*math.log10(float(math.sqrt(self.max**2))/(2**self.profbits))
        return self.picodbfs

    def sumadbfs(self):
        self.vmax1=(10**(self.num1/20))*(2**self.profbits)
        self.vmax2=(10**(self.num2/20))*(2**self.profbits)
        if self.signo == 9:
            self.total = self.vmax1+self.vmax2
            self.totaldbfs=20*math.log10(float(self.total)/2**self.profbits)
            return self.totaldbfs
        elif self.signo == 0:
            self.total = self.vmax1-self.vmax2
            self.totaldbfs=20*math.log10(float(self.total)/2**self.profbits)
            return self.totaldbfs
