import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure, CommandNotFound
from discord.utils import get
import os



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




###################버튼 클릭함수



#role = discord.utils.get(member.guild.roles, name="Time out") # make sure role is named muted and not Muted
            #await member.add_roles(role)
"""
@buttons.click
async def button_one(ctx, member):
    role = discord.utils.get(member.guild.roles, name="Member") # make sure role is named muted and not Muted
    await member.add_roles(role)
    

await buttons.send(
        channel = channel_,
        components = [
            ActionRow([
                Button(
                    label=":apple: 수락하기", 
                    style=ButtonType().Success, 
                    custom_id="button_one"       
                )
            ])
        ]
    )
    


버튼 함수
"""

access_token = os.environ["BOT_TOKEN"]


client.run(access_token)
