class Secuencia:
    def verificarSecuencia(self,cadena):
        if cadena=="":
            return [0,0,0,0]
        elif "," in cadena:
            arreglo=cadena.split(",")
            arreglo=map(int, arreglo)
            suma=0.0
            prome=0.0

            for i in arreglo:
                suma=suma+i

            prome=suma/len(arreglo)

            return [len(arreglo), min(arreglo), max(arreglo), prome]

        else:
            return [1,int(cadena), int(cadena), int(cadena)]