from math import *

def fx(x):
	y = (1/3)*pow(x,2) - (1 + x)*(log1p(x) - 1)
	return y

e = 0.001
L = 1
i = 0

a = [0] * 50
b = [0] * 50
x_m = [0] * 50
a[0] = -0.5
b[0] = 0.5


x_m[0] = (a[0] + b[0]) / 2


L = b[0] - a[0]
print(L)

while fabs(L) > e:
	f_x_m = fx(x_m[i])
	L1 = 1
	x_1 = a[i] + L/4
	x_2 = b[i] - L/4
	print("Ітерація №" + str(i))
	print("Початок інтервалу: " + str(a[i]))
	print("Закінчення інтервалу: " + str(b[i]))
	print("Xm: " + str(x_m[i]))
	print("Значення ф-ії F(xm):" + str(f_x_m))
	print("X1: " + str(x_1))
	print("X2: " + str(x_2))
	

	f_x_1 = fx(x_1)
	print("F(x1) = " + str(f_x_1))
	f_x_2 = fx(x_2)
	print("F(x2) = " + str(f_x_2))
	print("L = " + str(L))


	if(f_x_1 < f_x_m):
		b[i+1] = x_m[i]
		x_m[i+1] = x_1
		a[i+1] = a[i]
	else:
		if(f_x_2 < f_x_m):
			a[i+1] = x_m[i]
			x_m[i+1] = x_2
			b[i+1] = b[i]
		else:
			a[i+1] = x_1
			b[i+1] = x_2
			x_m[i+1] = x_m[i]

	L = b[i+1] - a[i+1]
	i = i + 1

print("Ітерація №" + str(i))
print("Початок інтервалу: " + str(a[i]))
print("Закінчення інтервалу: " + str(b[i]))
print("Середнє значення(xm): " + str(x_m[i]))
print("Значення ф-ії F(xm):" + str(f_x_m))
print("X1: " + str(x_1))
print("X2: " + str(x_2))
print("F(x1) = " + str(f_x_1))
print("F(x2) = " + str(f_x_2))
print("L = " + str(L))


#зміна №2

#створення нової гілки

#змніна 12.11.20


