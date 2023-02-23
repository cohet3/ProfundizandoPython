# NaN - Not a number (no es un número)
# NaN no es sensible a mayúsculas /minisculas
#NaN es un tipo de dato numérico indefinido
import math
from decimal import Decimal

a = float('Nan')
print(f'a: {a}')
print(f' Es Nan (not a number)?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es Nan (not a number)?: {math.isnan(a)}')