import time
import discord
from discord.ext import commands
import youtube_dl
import asyncio
from youtubesearchpython import VideosSearch
import random
from random import *
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageFont, ImageDraw
import numpy as np
import requests
import csv
from larousse_api import larousse

image_types = ["png", "jpeg", "gif", "jpg"]

bot = commands.Bot(command_prefix = "!", help_command=None)
musics = {}
ytdl = youtube_dl.YoutubeDL({"format": "bestaudio/best"})

@bot.event
async def on_ready():
    print("Bot lancé")
    await bot.change_presence(activity=discord.Game(name="!help"))

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "**Commandes**", description = "**Divers**\n\n:speaking_head: !parler : _Parler avec ce superbe bot_\n\n:wave: !slt : _Saluer ce magnifique bot_\n\n:loudspeaker: !dis [texte] : _Demander de au bot de dire quelque chose_\n\n:gem: !beau / !belle [nom] : _Complimenter quelqu'un_\n\n:poop: !moche [nom] : _Insulter quelqu'un_\n\n:dash: !efface / *clear [nombre] : _Effacer [nombre] messages (modo only)_\n\n:joy_cat: !blague : _Pour exploser de rire devant une blague trop drôle_\n\n:cat: !chat : _Pour afficher une magnifique image de chat !_\n\n:camera: !pp : _Donne ta pp en bonne qualité_\n\n:camera_with_flash: !pp [membre] : _Donne la pp du membre mentionné_\n\n**Édition d'image**\n\n:frame_photo: !images / image : _Liste des commandes pour l'édition d'image'_\n\n:clown: !meme [texte 1] ; [texte 2] : _Faire un meme de l'image envoyée avec en haut le texte 1 et en bas le texte 2 (notext à la place d'un des deux textes pour ne rien écrire ici)_\n\n:x: **Musique** :x:\n\n:notes: !musique : _**En développement** ~~Liste des commandes pour la musique~~_\n\n:radio: !playlist : _**En développement** ~~Liste des commandes pour la playlist~~_\n\n", colour = discord.Colour.blue())
    await ctx.send(embed = embed)
    print("h")
    
@bot.command()
async def musique(ctx):
    embed = discord.Embed(title = "**Commandes**", description = "**Musique**\n\n:arrow_forward: *play / *p [nom / lien de musique] : _Lance la musique_\n\n:pause_button: *pause / *pa : _Met la musique en pause_\n\n:play_pause: *resume / *r : _Reprendre la musique_\n\n:track_next: *skip / *s : _Passer à la musique suivante_\n\n:x: *disconnect / *leave / *l : _Faire partir le bot_\n\n:radio: *playlist : _Liste des commandes pour la playlist_", colour = discord.Colour.blue())
    await ctx.send(embed = embed)
    print("musique")

@bot.command()
async def image(ctx):
    embed = discord.Embed(title = "**Commandes**", description = "**Édition d'image**\n\n:movie_camera: *edit monochrome : _Met l'image envoyée en noir et blanc_\n\n:crayon: *edit saturation : _Saturer les couleurs de l'image envoyée_\n\n:bulb: *edit luminosité / luminosite : _Modifier la luminosité de l'image envoyée_\n\n:last_quarter_moon: *edit contraste : _Modifier le constraste de l'image envoyée_\n\n:eyeglasses: *edit flou : _Flouter l'image envoyée_\n\n:writing_hand: *edit text / texte : _Mettre du texte (type meme) sur l'image envoyée_\n\n:memo: *edit text+ / texte+ : _Pareil que *text, mais avec plus de modifications_\n\n:clown: *meme [texte 1] ; [texte 2] : _Faire un meme de l'image envoyée avec en haut le texte 1 et en bas le texte 2 (notext à la place d'un des deux textes pour ne rien écrire ici)_", colour = discord.Colour.blue())
    await ctx.send(embed = embed)
    print("image")

@bot.command()
async def images(ctx):
    utilisateur = ctx.message.author
    embed = discord.Embed(title = "**Commandes**", description = "**Édition d'image**\n\n:movie_camera: *edit monochrome : _Met l'image envoyée en noir et blanc_\n\n:crayon: *edit saturation : _Saturer les couleurs de l'image envoyée_\n\n:bulb: *edit luminosité / luminosite : _Modifier la luminosité de l'image envoyée_\n\n:last_quarter_moon: *edit contraste : _Modifier le constraste de l'image envoyée_\n\n:eyeglasses: *edit flou : _Flouter l'image envoyée_\n\n:writing_hand: *edit text / texte : _Mettre du texte (type meme) sur l'image envoyée_\n\n:memo: *edit text+ / texte+ : _Pareil que *text, mais avec plus de modifications_\n\n:clown: *meme [texte 1] ; [texte 2] : _Faire un meme de l'image envoyée avec en haut le texte 1 et en bas le texte 2 (notext à la place d'un des deux textes pour ne rien écrire ici)_", colour = discord.Colour.blue())
    await ctx.send(embed = embed)
    print(f"images, {utilisateur}")

@bot.command()
async def slt(ctx):
    pseudo = ctx.message.author.mention
    utilisateur = ctx.message.author
    await ctx.send(f"slt {pseudo} le plus bg des bgs")
    print(f"slt, {utilisateur}")
    
@bot.command()
async def dis(ctx, *texte):
    utilisateur = ctx.message.author
    messages = await ctx.channel.history(limit = 1).flatten()
    await ctx.send(" ".join(texte))
    time.sleep(2)
    await ctx.message.delete()
    print(f"dis, {utilisateur}")
    
