# A movie review app tracks how well a movie is liked based on emoji submissions from users. Given a list, keep track of how the movies likeability is going using the emojis provided. A thumbs up emoji is +1, starry face +2, thumbs down -1, vomit face -2 points. Write a function that returns both the percentage of people that liked the movie in general as well as the overall +/- point total.


ratings = ["\U0001F44D", "\N{thumbs up sign}",  "\N{Face with Open Mouth Vomiting}", "\U0001F44D", "\U0001f929", "\N{thumbs down sign}", "\U0001F44E", "\U0001F92E", "\U0001f929", "\N{thumbs down sign}", "\N{thumbs up sign}", "\U0001F44D", "\U0001F44D", "\N{Face with Open Mouth Vomiting}", "\N{thumbs down sign}", "\U0001F44D", "\U0001f929", "\U0001F44D", "\N{thumbs down sign}", "\N{thumbs down sign}"]

print(ratings)

def rottenTomatoes(ratings: list) -> int:
    
    score = 0
    people = 0
    positiveReviews = 0
    for review in ratings:
        
        if(review == "\U0001F44D"):
            score = score + 1
            people = people + 1
            positiveReviews = positiveReviews + 1
            # print(score)
        elif(review == "\U0001F92E"):
            score = score - 2
            people = people + 1
            # print(score)
        elif(review == "\U0001F44E"):
            score = score - 1
            people = people + 1
            # print(score)
        elif(review == "\U0001f929"):
            score = score + 2
            people = people + 1
            positiveReviews = positiveReviews + 1
            # print(score)
            
    quotent = positiveReviews / people
    percentage = quotent * 100
    tomatoes = round(percentage)
    
    return score, (f'{tomatoes}%')
        
print(rottenTomatoes(ratings))