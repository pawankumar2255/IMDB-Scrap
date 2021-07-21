import json
movie_data = open("task4s.json","r")
movie_details_list = json.load(movie_data)
dict_dir_det = {}
def analyse_language_and_director():
    for movie_det_dict in movie_details_list:
        dict_dir_det[movie_det_dict["director"]] = {}
    for movie_num in range(len(movie_details_list)):
        for director in dict_dir_det:
            if director in movie_details_list[movie_num]["director"]:
                for language in movie_details_list[movie_num]["language"]:
                    dict_dir_det[director][language] = 0
    for movie_num in range(len(movie_details_list)):
        for director in dict_dir_det:
            if director in movie_details_list[movie_num]["director"]:
                for language in movie_details_list[movie_num]["language"]:
                    dict_dir_det[director][language] +=1
    file = open("task10s.json","w")
    json.dump(dict_dir_det,file,indent = 4)
    file.close()
analyse_language_and_director()