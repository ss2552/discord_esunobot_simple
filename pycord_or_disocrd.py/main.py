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
                
        elif data["d"]["channel_id"] == "1241185004575522968":
            match content:
                case "すいちゃんは〜？":
                    await send("今日も可愛い〜！")
                case "ミオしゃ":
                    await send("うちうち！うちだよ！大神ミオだよ〜！")
                case _:
                    await send(">>>"+content)
bot.run(env.TOKEN)
