#annasullivanLab104
lemon= {"egg": 8,"milk":2, "sugar":1, "flour":3, "lemon zest": 1}

velvet= {"egg":8,"flour":1, "Chocolate":2, "Cream Cheese": 3}

for i in lemon:
    for j in velvet:
        if i==j:
            print("The recipes have", i ,"as a similar ingrediant")
        else:
            print(i, "and", j, "are not the same ingrediant")
