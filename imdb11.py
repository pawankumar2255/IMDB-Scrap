import json
file = open("task4s.json","r")
m_dict = json.load(file)
genre_dict = {}
def analyse_genre():
    for i in m_dict:
        genre_dict[i["genre"]] = 0
    for i in m_dict:
        genre_dict[i["genre"]] += 1
    file = open("task11s.json","w")
    json.dump(genre_dict,file,indent = 4)
    file.close()
analyse_genre()