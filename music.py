''' class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.is_playing = False
        self.music_queue = []
        self.vc = ''
        self.FFMPEG_OPTIONS = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
        }
    def next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0]['source']
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegOpusAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda x: self.next())
        else:
            self.is_playing = False
    @commands.command(name="play", aliases=["p"], description="Reproduce canciones")
    async def play(self, ctx, *, music):
        if ctx.author.voice is None:
            await ctx.send("No estás en ningún canal")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        YDL_OPTIONS = {'format': "bestaudio"}
        self.vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info("ytsearch:%s" %music , download=False)['entries'][0]
            self.music_queue.append({'source': info['formats'][0]['url'], 'title': info['title']})
        if self.is_playing == False:
            self.is_playing = True
            m_url = self.music_queue[0]['source']
            title = self.music_queue[0]['title']
            source = await discord.FFmpegOpusAudio.from_probe(m_url, **self.FFMPEG_OPTIONS)
            self.music_queue.pop(0)
            self.vc.play(source, after=lambda x: self.next())
            await ctx.send('▶️ Reproduciendo...\n' + title)
        else:
            await ctx.send('Añadido a la cola') '''