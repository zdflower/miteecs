#!/usr/bin/env python
# -*- coding: utf-8 -*-
# polynomial.py

################################### Auxiliares ############################################
# grado
# Polynomial -> Integer
# produce el grado del polinomio, el resultado es un entero positivo mayor o igual a 0.
# debería ser un método de clase, ya que usa el atributo de la instancia.
def grado(p):
  return len(p.coeffs) - 1

# agregarLosCoefQueFaltan(desde, hasta, pol, newCoeffs)
# Integer, Integer, Polynomial, List of Float -> 
# Modifica la lista de float. Sólo debería agregar adelante los coeficientes de pol entre desde y hasta y no quitar nada.
def agregarLosCoefQueFaltan(desde, hasta, pol, newCoeffs):
  for j in range(desde, hasta): # si fueran iguales no habría ningún loop para hacer, porque el rango estaría vacío
        newCoeffs.insert(0, pol.coeff(j))  


# copiarLosQueFaltan
# Integer, Integer, List of Float, List of Float -> 
# Modifica la segunda lista. 
# Agrega los elementos de xs desde desde hasta hasta - 1 en ys.
# Se supone que desde y hasta están en el rango de xs.
# Esta función es similar a agregarLosCoefQueFaltan. Tal vez se podría reescribir el código que usa ambas para que quede una sola.
def copiarLosQueFaltan(desde, hasta, xs, ys):
  for i in range(desde, hasta):
    ys.append(xs[i]) 


# filtrarPrimerosCoefsNulos
# List of Float -> List of Float
# Produce una nueva lista que contiene los mismos elementos que el input salvo los primeros 0 consecutivos desde el índice 0 hasta el primer elemento que no sea 0 excluído.
# Respeta el mismo orden que tenían en el input los elementos restantes.
def filtrarPrimerosCoefsNulos(cs):
  # sería una cosa así como buscar el primer no 0 desde la izquierda y a partir de ahí copiar todo lo que quede de la lista.
  # acá copiar no es un problema porque el tipo de dato del elemento de la lista es primitivo, es Float.
  # ¿Cómo se compara la complejidad entre crear una nueva lista o remover los primeros elementos iguales a 0, cuando la lista es grande?

  # tiene que ignorar los primeros ceros, cuando encuentra algo que no es cero sale del loop e incorpora todo el resto a la nueva lista.
  nuevaCs = []
  i = 0 # empieza de la izquierda
  tope = len(cs)
  while (i < tope and cs[i] == 0):
    i += 1

  # si i es menor que tope, entonces es que encontró un no cero. En este caso hay que seguir desde i hasta tope-1 copiando los elementos en la nueva lista
  if i < tope:
    copiarLosQueFaltan(i, tope, cs, nuevaCs) # esto podría ser similar a agregarLosCoeffsQueFaltan, aunque tienen distinto input y distinto acceso a los coeficientes...
                                             # tal vez convendría reescribir alguna de estas funciones para que quede una sola que sirva para los dos casos.
  else:
    # si i es igual al tope, todos eran cero. en este caso la nueva lista va a ser [0]
    nuevaCs.append(0.0)
  return nuevaCs

# Integer -> List of Integer
# Produce una lista con tantos ceros como se indica en el input. El input debe ser entero mayor que 0.
# borrador
def inicializarLista(n):
  res = []
  for i in range(n):
    res.append(0)
  return res

############################################################################################


