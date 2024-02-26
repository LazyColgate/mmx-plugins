import discord
from discord.ext import commands


class RawPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def raw(self, message, ctx):
        try:
            message = await ctx.channel.fetch_message(message)
            embed = discord.Embed(
                title=f"```{message}```",
                description=message.content,
                color=discord.Color.blue()
            )
            await ctx.send(embed=embed)
        except discord.NotFound:
            await ctx.send(f"Message with ID `{message}` not found.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")


def setup(bot):
    bot.add_cog(RawPlugin(bot))
