from discord import Client, Intents
i = Intents.default()
i.message_content = True
bot = Client(intents = i)

@bot.event
async def on_message(ctx):
    if not ctx.author.bot:
        if ctx.content == "( ・∇・)":
            res = "( ・∇・)"
        elif ctx.content.startswith("オウム返し"):
            res = ctx.content.removeprefix('オウム返し')
            if not res:
                res = "えい！"
        elif ctx.channel.id == env.CHANNEL_ID:
            match ctx.content:
                case "すいちゃんは〜？":
                    res = "今日も可愛い〜！"
                case "ミオしゃ":
                    res = "うちうち！うちだよ！大神ミオだよ〜！"
        elif "えい！" in ctx.content:
            res = "えい！"
        await ctx.channel.send(res)
bot.run(env.TOKEN)
