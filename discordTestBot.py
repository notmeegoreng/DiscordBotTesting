# bot.py
import os
import re

import random

import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
from SSIM_PIL import compare_ssim
from PIL import Image
import requests
from io import BytesIO

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=';')
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    servers = list(bot.guilds)
    print("Connected on " + str(len(servers)) + " servers:")
    print(f'\n'.join(server.name for server in servers))
    await bot.change_presence(activity = discord.Activity(name = "with your mom", type = discord.ActivityType.playing))


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.event
async def on_message(message):
    try:
        url = message.attachments[0].url
        response = requests.get(url)
        imgSent = Image.open(BytesIO(response.content)).resize((371, 365))
        img = Image.open("Kiss gifs/image0.png")
        value = compare_ssim(img, imgSent)
        print(value)
        if value >= 0.3:
            await message.delete()
    except:
         pass
    '''
    except IndexError:
        urls = re.findall(r"(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])", message.content)
        count = 0
        for i in urls:
            count += 1
            print(count)
        print(urls[0])
        if urls:
            print("here")
            for i in range(1, count + 1):
                try:
                    response = requests.get(urls.group(i))
                    print(urls.group(i))
                    imgSent = Image.open(BytesIO(response.content)).resize((371, 365))
                    img = Image.open("Kiss gifs/image0.png")
                    value = compare_ssim(img, imgSent)
                    print(value)
                    if value >= 0.3:
                        await message.delete()
                        break
                        '''
    await bot.process_commands(message)

global fishes, upgradesName, upgrades, rods, cost, rodPower, price
fishes = ["Goldfish", "Common Carp", "Blue Tang", "Guppy", "Sunfish"]
upgradesName = ["Rod"]
upgrades = ["rod"]
rods = ["Weak Rod", "Fragile Rod", "Delicate Rod", "Good Rod", "Great Rod", "Superior Rod"]
cost = [750, 1500, 2500, 3500, 5000, 7500]
rodPower = [1.1, 1.2, 1.3, 1.5, 2, 3]
fishPrice = [5, 7, 10, 13, 20]

#Social
@bot.command(name='hug')
async def hug(ctx, member: discord.Member):
    links = ["https://cdn.discordapp.com/attachments/702997611912888351/703668253381099560/tenor_2.gif", "https://cdn.discordapp.com/attachments/702997611912888351/703666705410424882/tenor.gif", "https://cdn.discordapp.com/attachments/702997611912888351/703668020559478816/tenor_1.gif", "https://cdn.discordapp.com/attachments/702997611912888351/703321829825314826/tenor_1.gif", "https://cdn.discordapp.com/attachments/702997611912888351/703321240449974304/tenor.gif", "https://cdn.nekos.life/hug/hug_011.gif" ]
    embed = discord.Embed(title=ctx.author.name + " hugs " + member.name,
                          colour=discord.Colour(0x21fa55))
    embed.set_image(url = links[random.randint(0,len(links)) - 1])
    guild = ctx.author.guild
    if member == guild.me:
        response = "b-baka its not like i like u or anything"
        await ctx.send(response)
    elif member.bot:
        response = "you can't hug code baka"
        await ctx.send(response)
    else:
        await ctx.send(embed = embed)
@hug.error
async def hug_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Are u dumb thats not a member")


@bot.command(name='kiss')
async def kiss(ctx, member: discord.Member):
    links = ["https://cdn.discordapp.com/attachments/702997611912888351/703669191093256272/tenor_3.gif", "https://cdn.discordapp.com/attachments/702997611912888351/703669867760582656/tenor_1.gif", "https://cdn.discordapp.com/attachments/702997611912888351/703669872210739380/tenor_2.gif", "https://cdn.discordapp.com/attachments/702997611912888351/703669873640734761/tenor_4.gif", "https://cdn.discordapp.com/attachments/702997611912888351/703669881597330031/tenor.gif"]
    embed = discord.Embed(title=ctx.author.name + " kisses " + member.name,
                          colour=discord.Colour(0x21fa55))
    embed.set_image(url = links[random.randint(0,len(links)) - 1])
    guild = ctx.author.guild
    if member == guild.me:
        response = "w-what are you doing you disgusting pervert"
        await ctx.send(response)
    elif member.bot:
        response = "you can't kiss code baka"
        await ctx.send(response)
    else:
        await ctx.send(embed = embed)
