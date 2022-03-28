import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, CommandNotFound
from discord.utils import get
import os
from ast import literal_eval
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request
import urllib.parse
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import time
import json
import random
import re
from pytube import YouTube


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='?', intents=intents)




@client.event
async def on_ready():
    print("로그인중")
    print(client.user.name)
    print("connect was sucessful")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("정보수집"))

@client.event
async def on_member_join(member):
    channel = client.get_channel(954705090621616138)
    print(channel)
    
    embed = discord.Embed(title = f"{member.guild.name} 서버에 오신것을 환영합니다.", description = f"{member.mention}님 아래 이모지를 눌러 인증을 완료하여 주세요.", color = 0x6E17E3)
    embed.set_author(name= member,icon_url= member.avatar_url)
    msg = await channel.send(embed=embed)
    await msg.add_reaction("✅")


"""
#인증없는 환영인사
@client.event
async def on_member_join(member):
    channel = await member.create_dm()
    embed = discord.Embed(title = f"{member.guild.name} 서버에 오신것을 환영합니다.", description = f"{member.mention}님 Dm메시지를 확인하여주세요!", color = 0x6E17E3)
    embed.set_author(name= member,icon_url= member.avatar_url)
    embed_ = discord.Embed(title = f"{member.guild.name} 서버에 오신것을 환영합니다.", description = f"{member.mention}님 반갑습니다. **{member.guild.name}**의 서버지킴이 **{client.user.name}**이라고 해요. \n\n 1.가급적 들낙은 자제해주셨으면해요. \n 2.기본적인 예의범절을 지켜주셨으면해요. \n 3. 친목질과 상업성 홍보는 금지하고있어요. \n", color = 0x6E17E3)
    embed_.set_author(name= member,icon_url= member.avatar_url)
    embed_.set_footer(text=f"서버규칙을 잘 확인하셨겠죠? \n문의사항 있으시다면 **{member.guild.name}**의 질문방을 사용하여 주세요.")
    role = discord.utils.get(member.guild.roles, name="Member") # make sure role is named muted and not Muted
    await member.add_roles(role)
    await channel.send(embed=embed_)
    await channel_.send(embed=embed)
"""

@client.command()
async def hello(ctx):
    ch = await ctx.send("반갑다 이기야")



"""
#봇이 정확한 24시간 인증봇이 아니라 대체수단으로 다른것을 씀
@client.command()
async def 인증(ctx):
    try:
        if ctx.message.author.guild_permissions.administrator:
            embed = discord.Embed(title = f"{ctx.guild.name} 서버에 오신것을 환영합니다.", description = f"사용자님 아래 이모지를 눌러 인증을 완료하여 주세요.", color = 0x6E17E3)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("✅")
        else:
            await ctx.send(ctx.author.mention + "님은 관리자 권한이 없습니다.")
    except:
        await ctx.send("봇의 권한이 부족합니다 \n관리자 권한이 부여되어있는지 확인하여주세요.")   
            
"""         

@client.event
async def on_reaction_add(reaction, member):
    if member.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "✅":
        channel = await member.create_dm()
        
        embed_ = discord.Embed(title = f"{member.guild.name} 서버에 오신것을 환영합니다.", description = f"{member.mention}님 반갑습니다. **{member.guild.name}**의 서버지킴이 **{client.user.name}**이라고 해요. \n\n 1.가급적 들낙은 자제해주셨으면해요. \n 2.기본적인 예의범절을 지켜주셨으면해요. \n 3. 친목질과 상업성 홍보는 금지하고있어요. \n", color = 0x6E17E3)
        embed_.set_author(name= member,icon_url= member.avatar_url)
        embed_.set_footer(text=f"서버규칙을 잘 확인하셨겠죠? \n문의사항 있으시다면 **{member.guild.name}**의 질문방을 사용하여 주세요.")
        role = discord.utils.get(member.guild.roles, name="유저 - 인증완료") # make sure role is named muted and not Muted
        await member.add_roles(role)
        await channel.send(embed=embed_)


