import discord
from discord.ext import commands
import psutil
import time

intents = discord.Intents.default()
intents.message_content = True

prefix = "!!"

bot = commands.Bot(command_prefix=prefix, intents=intents)

hug_gif_url = "https://usagif.com/wp-content/uploads/gif/anime-hug-38.gif"
kiss_gif_url = "https://gifsec.com/wp-content/uploads/2022/11/love-anime-gif-42.gif"
slap_gif_url = "https://media.tenor.com/CvBTA0GyrogAAAAC/anime-slap.gif"


@bot.event
async def on_ready():
    print(f'✅ {bot.user} está online corretamente.')

    game = discord.Game("discord.py")
    await bot.change_presence(activity=game, status=discord.Status.dnd)


@bot.command()
async def ping(ctx):
    start_time = time.time()
    embed = discord.Embed(
        title="🏓 Pong!",
        description="O websocket está carregando...",
        color=discord.Color.blurple()
    )
    message = await ctx.send(embed=embed)

    latency = round((time.time() - start_time) * 1000)

    new_embed = discord.Embed(
        title="🏓 Pong!",
        description=f"O websocket está {latency} ms.",
        color=discord.Color.blurple()
    )

    await message.edit(embed=new_embed)


@bot.command()
async def pnerd(ctx):
    cpu_usage = psutil.cpu_percent()

    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"🏗️ Versão do Interpreter: Python 3.11.5\n"
                    f"🖥️ Porcentagem de CPU Usada: {cpu_usage}%\n"
                    f"🖥️ Hospedagem: SquareCloud | Python",
        color=discord.Color.blurple()
    )

    message = await ctx.send(embed=embed)


@bot.command()
async def clear(ctx, amount: int = None):
    if not ctx.author.guild_permissions.manage_messages:
        embed = discord.Embed(
            title="Erro",
            description="Você não tem permissão para apagar mensagens.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    if amount is None:
        embed = discord.Embed(
            title="Erro",
            description="Você precisa especificar a quantidade de mensagens a serem apagadas. Por exemplo: `!!clear 5`",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    elif amount <= 0:
        embed = discord.Embed(
            title="Erro",
            description="A quantidade de mensagens a serem apagadas deve ser maior que 0.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    else:
        await ctx.channel.purge(limit=amount + 1)  # Limpa a quantidade de mensagens especificada
        embed = discord.Embed(
            title="🗑️ Mensagens Apagadas",
            description=f"{amount} mensagens foram apagadas.",
            color=discord.Color.blurple()
        )
        await ctx.send(embed=embed)


@bot.command()
async def kiss(ctx, member: discord.Member = None):
    if member is None:
        embed = discord.Embed(
            title="Erro",
            description="Você precisa mencionar um membro para beijar!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    response = f"{ctx.author.mention} beijou {member.mention}!"
    embed = discord.Embed(description=response, color=discord.Color.blurple())
    embed.set_image(url=kiss_gif_url)
    await ctx.send(embed=embed)


@bot.command()
async def slap(ctx, member: discord.Member = None):
    if member is None:
        embed = discord.Embed(
            title="Erro",
            description="Você precisa mencionar um membro para dar um tapa!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    response = f"{ctx.author.mention} deu um tapa em {member.mention}!"
    embed = discord.Embed(description=response, color=discord.Color.blurple())
    embed.set_image(url=slap_gif_url)
    await ctx.send(embed=embed)


@bot.command()
async def hug(ctx, member: discord.Member = None):
    if member is None:
        embed = discord.Embed(
            title="Erro",
            description="Você precisa mencionar um membro para abraçar!",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        return

    response = f"{ctx.author.mention} abraçou {member.mention}!"
    embed = discord.Embed(description=response, color=discord.Color.blurple())
    embed.set_image(url=hug_gif_url)
    await ctx.send(embed=embed)


@bot.command()
async def curiosidade(ctx):
    embed1 = discord.Embed(
        title="⌨️ Fatos engraçados do Python",
        description="Sabia que para escrever este comando eu usei um marcador chamado `@bot.command()`?",
        color=discord.Color.blurple()
    )

    embed1.add_field(
        name="Decorador",
        value="O @ é uma sintaxe em Python chamada `decorator` (ou decorador). Decorators são usados para modificar ou estender o comportamento de funções ou métodos sem alterar a própria função ou método.",
        inline=False
    )
    embed1.add_field(
        name="Uma instância (ou objeto)",
        value="`bot` se refere a uma instância (um objeto) da classe commands.Bot no Discord.py. A classe commands.Bot é fornecida pela biblioteca Discord.py e representa o bot. A instância bot é criada a partir dessa classe e é usada para definir comandos, lidar com eventos e mais.",
        inline=False
    )
    embed1.add_field(
        name=".command()",
        value="`.command()` é um método (uma função dentro de uma classe) da classe commands.Bot. Quando você usa `@bot.command()`, está dizendo ao Discord.py que a função decorada é um comando que o bot deve reconhecer."
    )

    embed2 = discord.Embed(
        title="Como ficaria este comando em geral?",
        description="Sim, tem muito mais pra aprender, mais é meio complexo, mais caso queira saber como esse comando foi feito pegue minha [source](https://github.com/PowerzinBR/powernerd) aqui!",
        color=discord.Color.blurple()
    )

    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)

# BOTE TOKEN DO SEU BOT COM O TOKEN DO SEU BOT.
bot.run('TOKEN DO SEU BOT')
