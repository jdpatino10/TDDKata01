class Secuencia:
    def verificarSecuencia(self,cadena):
        if cadena=="":
            return [0,0,0,0]
        elif "," in cadena:
            arreglo=cadena.split(",")
            arreglo=map(int, arreglo)
            suma=0.0
            prome=0.0
            if len(arreglo)==2:
                suma= suma + arreglo[0]+ arreglo[1]
            prome=suma/2

            return [len(arreglo), min(arreglo), max(arreglo), prome]

        else:
            return [1,int(cadena), int(cadena), int(cadena)]