@kiss.error
async def kiss_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Are u dumb thats not a member")


#Game
@bot.command(name='start')
@commands.has_permissions(send_messages = True)
async def start(ctx):
    profiles = open("profiles/id.txt", "r")
    id = profiles.read().split('\n')
    profiles.close()
    haveProfile = str(ctx.author.id) in id

    if haveProfile:
        response = "You already have a profile!"
    else:
        response = "Profile created"
        profiles = open("profiles/id.txt", "a")
        profiles.write(str(ctx.author.id) + "\n")
        profiles.close()
        userPath = "profiles/" + str(ctx.author.id) + ".txt"
        user = open(userPath, "w")
        user.write("3000\n"
                   "0,0,0,0,0\n"
                   "0")
        user.close()
    await ctx.send(response)


@bot.command(name='balance', aliases = ["bal", 'b'])
async def bal(ctx):
    profiles = open("profiles/id.txt", "r")
    id = profiles.read().split('\n')
    profiles.close()
    haveProfile = str(ctx.author.id) in id
    if not haveProfile:
        response = "Create a profile with ;start!"
    else:
        userPath = "profiles/" + str(ctx.author.id) + ".txt"
        profile = open(userPath, "r")
        bal = profile.readline()
        profile.close()
        embed = discord.Embed(colour=discord.Colour(0x21fa55))

        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

        embed.add_field(name="**Balance**", value = "$" + bal)

    await ctx.send(embed = embed)


@bot.command(name = 'price')
async def price(ctx):
    embed = discord.Embed(title="Prices",
                          colour=discord.Colour(0x21fa55))

    value = f"""Goldfish - ${fishPrice[0]}
Common Carp - ${fishPrice[1]}
Blue Tang - ${fishPrice[2]}
Guppy - ${fishPrice[3]}
Sunfish - ${fishPrice[4]}"""

    embed.add_field(name="Prices", value=value, inline=False)

    await ctx.send(embed = embed)

@bot.command(name = 'fish', aliases = ['f'])
@commands.cooldown(1, 10, commands.BucketType.user)
@commands.bot_has_permissions(send_messages = True)
async def fish(ctx):
    profiles = open("profiles/id.txt", "r")
    id = profiles.read().split('\n')
    profiles.close()
    haveProfile = str(ctx.author.id) in id

    if not haveProfile:
        response = "Create a profile with ;start!"
    else:
        caught = random.randint(0,4)

        userPath = "profiles/" + str(ctx.author.id) + ".txt"
        profile = open(userPath, "r")
        bal = profile.readline()
        inv = profile.readline().split(',')
        rod = profile.readline()
        profile.close()
        profile = open(userPath, "w")
        profile.write(bal)
        profile.close()
        profile = open(userPath, "a")
        for i in range(len(fishes)):
            if i == caught:
                profile.write(str(int(inv[i]) + 1))
                if i == 4:
                    profile.write('\n')
            else:
                profile.write(inv[i])
            if i != 4:
                profile.write(',')
        profile.write(rod)
        profile.close()
        response = "You have caught a " + fishes[caught]
    await ctx.send(response)

@fish.error
async def fish_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is ratelimited, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.author.send(f'Hi {ctx.author.name}, I do not have permissions to send messages to that channel!')



