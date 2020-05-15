import newsapi
from newsapi.newsapi_client import NewsApiClient
import pandas
import json
import re
search_words = ["Canada","University","Dalhousie University","Halifax","Canada Education"]

api = NewsApiClient(api_key='e431b03ee39f4d94aa51d928f99b9ae6')





for i in search_words:
    all_articles = api.get_everything(q=i,
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',

                                      language='en',
                                      sort_by='relevancy',
                                      page_size=100)
    news_content = re.sub(r':', '',"value")
    news_content = re.sub(r'‚Ä¶', '', news_content)
    response_json_string = json.dumps(all_articles)

    response_dict = json.loads(response_json_string)
    print(response_dict)

    articles_list = response_dict['articles']

    df = pandas.read_json(json.dumps(articles_list))
    df.to_csv('newsextracted.csv', mode='a')


