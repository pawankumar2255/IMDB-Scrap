import time,random,requests,json
x=open("task4s.json","r")
y=json.load(x)
random_sleep=random.randint(1,3)
def scrape_movie_details():
    for i in y:
        time.sleep(random_sleep)
        print(str(i)+"\r",end="")
scrape_movie_details()