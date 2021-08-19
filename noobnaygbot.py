import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='늅냥아 ')
TOKEN = 'Import a bot token'

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('나는 너무 귀여워❤'))
    print('늅냥을 놀릴시간')

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def 도움말(ctx):
    await ctx.channel.send("```늅냥봇 도움말 = 알아서 찾아```")
    
@bot.command()
async def 죽어(ctx):
    await ctx.channel.send("너나 죽어")

@bot.command()
async def 어디가(ctx):
    await ctx.channel.send("너한테서 도망가는 중")

@bot.command()
async def 사랑해(ctx):
    await ctx.channel.send("나도 사랑함 ㅇㅇ")

@bot.command()
async def 꺼져(ctx):
    await ctx.channel.sendt("잘가")

@bot.command()
async def 커핀(ctx):
    await ctx.channel.send("씹덕")

@bot.command()
async def 셔으링(ctx):
    await ctx.channel.send("착함, 올런한테 디스코드 니트로 빼았음")

@bot.command()
async def 셔을(ctx):
    await ctx.channel.send("착함, 올런한테 디스코드 니트로 빼았음")

@bot.command()
async def 시온(ctx):
    await ctx.channel.send("북극곰")

@bot.command()
async def 엠준(ctx):
    await ctx.channel.send("**M**자 탈모")

@bot.command()
async def 만두(ctx):
    await ctx.channel.send("누구세요")

@bot.command()
async def 늅냥(ctx):
    await ctx.channel.send("커핀보다 똑똑한 **카와이** 늅냥짱!")

@bot.command()
async def 올런(ctx):
    await ctx.channel.send("어르신.. 왜 여기에..")

@bot.command()
async def 자러가(ctx):
    await ctx.channel.send("너 먼저")

@bot.command()
async def 닥쳐(ctx):
    await ctx.channel.send("불러놓고;")

@bot.command()
async def 배추봇(ctx):
    await ctx.channel.send("나 게임 잘함 ")

@bot.command()
async def 미육(ctx):
    await ctx.channel.send("미역줄기 맛있음")

@bot.command()
async def 뱉어(ctx):
    await ctx.channel.send("...")

@bot.command()
async def 짖어(ctx):
    await ctx.channel.send("난 고양이라고")

@bot.command()
async def 야옹(ctx):
    await ctx.channel.send("조용히 해")

@bot.command()
async def 제작자(ctx):
    await ctx.channel.send("올런이 나를 만들었다구! ||아 대사는 커핀||")

@bot.command()
async def 아이스크림(ctx):
    await ctx.channel.send("나는 고양이+아이스크림")

@bot.command()
async def 나가뒤져(ctx):
    await ctx.channel.send("너나;")

@bot.command()
async def 바보(ctx):
    await ctx.channel.send("바부부부붑")


@bot.command()
async def 하픽(ctx):
    await ctx.channel.send("망겜이야;")

@bot.command()
async def 얼불춤(ctx):
    await ctx.channel.send("갓겜이야!")
    await ctx.channel.send("||본 발언에는 봇 제작자의 사적인 의견이 듬뿍 들어가 있습니다||")


@bot.command()
async def 좀비고(ctx):
    await ctx.channel.send("뭔겜이지;")

@bot.command()
async def 마크(ctx):
    await ctx.channel.send("갓겜이야!")

@bot.command()
async def 로블록스(ctx):
    await ctx.channel.send("잼민겜")

@bot.command()
async def 원신(ctx):
    await ctx.channel.send("킹갓제네럴울트라초씹덕갓겜")

@bot.command()
async def 비상식량(ctx):
    await ctx.channel.send("페이몬!")

@bot.command()
async def 공순(ctx):
    await ctx.channel.send("근데 누구세요?")

@bot.command()
async def 솜사탕(ctx):
    await ctx.channel.send("디코에 있길래 넣어봤음 ㅎㅎ! -괴도 커핀")

@bot.command()
async def 승혀니(ctx):
    await ctx.channel.send("디코에 있길래 넣어봤음 ㅎㅎ! -괴도 커핀")

@bot.command()
async def 펭귄(ctx):
    await ctx.channel.send("디코에 있길래 넣어봤음 ㅎㅎ! -괴도 커핀")

@bot.command()
async def 박하사탄(ctx):
    await ctx.channel.send("그림 잘그림 ||근데 누구세요?||")

@bot.command()
async def 따비드(ctx):
    await ctx.channel.send("ㅄ||커핀이 그럼||")

@bot.command()
async def 가루(ctx):
    await ctx.channel.send("마약가루")

@bot.command()
async def 라면(ctx):
    await ctx.channel.send("[라면검열]")

@bot.command()
async def 세림이(ctx):
    await ctx.channel.send("순수한척 하는 변ㅌ((=")

