#list comprehesion
print([i for i in range(10) if i % 2 == 0])
#output [0, 2, 4, 6, 8]


#enumerate with list comprehesion
#demo1
print([i for i, elem in enumerate([4,5,6])])
#output [0, 1, 2]

#demo2
print([elem for i, elem in enumerate([4,5,6])])
#output [4, 5, 6]

#demo3
print([t for t in enumerate([4,5,6])])
#output [(0, 4), (1, 5), (2, 6)]


 
