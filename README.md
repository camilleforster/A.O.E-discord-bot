## A.O.E-discord-bot
Author: Camille Forster

Release Year: 2021

#### A.O.E. Discord Bot

An application used to send data about each club member's points individually through Discord direct messaging; built with Python, Google Sheets API, Discord API, and git, and hosted on Heroku.

## Project Screen Shots

#### Example:   

[ PRETEND SCREEN SHOT IS HERE ]


[ PRETEND OTHER SCREEN SHOT IS HERE ]

## Commands
To access this bot, you need to be in the club's official discord channel.

Current point data:

`!aoe points `  

Full list of commands:
`!aoe help`  

How to obtain points
`!aoe points info`  

To Visit App:
Must be in the AOE discord channel.

## Reflection

This was a 2 week-long project built during my first semester of UW-Madison. Project goals included learning Python, git, and implementing APIS from scratch to succeed my vision of making the bot accessible for all new members.

I had recently joined a women in technology club which requires new members to reach a certain number of points before becoming official members. I noticed that there was a Google Sheet the club president had access to that contained a list of our names with our number of points beside it. However, these points were not accessible to us as new members. In order to track the number of points we had, we had to contact the president who had access to the sheet. The issue with this was that it became extremely time consuming for us to ask and for the president to look up our points.

Thus, I proposed the idea of making a discord bot that could access the google sheet and send users their data through direct messages to keep their points private.

One of the main challenges I ran into was Authentication. This lead me to spend a few days on a research  into OAuth, Auth0, and two-factor authentication from both Google Sheets and Discord. Luckily, Google had an extensive tutorial on authentication on their website, but it took a while for me to understand this new API terminology. 

Another issue was learning Python. During my first semester of college, I was mainly acquited with Java, so I had never coded in Python before. This required me to watch multiple tutorials on Python syntax on YouTube and Stack Overflow.

I chose to use Heroku and Github in order to host my Discord bot for 24/7 use, since it was the only free option available. 
