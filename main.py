from discord import Client, Intents
i = Intents.default()
i.message_content = True
bot = Client(intents = i)

@bot.event
async def on_message(ctx):
    if not ctx.author.bot:
        if ctx.content == "( ・∇・)":
            res = "( ・∇・)"
            
        elif "えい！" in ctx.content:
            res = "えい！"
            
        elif ctx.content.startswith("オウム返し"):
            r = ctx.content.removeprefix('オウム返し')
            res = r if r else "えい！"
            
        elif ctx.channel.id == env.CAHNNEL_ID:
            match ctx.content:
                case "すいちゃんは〜？":
                    res = "今日も可愛い〜！"
                case "ミオしゃ":
                    res = "うちうち！うちだよ！大神ミオだよ〜！"
            return
        else:
            return
        await ctx.channel.send(res)
bot.run(env.TOKEN)