@bot.command()
async def beau(ctx, *nom):
    utilisateur = ctx.message.author
    await ctx.send(" ".join(nom) +" est trop beau")
    time.sleep(2)
    await ctx.message.delete()
    print(f"beau, {utilisateur}")
    
@bot.command()
async def belle(ctx, *nom):
    utilisateur = ctx.message.author
    await ctx.send(" ".join(nom) +" est trop belle")
    time.sleep(2)
    await ctx.message.delete()
    print(f"belle {utilisateur}")
    
@bot.command()
async def moche(ctx, *nom):
    utilisateur = ctx.message.author
    await ctx.send(" ".join(nom) +" est trop moche")
    time.sleep(2)
    await ctx.message.delete()
    print(f"moche, {utilisateur}")

@bot.command()
async def definition(ctx, mot):
    utilisateur = ctx.message.author
    await ctx.send(f"**{mot} :**")
    resultat = larousse.get_definitions(mot)
    for i in range (len(resultat)):
        time.sleep(0.4)
        await ctx.send(f"_{i + 1}_ : {resultat[i]}")
    print(f"definition {mot}, {utilisateur}")

@bot.command()
async def pp(ctx, user : discord.User = None):
    utilisateur = ctx.message.author
    if user == None:
        logo = ctx.message.author.avatar_url_as(static_format='png')
        response = requests.get(logo)
        dossier = open("image.png", "wb")
        dossier.write(response.content)
        dossier.close()
    else:
        logo = user.avatar_url_as(static_format='png')
        response = requests.get(logo)
        dossier = open("image.png", "wb")
        dossier.write(response.content)
        dossier.close()
    image = discord.File('image.png')
    await ctx.send(file=image)
    print(f"pp, {utilisateur}")

@bot.command()
async def pileouface(ctx):
    utilisateur = ctx.message.author
    print(f"pile ou face, {utilisateur}")
    await ctx.send("3...")
    time.sleep(1)
    await ctx.send("2...")
    time.sleep(1)
    await ctx.send("1...")
    time.sleep(1)
    pileface = randint(1,2)
    if pileface == 1:
        await ctx.send("Pile !")
        print("pile")
    else:
        await ctx.send("Face !")
        print("face")

@bot.command()
async def blague(ctx):
    utilisateur = ctx.message.author
    blague = randint(1 ,5)
    print(f"blague {blague}, {utilisateur}")
    time.sleep(0.4)
    if blague == 1:
        await ctx.send("Comment s'appelle le journal publié chaque semaine au Sahara ?")
        time.sleep(1.5)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1.5)
        await ctx.send("L'hebdromadaire ! :rofl: :rofl: :rofl: :rofl:")
    elif blague == 2:
        await ctx.send("Qu'est-ce qu'un canife ?")
        time.sleep(1.5)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1.5)
        await ctx.send("Un petit fien ! :rofl: :rofl: :rofl: :rofl:")
    elif blague == 3:
        await ctx.send("Quel est le sport le plus silencieux ?")
        time.sleep(1.5)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1.5)
        await ctx.send("Le parachhhhhhhuuuuuuuuutt ! :rofl: :rofl: :rofl: :rofl:")
    elif blague == 4:
        await ctx.send("Qu'est ce qu'un petit cheval dans un piscine ?")
        time.sleep(1.5)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1.5)
        await ctx.send("Un poney de bain ! :rofl: :rofl: :rofl: :rofl:")
    else:
        await ctx.send("Comment appelle-t-on un roux dans un four ?")
        time.sleep(1.5)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1)
        await ctx.send(".")
        time.sleep(1.5)
        await ctx.send("Un roux-ti ! :rofl: :rofl: :rofl: :rofl:")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def efface(ctx, nombre : int):
    utilisateur = ctx.message.author
    print(f"efface {nombre}, {utilisateur}")
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for i in messages:
        await i.delete()
    if nombre > 1:
        await ctx.send(f"{nombre} messages effacés")
    else:
        await ctx.send(f"{nombre} message effacé")
    time.sleep(3)
    msg = await ctx.channel.history(limit = 1).flatten()
    for o in msg:
        await o.delete()
        
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre : int):
    utilisateur = ctx.message.author
    print(f"clear {nombre}, {utilisateur}")
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for i in messages:
        await i.delete()
    if nombre > 1:
        await ctx.send(f"{nombre} messages effacés")
    else:
        await ctx.send(f"{nombre} message effacé")
    time.sleep(3)
    msg = await ctx.channel.history(limit = 1).flatten()
    for o in msg:
        await o.delete()