@client.command()
async def 청소(ctx, amount : int):
    try:
        if ctx.message.author.guild_permissions.administrator:
            if amount > 100:
                await ctx.send(ctx.author.mention + "한번에 너무 많은 메시지를 삭제시킬수 없습니다. \n x최대 `100`개의 메시지 까지만 삭제시킬수 있습니다.")
            else:
                channel = ctx.channel.id
                await ctx.channel.purge(limit=amount)
                embed = discord.Embed(title = "메시지 삭제가 정상적으로 처리되었습니다.", description = f"관리자 - {ctx.author.mention}({ctx.author})님의 의하여 \n메시지 `{amount}`개가 삭제처리되었습니다.")
                await ctx.send(embed=embed)
        else:
            await ctx.send(ctx.author.mention + "님은 관한 없습니다.")
    except:
        await ctx.send("봇에 권한이 부족합니다 \n관리자 권한이 부여되어있는지 확인하여주세요.")






@client.command(name="정보")
async def server_information(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}서버 정보", description="서버정보 - Information of this Server", color=discord.Colour.blue())
    embed.add_field(name='🆔서버 ID', value=f"`{ctx.guild.id}`", inline=False)
    embed.add_field(name='📆만들어진 날짜', value=ctx.guild.created_at.strftime("`%y년-%m월-%d일`"), inline=False)
    embed.add_field(name='👑서버주인', value=f"{ctx.guild.owner.mention}({ctx.guild.owner})", inline=False)
    embed.add_field(name='👥맴버', value=f'`{ctx.guild.member_count}` 명', inline=False)
    embed.add_field(name='💬채널', value=f'체팅체널 : `{len(ctx.guild.text_channels)}` \n음성체널 : `{len(ctx.guild.voice_channels)}`', inline=False)
    embed.add_field(name='🌎공개범위', value=f'{ctx.guild.region}', inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url) 
    embed.set_footer(text="⭐ • K-Jam")    

    await ctx.send(embed=embed)
    
    

        
    

@client.command(name="킥", pass_context=True)
async def Kick(ctx, nick: discord.Member, *, content):
    wr_channel = client.get_channel(954730121221242900)
    try:
        if ctx.message.author.guild_permissions.administrator:
            member = nick
            #role = discord.utils.get(member.guild.roles, name="Time out") # make sure role is named muted and not Muted
            #await member.add_roles(role)
            channel = await member.create_dm()
            embed=discord.Embed(title= f"추방 - {ctx.guild.name}서버", description="정보 - Kick", color=0x206694)
            embed.add_field(name = "관리자 : ", value = ctx.author.mention + f"({ctx.author})", inline = False)
            embed.add_field(name = "유저 : ", value = nick, inline = False)
            embed.add_field(name = "사유: ", value = f"`{content}`", inline = False)
            await wr_channel.send(embed=embed)
            await channel.send(embed=embed)
            await member.kick()
        else:
            await ctx.send("관리자권한이 없습니다.")
    except:
        if ctx.message.author.guild_permissions.administrator:
            member = nick
            #role = discord.utils.get(member.guild.roles, name="Time out") # make sure role is named muted and not Muted
            #await member.add_roles(role)
            embed=discord.Embed(title= f"추방 - {ctx.guild.name}서버", description="정보 - Kick", color=0x206694)
            embed.add_field(name = "관리자 : ", value = ctx.author.mention + f"({ctx.author})", inline = False)
            embed.add_field(name = "유저 : ", value = nick, inline = False)
            embed.add_field(name = "사유: ", value = f"`{content}`", inline = False)
            await wr_channel.send(embed=embed)
            await member.kick()
        else:
            await ctx.send("관리자권한이 없습니다.")


