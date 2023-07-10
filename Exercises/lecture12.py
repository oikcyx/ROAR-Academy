#Answers to Lecture 12 Exercises: Numpy
import numpy as np
#Exercise 1:
v = np.array([2., 2., 4.])

e0 = np.array([1. , 0., 0.])
e1 = np.array([0., 1., 0.])
e2 = np.array([0., 0., 1.])

projecctionE0 = np.dot(v, e0)
projecctionE1 = np.dot(v, e1)
projecctionE2 = np.dot(v, e2)

print("E0", projecctionE0)
print("E1", projecctionE1)
print("E2", projecctionE2)

#Excercise 2:
a = 2 
b = np.array([[6, -9, 1], [4, 24,8]])
print(a*b)

c = np.array([[1,0], [0,1]])
d = np.array([[6, -9, 1], [4, 24,8]])
print(np.dot(c,d))

e = np.array([[4,3], [3,2]])
f = np.array([[-2,3], [3, -4]])
print(np.dot(e,f))

#Exercise 3:
def swap_rows(M, a, b):
    if M.shape[0] < a or M.shape[0] < b:
        return "Invalid row"
    M[[a, b]] = M[[b, a]]
    return M

def swap_cols(M, a, b):
    if M.shape[1] < a or M.shape[1] < b:
        return "Invalid row inputs"
    M[:, [b,a]] = M[:,[a, b]]
    return M

#Exercise 4:
def set_array(L, rows, cols, order = "row-col"):
    try:
        rows = int(rows)
        cols = int(cols)
    except:
        print("invalid input")
        return None
    
    if len(L) != rows * cols:
        print("invalid dimension")
        return None
    order = order.lower()
    if order == 'row-col':
        return L.reshape(rows,cols)
    elif order == "col-row":
        return L.reshape(cols, rows)
    else:
        print("invalid order")
        return None

Exercise 5: 
c = np.array([[0,  1,  2,  3,  4,  5],
             [10, 11, 12, 13, 14, 15],
             [20, 21, 22, 23, 24, 25],
             [30, 31, 32, 33, 34, 35],
             [40, 41, 42, 43, 44, 45],
             [50, 51, 52, 53, 54, 55]])
print(c)

blues = c[:,1]
print(blues)

pinks = c[1, [2,3]]
print(pinks)

greens = c[[2,3], 4:6]
print(greens)

orange = c[2:5:2, 0:5:2]
print(orange)