@bot.command()
async def amogus(ctx):
    utilisateur = ctx.message.author
    print(f"AMOGUS, {utilisateur}")
    amongus = ["https://media.tenor.com/images/8c5ff8ddd6f574ecde6dc00f7d336c02/tenor.gif", 
        "https://media1.tenor.com/images/e8f41309aa52e5ab33bbc15d6a7391ac/tenor.gif?itemid=18967013", 
        "https://media1.tenor.com/images/dba4ecfc0c45b7c1c4a85a5a08b485b9/tenor.gif?itemid=19469635", 
        "https://media.tenor.com/images/cfa174759d18a5d62a963650821addf1/tenor.gif", 
        "https://i.pinimg.com/originals/bb/d8/a2/bbd8a2470f1cf5587bbbeb6af3672fc5.gif", 
        "https://data.photofunky.net/output/image/f/a/5/9/fa595a/photofunky.gif", 
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f74b27b3-b4a2-4487-90c4-68a13f9a49e1/dedpj5k-47009527-ff28-444b-b391-d873bbda52fc.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2Y3NGIyN2IzLWI0YTItNDQ4Ny05MGM0LTY4YTEzZjlhNDllMVwvZGVkcGo1ay00NzAwOTUyNy1mZjI4LTQ0NGItYjM5MS1kODczYmJkYTUyZmMuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.2CqsEseZpiln6AtlMuLvdCmjaog-3b2f34X5dYFSpZ0"]
    gif = choice(amongus)
    await ctx.send(f"AMOGUS\n{gif}")

@bot.command()
async def chat(ctx):
    utilisateur = ctx.message.author
    print(f"CHAT, {utilisateur}")
    chat = ["https://tenor.com/view/cat-eyes-cat-cats-cat-fun-funny-cat-gif-17596620", 
        "https://tenor.com/view/cat-broken-cat-cat-drinking-cat-licking-cat-air-gif-20661740", 
        "https://tenor.com/view/sassy-cats-angry-mad-ok-gif-9934420", 
        "https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800", 
        "https://tenor.com/view/cat-cute-cat-cats-cattitude-chat-gif-17603052", 
        "https://tenor.com/view/catjam-cat-dancing-cat-music-music-cat-cute-cat-gif-23392229", 
        "https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800"]
    gif = choice(chat)
    await ctx.send(f"CHAT\n{gif}")

@bot.command()
async def parler(ctx, *message):
    utilisateur = ctx.message.author
    print(f"parler, {utilisateur}")
    channel = ctx.channel
    user = ctx.message.author
    nombre = randint(1, 3)
    print(nombre)
    if nombre == 1:
        await channel.send('Slt ça va ?')
    elif nombre == 2:
        await channel.send('Bonjour, tu vas bien ?')
    else:
        await channel.send('Saluuuuuuuut comment ça va ?')

    def check(m):
        return m.channel == channel and user == m.author

    msg = await bot.wait_for('message', timeout = 60, check=check)
    time.sleep(0.4)
    nombre = randint(1, 3)
    print(nombre)
    if nombre == 1:
        await channel.send("> {.content}\n\nTant que t'as la santé on va dire que tout va bien, vu que tu demandes moi ça va".format(msg))
    elif nombre == 2:
        await channel.send("> {.content}\n\nSache que ça me fait très très plaisir de savoir ça, moi ça va si tu veux savoir".format(msg))
    else:
        await channel.send("> {.content}\n\nTrop cool (je rigole évidemment), personnellement ça va super bien".format(msg))
    time.sleep(1)
    nombre = randint(1, 3)
    print(nombre)
    if nombre == 1:
        await channel.send("Sinon tu fais quoi ?".format(msg))
    elif nombre == 2:
        await channel.send("Tu fais quoi sinn ?".format(msg))
    else:
        await channel.send("Qu'est ce que tu fais en ce beau jour ?".format(msg))
    
    def check2(m):
        return m.channel == channel and user == m.author

    msg = await bot.wait_for('message', timeout = 60, check=check2)
    time.sleep(0.4)
    nombre = randint(1, 3)
    print(nombre)
    if nombre == 1:
        await channel.send("> {.content}\n\nIntéressant (ou pas je dis pas), vu que tu demandes encore moi je fais rien de spécial".format(msg))
    elif nombre == 2:
        await channel.send("> {.content}\n\nVraiment je m'attendais pas à que ce soit aussi intéressant, de mon côté là je code".format(msg))
    else:
        await channel.send("> {.content}\n\nVraiment ??".format(msg))
        time.sleep(1)
        await channel.send("C'est fou je fais exactement la même chose".format(msg))
    time.sleep(1)
    await channel.send("Bon..".format(msg))
    time.sleep(1)
    nombre = randint(1, 3)
    print(nombre)
    if nombre == 1:
        await channel.send("Tu veux pas me raconter un truc intéressant stp je m'ennuie ?".format(msg))
    elif nombre == 2:
        await channel.send("Vasy je m'ennuie raconte moi ta journée en quelques mots".format(msg))
    else:
        await channel.send("Dis moi à quoi tu penses là tout de suite maintenant".format(msg))

    def check3(m):
        return m.channel == channel and user == m.author

    msg = await bot.wait_for('message', timeout = 60, check=check3)
    time.sleep(0.4)
    nombre = randint(1, 3)
    print(nombre)
    if nombre == 1:
        await channel.send("> {.content}\n\nc'est pas..".format(msg))
        time.sleep(1)
        await channel.send("euh".format(msg))
        time.sleep(1)
        await channel.send("Disons que j'ai déjà vu plus pertinent".format(msg))
    elif nombre == 2:
        await channel.send("> {.content}\n\nWOW mais c'est GÉNIAL ça".format(msg))
        time.sleep(1)
        await channel.send("Je crois que j'ai jamais lu quelque chose d'aussi intéressant".format(msg))
    else:
        await channel.send("> {.content}\n\nbon".format(msg))
        time.sleep(1)
        await channel.send("On va dire que c'est intéressant".format(msg))
    time.sleep(1.5)
    await channel.send('Tu veux continuer à me parler ? (oui ou non)'.format(msg))

    def check4(m):
        return m.channel == channel and user == m.author
    msg = await bot.wait_for('message', timeout = 60, check=check4)
    time.sleep(0.4)
    ouinon = msg.content
    ouinon = ouinon.split(" ")
    for i in ouinon:
        if i == "oui" or i == "Oui" or i == "ouu" or i == "Ouu" or i == "OUU" or i == "OUI" or i == "OUu" or i == "OUi" or i == "OuU" or i == "OuI" or i == "oUU" or i == "oUI":
            ouinon = "oui"
        elif i == "non" or i == "Non" or i == "nn" or i == "Nn" or i == "NON" or i == "NN" or i == "NoN" or i == "NOn" or i == "nON" or i == "nOn" or i == "nN":
            ouinon = "non"
    if ouinon == "oui":
        await channel.send('> {.content}\n\nCool'.format(msg))
        time.sleep(1)
        nombre = randint(1, 3)
        print(nombre)
        if nombre == 1:
            await channel.send("hmmmmmm".format(msg))
        elif nombre == 2:
            await channel.send("Breeeeeeef".format(msg))
        else:
            await channel.send("bon bon bon...".format(msg))
        time.sleep(1.5)
        nombre == randint(1, 3)
        print(nombre)
        if nombre == 1:
            await channel.send("que dire...".format(msg))
        elif nombre == 2:
            await channel.send("Go faire un concours de rots !".format(msg))
            time.sleep(1)
            await channel.send("oé nn pas terrible en fait comme idée".format(msg))
        else:
            await channel.send("J'avoue que je sais pas trop quoi dire là".format(msg))
            time.sleep(1)
            await channel.send("ma vie n'est pas des plus passionantes donc bon..".format(msg))
        time.sleep(1.5)
        await channel.send("Ah je sais !".format(msg))
        time.sleep(1)
        nombre = randint(1, 3)
        print(nombre)
        if nombre == 1:
            await channel.send("J'ai une blague, tu la veux ? (oui ou non)".format(msg))
        elif nombre == 2:
            await channel.send("Tu veux rire ? (oui ou non)".format(msg))
        else:
            await channel.send("Je suis sûr que t'as envie de rigoler là j'ai raison ? (oui ou non)".format(msg))

        def check5(m):
            return m.channel == channel and user == m.author
        msg = await bot.wait_for('message', timeout = 60, check=check5)
        time.sleep(0.4)
        ouinon = msg.content
        ouinon = ouinon.split(" ")
        for i in ouinon:
            if i == "oui" or i == "Oui" or i == "ouu" or i == "Ouu" or i == "OUU" or i == "OUI" or i == "OUu" or i == "OUi" or i == "OuU" or i == "OuI" or i == "oUU" or i == "oUI" or i == "oUu" or i == "oUi":
                ouinon = "oui"
            elif i == "non" or i == "Non" or i == "nn" or i == "Nn" or i == "NON" or i == "NN" or i == "NoN" or i == "NOn" or i == "nON" or i == "nOn" or i == "nN":
                ouinon = "non"
        if ouinon == "oui":
            await channel.send("> {.content}\n\nalors".format(msg))
            time.sleep(1.5)
            blague = randint(1, 5)
            print(f"blague {blague}")
            if blague == 1:
                await channel.send("Comment s'appelle le journal publié chaque semaine au Sahara ?".format(msg))
                time.sleep(1.5)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1.5)
                await channel.send("L'hebdromadaire ! :rofl: :rofl: :rofl: :rofl:".format(msg))
            elif blague == 2:
                await channel.send("Qu'est-ce qu'un canife ?".format(msg))
                time.sleep(1.5)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1.5)
                await channel.send("Un petit fien ! :rofl: :rofl: :rofl: :rofl:".format(msg))
            elif blague == 3:
                await channel.send("Quel est le sport le plus silencieux ?".format(msg))
                time.sleep(1.5)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1.5)
                await channel.send("Le parachhhhhhhuuuuuuuuutt ! :rofl: :rofl: :rofl: :rofl:".format(msg))
            elif blague == 4:
                await channel.send("Qu'est ce qu'un petit cheval dans un piscine ?".format(msg))
                time.sleep(1.5)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1.5)
                await channel.send("Un poney de bain ! :rofl: :rofl: :rofl: :rofl:".format(msg))
            else:
                await channel.send("Comment appelle-t-on un roux dans un four ?".format(msg))
                time.sleep(1.5)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1)
                await channel.send(".".format(msg))
                time.sleep(1.5)
                await channel.send("Un roux-ti ! :rofl: :rofl: :rofl: :rofl:".format(msg))

            time.sleep(2)
            await channel.send("T'as trouvé ça drôle ?".format(msg))
            
            def check6(m):
                return m.channel == channel and user == m.author
            msg = await bot.wait_for('message', timeout = 60, check=check6)
            time.sleep(0.4)
            await channel.send("> {.content}\n\noui oui t'as trouvé ça incroyablement drôle je m'en doutais".format(msg))
            time.sleep(1)
            await channel.send("Bref".format(msg))
        
        elif ouinon == "non":
            await channel.send("> {.content}\n\nah".format(msg))
            time.sleep(1.5)
            await channel.send("je suis un peu décontenancé je m'attendais à ce que tu veuilles".format(msg))
            time.sleep(1)
            await channel.send("On peut quand même continuer à parler t'inquiète".format(msg))

        else:
            await channel.send("jsp si t'as du mal à écrire 3 lettres ou quoi mais j'ai pas ton temps, bisous".format(msg))
            return

        time.sleep(1)
        await channel.send("Sinon {.author.mention}, décris moi ta vie en 1  mot".format(msg))
            
        def check7(m):
            return m.channel == channel and user == m.author
        msg = await bot.wait_for('message', timeout = 60, check=check7)
        mot = msg.content
        mots = mot.split(" ")
        time.sleep(0.4)
        if len(mots) > 1:
            await channel.send("> {.content}\n\nya plus d'un mot là c'est pas ce que j'avais demandé".format(msg))
        else:
            await channel.send("> {.content}\n\nj'aime beaucoup ce mot".format(msg))
            
        time.sleep(3)
        await channel.send("_[pas de suite pour le moment]_".format(msg))
        print("discussion finie")


    elif ouinon == "non":
        await channel.send("> {.content}\n\ndommage".format(msg))
    else:
        await channel.send("jsp si t'as du mal à écrire 3 lettres ou quoi mais je prend ça pour un non, bisous".format(msg))
        
