from config.config import settings

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = settings['prefix'])