@client.command(name="경고", pass_context=True)
async def Warning(ctx, nick: discord.Member, *, content):
    wr_channel = client.get_channel(954730121221242900)
    try:
        if ctx.message.author.guild_permissions.administrator:
            member = nick
            role = discord.utils.get(member.guild.roles, name="경고") # make sure role is named muted and not Muted
            await member.add_roles(role)
            channel = await member.create_dm()
            embed=discord.Embed(title= f"경고 - {ctx.guild.name}서버", description="정보 - Warning", color=0x206694)
            embed.add_field(name = "관리자 : ", value = ctx.author.mention + f"({ctx.author})", inline = False)
            embed.add_field(name = "유저 : ", value = nick, inline = False)
            embed.add_field(name = "사유: ", value = f"`{content}`", inline = False)
            await wr_channel.send(embed=embed)
            await channel.send(embed=embed)
        else:
            await ctx.send("관리자권한이 없습니다.")
    except:
        if ctx.message.author.guild_permissions.administrator:
            member = nick
            role = discord.utils.get(member.guild.roles, name="경고") # make sure role is named muted and not Muted
            await member.add_roles(role)
            embed=discord.Embed(title= f"경고 - {ctx.guild.name}서버", description="정보 - Warning", color=0x206694)
            embed.add_field(name = "관리자 : ", value = ctx.author.mention + f"({ctx.author})", inline = False)
            embed.add_field(name = "유저 : ", value = nick, inline = False)
            embed.add_field(name = "사유: ", value = f"`{content}`", inline = False)
            await wr_channel.send(embed=embed)
        else:
            await ctx.send("관리자권한이 없습니다.")


@client.command(name="차단", pass_context=True)
async def Ban(ctx, nick: discord.Member, *, content):
    wr_channel = client.get_channel(954730121221242900)
    try:
        if ctx.message.author.guild_permissions.administrator:
            member = nick
            #role = discord.utils.get(member.guild.roles, name="경고") # make sure role is named muted and not Muted
            #await member.add_roles(role)
            channel = await member.create_dm()
            embed=discord.Embed(title= f"차단 - {ctx.guild.name}서버", description="정보 - Ban", color=0x206694)
            embed.add_field(name = "관리자 : ", value = ctx.author.mention + f"({ctx.author})", inline = False)
            embed.add_field(name = "유저 : ", value = nick, inline = False)
            embed.add_field(name = "사유: ", value = f"`{content}`", inline = False)
            await wr_channel.send(embed=embed)
            await channel.send(embed=embed)
            await member.ban()
        else:
            await ctx.send("관리자권한이 없습니다.")
    except:
        if ctx.message.author.guild_permissions.administrator:
            member = nick
            #role = discord.utils.get(member.guild.roles, name="경고") # make sure role is named muted and not Muted
            #await member.add_roles(role)
            embed=discord.Embed(title= f"차단 - {ctx.guild.name}서버", description="정보 - Ban", color=0x206694)
            embed.add_field(name = "관리자 : ", value = ctx.author.mention + f"({ctx.author})", inline = False)
            embed.add_field(name = "유저 : ", value = nick, inline = False)
            embed.add_field(name = "사유: ", value = f"`{content}`", inline = False)
            await wr_channel.send(embed=embed)
            await member.ban()
        else:
            await ctx.send("관리자권한이 없습니다.")













user = []
musictitle = []
song_queue = []
musicnow = []

userF = []
userFlist = []
allplaylist = []


number = 1



def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    driver = load_chrome_driver()
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()
    
    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()
    
    return music, URL

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(client.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 

def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))


    else:
        if not vc.is_playing():
            client.loop.create_task(vc.disconnect())


def load_chrome_driver():
      
    options = webdriver.ChromeOptions()

    options.binary_location = os.getenv('GOOGLE_CHROME_BIN')

    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(executable_path=str(os.environ.get('CHROME_EXECUTABLE_PATH')), chrome_options=options)            

def again(ctx, url):
    global number
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if number:
        with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        if not vc.is_playing():
            vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e: again(ctx, url))



@client.event
async def on_ready():
    print("로그인중")
    print(client.user.name)
    print("connect was sucessful")
    
    if not discord.opus.is_loaded():
        discord.opus.load_opus('opus')
    