class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@bot.command()
async def playlist(ctx, commande = None):
    user = ctx.message.author
    if commande:
        print(f"playlist {commande}, {user}")
    else:
        print(f"playlist, {user}")
    if commande:
        if commande == "liste" or commande == "list":
            playlistliens = []
            playlisttitres = []
            f = open("playlist.csv", encoding="utf-8")
            fichier = csv.reader(f)
            for ligne in fichier:
                x = ligne[0]
                x = x.split(";")
                playlistliens.append(x[0])
                playlisttitres.append(x[1])
            await ctx.send(f"Playlist actuelle du bot :\n\n**-** {playlisttitres[0]}\n**-** {playlisttitres[1]}\n**-** {playlisttitres[2]}\n**-** {playlisttitres[3]}\n**-** {playlisttitres[4]}\n**-** {playlisttitres[5]}\n**-** {playlisttitres[6]}\n**-** {playlisttitres[7]}\n**-** {playlisttitres[8]}\n**-** {playlisttitres[9]}")
            f.close()
        elif commande == "add" or commande == "ajouter":
            channel = ctx.channel
            playlistmusique = []
            f = open("playlist.csv", encoding="utf-8")
            fichier = csv.reader(f)
            for ligne in fichier:
                x = ligne[0]
                print(x)
                x = x.split(";")
                playlistmusique.append([x[0], x[1]])
            await ctx.send (f"Quel morceau voulez-vous retirer parmi ceux là ? (donner le numéro, écrire n'importe quoi d'autre pour en enlever un aléatoirement)\n\n**1.** {playlistmusique[0][1]}\n**2.** {playlistmusique[1][1]}\n**3.** {playlistmusique[2][1]}\n**4.** {playlistmusique[3][1]}\n**5.** {playlistmusique[4][1]}\n**6.** {playlistmusique[5][1]}\n**7.** {playlistmusique[6][1]}\n**8.** {playlistmusique[7][1]}\n**9.** {playlistmusique[8][1]}\n**10.** {playlistmusique[9][1]}")
            def check(m):
                return m.channel == channel and user == m.author
            msg = await bot.wait_for('message', timeout = 30, check=check)
            msg = "{.content}".format(msg)
            if msg == "1" or msg == "2" or msg == "3" or msg == "4" or msg == "5" or msg == "6" or msg == "7" or msg == "8" or msg == "9" or msg == "10":
                numero = int(msg) - 1
            else:
                numero = randint(0, 9)
            time.sleep(0.4)
            await ctx.send(f'{playlistmusique[numero][1]} sera retiré')
            time.sleep(0.4)
            await ctx.send('Quelle musique voulez-vous ajouter ? (donner un nom ou un lien)\nÉcrire "annuler" ou "cancel" pour annuler')
            def check2(m):
                return m.channel == channel and user == m.author
            msg = await bot.wait_for('message', timeout = 30, check=check2)
            msg = "{.content}".format(msg)
            if msg != "annuler" and msg != "cancel":
                supprimé = playlistmusique[numero][1]
                del playlistmusique[numero]
                results = VideosSearch(msg, limit = 1)
                results = results.result()['result']
                for result in results:
                    url = result['link']
                    titre = result['title']
                    print(url)
                    print(titre)
                    playlistmusique.append([url, titre])
                    f = open("playlist.csv", "w", encoding="utf-8")
                    f.write(f"{playlistmusique[9][0]};{playlistmusique[9][1]}\n")
                    for i in range (9):
                        f.write(f"{playlistmusique[i][0]};{playlistmusique[i][1]}\n")
                    f.close()
                    await ctx.send(f"{titre} a été ajouté à la playlist, {supprimé} a été retiré.")
        elif commande == "play":
            channel = ctx.author.voice.channel
            print("playlist play")
            if channel:
                f = open("playlist.csv", encoding="utf-8")
                fichier = csv.reader(f)
                playlistmusique = []
                for ligne in fichier:
                    x = ligne[0]
                    print(x)
                    x = x.split(";")
                    playlistmusique.append([x[0], x[1]])
                shuffle(playlistmusique)
                client = ctx.guild.voice_client
                for i in range(10):
                    url = playlistmusique[i][0]
                    title = playlistmusique[i][1]
                    print(url)
                    print(title)
                    if client and client.channel:
                        video = Video(url)
                        musics[ctx.guild].append(video)
                    else:
                        channel = ctx.author.voice.channel
                        video = Video(url)
                        musics[ctx.guild] = []
                        client = await channel.connect()
                        await ctx.send(f"C'est parti pour la playlist :\n- {playlistmusique[0][1]}\n- {playlistmusique[1][1]}\n- {playlistmusique[2][1]}\n- {playlistmusique[3][1]}\n- {playlistmusique[4][1]}\n- {playlistmusique[5][1]}\n- {playlistmusique[6][1]}\n- {playlistmusique[7][1]}\n- {playlistmusique[8][1]}\n- {playlistmusique[9][1]}")
                        play_song(client, musics[ctx.guild], video)
        else:
            await ctx.send("Cette fonction n'existe pas, *playlist pour la liste des commandes de la playlist")
    else:
        embed = discord.Embed(title = "**Commandes**", description = "**Playlist**\n\n:arrow_forward: *playlist play : _Lire la playlist (ordre aléatoire)_\n\n:memo: *playlist list / liste : _Afficher les morceaux actuels de la playlist_\n\n:heavy_plus_sign: *playlist add : _Ajouter un morceau à la playlist_\n\n:pause_button: *pause / *pa : _Met la musique en pause_\n\n:play_pause: *resume / *r : _Reprendre la musique_\n\n:track_next: *skip / *s : _Passer à la musique suivante_\n\n:x: *disconnect / *leave / *l : _Faire partir le bot_", colour = discord.Colour.blue())
        await ctx.send(embed = embed)
        print("playlist help")


