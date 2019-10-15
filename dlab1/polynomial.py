#!/usr/bin/env python
# -*- coding: utf-8 -*-
# polynomial.py


# grado
# Polynomial -> Integer
# produce el grado del polinomio, el resultado es un entero positivo mayor o igual a 0.
# debería ser un método de clase, ya que usa el atributo de la instancia.
def grado(p):
  return len(p.coeffs) - 1

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
    if gradoSelf > i: # a esta altura i sería igual a menorGrado, entonces si gradoSelf es mayor que el menor grado...
      # insertar en newCoeffs los que faltan de self, entre 0 y la diferencia de grado con other
      for j in range(diferenciaGrados): # si fueran iguales no habría ningún loop para hacer, porque el rango estaría vacío
        newCoeffs.insert(0, self.coeff(j))
    elif gradoOther > i:
      for j in range(diferenciaGrados): # si fueran iguales no habría ningún loop para hacer, porque el rango estaría vacío
        newCoeffs.insert(0, other.coeff(j))
    # En otro caso, son iguales, ya está listo.
    
    # faltaría filtrar los ceros adelante de la lista cuando se anula el término ppal.
    return Polynomial(newCoeffs)

  # __str__
  # Polynomial --> String
  # Produce una representación textual del polinomio en forma de cadena de caracteres.
  def __str__(self):
    return str(self.coeffs)

#Ejemplos:

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

# POLY_4 + POLY_5 = [3, 5, 1.02] + [-5, 1.2] = [3, 0, 2.04]
# POLY_5 + POLY_4 = [-5, 1.2] + [3, 5, 1.02] = [3, 0, 2.04]
# POLY_5 + POLY_6 = [-5, 1.2] + [5, 1.2] = [2.04]
# POLY_6 + POLY_5 = [5, 1.2] + [-5, 1.2] = [2.04]
# POLY_6 + POLY_7 = [5, 1.2] + [5, -1.2] = [10, 0]
# POLY_7 + POLY_6 = [5, -1.2] + [5, 1.2] = [10, 0]
# POLY_4 + POLY_8 = [0]
# POLY_8 + POLY_4 = [0]