@bot.command()
async def 눼에일위(ctx):
    await ctx.channel.send("스타1을 좋아하는 사람")

@bot.command()
async def wrap(ctx):
    await ctx.channel.send("디코에 있길래 넣어봤음 ㅎㅎ! -괴도 커핀")

@bot.command()
async def 게임하자(ctx):
    await ctx.channel.send("끝말잇기 시작!")
    await ctx.channel.send("3")
    await ctx.channel.send("2")
    await ctx.channel.send("1")
    await ctx.channel.send("인듐")

@bot.command()
async def 마토홀릭(ctx):
    await ctx.channel.send("존경")

@bot.command()
async def 코마(ctx):
    await ctx.channel.send("저거저거 트롤")

@bot.command()
async def 김짱돌(ctx):
    await ctx.channel.send("트롤이야아ㅏㅏ")

@bot.command()
async def 공갈(ctx):
    await ctx.channel.send("트롤이양아ㅏㅏ")

@bot.command()
async def 르마(ctx):
    await ctx.channel.send("스피드런.. 개잘해..")

@bot.command()
async def 이제가(ctx):
    await ctx.channel.send("어우 드디어 해방이다 나도 너랑 놀기 지겨웠어")

@bot.command()
async def 당근먹자(ctx):
    await ctx.channel.send("싫어")

@bot.command()
async def 사귀는거다(ctx):
    await ctx.channel.send("https://cdn.discordapp.com/attachments/871752878275059713/877564301672587304/unknown-1.jpg")

@bot.command()
async def 그루비(ctx):
    await ctx.channel.send("에브리웨어~")

@bot.command()
async def 리듬(ctx):
    await ctx.channel.send("노래 잘불러")

@bot.command()
async def 사귀자(ctx):
    await ctx.channel.send("https://cdn.discordapp.com/attachments/871752878275059713/877564301672587304/unknown-1.jpg")

@bot.command()
async def 프레드봇(ctx):
    await ctx.channel.send("잘불러2222")

@bot.command()
async def 변태(ctx):
    await ctx.channel.send("헤으응... 나.. 죽어..")

@bot.command()
async def 시온서버(ctx):
    await ctx.channel.send("여기")

@bot.command()
async def 날(ctx):
    await ctx.channel.send("싫어")

@bot.command()
async def 이거(ctx):
    await ctx.channel.send("대본 - 커핀, 올런, : 제작 - 올런")

@bot.command()
async def 트위치(ctx):
    await ctx.channel.send("재밌어!")
    await ctx.channel.send("트위치 바로가기 v")
    await ctx.channel.send("https://twitch.tv/")


@bot.command()
async def 유튜브(ctx):
    await ctx.channel.send("너무 재밌어!")
    await ctx.channel.send("유튜브 바로가기 v")
    await ctx.channel.send("https://youtube.com/")

@bot.command()
async def 먹어줘(ctx):
    await ctx.channel.send("헤으응")

@bot.command()
async def 변태야(ctx):
    await ctx.channel.send("아니!")

@bot.command()
async def 때려줘(ctx):
    await ctx.channel.send("에잇!")
    await ctx.channel.send("챨싹")

@bot.command()
async def 섹드립쳐줘(ctx):
    await ctx.channel.send("싫어 그게 뭐야")

@bot.command()
async def 넣어줘(ctx):
    await ctx.channel.send("쓰레기는 쓰레기통에 넣어^^")

@bot.command()
async def 같이자자(ctx):
    await ctx.channel.send("싫어;")

@bot.command()
async def 울어줘(ctx):
    await ctx.channel.send("으에에에에엥..")
    
@bot.command()
async def 웃어줘(ctx):
    await ctx.channel.send("헤헤헤헤헷 :))))))))))))))))))))))))")

@bot.command()
async def 삐졌어(ctx):
    await ctx.channel.send("미안해요..")

@bot.command()
async def ㅅㅅ(ctx):
    await ctx.channel.send("세수")

@bot.command()
async def 오지마(ctx):
    await ctx.channel.send("다쳐..")

@bot.command()
async def 비트박스(ctx):
    await ctx.channel.send("빡치기 닥치기 빡치기 닥치기")

@bot.command()
async def 잘자(ctx):
    await ctx.channel.send("굿나잇!")

@bot.command()
async def 오우야(ctx):
    await ctx.channel.send("ㅗㅜㅑ")

@bot.command()
async def 올런멘션(ctx):
    await ctx.channel.send("<@533910705150361610>")

@bot.command()
async def 늅냥멘션(ctx):
    await ctx.channel.send("<@742217657415237673>")

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send("저리가")

@bot.command()
async def 좋아하는(ctx):
    await ctx.channel.send("난 셔을이 좋더라 ☆*: .｡. o(≧▽≦)o .｡.:*☆")

bot.run('Import A bot token')
