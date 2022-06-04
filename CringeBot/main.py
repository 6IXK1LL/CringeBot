from doctest import debug_script
import discord
from discord.ext import commands

import colorama
from colorama import Fore, Back, Style

from discord_components import DiscordComponents, Button, ButtonStyle

from config.config import settings
from config.emoji import *
from config.colors import *

from sex.choice import random_choice

from bot import bot

colorama.init()


@bot.event
async def on_ready():
    DiscordComponents(bot)

    print(Fore.GREEN + 'Bot started')


@bot.command()
async def sex(ctx, member):
    author = ctx.message.author

    offer = discord.Embed(
        title = f'{author} предложил секс корешу',
        description = f'{author.mention} предложил **сексануться** {member}',
        colour = BOT_COLOR
    )
    offer.set_image(url = random_choice())

    await ctx.send(embed=offer,
                components = [[
                    Button(label = 'да', 
                        custom_id = 'sex_yes',
                        style = ButtonStyle.green,
                        emoji = CHECK_MARK)]])

    responce = await bot.wait_for("button_click", check = lambda i: i.custom_id == 'sex_yes')
    await ctx.send(embed=discord.Embed(
        title = 'Свершилось',
        description = f'{author.mention} провёл ночь с {member} и залетел',
        colour = BOT_COLOR
    ))


@bot.command()
async def kiss(ctx, member):
    author = ctx.message.author

    offer = discord.Embed(
        description = f'{author.mention} **поцеловал** {member}',
        colour = BOT_COLOR
    )

    await ctx.send(embed = offer)


@bot.command()
async def clear(ctx, amount):
    amount = int(amount) + 1

    await ctx.channel.purge(limit = amount)


@bot.command()
async def kill(ctx, member, subject):
    offer = discord.Embed(
        title = 'СОВЕРШЕННО УБИЙСТВО',
        description = f'{member} был убит. На месте преступления был обнаружен {subject}..',
        colour = BOT_COLOR
    )

    await ctx.channel.purge(limit = 1)
    await ctx.send(embed = offer)


if __name__=='__main__':
    bot.run(settings['token'])