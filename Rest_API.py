import requests
# r=requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-05-17&to=2023-06-16&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c")
# content = r.json()
# articles=content['articles']
# for article in articles:
#     print("Title- ")
#     print("--------------------------------------------------------------------------------------------------------------------")
#     print(article['title'])
#     print("--------------------------------------------------------------------------------------------------------------------")
#     print("Content- ")
#     print(article['description'])
#     print("-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----")

def get_news(topic,from_date,to_date,language='en',apiKey='890603a55bfa47048e4490069ebee18c'):
    url=f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={apiKey}"
    r=requests.get(url)
    content = r.json()
    articles = content['articles']
    for article in articles:
        print("Title- ")
        print("--------------------------------------------------------------------------------------------------------------------")
        print(article['title'])
        print("--------------------------------------------------------------------------------------------------------------------")
        print("Content- ")
        print(article['description'])
        print("-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----")
            

get_news(topic='space',from_date='2023-05-30',to_date='2023-06-10')