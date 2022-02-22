from libraries import *
from cmds import *

load_dotenv()

bot = commands.Bot(command_prefix='!')
embed = discord.Embed()

@bot.event
async def on_ready():
    print('MewPet Online !')



  @bot.command('ayuda')
async def cmd_help(ctx):
  embed.colour = 15772077
  embed.title = "Ayuda General"
  embed.description = helper
  embed.set_footer(
    text = "Ǥг𝔦๓ ⅋ Ｍ𝑒𝔴", 
    icon_url = "https://i.ibb.co/fG1vwgT/Group-335.jpg")
  await ctx.send(
    embed = embed)


@bot.command('1')
async def cmd_reg(ctx):
  embed.colour = 1692134
  embed.title = "Registro de Jugador"
  embed.description = juego
  embed.set_footer(
    text = "Ǥг𝔦๓ ⅋ Ｍ𝑒𝔴", 
    icon_url = "https://i.ibb.co/fG1vwgT/Group-335.jpg")
  embed.set_thumbnail(
    url = "https://i.ibb.co/fG1vwgT/Group-335.jpg"
  )
  await ctx.channel.send(embed = embed)


  data = json.loads(cmd_all)
ele = json.loads(cmd_all)
for elementos in ele['commands']:
  com = elementos['name']



bot.run(os.getenv('TOKEN1'))