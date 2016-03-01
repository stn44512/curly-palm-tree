__author__ = 'oscarmolina'

from rangodinamico import taller

def main():
    print('1.Hallar profundidad en bits 2.Hallar Valor Pico dBfs 3. Sumar dBfs')
    opcion=input()
    if opcion==1:
        Numbits = input('digite la profundidad en bits')
        rango_dinamico=taller(Numbits,0,0,0,0)
        rd=rango_dinamico.rangdin()
        print('el rango dinamico es:'+str(rd))
    elif opcion==2:
        Vpico = input('digite el valor pico maximo')
        Numbits = input('digite la profundidad en bits')
        vp=taller(Numbits,Vpico,0,0,0)
        print('el valor pico en dbfs es:'+str(vp.Vpdbfs()))
    elif opcion==3:
        dbfs1=input('digite el primer valor')
        dbfs2=input('digite el segundo valor')
        signo=input('desea 9. sumar o 0.restar')
        solve=taller(0,0,dbfs1,dbfs2,signo)
        print(solve.sumadbfs())

if __name__=='__main__':
    main()