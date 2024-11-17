from django.shortcuts import render
from .twitter_client import TwitterClient
from textblob import TextBlob
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@csrf_exempt
def index(request):
    context = {}
    if request.method == 'POST':
        query = request.POST.get('query')
        twitter_client = TwitterClient()
        tweets = twitter_client.fetch_tweets(query)
        
        sentiments = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
        analyzed_tweets = []
        for tweet in tweets:
            sentiment = analyze_sentiment(tweet)
            sentiments[sentiment] += 1
            analyzed_tweets.append({'text': tweet, 'sentiment': sentiment})
        
        context = {
            'query': query,
            'analyzed_tweets': analyzed_tweets,
            'sentiments': sentiments
        }
    
    return render(request, 'index.html', context)
