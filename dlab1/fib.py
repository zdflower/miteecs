#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Objective:
# Write the definition of a Python procedure fib, such that fib(n) returns the nth Fibonacci number.
# n es un entero positivo (de 0 en adelante) que representa el índice del número de fibonacci en la serie.
# Según la definición dada, si fib(0) = 0, fib(1) = 1, y para n>1, fib(n) = fib(n-1) + fib(n-2)


# Natural --> Natural
def fib(n):
  # casos base
  if n == 0:
    return 0
  elif n == 1:
    return 1
  # caso recursivo
  elif n > 1:
    return fib(n - 1) + fib (n - 2)



# ejemplos

def test(input, expectedOutput):
  print "fib(" + str(input) + ") = " + str(fib(input))
  try:
    assert fib(input) == expectedOutput
  except:
    print "is wrong."
  else: 
    print "is fine."

# assert fib(1) == 1
# assert fib(2) == 1
# assert fib(2) == fib(1) + fib(0)
# assert fib(10) == fib(9) + fib(8)

test(0, 0)
test(1, 1)
test(2, 1)
test(2, fib(1) + fib(0))
test(10, fib(9) + fib(8))