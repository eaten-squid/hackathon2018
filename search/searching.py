from discord.ext import commands
from discord import Embed
from .utils import checks
from .utils.dataIO import dataIO
import os

class Search():
  def __init__(self.bot):
    self.bot = bot
  @commands.command(pass_context = true)
  async def search(self, ctx, role_name):
    a = ctx.server.roles
    for users in role:
      await self.bot.say(users)
