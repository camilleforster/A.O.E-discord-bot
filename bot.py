# Sources used to develop
# https://stackoverflow.com/questions/58686943/how-do-i-get-a-discord-bot-to-read-data-from-a-specific-range-of-a-google-sheet
# https://www.youtube.com/watch?v=aZ9in0_w46U
# https://www.youtube.com/watch?v=v8YTRDQsFUo 
# https://careerkarma.com/blog/python-typeerror-can-only-concatenate-str-not-int-to-str/
# https://stackoverflow.com/questions/37602460/gspread-exceptions-spreadsheetnotfound
# https://stackoverflow.com/questions/38709324/unexpected-credentials-type-none-expected-service-account-with-oauth2
# https://www.youtube.com/watch?v=v8YTRDQsFUo
# https://docs.gspread.org/en/latest/user-guide.html#getting-a-cell-value
# https://discordpy.readthedocs.io/en/latest/api.html#embed
# https://stackoverflow.com/questions/11748671/negative-form-of-isinstance-in-python


# Prints to console
print(f"Starting bot...")

from datetime import date

import time
startTime = time.time()

# Prints to console
print(f"Importing modules...")

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Setting up APIs/imports/installs
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import gspread
from oauth2client.service_account import ServiceAccountCredentials

print(f"Importing .env configuration...")


# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", 'https://www.googleapis.com/auth/spreadsheets']
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SAMPLE_SPREADSHEET_ID = os.getenv('SAMPLE_SPREADSHEET_ID')

bot = commands.Bot(command_prefix='!')

# Prints to console
print("Initializing Google Authentication...")

# Creds to use Google API methods
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Creds to use gspread methods
creds2 = ServiceAccountCredentials.from_json_keyfile_name('credentials2.json', SCOPES)
client2 = gspread.authorize(creds2)
sheet2 = client2.open('Attendance').sheet1

print(f"Startup complete!\t[ {(time.time()-startTime):.2f}s ]")

# Main aoe block
@bot.command(name ='aoe')
async def on_message(ctx, *args):
#    help = "\nFor a full list of a commands, use " + "`" + "!aoe help" + "`"
    tag = ctx.author.name + "#" + ctx.author.discriminator
    if (''.join(args) == "points"):
        findrow = sheet2.find(tag).row
        points = sheet2.acell('CH' + str(findrow)).value

        embedVar = discord.Embed(title="!aoe points", description=str(help), color=0x223b8d)
        embedVar.add_field(name="Total Points", value=str(points), inline=True)
        embedVar.add_field(name="Workshop Requirement", value=sheet2.acell('BZ' + str(findrow)).value, inline=False)
        embedVar.add_field(name="Friendship Pillar", value=sheet2.acell('CA' + str(findrow)).value, inline=False)
        embedVar.add_field(name="Leadership Pillar", value=sheet2.acell('CB' + str(findrow)).value, inline=False)
        embedVar.add_field(name="Professionalism Pillar", value=sheet2.acell('CC' + str(findrow)).value, inline=False)
        embedVar.add_field(name="1st Half of Semesters", value=sheet2.acell('CF' + str(findrow)).value, inline=False)
        embedVar.add_field(name="2nd Half of Semester", value=sheet2.acell('CG' + str(findrow)).value, inline=False)

        embedVar.set_thumbnail(url="https://scontent-msp1-1.xx.fbcdn.net/v/t1.6435-9/fr/cp0/e15/q65/83163447_2254255618208294_8284125460166606848_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=7aed08&_nc_ohc=234Se_Jt1FsAX--qate&_nc_ht=scontent-msp1-1.xx&oh=c7a9c86b3ca16dee286b36fc1a0e95ee&oe=61A0001A")
        await ctx.author.send(embed=embedVar)

# Other aoe blocks
#    if(''.join(args) == "pointsinfo") :
#       embedVar = discord.Embed(title="!aoe points info", description=str(help), color=0x223b8d)
#        embedVar.add_field(name="Carnation Conversations", value="`25` points each \nYou are required to complete 25", inline=False)
#        embedVar.add_field(name="Rose Buddy Dates", value="`25` points each \nYou are required to complete 3", inline=False)
#        embedVar.add_field(name="Weekly Quizzes", value="`20` points each \nYou must pass all of them including the final quiz", inline=False)
#        embedVar.add_field(name="Weekly Meetings", value="`10` points each \nIf you attend every meeting, you get an extra 30 points in addition to 10 points per meeting. If you miss a meeting, you are deducted 15 points and you are no longer eligible for the 30 extra points.", inline=False)
#        embedVar.add_field(name="Non-Mandatory Events", value="`25` points each \nYou are also welcome to attend any non-mandatory event (like study hours, socials, etc.)", inline=False)
#        embedVar.add_field(name="Bonus Points", value="`10-25` points each \nThere are also opportunities to earn bonus points at each candidate class", inline=False)
#        embedVar.set_thumbnail(url="https://scontent-msp1-1.xx.fbcdn.net/v/t1.6435-9/fr/cp0/e15/q65/83163447_2254255618208294_8284125460166606848_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=7aed08&_nc_ohc=234Se_Jt1FsAX--qate&_nc_ht=scontent-msp1-1.xx&oh=c7a9c86b3ca16dee286b36fc1a0e95ee&oe=61A0001A")
#        await ctx.author.send(embed=embedVar)

#    if(''.join(args) == "help") :
#        pointscommands = "`!aoe points info`" + " how to obtain points\n" + "`!aoe points`" + " your current points data"
#       embedVar = discord.Embed(title="!aoe help", description="", color=0x223b8d)
#        embedVar.add_field(name="Points", value=str(pointscommands), inline=True)
#        embedVar.set_thumbnail(url="https://scontent-msp1-1.xx.fbcdn.net/v/t1.6435-9/fr/cp0/e15/q65/83163447_2254255618208294_8284125460166606848_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=7aed08&_nc_ohc=234Se_Jt1FsAX--qate&_nc_ht=scontent-msp1-1.xx&oh=c7a9c86b3ca16dee286b36fc1a0e95ee&oe=61A0001A")
#        await ctx.author.send(embed=embedVar)

# Once the points send, it tells you to check your DMs
    if (len(args) == 0):
        embedVar = discord.Embed(title="!aoe", description=str(help), color=0x223b8d)
        embedVar.set_thumbnail(url="https://scontent-msp1-1.xx.fbcdn.net/v/t1.6435-9/fr/cp0/e15/q65/83163447_2254255618208294_8284125460166606848_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=7aed08&_nc_ohc=234Se_Jt1FsAX--qate&_nc_ht=scontent-msp1-1.xx&oh=c7a9c86b3ca16dee286b36fc1a0e95ee&oe=61A0001A")
        await ctx.channel.send(embed=embedVar)
    if (not isinstance(ctx.channel, discord.DMChannel)) :
        await ctx.channel.send("Check your dms!")
bot.run(TOKEN)
