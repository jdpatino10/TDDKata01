class Secuencia:
    def verificarSecuencia(self,cadena):
        if cadena=="":
            return [0,0]
        elif "," in cadena:
            arreglo=cadena.split(",")
            minimo=arreglo[1]
            if int(arreglo[0]) < int(arreglo[1]):
                minimo=arreglo[0]
            return [len(arreglo), int(minimo)]
        else:
            return [1,int(cadena)]