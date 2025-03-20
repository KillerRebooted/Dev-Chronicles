import requests

url = requests.get("https://open.spotify.com/track/6RoGQUXBKG54FHb2jdRSva?si=67ca6e56fa4f4d46").text

song_names = []

for i in range(len(url)):

    if url.startswith('class="EntityRowV2__AnchorLink-sc-ayafop-8 hfgfpQ">', i, i+51):

        start = 'class="EntityRowV2__AnchorLink-sc-ayafop-8 hfgfpQ">'

        song_names.append( url[i + len(start) : i + len(start) + url[i+len(start) : i+len(start)+200].index("<") ] )

for i in song_names:

    start = url.index(i) + url[url.index(i) : url.index(i)+1000].index('<a href="/artist/') + len('<a href="/artist/4fSMtiyC6lF5BUO1tUMWMs">')

    song_names[song_names.index(i)] = f"{i} by {url[ start : start+url[start:start+200].index('<') ]}"

for i in song_names:

    song_names[song_names.index(i)] = i.replace("&amp;", "&").replace("&#x27;", "'").replace("&quot;", '"')

start = url.index('meta property="og:title" content="')

print(url[ start+len('meta property="og:title" content="') : start+len('meta property="og:title" content="') + url[start+len('meta property="og:title" content="') : start+200].index('"')], ":")

print()

[print(song) for song in song_names]