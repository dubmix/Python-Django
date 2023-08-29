#!/usr/bin/python3

def my_var():
	var = 42
	print(var, "has a type", type(var))
	var = "42"
	print(var, "has a type", type(var))
	var = "forty-two"
	print(var, "has a type", type(var))
	var = 42.0
	print(var, "has a type", type(var))
	var = True
	print(var, "has a type", type(var))
	var = [42]
	print(var, "has a type", type(var))
	var.append(43)
	print(var, "has a type", type(var))
	var = {42: 42}
	print(var, "has a type", type(var))
	var = (42, 67)
	print(var, "has a type", type(var))
	var = set()
	print(var, "has a type", type(var))

my_var()