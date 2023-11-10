ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
print("\n")

ft_list[1] = "World!"
ft_tuple = ("Hello", "Germany")

ft_set.remove("tutu!")
ft_set.add("Berlin!")

ft_dict["Hello"] = "42 Berlin!"

print(ft_list) #mutable
print(ft_tuple) #immutable
print(ft_set) #unique elements
print(ft_dict) #key-value pairs