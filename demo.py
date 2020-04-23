import useful_functions as func

scores = [88, 92, 79, 93, 85]

mean = func.mean(scores)
curved = func.add_five(scores)

mean_c = func.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)
