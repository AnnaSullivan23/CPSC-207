#AnnaSullivanLab101
def my_get_method(dic,get, defa):
    dic.get("get", defa)

clothes={"pants":8, "shirt":medium, "shoe":8.5}

my_get_method(clothes, "pants", 9)

my_get_method(clothes, "shirt", "large")

my_get_method(clothes, "shoes", "small")

my_get_method(clothes, "shoe", True)
