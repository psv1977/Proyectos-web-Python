a = [5, 1, 4, 9, 0]
b = list(range(3, 10)) + list(range(20, 23))
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa', 'elefante']
e = ['a', a, 2 * a]


print(a[2])
# print(b[9]) 
print(c[1][2])
print(e[0] == e[1])
print(len(c))
print(len(c[0]))
print(len(e))
print(c[-1])
print(c[-1][+1])
print(c[2:] + d[2:])
print(a[3:10])
print(a[3:10:2])
print(d.index('jirafa'))
print(e[c[0][1]].count(5))
print(sorted(a)[2])
# print(complex(b[0], b[1]))
  