# Polynomial is Polynomial([Float])
# Representa un polinomio como una lista de Float que son los coeficientes, comenzando por el término de mayor grado.
class Polynomial:

  # Polynomial, List of Float --> Polynomial
  # Construye una nueva instancia de Polynomial
  # El elemento de la lista con el mayor índice será el coeficiente correspondiente al término constante.
  # La lista puede comenzar con 0 (para contemplar el caso de una suma de polinomios en que se anule el coeficiente principal y se baje el grado en el resultado respecto de los sumandos)
  # Se usará una función auxiliar para filtrarlos (¿hay otra opción mejor?).
  def __init__(self, coefficients):
    self.coeffs = coefficients # ojo con las listas, las referencias, los punteros, los alias, las mutaciones...

  # coeff
  # Polynomial, Integer --> Float
  # Produce el coeficiente del término de grado i (donde i es un entero positivo)
  # Se supone que i está entre 0 y el grado del polinomio inclusive.
  # Si se supone que el coeficiente con índice 0 en self.coeffs no es 0, entonces el grado del polinomio es longitud de self.coeffs - 1
  # El índice j del coeficiente de grado i va a ser: j = índice más alto de la lista - i, 
  # es decir, longitud de la lista - 1 - i
  # (puesto que los índices ascienden y los grados descienden).
  # Si i es 0, el índice de ese coeficiente va a ser el más alto de la lista.
  def coeff(self, i):
    indice = len(self.coeffs) - 1 - i # tal vez deba ponerlo en una función auxiliar si es que quizá lo vuelva a necesitar en la suma...
    return self.coeffs[indice]

  # add
  # Polynomial, Polynomial --> Polynomial
  # Produces a new polynomial that is the result of the sum of the two polinomials
  def add(self, other):
    # la suma de polinomios se hace sumándo los términos de igual grado.
    # habría que ver si self u other es el de mayor grado...
    # podría ser necesaria la recursión. Pensar los casos base.
    # idea: ir de atrás hacia adelante, ir corriendo el índice y de alguna manera poder chequear que 
    # para uno o para ambos ya no hay más que ver.
    # voy a dejar la recursión por ahora, tal vez la piense más adelante.
    # borrador
    newCoeffs = [] # la lista de coeficientes del resultado de la suma
    # debe haber una mejor forma...
    # averiguás el grado de self y el grado de other
    # dos loops, uno que suma 2 polinomios de igual grado, otro que agrega los coeficientes más altos que quedaron.
    # desde 0 hasta el grado del menor de los dos vas sumando self.coeff(i) y other.coeff(i) y agregando por delante a newCoeffs
    # y desde el grado del menor + 1 hasta el grado del mayor agregás por delante el self/other.coeff(i) según corresponda.
    gradoSelf = grado(self)
    gradoOther = grado(other)
    menorGrado = min(gradoSelf, gradoOther)
    diferenciaGrados = abs(gradoSelf - gradoOther)

    # acá sería como sumar dos polinomios de igual grado
    for i in range(menorGrado + 1):
      newCoeffs.insert(0, self.coeff(i) + other.coeff(i)) # insertar adelante

    # acá puede pasar que, si ambos son de igual grado, ya está. En ese caso puede pasar que el término principal sea nulo o no.
    # si son de distinto grado, entonces hay uno que todavía hay que recorrer e incorporar los coeficientes al resultado.
    # ¿cómo sabés cuál es, sin repetir cosas? puedo chequear la longitud (otra vez) de los polinomios ...

    # si el grado de self es mayor que el grado de other entonces ...
    # pará, también hay que ver que i esté dentro de los posibles índices que le queden al polinomio
    # qué pasa si los dos eran del mismo grado? nada, solo hacemos algo más si se da el otro caso.
    if gradoSelf > menorGrado: # a esta altura i sería igual a menorGrado, entonces si gradoSelf es mayor que el menor grado...
    # Me parece más claro usar menorGrado que i.
      # insertar en newCoeffs los que faltan de self, entre 0 y la diferencia de grado con other
      # ESTÁ MAL EL RANGO DE J, J TIENE QUE IR DE I+1 HASTA EL GRADO DE SELF INCLUIDO, NO SÉ PARA QUÉ QUERÍA LA DIFERENCIA DE GRADOS...
      # TAL VEZ PODÍA SERVIR SI NO USABA EL MÉTODO COEFF y accedía directamente a los elementos de la lista por sus índices...

#      for j in range(i+1, gradoSelf+1): # si fueran iguales no habría ningún loop para hacer, porque el rango estaría vacío
#        newCoeffs.insert(0, self.coeff(j))
      agregarLosCoefQueFaltan(menorGrado+1, gradoSelf+1, self, newCoeffs)

    elif gradoOther > menorGrado:
      # MISMA CORRECCIÓN ACÁ:
      # podría usar una función auxiliar ya que repito estos loops, pero qué inputs y qué outputs se necesitarían, y qué pasa con la mutabilidad de las listas y la ausencia o presencia de efectos secundarios...
      
