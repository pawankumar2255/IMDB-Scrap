import json,pprint
f = open("task1s.json","r")
n = json.load(f)
def group_by_decade(movies):
    list = []
    for i in movies:
        yr = i["year"]
        dec = yr%10
        d_y = yr-dec
        if d_y not in list:
            list.append(d_y)
    dict_movie = {j:[]for j in list}
    for k in movies:
        yy = k["year"]
        for l in dict_movie:
            deff = yy-l
            if int(l)<=int(yy) and deff<=9:
                dict_movie[l].append(k)
    pprint.pprint(dict_movie)
    h = json.dumps(dict_movie,indent = 4)
    with open("task3s.json","w") as file:
        file.write(h)
group_by_decade(n)