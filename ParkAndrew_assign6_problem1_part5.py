def simple_sort_version2(a,b,c):
    num = [a,b,c]
    num.sort()
    return num

a,b,c = simple_sort_version2(10,20,30)
print(a,b,c)

a,b,c = simple_sort_version2(10,30,20)
print(a,b,c)

a,b,c = simple_sort_version2(30,20,10)
print(a,b,c)

a,b,c = simple_sort_version2(30,20,20)
print(a,b,c)
