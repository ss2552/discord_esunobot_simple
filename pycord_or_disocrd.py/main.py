from discord import Client, Intents
i = Intents.default()
i.message_content = True
bot = Client(intents = i)

@bot.event
async def on_message(ctx):
    if not ctx.author.bot:
        send = lambda c: ctx.channel.send(c)
        if content == "( ・∇・)":
            await send("( ・∇・)")
            
        elif "えい！" in content:
            await send("えい！")
            
        elif content.startswith("オウム返し"):
            res = content.removeprefix('オウム返し')
            if not res:
                await send("えい！")
            else:
                await send(res)
                
bot.run(env.TOKEN)