@bot.command(name = 'sell', aliases=['s'])
@commands.bot_has_permissions(send_messages = True)
async def sell(ctx, arg = None):
    profiles = open("profiles/id.txt", "r")
    id = profiles.read().split('\n')
    profiles.close()
    haveProfile = str(ctx.author.id) in id

    if not haveProfile:
        response = "Create a profile with ;start!"
    else:
        userPath = "profiles/" + str(ctx.author.id) + ".txt"
        profile = open(userPath, "r")
        bal = profile.readline()
        inv = profile.readline().split(",")
        rod = int(profile.readline())
        profile.close()
        sold = 0
        if arg == None:
            for i in range(5):
                sold += int(inv[i]) * fishPrice[i]
            response = "Sold all fishes for $" + str(sold)
            rodSold = 0
            if rod >= 1:
                rodSold = round(rodPower[rod - 1] * sold - sold)
                response += f"\nYour rod earned you an extra ${rodSold}"
            response += "\nYou now have ${int(bal) + sold + rodSold}"
            profile = open(userPath, "w")
            profile.write(str(int(bal) + sold + rodSold) +"\n0,0,0,0,0" + "\n" + str(rod))
            profile.close()
        else:
            try:
                if 1 <= int(arg) <= 5:
                    sold += int(inv[int(arg) - 1]) * fishPrice[int(arg) - 1]
                    response = "Sold " + str(inv[int(arg) - 1].split('\n')[0]) + " " + fishes[int(arg) - 1] + " for $" + str(sold)
                    rodSold = 0
                    if rod >= 1:
                        rodSold = round(rodPower[rod - 1] * sold - sold)
                        response += "\nYour rod earned you an extra $" + str(rodSold)
                    response += "\nYou now have $" + str(int(bal) + sold + rodSold)
                    profile = open(userPath, "w")
                    profile.write(str(int(bal) + sold) + '\n')
                    for i in range(5):
                        if i == (int(arg) - 1):
                            profile.write('0')
                        else:
                            profile.write(inv[i])
                        if i != 4:
                            profile.write(',')
                        elif int(arg) == 5:
                            profile.write('\n')
                    profile.write(str(rod))
                    profile.close
                else:
                    response = "Invalid fish id!"
            except:
                response = "That is not a number!"
        await ctx.send(response)
@sell.error
async def sell_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.author.send(
            f'Hi {ctx.author.name}, I do not have permissions to send messages to that channel!'
        )


@bot.command(name='inventory', aliases=["inv"])
async def inv(ctx):
    profiles = open("profiles/id.txt", "r")
    id = profiles.read().split('\n')
    profiles.close()
    haveProfile str(ctx.author.id) in id

    if not haveProfile:
        response = "Create a profile with ;start!"
    else:
        embed = discord.Embed(title=ctx.author.name + "'s inventory",
                              colour=discord.Colour(0x21fa55))
        userPath = "profiles/" + str(ctx.author.id) + ".txt"
        profile = open(userPath, "r")
        profile.readline()
        inv = profile.readline().split(",")
        profile.close()
        response = ""
        for i in range(len(fishes)):
            response += str(i + 1) + ". " + fishes[i] + " - " + str(inv[i])
            if(i != len(fishes) - 1):
                response += "\n"
        embed.add_field(name="Inventory", value=response, inline=False)
        await ctx.send(embed=embed)

