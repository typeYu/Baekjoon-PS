father_color_list = input().split()
mother_color_list = input().split()

all_color_list = list(set(father_color_list + mother_color_list))

length = len(all_color_list)

color_combination_list = [
    (all_color_list[i], all_color_list[j]) 
    for j in range(length)
    for i in range(length)
]

color_combination_list.sort(key=lambda x: (x[0], x[1]))

for (color_1, color_2) in color_combination_list:
    print(color_1, color_2)