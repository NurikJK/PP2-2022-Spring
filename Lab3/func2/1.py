movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
listscore55 = []
categorylist = []

def score55bool(name):
    for i in range(len(movies)):
        if name == movies[i]['name']:
            if movies[i]['imdb'] > 5.5:
                print("True")
    print("False")

def score55(movies):
    for i in range (len(movies)):
        if movies[i]['imdb'] > 5.5:
            listscore55.append(movies[i]['name'])

def categoryselect(movies):
    category = input()
    for i in range(len(movies)):
        if movies[i]['category'] == category:
            categorylist.append(movies[i]['name'])

def average(movies):
    summa = 0
    for i in range(len(movies)):
        summa += movies[i]['imdb']
    print(summa/len(movies))

def averagecategory(movies):
    summa = cnt = 0
    category = input()
    for i in range(len(movies)):
        if movies[i]['category'] == category:
            summa = summa + movies[i]['imdb']
            cnt += 1
    print(summa/cnt)

print("Select function: \nTo show value of single movie: Press 1 \nTo show list Good movies: Press 2\nTo select category: Press 3\nTo see average score : Press 4\nTo see average score of selected category: Press 5")
n = int(input())
if n == 1:
    name = input()
    score55bool(name)
if n ==2 :
    score55(movies)
    print(listscore55)
if n == 3: 
    categoryselect(movies)
    print(categorylist)
if n == 4:
    average(movies)
if n == 5:
    averagecategory(movies)

