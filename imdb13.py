import json
movie_file = open("task4s.json","r")
movie_det_dict = json.load(movie_file)
m = open("task1s.json","r")
nm = json.load(m)
def scrape_movie_details():
    for i,j in zip(nm,movie_det_dict):
        id = i["movie_link"][28:37]
        a=open(id+"_cast.json","r")
        v=json.load(a)
        j["cast"] = v
        file = open(str(id)+"___.json","w")
        json.dump(j,file,indent = 4)
scrape_movie_details()