#      for j in range(i+1, gradoOther+1): # si fueran iguales no habría ningún loop para hacer, porque el rango estaría vacío
#        newCoeffs.insert(0, other.coeff(j))
      agregarLosCoefQueFaltan(menorGrado+1, gradoOther+1, other, newCoeffs)

    # En otro caso, son iguales, ya está listo.
    
    # faltaría filtrar los ceros adelante de la lista cuando se anula el término ppal.
    return Polynomial(filtrarPrimerosCoefsNulos(newCoeffs))

  # __add__
  # Polynomial, Polynomial -> Polynomial
  # Suma dos polinomios.
  def __add__(self, other):
    return self.add(other)

  # mul(self,other)
  # Polynomial, Polynomial -> Polynomial
  # Returns a new Polynomial representing the product of Polynomials self and other
  def mul(self, other):
    
    # hagamos el siguiente paso: multiplicar las variables
    # para cada término de self, multiplicar por uno de other
    # sólo eso, por ejemplo self= [1,1,1] y other [1,0,0]
    # supongamos que resultado = []
    # multiplico 1x² * 1x². cómo sabría dónde va el resultado, con qué exponente queda, etc.?
    # el resultado de multiplicar los coeficientes es 1, y correspondería al término de grado 4, ya que los coeficientes corresponden al grado 2.
    # ahora multiplico 1x * 1x², el coeficiente queda 1 y la variable x³, puesto que ...
    # ahora multiplico 1x⁰ * 1x², queda 1x²
    # ahora vendría otra vuelta donde multiplicaría cada item de self por el siguiente item de other
    # y luego la vuelta que multiplica por el que queda en other.

    # unos índices iterarían por other, a partir de los índices obtendríamos a qué término pertenece, qué exponente tiene la variable
    # y también accedemos al coeficiente.
    # una vez que sabemos los exponentes, los multiplicamos y sabemos en qué lugar debería ir el resultado del producto de los coeficientes.
    # ¿se puede saber el máximo grado posible del producto de dos polinomios? supongo que sí.
    # podría inicializar con ceros el resultado, tantos como de el cálculo del grado del producto a realizar.
    # por ejemplo si multiplicamos dos polinomios de grado 0, el grado del producto será 0
    # si multiplicamos un polinomio de grado 1 por un polinomio de grado 0, el grado puede ser 1 o 0 (si se anula)
    # grado 1 por grado 1, da grado 2
    # En un apunte de álgebra 1 dice que el grado del producto (no nulo) de dos polinomios es igual a la suma de los grados de esos polinomios.
    # Entonces, un polinomio de grado 2 * polinomio de grado 2, da un polinomio de grado 3 y así.
    # Idea, inicializo una lista resultado con tantos ceros como la suma de los grados de self y other.
    # luego voy multiplicando todo self por el coeficiente ppal de other, por ejemplo el x² * x² va en resultado[gradoresultado-2+2-1], proque el de mayor grado va adelante, es una cuenta así o parecida, lo importante es que tiene que ubicar los de mayor grado adelante.
    gSelf = grado(self)
    gOther = grado(other)
    gradoResultado = gSelf + gOther # salvo que alguno sea nulo, pero eso me parece que se va a arreglar al filtrar los ceros...
    # inicializo resultado
    resultadoCoeffs = inicializarLista(gradoResultado + 1) # la cantidad de términos es una más que el número del grado.
    # print "resultadoCoeffs: " + str(resultadoCoeffs)
    #multiplico una vuelta sola, para probar
    i = gSelf
    j = gOther
    while j >= 0:
      ## tendría que sumarle a lo que hay en resultadoCoeffs[gradoResultado - (i+j)] en vez de directamente asignar
      while i >= 0:
        #print self.coeff(i)
        #print "por"
        #print other.coeff(j)
        #print "="
        #print self.coeff(i) * other.coeff(j)
        #print "va en el término de grado: "
        #print "{} + {} = {}".format(i, j, i + j)
        #print "i+j={}".format(i + j)
        resultadoCoeffs[gradoResultado - (i + j)] += self.coeff(i) * other.coeff(j) # sumo a lo que hay ahí.
        #print str(resultadoCoeffs[i+j])
        i -= 1
      j -= 1
      i = gSelf # tengo que resetear i para que vuelva a recorrer esos elementos para cada j. ¡EXPLICARLO!

    #print "resultadoCoeffs: " + str(resultadoCoeffs)
    return Polynomial(filtrarPrimerosCoefsNulos(resultadoCoeffs))

  # __mul__
  # Polynomial, Polynomial -> Polynomial
  # produces a new polynomial that represents the product of self and other.
  def __mul__(self, other):
    return self.mul(other)

  # val(self,v)
  # Polynomial, Float -> Float
  # Returns the numerical result of evaluating the polynomial when x equals v.
  def val(self, v):
    res = 0
    exp = grado(self)
    while (exp >= 0):
      res += self.coeff(exp) * (v ** exp)
      exp -= 1

    return res

  
  # __str__
  # Polynomial --> String
  # Produce una representación textual del polinomio en forma de cadena de caracteres.
  def __str__(self):
    res = ""
    i = grado(self)
    while i > 0:
      res += "{0:.3f} z**{1:d} + ".format(self.coeff(i), i) # el "0" y el "1" delante de ":" se refieren al primer y segundo argumentos de format.
      i -= 1

    res += "{:.3f}".format(self.coeff(i)) # se puede omitir el número de argumento pero tenés que poner los dos puntos...
    return res