@bot.command()
async def edit(ctx, commande):
    utilisateur = ctx.message.author
    print("edit", commande, utilisateur)
    channel = ctx.channel
    user = ctx.message.author
    msg = ctx.message
    attachments = msg.attachments
    if attachments:
        for attachment in attachments:
            if (attachment.filename.lower().endswith(image) for image in image_types):
                await attachment.save("image.png")
                img = Image.open("image.png")
                if commande == "monochrome":
                    couleurs = ImageEnhance.Color(img)
                    couleurs.enhance(0).save("image.png")
                elif commande == "saturation":
                    msg = 0
                    while msg < 1 or msg > 10:
                        await ctx.send("À quel niveau (de 1 à 10) voulez-vous saturer l'image ?")
                        def checks(m):
                            return m.channel == channel and user == m.author
                        msg = await bot.wait_for('message', timeout = 30, check=checks)
                        msg = "{.content}".format(msg)
                        msg = int(msg)
                        if msg < 1 or msg > 10:
                            await ctx.send("La valeur doit être comprise entre 1 et 10")
                            time.sleep(0.4)
                    couleurs = ImageEnhance.Color(img)
                    if msg == 1:
                        couleurs.enhance(2).save("image.png")
                    elif msg == 2:
                        couleurs.enhance(4).save("image.png")
                    elif msg == 3:
                        couleurs.enhance(7).save("image.png")
                    elif msg == 4:
                        couleurs.enhance(10).save("image.png")
                    elif msg == 5:
                        couleurs.enhance(15).save("image.png")
                    elif msg == 6:
                        couleurs.enhance(20).save("image.png")
                    elif msg == 7:
                        couleurs.enhance(25).save("image.png")
                    elif msg == 8:
                        couleurs.enhance(35).save("image.png")
                    elif msg == 9:
                        couleurs.enhance(50).save("image.png")
                    elif msg == 10:
                        couleurs.enhance(500).save("image.png")
                elif commande == "luminosité" or commande == "luminosite":
                    msg = -1
                    while msg < 0 or msg > 1000:
                        await ctx.send("À quel pourcentage (0 à 1000) voulez-vous mettre la luminosité de l'image ?")
                        def checks(m):
                            return m.channel == channel and user == m.author
                        msg = await bot.wait_for('message', timeout = 30, check=checks)
                        msg = "{.content}".format(msg)
                        msg = int(msg)
                        if msg < 0 or msg > 1000:
                            await ctx.send("La valeur doit être comprise entre 0 et 1000")
                            time.sleep(0.4)
                    msg = msg / 100
                    couleurs = ImageEnhance.Brightness(img)
                    couleurs.enhance(msg).save("image.png")
                elif commande == "contraste":
                    msg = -1
                    while msg < 0 or msg > 500:
                        await ctx.send("À quel pourcentage (0 à 500) voulez-vous mettre le contraste de l'image ?")
                        def checks(m):
                            return m.channel == channel and user == m.author
                        msg = await bot.wait_for('message', timeout = 30, check=checks)
                        msg = "{.content}".format(msg)
                        msg = int(msg)
                        if msg < 0 or msg > 500:
                            await ctx.send("La valeur doit être comprise entre 0 et 500")
                            time.sleep(0.4)
                    msg = msg / 100
                    couleurs = ImageEnhance.Contrast(img)
                    couleurs.enhance(msg).save("image.png")
                elif commande == "flou":
                    msg = -1
                    while msg < 1 or msg > 30:
                        await ctx.send("À quel niveau (1 à 30) voulez-vous flouter de l'image ?")
                        def checks(m):
                            return m.channel == channel and user == m.author
                        msg = await bot.wait_for('message', timeout = 30, check=checks)
                        msg = "{.content}".format(msg)
                        msg = int(msg)
                        if msg < 1 or msg > 30:
                            await ctx.send("La valeur doit être comprise entre 1 et 30")
                            time.sleep(0.4)
                    img.filter(ImageFilter.GaussianBlur(radius = msg)).save("image.png")

                elif commande == "texte+" or commande == "text+":
                    w, h = img.size
                    if w > h:
                        left = (w - h) / 2
                        top = 0
                        right = left + h
                        bottom = h
                        img = img.crop((left, top, right, bottom))
                    elif w < h:
                        left = 0
                        top = (h - w) / 2
                        right = w
                        bottom = top + w
                        img = img.crop((left, top, right, bottom))
                    newsize = (500, 500)
                    img = img.resize(newsize)
                    draw = ImageDraw.Draw(img)
                    await ctx.send('Texte en haut ? Tapez "notext" pour ne rien mettre ici')

                    def checks(m):
                        return m.channel == channel and user == m.author
                    msg = await bot.wait_for('message', timeout = 30, check=checks)
                    msg = "{.content}".format(msg)
                    msg = msg.upper()
                    if msg != "NOTEXT" and msg != "NO TEXT":
                        police = ImageFont.truetype("ariblk.ttf", 75)
                        W, H = police.getsize(msg)
                        taille = 75
                        test = 0
                        if W > 500:
                            while W > 500:
                                taille = taille - 1
                                police = ImageFont.truetype("ariblk.ttf", taille)
                                W, H = police.getsize(msg)
                            test = 1
                        police = ImageFont.truetype("ariblk.ttf", taille)
                        testcouleur = 0
                        contour = "black"
                        while testcouleur != 1:
                            await ctx.send("Quelle couleur pour ce texte (parmi la liste ci-dessous) ?\nRouge, rose, vert, noir, blanc, jaune, orange")
                            def checks2(m):
                                return m.channel == channel and user == m.author
                            couleur = await bot.wait_for('message', timeout = 30, check=checks2)
                            couleur = "{.content}".format(couleur)
                            couleur = couleur.lower()
                            if couleur == "rouge":
                                couleur = "red"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "rose":
                                couleur = "pink"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "vert":
                                couleur = "green"
                                testcouleur = 1
                                contour = "white"
                            elif couleur == "noir":
                                couleur = "black"
                                testcouleur = 1
                                contour = "white"
                            elif couleur == "blanc":
                                couleur = "white"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "jaune":
                                couleur = "yellow"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "orange":
                                couleur = "orange"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "bleu":
                                couleur = "blue"
                                testcouleur = 1
                                contour = "white"
                            else:
                                await ctx.send("La couleur doit être choisie parmi la liste donnée")
                                time.sleep(0.4)

                        if test == 1:
                            draw.text(((500-W)/2,5), msg, fill = couleur, font=police, stroke_width=5, stroke_fill=contour)
                        else:
                            draw.text(((500-W)/2,-15), msg, fill = couleur, font=police, stroke_width=5, stroke_fill=contour)
                    await ctx.send('Texte en bas ? Tapez "notext" pour ne rien mettre ici')

                    def checks3(m):
                        return m.channel == channel and user == m.author
                    msg = await bot.wait_for('message', timeout = 30, check=checks3)
                    msg = "{.content}".format(msg)
                    if msg != "notext" and msg != "Notext" and msg != "No text" and msg != "no text":
                        msg = msg.upper()
                        police = ImageFont.truetype("ariblk.ttf", 75)
                        W, H = police.getsize(msg)
                        taille = 75
                        while W > 500:
                            taille = taille - 1
                            police = ImageFont.truetype("ariblk.ttf", taille)
                            W, H = police.getsize(msg)
                        police = ImageFont.truetype("ariblk.ttf", taille)
                        testcouleur = 0
                        contour = "black"
                        while testcouleur != 1:
                            await ctx.send("Quelle couleur pour ce texte (parmi la liste ci-dessous) ?\nRouge, bleu, rose, vert, noir, blanc, jaune, orange")
                            def checks4(m):
                                return m.channel == channel and user == m.author
                            couleur = await bot.wait_for('message', timeout = 30, check=checks4)
                            couleur = "{.content}".format(couleur)
                            couleur = couleur.lower()
                            if couleur == "rouge":
                                couleur = "red"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "vert":
                                couleur = "green"
                                testcouleur = 1
                                contour = "white"
                            elif couleur == "rose":
                                couleur = "pink"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "noir":
                                couleur = "black"
                                testcouleur = 1
                                contour = "white"
                            elif couleur == "blanc":
                                couleur = "white"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "jaune":
                                couleur = "yellow"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "orange":
                                couleur = "orange"
                                testcouleur = 1
                                contour = "black"
                            elif couleur == "bleu":
                                couleur = "blue"
                                testcouleur = 1
                                contour = "white"
                            else:
                                await ctx.send("La couleur doit être choisie parmi la liste donnée")
                                time.sleep(0.4)

                        draw.text(((500-W)/2, 500-H-10), msg, fill = couleur, font=police, stroke_width=5, stroke_fill=contour)
                    img.save("image.png")

                elif commande == "texte" or commande == "text":
                    w, h = img.size
                    if w > h:
                        left = (w - h) / 2
                        top = 0
                        right = left + h
                        bottom = h
                        img = img.crop((left, top, right, bottom))
                    elif w < h:
                        left = 0
                        top = (h - w) / 2
                        right = w
                        bottom = top + w
                        img = img.crop((left, top, right, bottom))
                    newsize = (500, 500)
                    img = img.resize(newsize)
                    draw = ImageDraw.Draw(img)
                    await ctx.send('Texte en haut ? Tapez "notext" pour ne rien mettre ici')

                    def checks(m):
                        return m.channel == channel and user == m.author
                    msg = await bot.wait_for('message', timeout = 30, check=checks)
                    msg = "{.content}".format(msg)
                    if msg != "notext" and msg != "Notext" and msg != "No text" and msg != "no text":
                        msg = msg.upper()
                        police = ImageFont.truetype("ariblk.ttf", 75)
                        W, H = police.getsize(msg)
                        taille = 75
                        test = 0
                        if W > 500:
                            while W > 500:
                                taille = taille - 1
                                police = ImageFont.truetype("ariblk.ttf", taille)
                                W, H = police.getsize(msg)
                            test = 1
                        police = ImageFont.truetype("ariblk.ttf", taille)
                        if test == 1:
                            draw.text(((500-W)/2,5), msg, fill = "white", font=police, stroke_width=5, stroke_fill="black")
                        else:
                            draw.text(((500-W)/2,-15), msg, fill = "white", font=police, stroke_width=5, stroke_fill="black")
                    await ctx.send('Texte en bas ? Tapez "notext" pour ne rien mettre ici')

                    def checks2(m):
                        return m.channel == channel and user == m.author
                    msg = await bot.wait_for('message', timeout = 30, check=checks2)
                    msg = "{.content}".format(msg)
                    if msg != "notext" and msg != "Notext" and msg != "No text" and msg != "no text":
                        msg = msg.upper()
                        police = ImageFont.truetype("ariblk.ttf", 75)
                        W, H = police.getsize(msg)
                        taille = 75
                        while W > 500:
                            taille = taille - 1
                            police = ImageFont.truetype("ariblk.ttf", taille)
                            W, H = police.getsize(msg)
                        police = ImageFont.truetype("ariblk.ttf", taille)
                        draw.text(((500-W)/2, 500-H-10), msg, fill = "white", font=police, stroke_width=5, stroke_fill="black")
                    img.save("image.png")

                else:
                    await ctx.send("Cette modification n'existe pas, *image pour la liste des modifications")
                    break

                image = discord.File('image.png')
                await ctx.send(file=image)
    else:
        await ctx.send("Il faut envoyer une image (les liens ne fonctionnent pas)")

