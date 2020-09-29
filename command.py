reactions = ["👍", "👎"]

@bot.command()
async def poll(ctx, *, question):
    m = await ctx.send(f"Poll: {question} -{ctx.author}")
    for name in reactions:
        emoji = get(ctx.guild.emojis, name=name)
        await m.add_reaction(emoji or name)
