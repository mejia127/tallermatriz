import matriz

def main():
    M = False
    while M!=True:

            mi_menu = matriz.Menu()
            a=mi_menu.loop()

            if a == 1:
                matrizA = matriz.Matriz()
                matrizA.crearMatrizA()
                a=matrizA.llenarmatrizA()
                matrizA.imprime_matriz()
                matrizA.matriz_det(a)
            if a == 2:
                matrizA = matriz.Matriz()
                matrizA.crearMatrizA()
                a=matrizA.llenarmatrizA()
                matrizA.imprime_matriz()
                matrizA.matriz_inversa(a)
            if a == 3:
                matrizA = matriz.Matriz()
                matrizA.crearMatrizA()
                matrizA.llenarmatrizA()
                matrizA.imprime_matriz()
                matrizA.transpuesta()
            if a == 4:
                matrizA = matriz.Matriz()
                matrizA.crearMatrizA()
                matrizA.llenarmatrizA()
                matrizA.imprime_matriz()
                matrizA.matriz_numero()
            if a == 5:
                matrizA = matriz.Matriz()
                matrizA.crearMatrizA()
                matrizA.llenarmatrizA()
                matrizA.imprime_matriz()
                matrizA.matriz_elevada()

            if a == 6:
                matrizA = matriz.Matriz()
                matrizA.matrizSimetrica()

            if a == 7:
                matrizA = matriz.Matriz()
                matrizA.matrizidentica()

            if a == 8:
                matrizA = matriz.Matriz()
                matrizA.crearMatrizA()
                a=matrizA.llenarmatrizA()
                matrizA.imprime_matriz()
                columnasA = matrizA.getColumnas()
                filasA = matrizA.getFilas()

                matrizB = matriz.Matriz()
                matrizB.crearMatrizA()
                b = matrizB.llenarmatrizA()
                matrizB.imprime_matrizC()

                columnasB = matrizB.getColumnas()
                filasB = matrizB.getFilas()
                matrizA.multiplicacionmatriz(filasA,columnasB,filasB,columnasA,a,b)

            if a == 9:
                matrizA = matriz.Matriz()
                matrizA.crearMatrizA()
                a = matrizA.llenarmatrizA()
                matrizA.imprime_matriz()
                columnasA = matrizA.getColumnas()
                filasA = matrizA.getFilas()

                matrizB = matriz.Matriz()
                matrizB.crearMatrizA()
                b = matrizB.llenarmatrizA()
                matrizB.imprime_matrizC()

                columnasB = matrizB.getColumnas()
                filasB = matrizB.getFilas()
                matrizA.sumamatriz(filasA, columnasB, filasB, columnasA, a, b)

            if a == 10:
                matrizA = matriz.Matriz()
                matrizA.crearMatrizA()
                a = matrizA.llenarmatrizA()
                matrizA.imprime_matriz()
                columnasA = matrizA.getColumnas()
                filasA = matrizA.getFilas()

                matrizB = matriz.Matriz()
                matrizB.crearMatrizA()
                b = matrizB.llenarmatrizA()
                matrizB.imprime_matrizC()

                columnasB = matrizB.getColumnas()
                filasB = matrizB.getFilas()
                matrizA.restamatriz(filasA, columnasB, filasB, columnasA, a, b)

            if a == 11:
                print "Hasta Luego "
                M = True
            else:
                b = raw_input("Presione enter para volver al menu")
                M = False












if __name__ == '__main__':
    main()