#Ejemplos:
POLY_0 = Polynomial([0]) # polinomio nulo
POLY_1 = Polynomial([1]) # polinomio constante 1, grado 0
POLY_2 = Polynomial([1, -0.001, 0, 0, 2]) # 1z⁴ - 0.001z³ + 2, grado 4
POLY_3 = Polynomial([0, 1, -0.001, 0, 0, 2])  # no tiene sentido darle coeficiente 0 al primer término, debería ser equivalente al anterior
# POLY_3 no tiene grado 5, ya que el coeficiente del término de grado 5 es 0, entonces es de grado 4 aunque (longitud - 1) = 5
# Habría que exigir que los primeros términos no puedan tener coeficiente 0, o habría que tener una forma de determinar el grado que chequee que los primeros elementos de la lista no sean todos 0. 
POLY_4 = Polynomial([3, 5, 1.02])
POLY_5 = Polynomial([-5, 1.2])
POLY_6 = Polynomial([5, 1.2])
POLY_7 = Polynomial([5, -1.2])
POLY_8 = Polynomial([-3, -5, -1.02])
POLY_9 = Polynomial([3.1, -50.07, 4, -0.02])
POLY_10 = Polynomial([-3.1, 50.07, 14.09, -1.02])
POLY_11 = Polynomial([11])
print "########## Ejemplos de Polynomial ##########"
print POLY_1
print POLY_2
print POLY_3
print POLY_4
print POLY_5

print "########## Ejemplos de coeff(self, i) #########"

print POLY_1.coeff(0) 
assert POLY_1.coeff(0) == 1

print POLY_2.coeff(0)
assert POLY_2.coeff(0) == 2

print POLY_2.coeff(1)
assert POLY_2.coeff(1) == 0

print POLY_2.coeff(2)
assert POLY_2.coeff(2) == 0

print POLY_2.coeff(3)
assert POLY_2.coeff(3) == -0.001

print POLY_2.coeff(4)
assert POLY_2.coeff(4) == 1

print "########## Ejemplos de add(self, other) ##########"

# POLY_1 + POLY_1 = [1] + [1] = [2]
print "POLY_1 + POLY_1 = [2]"
print "{p1} + {p1} = [2]".format(p1=POLY_1)
# assert POLY_1.add(POLY_1) == [2] # esto siempre va a dar mal, ahora me doy cta.
# porque de un lado tenés una instancia de Polynomial y del otro una lista. ayayayayayayay
# assert POLY_1.add(POLY_1) == Polynomial([2]) # ¿compara objetos o propiedades? dos objetos distintos como estos porque tienen su propio lugar en la memoria, supongo, no van a ser iguales nunca, aunque sus propiedades sí puedan serlo...
# podría comparar la cadena que resulta de convertir cada uno a str.
print "POLY_1.add(POLY_1): {}".format(POLY_1.add(POLY_1))
print "Polynomial([2]): {}".format(Polynomial([2]))
assert str(POLY_1.add(POLY_1)) == str(Polynomial([2]))

