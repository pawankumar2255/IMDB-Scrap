import json
# from pprint import pprint
f=open("task4s.json","r")
movie_list=json.load(f)
g_movie,top_movie=0,[]
def scrape_movie_details():
    g_movie=0
    for i in movie_list:
        top_movie.append(i)
        if g_movie==10:
            break
        g_movie+=1
    file=open("task5s.json","w")
    json.dump(top_movie,file,indent=4)
    file.close()
    return top_movie
print(scrape_movie_details())