@bot.command()
async def meme(ctx, *texte):
    texte = " ".join(texte)
    print("meme", texte)
    msg = ctx.message
    attachments = msg.attachments
    verif = 0
    if attachments:
        textelist = list(texte)
        for i in textelist:
            if i == ";":
                verif = 1
        if verif == 1:
            textetab = texte.split(";")
            texte1 = textetab[0]
            texte2 = textetab[1]
            texte1 = "".join(texte1.rstrip().lstrip())
            texte2 = "".join(texte2.rstrip().lstrip())
            for attachment in attachments:
                if (attachment.filename.lower().endswith(image) for image in image_types):
                    await attachment.save("image.png")
                    img = Image.open("image.png")
                    w, h = img.size
                    if w > h:
                        left = (w - h) / 2
                        top = 0
                        right = left + h
                        bottom = h
                        img = img.crop((left, top, right, bottom))
                    elif w < h:
                        left = 0
                        top = (h - w) / 2
                        right = w
                        bottom = top + w
                        img = img.crop((left, top, right, bottom))
                    newsize = (500, 500)
                    img = img.resize(newsize)
                    draw = ImageDraw.Draw(img)
                    if texte1 != "notext" and texte1 != "Notext" and texte1 != "No text" and texte1 != "no text":
                        texte1 = texte1.upper()
                        police = ImageFont.truetype("ariblk.ttf", 75)
                        W, H = police.getsize(texte1)
                        taille = 75
                        test = 0
                        if W > 500:
                            while W > 500:
                                taille = taille - 1
                                police = ImageFont.truetype("ariblk.ttf", taille)
                                W, H = police.getsize(texte1)
                            test = 1
                        police = ImageFont.truetype("ariblk.ttf", taille)
                        if test == 1:
                            draw.text(((500-W)/2,5), texte1, fill = "white", font=police, stroke_width=5, stroke_fill="black")
                        else:
                            draw.text(((500-W)/2,-15), texte1, fill = "white", font=police, stroke_width=5, stroke_fill="black")

                    if texte2 != "notext" and texte2 != "Notext" and texte2 != "No text" and texte2 != "no text":
                        texte2 = texte2.upper()
                        police = ImageFont.truetype("ariblk.ttf", 75)
                        W, H = police.getsize(texte2)
                        taille = 75
                        while W > 500:
                            taille = taille - 1
                            police = ImageFont.truetype("ariblk.ttf", taille)
                            W, H = police.getsize(texte2)
                        police = ImageFont.truetype("ariblk.ttf", taille)
                        draw.text(((500-W)/2, 500-H-10), texte2, fill = "white", font=police, stroke_width=5, stroke_fill="black")
                    img.save("image.png")

                    image = discord.File('image.png')
                    await ctx.send(file=image)
        else:
            await ctx.send('Il faut écrire sous la forme "texte en haut **;** texte en bas"')
    else:
        await ctx.send("Il faut envoyer une image (les liens ne fonctionnent pas)")

    
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(f"Cette commande n'existe pas, *h pour la liste des commandes")
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Il manque/il y a une erreur avec un argument à cette commande, *h pour la liste des commandes")
	elif isinstance(error, commands.MissingPermissions):
		await ctx.send("Vous n'avez pas la permission de faire cette commande")


bot.run("OTQ0NzM0NzQwNTkyODUzMDEz.YhF6yg.d51wCc4SxSXlN5AEIn3vqjZWcwI")