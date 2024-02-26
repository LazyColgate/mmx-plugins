import discord
from discord.ext import commands


class ChannelTag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.api.get_plugin_partition(self)

    @commands.command()
    async def tag(self, ctx, prefix: str = None):
        query = {prefix: f"《{prefix}》"}
        self.coll.find_one(query)
        if prefix:
            channel_name = ctx.channel.name

            new_channel_name = f'《{prefix}》-{channel_name}'

            # Update the channel with the new name
            await ctx.channel.edit(name=new_channel_name)
            await ctx.send(f'> Channel tag updated to: {new_channel_name}')
        else:
            await ctx.send('> Error: prefix not found. Please enter an existing tag.')\


    @commands.command()
    async def tag_add(self, ctx, prefix: str = None):
        if prefix:
            await self.coll.insert_one({prefix: f"《{prefix}》"})
            await ctx.send(f'> `《{prefix}》` added to database.')
        else:
            await ctx.send('> Error: invalid arguments. Please enter a valid tag.')


def setup(bot):
    bot.add_cog(ChannelTag(bot))
