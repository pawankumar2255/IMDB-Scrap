import json 
m_f = open("task4s.json","r")
movie_list = json.load(m_f)
langs_list,set1,dict_ana_lang = [],set(),{}
def Analysis_movie_language():
    for movie_det in movie_list:
        for language in movie_det["language"]:
            langs_list.append(language)
            set1.add(language)
    for langs in set1:
        dict_ana_lang[langs]=langs_list.count(langs)
    file = open("task6s.json","w")
    json.dump(dict_ana_lang,file,indent = 4)
    file.close()
Analysis_movie_language()
