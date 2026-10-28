import requests
from pprint import pprint
# url="http://www.omdbapi.com/?i=tt3896198&apikey=62666bb&t=Guardians+of+the+Galaxy+Vol.+2"
# response=requests.get(url)
# data=response.json()
# pprint(data)


def rating():
    movie=input("Enter movie or webseries Name: ")
    farzi=movie
    fix_movie=movie
    count=1
    for char in farzi:
        if(char==" "):
            fix_movie=farzi.replace(" ","+",count)
            farzi=fix_movie
            count=count+1
    # print(fix_movie)
    try:
        url=f"http://www.omdbapi.com/?i=tt3896198&apikey=62666bb&t={fix_movie}"
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        data=response.json()
        if data["Response"]=="True":

            print(f"IMDb Rating of {movie} is {data['imdbRating']}")
        else:
            print("Movie not found!")
    except requests.exceptions.RequestException:
        print("Network or request error occurred.")
    ans=True
    while(ans):
        value=input("Want to Search for other Movie? Yes/No: ").lower()
        if(value=="no"):
            return
        elif(value=="yes"):
            ans=False
            rating()
            
        else:
            print("Please Answer is Yes or No only.")

rating()

