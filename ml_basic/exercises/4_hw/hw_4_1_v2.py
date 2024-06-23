val_int = int(input())

#format(val_str, )
val_tmp =f"{val_int:,}"
result = val_tmp.replace(",", " ")
print(f"{result}")