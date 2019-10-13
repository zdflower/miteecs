#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (x,y)
# V2 is a (Float, Float)
# interp. a 2D vector
# attributes: coordinate x and coordinate y
# methods: getters, vector sum, vector scalar multiplication, convert to string.

class V2:
  
  # V2, Float, Float --> V2 ;; ¿Está bien decir que devuelve un V2?
  # constructor de instancias
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # V2 --> Float
  # produce la coordenada X del vector
  def getX(self):
    return self.x

  # V2 --> Float
  # produce la coordenada Y del vector
  def getY(self):
    return self.y

  ## ¿Por qué necesito __add__ y también add? ¿Para poder usar tanto el operador + (operand overloading), como el método add para sumar los vectores?
    
  # add
  # V2, V2 --> V2
  # Add two V2 and produce a new V2
  def add(self, other):
    x = self.getX() + other.getX()
    y = self.getY() + other.getY()
    return V2(x, y)

  # __add__
  # V2, V2 --> V2
  # Add two V2 and produce a new V2
  def __add__(self, other):
    return  self.add(other)

  #mul

  #__mul__

  # V2 --> String
  def __str__(self):
    return "X: {v.x}, Y: {v.y}".format(v=self)

####################################################################
# Ejemplos / tests

# Number, Number --> ---
def testV2_constructor(x,y):
  print "TESTING V2 CONSTRUCTOR"
  newVector = V2(x, y)
  print "x: " + str(x)
  print "newVector.x is " + str(newVector.x)
  try:
    assert newVector.x == x
  except:
    print "Wrong!"
  else:
    print "OK!"

  print "y: " + str(y)
  print "newVector.y is " + str(newVector.y)
  try:
    assert newVector.y == y
  except:
    print "Wrong!"
  else:
    print "OK!"

testV2_constructor(2, 1)
testV2_constructor(1.2, 230.3333331)
testV2_constructor(-99, 0)
#testV2_constructor("hello", "goodbye") #esto tal vez funcione, pero estaría mal porque en la definición del tipo se indicó que x e y son Float.
# creo que entonces no debería hacer ese test.

# V2, String --> ---
def testV2_str(v, string):
  print "TESTING V2 __str__"
  print str(v) 
  print string
  try:
    assert str(v) == string
  except:
    print "Wrong!"
  else:
    print "OK!"

VECTOR_0 = V2(2.1, 3.3)
VECTOR_1 = V2(1.2, 230.3333331)
VECTOR_2 = V2(-99, 0)

testV2_str(VECTOR_0, "X: 2.1, Y: 3.3")
testV2_str(VECTOR_1, "X: 1.2, Y: 230.3333331")
testV2_str(VECTOR_2, "X: -99, Y: 0")

# V2, Float --> String
# test getX
def testV2GetX(v, x):
  print "TESTING V2 GETX"
  print v
  print "x: " + str(x)
  try:
    assert x == v.getX()
  except:
    return "Wrong!"
  else:
    return "OK!"

print testV2GetX(VECTOR_0, 2.1)
print testV2GetX(VECTOR_1, 2.1) # este tiene que dar error
print testV2GetX(VECTOR_1, 1.2)
print testV2GetX(VECTOR_2, -99)

# V2, Float --> String
# test getY
def testV2GetY(v, y):
  print "TESTING V2 GETY"
  print v
  print "y: " + str(y)
  try:
    assert y == v.getY()
  except:
    return "Wrong!"
  else:
    return "OK!"

print testV2GetY(VECTOR_0, 2.1) # este tiene que dar error
print testV2GetY(VECTOR_0, 3.3)
print testV2GetY(VECTOR_1, 230.3333331) 
print testV2GetY(VECTOR_2, 0)


# V2, V2 --> String
# test V2 ADD
def testV2ADD(v1, v2):
  print "TESTING V2 ADD"
  print v1
  print v2
  newX = v1.getX() + v2.getX() 
  newY = v1.getY() + v2.getY()
  expectedResult = V2(newX, newY)
  resultVector = v1.add(v2)
  print "v1 + v2 = " + "({}, {})".format(newX, newY)
  try:
    # assert v1.add(v2) == newVector # no van a ser iguales porque no van a ser los mismos objetos, o eso esperaría que pase, la igualdad que puedo testear tal vez es la de cada coordenada.
    assert resultVector.getX() == expectedResult.getX()
  except:
    print "Wrong X!"
  else:
    print "X OK!"

  try:
    assert resultVector.getY() == expectedResult.getY()
  except:
    print "Wrong Y!"
  else:
    print "Y OK!"

  return "Test finished"


testV2ADD(VECTOR_0, VECTOR_0)
testV2ADD(VECTOR_0, VECTOR_1)
testV2ADD(VECTOR_1, VECTOR_0)


# testeo el uso de +
def testPlus(v1, v2):
  print "TESTING PLUS"
  result = v1 + v2
  newX = v1.getX() + v2.getX() 
  newY = v1.getY() + v2.getY()
  expectedResult = V2(newX, newY)
  print "Result: " + str(result)
  print "Expected: " + str(expectedResult)
  try:
    assert str(result) == str(expectedResult)
  except:
    print "Wrong!"
  else:
    print "Right!"

testPlus(VECTOR_0, VECTOR_0)
testPlus(VECTOR_0, VECTOR_1)
testPlus(VECTOR_1, VECTOR_0)

# Faltan tests (para muchas de los métodos) que estén destinados a dar error, a propósito, para ver que se reconocen los errores.

# Podría hacer un módulo de tests para esta clase que la importe y entonces ejecutar el archivo con los tests.

# También podría usar una función main.