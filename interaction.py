# set the apikey and limit
apikey = #apikey
lmt = 4

# our test search
#search = "anime hi"
def product(search):
  if search != "":
    r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search, apikey, lmt))
    if r.status_code == 200:
      gifs = json.loads(r.content)['results']
      if gifs:
        for data in gifs:
          media = data['media']
          #print(media)

        for imagen in media:
          url = imagen['gif']
          return url['url']