import requests

def get_subreddit(subreddit, limit, timeframe, listing):

    """
    subreddit = 'memes'
    limit = 100
    timeframe = 'month' #hour, day, week, month, year, all
    listing = 'hot' # controversial, best, hot, new, random, rising, top
    """

    def get_reddit(subreddit,listing,limit,timeframe):
        try:
            base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
            request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
        except:
            print('An Error Occured')
        return request.json()

    r = get_reddit(subreddit,listing,limit,timeframe)

    def get_post_titles(r):
        
        #Get a List of post titles

        titles = []
        links = []
        try:
            for post in r['data']['children']:
                #for k in post['data'].keys():
                    #print(k)

                titles.append(post['data']['title'])
                links.append(post['data']['url'])

        except:
            for post in r[0]['data']['children']:
                #for k in post['data'].keys():
                    #print(k)

                titles.append(post['data']['title'])
                links.append(post['data']['url'])

        return titles, links

    titles, links = get_post_titles(r)

    return titles, links

if __name__ == '__main__':
    subreddit = 'memes'
    limit = 100
    timeframe = 'month' #hour, day, week, month, year, all
    listing = 'hot' # controversial, best, hot, new, random, rising, top

    print(get_subreddit(subreddit, limit, timeframe, listing))