@bot.command(name = 'upgrades', aliases = ["upgrade", "up"])
@commands.bot_has_permissions(send_messages = True)
async def upgrade(ctx, arg = None):
    if arg == None:
        embed = discord.Embed(title="M20301TestBot | Upgrades",
                              colour=discord.Colour(0x21fa55),
                              description= "Do `;upgrade [id]` to browse further")


        embed.add_field(name="**1. Fishing rods**", value = "\u200b")

        await ctx.send(embed=embed)
    else:
        profiles = open("profiles/id.txt",
                        "r")
        id = profiles.read().split('\n')
        profiles.close()
        haveProfile = str(ctx.author.id) in id:

        if not haveProfile:
            response = "Create a profile with ;start!"
            await ctx.send(response)
        else:
            profile = open("profiles/" + str(ctx.author.id) + ".txt", "r")
            bal = int(profile.readline())
            inv = profile.readline()
            rod = int(profile.readline())
            profile.close()
            try:
                if int(arg) == 1:
                    embed = discord.Embed(title="M20301TestBot | " + upgradesName[int(arg) - 1],
                                          colour=discord.Colour(0x21fa55),
                                          description= "Check rod abilities with ;rods\nUpgrade your rod with ;upgrade rod\n")

                    embed.add_field(name = "__" + upgradesName[int(arg) - 1] + "__", value = rods[rod] + " - $" + str(cost[rod]))

                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Not a valid upgrade id!")
            except:
                if arg in upgrades:
                    if(bal >= cost[rod]):
                        profile = open("profiles/" + str(ctx.author.id) + ".txt", "w")
                        profile.write(str(bal - cost[rod]) + '\n' + inv + str(rod + 1))
                        await ctx.send(ctx.author.name + " has bought the " + rods[rod])
                    else:
                        await ctx.send(ctx.author.name + ", you do not have enough money!")

                else:
                    await ctx.send("Not a valid upgrade id!")
@upgrade.error
async def sell_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.author.send(
            f'Hi {ctx.author.name}, I do not have permissions to send messages to that channel!'
        )

@bot.command(name = 'rods')
async def rodsName(ctx):
    embed = discord.Embed(title="M20301TestBot | Rods",
                          colour=discord.Colour(0x21fa55))

    rodValue = ""
    costValue = ""
    powerValue = ""
    for i in range(len(rods)):
        rodValue += str(i + 1) + ". " + rods[i] + '\n'
        costValue += "$" + str(cost[i]) + '\n'
        powerValue += str(rodPower[i]) + 'x\n'

    embed.add_field(name = "Rods", value = rodValue)

    embed.add_field(name = "Cost", value = costValue)

    embed.add_field(name = "Power", value = powerValue)

    await ctx.send(embed = embed)

@bot.command(name = 'rod')
async def userRod(ctx):
    profiles = open("profiles/id.txt", "r")
    id = profiles.read().split('\n')
    profiles.close()
    haveProfile = str(ctx.author.id) in id:

    if not haveProfile:
        response = "Create a profile with ;start!"
        await ctx.send(response)
    else:
        embed = discord.Embed(title="M20301TestBot | " + ctx.author.name + "'s Rod",
                              colour=discord.Colour(0x21fa55))

        profile = open("profiles/" + str(ctx.author.id) + ".txt", "r")
        int(profile.readline())
        profile.readline()
        rod = int(profile.readline())
        profile.close()

        if rod != 0:
            value = rods[rod - 1]
        else:
            value = "Broken Rod"

        embed.add_field(name = "Rod", value = value)

        await ctx.send(embed = embed)


#Miscellaneous
@bot.command(name='ping')
async def ping(ctx):
    response = "pong! " + str(round(bot.latency * 1000)) + "ms"
    await ctx.send(response)


