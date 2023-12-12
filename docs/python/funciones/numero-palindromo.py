def es_palindromo(n):
   n1 = n
   n2 = 0
   while n>0:
      n2 = 10*n2 + n%10
      n //= 10
      print(n2)
   return n1==n2

print(es_palindromo(123))
print(es_palindromo(123321))
print(es_palindromo(int(input())))
