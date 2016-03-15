class Secuencia:
    def verificarSecuencia(self,cadena):
        if cadena=="":
            return [0,0,0]
        elif "," in cadena:
            arreglo=cadena.split(",")
            arreglo=map(int, arreglo)

            maximo=arreglo[1]
            if int(arreglo[0]) > int(arreglo[1]):
                maximo=arreglo[0]


            return [len(arreglo), min(arreglo), int(maximo)]

        else:
            return [1,int(cadena), int(cadena)]