@client.command()
async def 도움(ctx):
    embed = discord.Embed(title = "음악한곡", description = "유튜브 라이센스를 사용합니다.", color = 0x6E17E3) 
    embed.add_field(name = client.command_prefix + "도움", value = "명령어를 볼수 있습니다,", inline = False)
    embed.add_field(name = client.command_prefix + "들어와", value = "뮤직봇이 음성채널에 들어갑니다.", inline = False)
    embed.add_field(name = client.command_prefix + "나가", value = "뮤직봇이 채널에서 나갑니다.", inline = False)
    embed.add_field(name = client.command_prefix + "재생 [노래 이름]  [작곡가] ", value = "유튜브검색기능을 활용하여 찾아드립니다.", inline = False)
    embed.add_field(name = client.command_prefix + "반복재생 [노래 이름] [작곡가] ", value = "찾은 노래를 반복재생합니다..", inline = False)
    embed.add_field(name = client.command_prefix + "목록", value = "자신의 플레이 리스트를 볼수있습니다", inline = False)
    embed.add_field(name = client.command_prefix + "목록초기화", value = "목록에 있는 모든 대기열을 삭제합니다", inline = False)
    embed.add_field(name = client.command_prefix + "목록추가 [노래 이름] [작곡가]", value = "음악이 목록에 추가됩니다.", inline = False)
    embed.add_field(name = client.command_prefix + "목록삭제 [대기열 번호]", value = "대기열에 있는 목록이 삭제됩니다..", inline = False)
    embed.add_field(name = client.command_prefix + "차트", value = "멜론 차트순위 1~10위까지의 노래를 가져옵니다.", inline = False)
    embed.add_field(name = client.command_prefix + "가사 [노래이름]", value = "노래재목과 유사한 노래 1~5개 까지의 리스트를 뽑아옵니다.", inline = False)
    embed.add_field(name = client.command_prefix + "선택 [번호]", value = "선택된 노래의 가사를 가져옵니다.", inline = False)
    await ctx.send(embed=embed)
    
    



@client.command(aliases = ('ㄷ', '컴온', '들와', '참가'))
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send(f"{ctx.author.mention} 채널에 유저가 접속해있지 않습니다.")

@client.command(aliases=('나가', 'ㄲ', '안해', '끄기'))
async def 꺼져(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send(f"{ctx.author.mention} 이미 그 채널에 속해있지 않아요.")


@client.command()
async def URL재생(ctx, *, url):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send(f"{ctx.author.mention} 채널에 유저가 접속해있지 않습니다.")

            
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "을(를) 재생하고 있습니다.", color = 0x00ff00))
    else:
        await ctx.send("노래가 이미 재생되고 있습니다!")

@client.command(aliases=('탐색', '시작', '플레이', 'ㅈㅅ'))
async def 재생(ctx, *, msg):


    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send(f"{ctx.author.mention} 채널에 유저가 접속해있지 않습니다.")


    
    if not vc.is_playing():

        #selenium웹 드라이버를 보이지 않게하는 설정
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("lang=ko_KR")

        
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        driver = load_chrome_driver()
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl
        
        yt = YouTube(url)

        #드라이버 닫기

        driver.quit()

        musicnow.insert(0, entireText)

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        embed = discord.Embed(title= "노래 재생", description = "현재 " + "[{0}](<{1}>)".format(entireText, url) + "을(를) 재생하고 있습니다.", color = 0x00ff00)
        embed.add_field(name = '재생시간', value = str(yt.length) + "초", inline = False)
        embed.add_field(name = '평점', value = str(yt.rating) + "회", inline = False)
        embed.set_footer(text = '게시자 - ' + yt.author)
        embed.set_thumbnail(url=yt.thumbnail_url)
        await ctx.send(embed=embed)
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e: play_next(ctx))
    else:
        user.append(msg)
        result,URLTEST = title(msg)
        song_queue.append(URLTEST)
        await ctx.send("이미 노래가 재생 중이라" + result + "을(를) 대기열로 추가시켰습니다")
        

        
