immutable_var = 1, 2, 23
#immutable_var[1] = 5 # В кортеже содержится ссылка на список, а не сам список.
print(immutable_var)
mutable_list = [2, 4, 43]
mutable_list[0] = 232
print(mutable_list)