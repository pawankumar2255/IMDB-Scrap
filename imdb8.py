import json 
movies_data=open("task4s.json","r")
movies_list=json.load(movies_data)
def scrape_movie_details():
    for movie_dict in movies_list:
        movie_url_id=movie_dict["img_url"][27:38]
        movie_id=movie_url_id.replace("/","")
        conv_id_json=open(str(movie_id)+".json","w")
        nn=json.dump(movie_dict,conv_id_json,indent=2)
scrape_movie_details()