# Polynomial, Polynomial, Polynomial -> 
def testPolyAdd(p1, p2, res):
  suma = p1.add(p2)
  print "{} + {} = {}".format(p1, p2, suma)
  print "suma: " + str(suma)
  print "res: " + str(res)
  assert str(suma) == str(res) # acá puede haber problema con la comparación de Float y el redondeo o recorte.


testPolyAdd(POLY_1, POLY_1, Polynomial([2]))
testPolyAdd(POLY_4, POLY_5, Polynomial([3, 5 - 5, 1.2 + 1.02]))
#testPolyAdd(POLY_4, POLY_5, Polynomial([3, 0, 2.22])) # acá me da error porque la suma del término cte. da 2.219999999999998 y yo lo comparo con 2.22, tal vez debería usar redondeo a 3 cifras significativas o algo así.
#testPolyAdd(POLY_5, POLY_4, Polynomial([3, 0, 2.22]))
testPolyAdd(POLY_5, POLY_4, Polynomial([3, -5 + 5, 1.02 + 1.2]))

# POLY_4 + POLY_5 = [3, 5, 1.02] + [-5, 1.2] = [3, 0, 2.22]
# POLY_5 + POLY_4 = [-5, 1.2] + [3, 5, 1.02] = [3, 0, 2.22]

testPolyAdd(POLY_5, POLY_6, Polynomial([1.2 + 1.2])) # ahora que incorporé el filtro de ceros iniciales esto tiene que dar bien
#testPolyAdd(POLY_5, POLY_6, Polynomial([-5 + 5, 1.2 + 1.2])) # todavía no va a dar como debe ser porque acá va a quedar un 0 adelante, faltaría una función que lo filtre o en la suma chequear antes de crear el polinomio si los primeros elementos consecutivos de la lista son 0. Habría que remover todos los ceros consecutivos desde el inicio, SALVO que la lista tuviera un único elemento y fuera 0, ese sí hay que dejarlo.
# POLY_5 + POLY_6 = [-5, 1.2] + [5, 1.2] = [2.4]
# POLY_6 + POLY_5 = [5, 1.2] + [-5, 1.2] = [2.4]
# POLY_6 + POLY_7 = [5, 1.2] + [5, -1.2] = [10, 0]
# POLY_7 + POLY_6 = [5, -1.2] + [5, 1.2] = [10, 0]

testPolyAdd(POLY_4, POLY_8, Polynomial([0.0]))
#testPolyAdd(POLY_4, POLY_8, Polynomial([3 - 3, 5 - 5, 1.02 - 1.02])) # mismo comentario que antes respecto de los primeros ceros salvo el último
# POLY_4 + POLY_8 = [0]
# POLY_8 + POLY_4 = [0]

# testear un caso en que se anulen los primeros 2 coeficientes pero no el o los últimos.
#POLY_9 = Polynomial([3.1, -50.07, 4, -0.02])
#POLY_10 = Polynomial([-3.1, 50.07, 14.09, -1.02])
#testPolyAdd(POLY_9, POLY_10, Polynomial([3.1 - 3.1, -50.07 + 50.07 , 4 + 14.09, -0.02 - 1.02]))
testPolyAdd(POLY_9, POLY_10, Polynomial([4 + 14.09, -0.02 - 1.02]))

# test copiarlosquefaltan
print "########## TEST COPIAR LOS QUE FALTAN #############"
L1 = [25, 3, 8, 4.000009102]
L2 = [1]

print "L2: " + str(L2)
copiarLosQueFaltan(2, 4, L1, L2) # tendría que quedar como [1, 8, 4.000009102]
print "L2 con los agregados: " + str(L2)
print [1, 8, 4.000009102]


# List Of Float, List Of Float -> 
def testFiltrarCerosIniciales(cs, res):
  print "#### TEST FILTRAR CEROS INICIALES ####"
  filtrado = filtrarPrimerosCoefsNulos(cs)
  print "original: " + str(cs)
  print "esperado: " + str(res)
  print "filtrado: " + str(filtrado)
  assert str(filtrado) == str(res)

testFiltrarCerosIniciales(POLY_4.add(POLY_8).coeffs, [0.0])