@bot.command(name = 'help')
async def help(ctx, arg = None):
    #command = [Name, Description, Aliases]
    #Social
    hug = ["Hug", "Hugs the person you mention!", []]
    kiss = ["Kiss", "Kisses the person you mention!", []]

    #Game
    start = ["Start", "Start a new profile for the fishing game", []]
    balance = ["Balance", "Checks your balance!", ["bal", "b"]]
    fish = ["Fish", "Catches a fish for you", ["f"]]
    inventory = ["Inventory", "Checks your Inventory of fishes", ["inv"]]
    price = ["Price", "Checks the prices of fish", []]
    sell = ["Sell", "Sells all your fishes or the fish you specify", ["s"], ";sell\n;s [fish id]"]
    upgrades = ["Upgrades", "Displays a list of upgrades", ["upgrade", "up"], ";upgrades\n;upgrade [upgrade id]\n;up"]
    rods = ["Rods", "Show lists of rods along with their cost and power", []]
    rod = ["Rod", "Shows the user's current rod", []]

    #Miscellaneous
    ping = ["Ping", "Displays the latency of the bot", []]
    help = ["Help", "Displays the help page", []]
    servers = ["Servers", "Displays which servers the bot is connected to", []]
    embed = ["Embed", "Helps send an embed with the format `;embed [title],[description],[footer],[colour hex code]`", [], ";embed This bot,is the coolest,bot ever,0x000000"]

    social = [hug, kiss]
    game = [start, balance, fish, inventory, price, sell, upgrades, rods, rod]
    miscellaneous = [ping, help, servers, embed]
    categories = [social, game, miscellaneous]
    if arg is None:
        image = "https://cdn.discordapp.com/attachments/702997611912888351/703319285799583854/WhatsApp_Image_2020-04-25_at_02.59.29.jpeg"
        embed = discord.Embed(title="M20301TestBot | Help",
                              colour=discord.Colour(0x21fa55),
                              description="Use `;help [command]` to find out more about a command!")

        embed.set_thumbnail(url=image)

        embed.add_field(name="Social", value="hug\n"
                                             "kiss", inline=False)

        embed.add_field(name="Game", value="start\n"
                                           "balance\n"
                                           "fish\n"
                                           "inventory\n"
                                           "price\n"
                                           "sell\n"
                                           "upgrade\n"
                                           "rods\n"
                                           "rod", inline=False)

        embed.add_field(name="Miscellaneous",
                        value="ping\n"
                              "help\n"
                              "servers\n"
                              "embed", inline=False)

        await ctx.send(embed=embed)

    else:
        try:
            for i in categories:
                for j in i:
                    aliases = [j[0].lower()]
                    for k in j[2]:
                        aliases.append(k)
                    for k in aliases:
                        if arg.lower() == k.lower():
                            command = j
                            raise BreakOutException
        except BreakOutException:
            image = "https://cdn.discordapp.com/attachments/702997611912888351/703319285799583854/WhatsApp_Image_2020-04-25_at_02.59.29.jpeg"
            embed = discord.Embed(title="M20301TestBot | " + command[0].capitalize(),
                                  colour=discord.Colour(0x21fa55))

            embed.set_thumbnail(url=image)

            embed.add_field(name = command[0].capitalize(), value = command[1])

            value = "None"
            if len(command[2]) != 0:
                value = ""
                for i in range(len(command[2])):
                    value += command[2][i]
                    if i != (len(command[2]) - 1):
                        value += '\n'
            embed.add_field(name = "Aliases", value = value)

            example = ""
            if len(command) == 3:
                for i in range(len(aliases)):
                    example += ";" + aliases[i]
                    if i != (len(aliases) - 1):
                        example += '\n'
            else:
                example = command[3]
            embed.add_field(name = "Examples", value = example, inline = False)

            await ctx.send(embed = embed)


@bot.command(name = 'servers')
async def servers(ctx):
    servers = list(bot.guilds)
    await ctx.send(f"Connected on {str(len(servers))} servers:\n" + '\n'.join(server.name for server in servers))

@bot.command(name = 'gift')
async def gift(ctx, member: discord.Member):
    authorised = [286402043826929664]
    if ctx.author.id in authorised:
        profiles = open("profiles/id.txt", "r")
        id = profiles.read().split('\n')
        profiles.close()
        haveProfile = str(member.id) in id

        if not haveProfile:
            response = "Member does not have profile"
        else:
            profile = open("profiles/" + str(member.id) + ".txt", "r")
            data = profile.read().split('\n')
            profile.close()
            profile = open("profiles/" + str(member.id) + ".txt", "w")
            check = True
            for i in data:
                if check:
                    check = False
                    profile.write(str(int(i) + 5000) + '\n')
                else:
                    profile.write(i + '\n')
            profile.close()
            response = "Gifted $5000 to " + member.name + "\nMember's id was: " + str(member.id)
            await ctx.send(response)
    else:
        await ctx.send("Only authorised people can use this command!")


