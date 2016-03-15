class Secuencia:
    def verificarSecuencia(self,cadena):
        if cadena=="":
            return [0,0,0]
        elif "," in cadena:
            arreglo=cadena.split(",")
            arreglo=map(int, arreglo)
            return [len(arreglo), min(arreglo)]
        else:
            return [1,int(cadena), int(cadena)]