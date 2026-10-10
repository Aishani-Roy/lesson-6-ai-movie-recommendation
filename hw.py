import pandas as pd
from textblob import TextBlob
try:
    df=pd.read_csv('1.csv')
except:
    print("error:the file was not found")
    exit()
genres=sorted({g.strip() for x in df["Genre"].dropna().str.split(", ") for g in x})
print("welcome to the movie machine!!!!!")
name=input("your name:")
print("\ngenres")
for i, genre in enumerate(genres,1):
    print(f"{i}.{genre}")
g=input("\nSelect a genre by entering the corresponding number:")
genre=genres[int(g)-1] if g.isdigit() else g.title()
mood=input("how are you today?:")
pol=TextBlob(mood).sentiment.polarity
if pol>0:
    mood="positive"
elif pol<0:
    mood="negative"
else:
    mood="neutral"
r=input("minimum rating(0-10)")
movies=df[
(df["Genre"].str.contains(genre,case=False,na=False))&(df["IMDB_Rating"]>=float(r)if r else True)
]
print(f"\n{name},based on your mood({mood})and selected genres({genre}),here are some movie recommendations:\n")
count=0
for _,row in movies.iterrows():
    if TextBlob(str(row["Overview"])).sentiment.polarity*pol>0:
        print(f"title:{row['Series_Title']}\nGenre:{row['Genre']}\nrating:{row['IMDB_Rating']}\ndescription:{row['Overview']}\n")
        count+=1
    if count==5:
        break
if count==0:
    print("no movies were found. please be less picky")