@bot.command(name = 'info')
async def info(ctx, *, arg = None):
    #hard coded for now cause im too lazy kafojadoh
    response = "No info"
    if arg.lower() == 'cold war start':
            response = "-soviet expansionism into poland and eastern europe, commie govts set up after coups\n" \
                        "-american containment policy [curb soviet expansion into europe]\n" \
                        "-truman doctrine [give turkey + greece weapons and money to stop rebels and civil war respectively]\n" \
                        "-marshall plan [give western europe money to recover and spur economic growth]\n" \
                        "-these 2 policies greatly improved standard of living and economies of devastated europe\n" \
                        "-however, in countries like italy, money often fell into hands of politicians and did not reach the populace\n"

    await ctx.send(response)


@bot.command(name = 'kick')
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    if reason == None:
        await ctx.send("Please include a reason in `kick [reason]`")
    else:
        if member.id == 286402043826929664:
            await ctx.send("You can't kick the owner of the bot muahahaha")
        else:
            await member.kick(reason = reason)
            await ctx.send(f"{member.display_name} has been kicked for {reason}")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the perms for this command!", delete_after = 3)
    else:
        print(error)


@bot.command(name = 'nick')
@commands.has_permissions(manage_nicknames = True)
async def nickname(ctx, member : discord.Member, *, nickname = None):
    if member.id == 286402043826929664 and ctx.author.id != 286402043826929664: #hmm
        await ctx.send("no can do")
    else:
        initialName = member.display_name
        try:
            await member.edit(nick = nickname)
            await ctx.send(f"{initialName} has been nicked to {nickname}")
        except:
            if ctx.guild.me.top_role < member.top_role:
                await ctx.send(f"my power level is weaker than {member.display_name}")
            else:
                await ctx.send("what the fuck is this edge case im having an aneurysm help me")
@nickname.error
async def nick_error(ctx, error):
    error = getattr(error, "original", error)
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the perms for this command!", delete_after = 3)
    elif isinstance(error, discord.HTTPException):
        await ctx.send("r u returd thats longer than 32 characters", delete_after = 3)
    else:
        print(error)


@bot.command(name = 'iq')
async def iq(ctx, member : discord.Member):
    if member.id == 286402043826929664: #dammit mug1wara26
        await ctx.send(f"{member.display_name} iq is {random.randint(200, 300)}, very big brain")
    else:
        await ctx.send(f"{member.display_name} iq is {random.randint(-100,-20)}, smol brain")


@bot.command(name='assign')
@commands.has_permissions(manage_roles = True)
async def assign(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)
    await ctx.send(f"{member.display_name} has been given the role {role.name}")
@assign.error
async def assign_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("You don't have the permissions for this command!", delete_after = 3)
  else:
    print(error)


@bot.command(name='embed')
async def embed(ctx, *, arg):
    message = await ctx.send('Where to post embed?')
    while True:
        ch = await bot.wait_for('message', timeout=20)
        if ch.author.bot == False and ch.author == ctx.author:
            if len(ch.channel_mentions) == 1:
                await ch.delete()
                await message.delete()
                await ctx.message.delete()
                break
            else:
                await ctx.send("Invalid input, try again")

    arg = arg.split(',')
    title = arg[0]
    description = arg[1]
    footer = arg[2]
    color = arg[3]
    embed = discord.Embed(title = title, description = description, color = int(color, 16))

    embed.set_footer(text = footer)
    await ch.channel_mentions[0].send(embed=embed)
@embed.error
async def embed_error(ctx, error):
    if isinstance(error, TimeoutError):
        await ctx.send("Timeout(20s)")
    else:
        await ctx.send(error)
        
class BaseException(Exception):
    """All our exceptions should inherit from this"""
    
class BreakOutException(BaseException):
    """Never meant not to be caught."""

bot.run(TOKEN)