@client.command()
async def 스킵(ctx):
    if len(user) >= 1:
        if vc.is_playing():
            vc.stop()
            global number
            number = 0
            await ctx.send(embed = discord.Embed(title = "스킵", description = musicnow[1] + "을(를) 다음에 재생합니다!", color = 0x00ff00))
        else:
            await ctx.send("노래가 이미 재생되고 있어요!")
    else:
        await ctx.send("더이상 스킵할 노래가 없습니다.")
        

@client.command(aliases=('ㅈㅈ', 'ㅇㅅㅈㅈ'))
async def 일시정지(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "일시정지", description = musicnow[0] + "을(를) 일시정지 했습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@client.command(aliases=('ㄷㅅㅈㅅ', '리플레이'))
async def 다시재생(ctx):
    try:
        vc.resume()
    except:
         await ctx.send("지금 노래가 재생되지 않네요.")
    else:
         await ctx.send(embed = discord.Embed(title= "다시재생", description = musicnow[0]  + "을(를) 다시 재생했습니다.", color = 0x00ff00))

@client.command(aliases=('ㄲㄱ', '노래스탑'))
async def 노래끄기(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "노래끄기", description = musicnow[0]  + "을(를) 종료했습니다.", color = 0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")


@client.command(aliases=('지금나오는거', '현재노래', '노래정보'))
async def 지금노래(ctx):
    if not vc.is_playing():
        await ctx.send("지금은 노래가 재생되지 않네요..")
    else:
        await ctx.send(embed = discord.Embed(title = "지금노래", description = "현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color = 0x00ff00))


@client.command(aliases=('ㅁㄹㅊㄱ', '목록추가'))
async def 대기열추가(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "를 재생목록에 추가했어요!")

@client.command(aliases=('ㅁㄹㅅㅈ', '목록삭제'))
async def 대기열삭제(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await ctx.send("대기열이 정상적으로 삭제되었습니다.")
    except:
        if len(list) == 0:
            await ctx.send("대기열에 노래가 없어 삭제할 수 없어요!")
        else:
            if len(list) < int(number):
                await ctx.send("숫자의 범위가 목록개수를 벗어났습니다!")
            else:
                await ctx.send("숫자를 입력해주세요!")

@client.command(aliases=('ㅁㄹ', '대기열'))
async def 목록(ctx):
    if len(musictitle) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await ctx.send(embed = discord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))

@client.command(aliases=('ㅁㄹㅊㄱㅎ', '대기열초기화'))
async def 목록초기화(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다. 이제 노래를 등록해볼까요?""", color = 0x00ff00))
    except:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")

@client.command(aliases=('ㅁㄹㅈㅅ', '대기열재생'))
async def 목록재생(ctx):

    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send(f"{ctx.author.mention} 채널에 유저가 접속해있지 않습니다.")

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(user) == 0:
        await ctx.send("아직 아무노래도 등록하지 않았어요.")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(ctx)
        else:
            await ctx.send("노래가 이미 재생되고 있어요!")




@client.command()
async def 차트(ctx):
    RANK = 10
 
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get('https://www.melon.com/chart/week/index.htm', headers = header) ## 주간 차트를 크롤링 할 것임
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')
 
    titles = parse.find_all("div", {"class": "ellipsis rank01"}) 
    singers = parse.find_all("div", {"class": "ellipsis rank02"}) 
    albums = parse.find_all("div",{"class": "ellipsis rank03"})
 
    title = []
    singer = []
    album = []
 
    for t in titles:
        title.append(t.find('a').text)
 
    for s in singers:
        singer.append(s.find('span', {"class": "checkEllipsis"}).text)

    for a in albums:
        album.append(a.find('a').text)

   
    embed = discord.Embed(title = "Music chart", description = "출처 - 멜론 공식사이트", color = 0x6E17E3)
    for i in range(RANK):
        embed.add_field(name='%3d위: %s [ %s ] - %s'%(i+1, title[i], album[i], singer[i]), value = "ㅤ")
        embed.set_footer(text="주간순위")
        #value -> 공백문자임
    await ctx.send(embed=embed)
            
            
       
        
        
        
        


@client.command(aliases=('ㅂㅂㅈㅅ', '계속재생'))
async def 반복재생(ctx, *, msg):
    
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
      
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()   
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            pass
    
    global entireText
    global number
    number = 1
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(musicnow) - len(user) >= 1:
        for i in range(len(musicnow) - len(user)):
            del musicnow[0]
            
    driver = load_chrome_driver()
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    entireText = entireNum.text.strip()
    musicnow.insert(0, entireText)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com'+test1
    yt = YouTube(url)
    embed = discord.Embed(title= "반복재생", description = "현재 " + "[{0}](<{1}>)".format(musicnow[0], url)+ "을(를) 반복재생하고 있습니다.", color = 0x00ff00)
    embed.add_field(name = '재생시간', value = str(yt.length) + "초", inline = False)
    embed.add_field(name = '평점', value = str(yt.rating) + "회", inline = False)
    embed.set_footer(text = '게시자 - ' + yt.author)
    embed.set_thumbnail(url=yt.thumbnail_url)
    await ctx.send(embed = embed)
    again(ctx, url)



@client.command()
async def 가사(ctx, song):
    global datas
    global title1

    
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    
    # webdriver 생성 및 대기
    driver = load_chrome_driver()
    driver.implicitly_wait(2)
    # 곡 입력 및 url 접근
    driver.get('https://vibe.naver.com/search/tracks?query='+song)
    time.sleep(2)
    # 페이지 HTML 소스 받기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 곡 목록 받아오기
    tbody = soup.select_one('div.tracklist > table > tbody')
    trs = tbody.select('tr')
    datas = []
    count = 0
    embed = discord.Embed(title = "Music chart", description = "출처 - 멜론 공식사이트", color = 0x6E17E3)

    for tr in trs:
        title1 = tr.select_one('td.song > div.title_badge_wrap > span > a').get_text()
        artist = tr.select_one('td.artist > span > span > span > a > span').get_text()
        title_id = tr.select_one('td.song > div.title_badge_wrap > span > a')['href']
        datas.append([title1, artist, title_id])
        if count < 4:
            count += 1
        else:
            driver.quit()
            break


    for i in range(count+1):
        embed.add_field(name=f'{i+1}번 : {datas[i][0]} by {datas[i][1]}', value = "ㅤ")
    embed.add_field(name="찾으시는 곡번을 선택해주세요.\n 종료하시려면 0번을 입력해주세요.", value = "ㅤ")
    embed.set_footer(text="출처 - 바이브 공식사이트")
    driver.quit()
    await ctx.send(embed=embed)
    try:
        pass
    except:
        await ctx.send("불러오는 도중 오류가 발생하거나 검색하신 내용이 없어요..")




            

@client.command()
async def 선택(ctx, menu):
    try:
        pass 
    except:
        await ctx.send("선택하신 사항이 없어요..")
    mem = 0
    mem = int(menu)
    
    

    
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = load_chrome_driver()
    
    embed = discord.Embed(title = "Music lyrics", description = "출처 - 바이브 공식사이트", color = 0x6E17E3)
    if mem == 0:
        await ctx.send("종료했습니다.")
        driver.quit()
            
        
    else:
        driver.get('https://vibe.naver.com'+datas[mem-1][2])
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        lyrics = soup.select_one('#content > div > p.lyrics').get_text()
        for i in range(0, len(lyrics),1024):
            embed.add_field(name=title1, value = lyrics[i:i+1024])
            embed.set_footer(text="출처 - 바이브 공식사이트")
            await ctx.send(embed=embed)
        
        
            
            
    driver.quit()

access_token = os.environ["BOT_TOKEN"]


client.run(access_token)
