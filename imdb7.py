import json
movie_file = open("task4s.json","r")
movie_list = json.load(movie_file)
dict_director,set_director,list_of_director = {},set(),[]
def movies_of_director():
    for movie_dict in movie_list:
        list_of_director.append(movie_dict["director"])
        set_director.add(movie_dict["director"])
    for count_director in set_director:
        dict_director[count_director] = list_of_director.count(count_director)
    file_director = open("task7s.json","w")
    json.dump(dict_director,file_director, indent = 4)
movies_of_director()