testFiltrarCerosIniciales(POLY_5.add(POLY_6).coeffs, [2.4])

testFiltrarCerosIniciales(POLY_9.add(POLY_10).coeffs, [18.09, -1.04])

testFiltrarCerosIniciales(POLY_6.add(POLY_7).coeffs, [10, -1.2 + 1.2])

# testear un caso en que no haya que suprimir ningún cero adelante
testFiltrarCerosIniciales(POLY_4.add(POLY_4).coeffs, [6, 10, 1.02 + 1.02])

print "#### Test + ####"
print POLY_1 + POLY_1
print POLY_1.add(POLY_1)
assert str(POLY_1 + POLY_1) == str(POLY_1.add(POLY_1))

print "#### MULTIPLICACIÓN ####"
# ejemplo:
# multiplicación de dos polinomios constantes.
assert POLY_1.mul(POLY_1).coeffs == [POLY_1.coeff(0) * POLY_1.coeff(0)] 
print "Multiplicación de dos polinomios constantes OK."

# multiplicación de un polinomio de cualquier grado por el polinomio constante 0.
assert POLY_2.mul(POLY_0).coeffs == [0] 
print "Multiplicación de un polinomio de cualquier grado por el polinomio constante 0 OK."

# multiplicación de un polinomio de cualquier grado por el polinomio constante 1.
assert POLY_9.mul(POLY_1).coeffs == POLY_9.coeffs 
print "Multiplicación de un polinomio de cualquier grado por el polinomio constante 1 OK."

# multiplicación de un polinomio lineal por uno constante.
assert POLY_6.mul(POLY_11).coeffs == [5 * 11, 1.2 * 11] == [POLY_6.coeff(1) * POLY_11.coeff(0), POLY_6.coeff(0) * POLY_11.coeff(0)] 

POLY_12 = Polynomial([1, 0]) # x
POLY_13 = Polynomial([1, 1]) # x + 1
POLY_14 = Polynomial([1, 0, 0]) # x²
POLY_15 = Polynomial([1, 0, 1]) # x² + 1
POLY_16 = Polynomial([1, 1, 1]) # x² + x + 1

# multiplicación de dos polinomios lineales
# x * x = x²
assert POLY_12.mul(POLY_12).coeffs == [1, 0, 0]

# multiplicación de dos polinomios lineales, otro:
# (x + 1) * (x + 1) = x² + 2x + 1
# multiplicación de un polinomio cuadrático por uno constante
# multiplicación de un polinomio cuadrático por uno lineal
# multiplicación de dos polinomios cuadráticos.
# x² * x² = x⁴
# (x² + 0x + 1)² 
# etc.


# print "test inicializarLista con ceros"
# print str(inicializarLista(2))
# print str(inicializarLista(10))


print "Test mul"
print Polynomial([1,1,1]).mul(Polynomial([1,1,1]))
print Polynomial([1,1,1]) * Polynomial([1,1,1])

print "Test val"
assert POLY_0.val(-0.26) == 0
assert POLY_2.val(1) == 1 - 0.001 + 2 == POLY_2.coeff(4) * (1 ** 4) + POLY_2.coeff(3) * (1 ** 3) + POLY_2.coeff(2) * (1 ** 2) + POLY_2.coeff(1) * (1 ** 1) + POLY_2.coeff(0) * (1 ** 0)

print POLY_2.val(-3.01) 
print POLY_2.coeff(4) * ((-3.01) ** 4) + POLY_2.coeff(3) * ((-3.01) ** 3) + POLY_2.coeff(2) * ((-3.01) ** 2) + POLY_2.coeff(1) * ((-3.01) ** 1) + POLY_2.coeff(0) * ((-3.01) ** 0)
                        #^--tengo que poner el negativo entre paréntesis si no le cambia el signo al resultado. No sé si es un problema de la exponenciación o de qué parte de python.
assert POLY_2.val(-3.01) == POLY_2.coeff(4) * ((-3.01) ** 4) + POLY_2.coeff(3) * ((-3.01) ** 3) + POLY_2.coeff(2) * ((-3.01) ** 2) + POLY_2.coeff(1) * ((-3.01) ** 1) + POLY_2.coeff(0) * ((-3.01) ** 0)