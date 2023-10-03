import discord

import gspread 
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import matplotlib.pyplot as plt
import random
from collections import Counter
from keep_alive import keep_alive
import os
import time




scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Songs").sheet1
data = sheet.get_all_records()


insertRow = ["hello", "5", "52"]
#sheet.insert_row(insertRow, 8)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

  

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    wanted_artist = ""
    points = 0
    count = 0
    if message.author == client.user:
        return
    msg = message.content
    spotify = "https://open.spotify.com/playlist/2pCQuRM3P7G0T0DHnoSveX?si=c47a3b307732442f"
    youtube = "https://www.youtube.com/playlist?list=PL4vDECCysjPZWaloOkqYmkZ-3F00-lqbE"
    duedate = "Due: <t:1691290800> <t:1691290800:R>"
    if message.content.startswith('$due'):
        await message.channel.send(duedate)
    if message.content.startswith('$sorryj'):
        await message.channel.send("I am so sorry for your troubles Julissa. The bot is now back up.")
    if message.content.startswith('$spotify'):
        await message.channel.send(spotify)
    if message.content.startswith('$sorter'):
        await message.channel.send("https://witchessongcontest.tumblr.com/")
    if message.content.startswith('$youtube'):
        await message.channel.send(youtube)
    if message.content.startswith('$corey'):
        await message.channel.send(":angry:")
    if message.content.startswith('$josh'):
        await message.channel.send("Ugh.")
    if message.content.startswith('$kesha'):
        await message.channel.send("Has Kesha Won WSC Yet?")
        time.sleep(1)
        await message.channel.send(file=discord.File('paula.jpg'))
    if message.content.startswith('$davidsdog'):
        await message.channel.send(file=discord.File('davidsdog.png'))
    if message.content.startswith('$fruitripeness'):
        await message.channel.send(file=discord.File('fruit.png'))
    if message.content.startswith('$liam'):
        await message.channel.send(file=discord.File('liam.png'))
    if message.content.startswith('$julissa'):
        await message.channel.send(":heart: :heart: :heart: :heart: :heart::heart:\n:heart:       Julissa         :heart:\n:heart: :heart: :heart: :heart: :heart::heart:")
    if message.content.startswith('$artist'):
        wanted_artist = msg.split("$artist ", 1)[1]
        finished = ">>> " 
        for numbers in data:
          if wanted_artist.lower() in str(numbers['Artist']).lower():
            count = count + 1
            points = points + numbers['Number']
            if count < 200:
              finished += str(numbers['Season']) + ": " + str(numbers['Song'])  + " [" + str(numbers['Sent By']) + "] (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
        embed = discord.Embed(title = (str(wanted_artist)), description = (finished))
        await message.channel.send(embed = embed)
        await message.channel.send("Total Times Submitted: " + str(count))
        await message.channel.send("Average: " + str(round(points/count, ndigits=1)))
    if message.content.startswith('$song'):
        wanted_artist = msg.split("$song ", 1)[1]
        finished = ">>> " 
        finished2 = ">>> "
        finished3 = ">>> "
        for numbers in data:
          if str(wanted_artist).lower() in str(numbers['Song']).lower():
            count = count + 1
            points = points + numbers['Number']
            if count < 30:
              finished += str(numbers['Season']) + ": " + str(numbers['Song']) + ", " +     str(numbers['Artist']) + " [" + str(numbers['Sent By']) + "] (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
            if count >= 30 and count < 60:
              finished2 += str(numbers['Season']) + ": " + str(numbers['Song']) + ", " +     str(numbers['Artist']) + " [" + str(numbers['Sent By']) + "] (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
            if count >= 60 and count < 90:
              finished3 += str(numbers['Season']) + ": " + str(numbers['Song']) + ", " +     str(numbers['Artist']) + " [" + str(numbers['Sent By']) + "] (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
        embed = discord.Embed(title = (str(wanted_artist)), description = (finished))
        await message.channel.send(embed = embed)
        if count >= 30:
          embed = discord.Embed(title = (str(wanted_artist)), description = (finished2))
          await message.channel.send(embed = embed)
        if count >= 60:
          embed = discord.Embed(title = (str(wanted_artist)), description = (finished3))
          await message.channel.send(embed = embed)
        await message.channel.send("Total Times Submitted: " + str(count))
        await message.channel.send("Average: " + str(round(points/count, ndigits=1)))


    if message.content.startswith('$season'):
        wanted_artist = msg.split("$season ", 1)[1]
        finished = ">>> " 
        for numbers in data:
          if wanted_artist.lower() == str(numbers['Season']).lower():
            finished += str(numbers['Placement']) +" - " + str(numbers['Song']) + ", " +     str(numbers['Artist']) + " [" + str(numbers['Sent By']) + "] (" + str(numbers['Points']) + " Points)\n"
        embed = discord.Embed(title = ("Season " + str(wanted_artist)[3:]), description = (finished))
        await message.channel.send(embed = embed)
    if message.content.startswith('$points'):
        finished = ">>> " 
        wanted_artist = msg.split("$points ", 1)[1]
        for numbers in data:
          if wanted_artist.lower() == str(numbers['Points']).lower():
            count += 1
            finished += str(numbers['Season']) + ": " + str(numbers['Song']) + ", " +     str(numbers['Artist']) + " [" + str(numbers['Sent By']) + "] (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
        embed = discord.Embed(title = (str(wanted_artist)), description = (finished))
        await message.channel.send(embed = embed)
        await message.channel.send("Total: " + str(count))
    if message.content.startswith('$placement'):
        wanted_artist = msg.split("$placement ", 1)[1]
        finished = ">>> " 
        for numbers in data:
          if wanted_artist.lower() == str(numbers['Placement']).lower():
            finished += str(numbers['Season']) + ": " + str(numbers['Song']) + ", " +     str(numbers['Artist']) + " [" + str(numbers['Sent By']) + "] (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
        embed = discord.Embed(title = (str(wanted_artist)), description = (finished))
        await message.channel.send(embed = embed)
    
    if message.content.startswith('$submissions'):
        finished = ">>> " 
        finished2 = ">>> "
        finished3 = ">>> "
        wanted_artist = msg.split("$submissions ", 1)[1]
        for numbers in data:
          if wanted_artist.lower() == str(numbers['Sent By']).lower():
            count = count + 1
            points = points + numbers['Number']
            if count < 30:
              finished += str(numbers['Season']) + ": " + str(numbers['Song']) + ", " +     str(numbers['Artist']) +  " (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
            if count >= 30 and count < 60:
              finished2 += str(numbers['Season']) + ": " + str(numbers['Song']) + ", " +     str(numbers['Artist']) + " (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
            if count >= 60 and count < 90:
              finished3 += str(numbers['Season']) + ": " + str(numbers['Song']) + ", " +     str(numbers['Artist']) + " (" +  str(numbers['Placement']) + " - " + str(numbers['Points']) + " Points)\n"
        embed = discord.Embed(title = (str(wanted_artist)), description = (finished))
        await message.channel.send(embed = embed)
        if count >= 30:
          embed = discord.Embed(title = (str(wanted_artist)), description = (finished2))
          await message.channel.send(embed = embed)
        if count >= 60:
          embed = discord.Embed(title = (str(wanted_artist)), description = (finished3))
          await message.channel.send(embed = embed)
        await message.channel.send("Total Times Submitted: " + str(count))
        await message.channel.send("Average: " + str(round(points/count, ndigits=1)))
    if message.content.startswith("$checker"):
      first = "❌"
      second = "❌"
      third = "❌"
      fourth = "❌"
      fifth = "❌"
      sixth = "❌"
      seventh = "❌"
      eighth = "❌"
      ninth = "❌"
      tenth = "❌"
      eleventh = "❌"
      twelth = "❌"
      thirteenth = "❌"
      forteenth = "❌"
      fifteenth = "❌"
      sixteenth = "❌"
      seventeenth = "❌"
      eighteenth = "❌"
      nineteenth = "❌"
      twenty = "❌"

      
      firstAmt = 0
      secondAmt = 0
      thirdAmt = 0
      fourthAmt = 0
      fifthAmt = 0
      sixthAmt = 0
      seventhAmt = 0
      eighthAmt = 0
      ninthAmt = 0
      tenthAmt = 0
      eleventhAmt = 0
      twelthAmt = 0
      thirteenthAmt = 0
      fourteenthAmt = 0
      fifteenthAmt = 0
      sixteenthAmt = 0
      seventeenthAmt = 0
      eighteenthAmt = 0
      nineteenthAmt = 0
      twentiethAmt = 0
      wanted_artist = msg.split("$checker ", 1)[1]
      for numbers in data:
        if wanted_artist.lower() == str(numbers['Sent By']).lower():
          if str(numbers['Number']).lower() == "1":
            first = "✅"
            firstAmt += 1
          if str(numbers['Number']).lower() == "2":
            second = "✅"
            secondAmt += 1
          if str(numbers['Number']).lower() == "3":
            third = "✅"
            thirdAmt += 1
          if str(numbers['Number']).lower() == "4":
            fourth = "✅"
            fourthAmt += 1
          if str(numbers['Number']).lower() == "5":
            fifth = "✅"
            fifthAmt += 1
          if str(numbers['Number']).lower() == "6":
            sixth = "✅"
            sixthAmt += 1
          if str(numbers['Number']).lower() == "7":
            seventh = "✅"
            seventhAmt += 1
          if str(numbers['Number']).lower() == "8":
            eighth = "✅"
            eighthAmt += 1
          if str(numbers['Number']).lower() == "9":
            ninth = "✅"
            ninthAmt += 1
          if str(numbers['Number']).lower() == "10":
            tenth = "✅"
            tenthAmt += 1
          if str(numbers['Number']).lower() == "11":
            eleventh = "✅"
            eleventhAmt += 1
          if str(numbers['Number']).lower() == "12":
            twelth = "✅"
            twelthAmt += 1
          if str(numbers['Number']).lower() == "13":
            thirteenth = "✅"
            thirteenthAmt += 1
          if str(numbers['Number']).lower() == "14":
            forteenth = "✅"
            fourteenthAmt += 1
          if str(numbers['Number']).lower() == "15":
            fifteenth = "✅"
            fifteenthAmt += 1
          if str(numbers['Number']).lower() == "16":
            sixteenth = "✅"
            sixteenthAmt += 1
          if str(numbers['Number']).lower() == "17":
            seventeenth = "✅"
            seventeenthAmt += 1
          if str(numbers['Number']).lower() == "18":
            eighteenth = "✅"
            eighteenthAmt += 1
          if str(numbers['Number']).lower() == "19":
            nineteenth = "✅"
            nineteenthAmt += 1
          if str(numbers['Number']).lower() == "20":
            twenty = "✅"
            twentiethAmt += 1
      await message.channel.send(">>> " + "First: " + first + " (" + str(firstAmt) + "x)" + "\n" + "Second: " + second + " (" + str(secondAmt) + "x)" + "\n" + "Third: " + third + " (" + str(thirdAmt) + "x)" +"\n" + "Fourth: " + fourth + " (" + str(fourthAmt) + "x)" +"\n" + "Fifth: " + fifth + " (" + str(fifthAmt) + "x)" +"\n" + "Sixth: " + sixth + " (" + str(sixthAmt) + "x)" +"\n" + "Seventh: " + seventh + " (" + str(seventhAmt) + "x)" +"\n" + "Eighth: " + eighth + " (" + str(eighthAmt) + "x)" +"\n" + "Ninth: " + ninth + " (" +str( ninthAmt) + "x)" +"\n" + "Tenth: " + tenth + " (" + str(tenthAmt) + "x)" +"\n" + "Eleventh: " + eleventh + " (" + str(eleventhAmt) + "x)" +"\n" + "Twelth: " + twelth + " (" + str(twelthAmt) + "x)" +"\n" + "Thirteenth: " + thirteenth + " (" + str(thirteenthAmt) + "x)" +"\n" + "Fourteenth: " + forteenth + " (" + str(fourteenthAmt) + "x)" +"\n" + "Fifteenth: " + fifteenth + " (" + str(fifteenthAmt) + "x)" +"\n"+ "Sixteenth: " + sixteenth + " (" + str(sixteenthAmt) + "x)" +"\n" + "Seventeenth: " + seventeenth + " (" + str(seventeenthAmt) + "x)" +"\n" + "Eighteenth: " + eighteenth + " (" + str(eighteenthAmt) + "x)" +"\n"+ "Nineteenth: " + nineteenth + " (" + str(nineteenthAmt) + "x)" +"\n" + "Twentieth: " + twenty + " (" + str(twentiethAmt) + "x)" +"\n")
    if message.content.startswith("$mostpart"):
        everyone = []
        for numbers in data:
          everyone.append(numbers['Sent By'])
        value = Counter(everyone).most_common(10)
        counter = 0
        await message.channel.send("**Top 10 Most Participations**")
        finished = ""
        for values in value:
          counter += 1
          finished += ">>> " + str(counter) + ". " + str(values) + "\n"
          await message.channel.send(finished)
    if message.content.startswith("$mostwins"):
        everyone = []
        for numbers in data:
          if numbers["Number"] == 1:
            everyone.append(numbers['Sent By'])
        value = Counter(everyone).most_common(10)
        counter = 0
        for values in value:
          counter += 1
          await message.channel.send(">>> " + str(counter) + ". " + str(values) + "\n")
    if message.content.startswith("$mostap"):
        everyone = set([])
        count2 = 0
        count3 = 0
        count = 0
        for numbers in data:
          everyone.add(numbers['Sent By'])
        for stuff in everyone:
          count2 = count2 + 1
        res = dict.fromkeys(everyone, 0)
        list_res = list(res.keys())
        while (count3 < count2):
          points = 0
          count = 0
          average = 0
          for numbers in data:
            if numbers['Sent By'] == list(res.keys())[count3]:
              points = points + numbers['Points']
              count = count + 1
              average = points/count
          res[(list_res)[count3]] = str(round(average, ndigits = 2))
          count3 += 1
        sorted_ap = sorted(res.items(), key=lambda x:x[1], reverse=True)
        counter = 0
        for sorting in sorted_ap:
          counter += 1
          if counter < 11:
            await message.channel.send(">>> " + str(counter) + ". " + str(sorting) + "\n")
    if message.content.startswith("$mostpoints"):
        everyone = set([])
        count2 = 0
        count3 = 0
        count = 0
        for numbers in data:
          everyone.add(numbers['Sent By'])
        for stuff in everyone:
          count2 = count2 + 1
        res = dict.fromkeys(everyone, 0)
        list_res = list(res.keys())
        while (count3 < count2):
          points = 0
          count = 0
          average = 0
          for numbers in data:
            if numbers['Sent By'] == list(res.keys())[count3]:
              points = points + numbers['Points']
          res[(list_res)[count3]] = points
          count3 += 1
        sorted_ap = sorted(res.items(), key=lambda x:x[1], reverse=True)
        counter = 0
        for sorting in sorted_ap:
          counter += 1
          if counter < 11:
            await message.channel.send(">>> " + str(counter) + ". " + str(sorting) + "\n")
    if message.content.startswith("$bestlast10"):
        everyone = set([])
        count2 = 0
        count3 = 0
        count = 0
        count10 = 0
        for numbers in data:
          if numbers['Sent By'] == "Ty":
            count10 += 1
        for numbers in data:
          if int(numbers['Season'][3:]) > (count10-10):
            everyone.add(numbers['Sent By'])
        for stuff in everyone:
          count2 = count2 + 1
        res = dict.fromkeys(everyone, 0)
        list_res = list(res.keys())
        while (count3 < count2):
          points = 0
          count = 0
          average = 0
          for numbers in data:
            if int(numbers['Season'][3:]) > (count10-10):
              if numbers['Sent By'] == list(res.keys())[count3]:
                points = points + numbers['Number']
                count = count + 1
                average = points/count
          res[(list_res)[count3]] = round(average, ndigits = 2)
          count3 += 1
        sorted_ap = sorted(res.items(), key=lambda x:x[1], reverse=False)
        counter = 0
        await message.channel.send("**Top 10 Best Averages (Last 10 Seasons)**")
        for sorting in sorted_ap:
          counter += 1
          if counter < 11:
            await message.channel.send(">>> " + str(counter) + ". " + str(sorting) + "\n")
    if message.content.startswith("$bestaverage"):
        everyone = set([])
        count2 = 0
        count3 = 0
        count = 0
        for numbers in data:
          everyone.add(numbers['Sent By'])
        for stuff in everyone:
          count2 = count2 + 1
        res = dict.fromkeys(everyone, 0)
        list_res = list(res.keys())
        while (count3 < count2):
          points = 0
          count = 0
          average = 0
          for numbers in data:
            if numbers['Sent By'] == list(res.keys())[count3]:
              points = points + numbers['Number']
              count = count + 1
              average = points/count
          res[(list_res)[count3]] = round(average, ndigits = 2)
          count3 += 1
        sorted_ap = sorted(res.items(), key=lambda x:x[1], reverse=False)
        counter = 0
        await message.channel.send("**Top 10 Best Averages**")
        for sorting in sorted_ap:
          counter += 1
          if counter < 11:
            await message.channel.send(">>> " + str(counter) + ". " + str(sorting) + "\n")
    if message.content.startswith("$randomsong"):
        points = 0
        count = 0
        count3 = 0
        count2 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        song = ''
        artist = ''
        if message.content == "$randomsong":
          for numbers in data:
            count4 += 1
          count5 = random.randint(1,count4)
          for numbers in data:
            if count6 <= count5:
                song = numbers['Song']
                artist = numbers['Artist']
                count6 += 1
          await message.channel.send(str(song) + " by " + str(artist))
        else:
          wanted_artist = msg.split("$randomsong ", 1)[1]
          for numbers in data:
            if numbers['Sent By'].lower() == wanted_artist.lower():
              count = count + 1
          count2 = random.randint(1,count)
          for numbers in data:
            if count3 <= count2:
              if numbers['Sent By'].lower() == wanted_artist.lower():
                song = numbers['Song']
                artist = numbers['Artist']
                count3 += 1
          await message.channel.send(str(song) + " by " + str(artist))
    if message.content.startswith("$simulate"): 
      themes = ["Power Ballads", "Girl Groups", "Obscure Songs", "Remixes", "K-Pop", "Colors", "Instrumentals", "Drag Race Lipsyncs", "Singing Competition Contestants", "Halloween","Male/Female Duets", "20th Century Disco", "The Letter T", "Break Up Songs", "Film Soundtracks", "Male Artists", "Sad Songs", "Christmas", "Best of 2023", "Drugs", "Sex Songs", "Money", "K-Pop B-Sides", "Covers", "Valentine's Day", "The Four Elements", "Julissa Week", "Throwback British Artists", "Latin Songs", "Numbers", "French Songs", "Around The World", "Obscure Songs II", "Questions", "Album Openers", "Short Songs", "Old Songs", "No Pop Songs", "Pronouns", "Male Ballads", "Case Sensitive", "Animals", "Features"]
      theme = random.randint(0, len(themes))
      everyone = set([])
      for numbers in data:
        if int(numbers['Season'][3:]) > 45:
          everyone.add(numbers['Sent By'])
      listed = list(everyone)
      length = len(listed)
      pppoints = 0
      
      while length > 20:
        random_pop = random.randint(0,int(length)-1)
        listed.pop(random_pop)
        length = len(listed)
      await message.channel.send(">>> Theme: **" + themes[theme] + "**")
      result = ' '.join(str(item) for item in listed)
      embed = discord.Embed(title = ("The 20 Competing..."), description = ([result]))
      
      await message.channel.send(embed = embed)
      time.sleep(4)
      while length > 10:
        await message.channel.send("In " + "*" + str(length) + "*" + "th place...")
        total_points = random.randint(pppoints, pppoints+10)
        pppoints = total_points
        popped = random.randint(0,length-1)
        await message.channel.send(">>> " + "**" + listed[popped] + "**" + " (" + str(total_points)+ " Points)")
        time.sleep(2)
        listed.pop(popped)
        length = len(listed)
      result = ' '.join(str(item) for item in listed)
      embed = discord.Embed(title = ("The Top 10"), description = ([result]))
      await message.channel.send(embed = embed)
      time.sleep(4)
      while length > 3:
        await message.channel.send("In " + str(length) + "th place...")
        total_points = random.randint(pppoints, pppoints+10)
        pppoints = total_points
        popped = random.randint(0,length-1)
        await message.channel.send(">>> **" + listed[popped] + "**" + " (" + str(total_points)+ " Points)")
        time.sleep(2)
        listed.pop(popped)
        length = len(listed)
      await message.channel.send("In 3rd place...")
      total_points = random.randint(pppoints, pppoints+10)
      pppoints = total_points
      popped = random.randint(0,length-1)
      await message.channel.send(">>> **" + listed[popped] + "**" + " (" + str(total_points)+ " Points)")
      time.sleep(2)
      listed.pop(popped)
      length = len(listed)
      second_points = random.randint(pppoints, pppoints+10)
      pppoints = total_points
      first_points = random.randint(second_points, pppoints+10)
      pppoints = total_points
      popped = random.randint(0,length-1)
      the_winner = listed[popped]
      embed = discord.Embed(title = ("The Final 2..."), description = (str(listed[0]) + " vs " + str(listed[1])))
      await message.channel.send(embed = embed)
      await message.channel.send("Second place scored... ")
      await message.channel.send(">>> " + str(second_points) + " Points" )
      await message.channel.send("First place scored ")
      await message.channel.send(">>> " + str(first_points) + " Points..." )
      
      
      await message.channel.send("The Winner of WSC...")
      time.sleep(4)
      
      await message.channel.send(">>> **" + listed[popped] + "**" + " (" + str(first_points)+ " Points)")
      listed.pop(popped)
      length = len(listed)
      await message.channel.send(">>> **" + listed[0] + "**" + " finished second. (" + str(second_points) + " Points)")
      embed = discord.Embed(title = ("The Winner of WSC" + str(random.randint(60,200))), description = (the_winner + " with " + str(first_points) + " Points!\nTheme: " + themes[theme]))
      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/751065145073074350/1131270811848806493/cartoon-trophy-2018-1.jpg")
      await message.channel.send(embed = embed)
      
      
    if message.content.startswith("$average10"):
        points1 = 0
        count1 = 0
        points2 = 0
        count2 = 0
        points3 = 0
        count3 = 0
        points4 = 0
        count4 = 0
        points5 = 0
        count5 = 0
        count = 0
        points = 0
      
        count2 = 0
        wanted_artist = msg.split("$average10 ", 1)[1]
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            if int(numbers['Season'][3:]) <= 10:
              count1 = count1 + 1
              points1 = points1 + numbers['Number']
              count = count + 1
              points = points + numbers['Number']
            if int(numbers['Season'][3:]) > 10 and int(numbers['Season'][3:]) < 21:

              count2 = count2 + 1
              points2 = points2 + numbers['Number']
              count = count + 1
              points = points + numbers['Number']
            if int(numbers['Season'][3:]) > 20 and int(numbers['Season'][3:]) < 31:
              
              count3 = count3 + 1
              points3 = points3 + numbers['Number']
              count = count + 1
              points = points + numbers['Number']
            if int(numbers['Season'][3:]) > 30 and int(numbers['Season'][3:]) < 41:
              
              count4 = count4 + 1
              points4 = points4 + numbers['Number']
              count = count + 1
              points = points + numbers['Number']
            if int(numbers['Season'][3:]) > 40 and int(numbers['Season'][3:]) < 51:
              
              count5 = count5 + 1
              points5 = points5 + numbers['Number']
              count = count + 1
              points = points + numbers['Number']
        message_send = ''
        message_send2 = ''
        message_send3 = ''
        message_send4 = ''
        message_send5 = ''
        if count1 > 0 and points1 > 0:
          await message.channel.send(">>> Average 1-10: " + str(round(points1/count1, ndigits=1)))
          average1 = points1/count1
        if count1 == 0 and points1 == 0:
          await message.channel.send(">>> Average 1-10: Didn't Participate")
          average1 = 0
        if count2 > 0 and points2 > 0:
          await message.channel.send(">>> Average 11-20: " + str(round(points2/count2, ndigits=1)))
          average2 = points2/count2
        if count2 == 0 and points2 == 0:
          await message.channel.send(">>> Average 11-20: Didn't Participate")
          average2 = 0
        if count3 > 0 and points3 > 0:
          await message.channel.send(">>> Average 21-30: " + str(round(points3/count3, ndigits=1)))
          average3 = points3/count3
        if count3 == 0 and points3 == 0:
          await message.channel.send(">>> Average 21-30: Didn't Participate")
          average3 = 0
        if count4 > 0 and points4 > 0:
          await message.channel.send(">>> Average 31-40: " + str(round(points4/count4, ndigits=1)))
          average4 = points4/count4
        if count4 == 0 and points4 == 0:
          await message.channel.send(">>> Average 31-40: Didn't Participate")
          average4 = 0
        if count5 > 0 and points5 > 0:
          await message.channel.send(">>> Average 41-50: " + str(round(points5/count5, ndigits=1)))
          average5 = points5/count5
        if count5 == 0 and points5 == 0:
          await message.channel.send(">>> Average 41-50: Didn't Participate")
          average5 = 0
        if count > 0 and points > 0:
          await message.channel.send(">>> Average: " + str(round(points/count, ndigits=1)))
        
        
        
        
        
        averages = [average1,average2,average3,average4,average5]
        seasons = [10,20,30,40,50]
        with plt.style.context('dark_background'):
          plt.plot(seasons, averages)
        
        plt.axis([1, 60, 22, 0.9])
        plt.ylabel('Average Placement')
        plt.xlabel('Seasons')
        plt.title("Average Placement Over Seasons")
        plt.savefig(fname='plot')
        await message.channel.send(file=discord.File('plot.png'))
        plt.clf()
    if message.content.startswith("$graph"):
        everyone = []
        everyone2 = []
        wanted_artist = msg.split("$graph ", 1)[1]
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            everyone.append(int(numbers['Season'][3:]))
            everyone2.append(int(numbers['Number']))
        res = {everyone[i]: everyone2[i] for i in range(len(everyone))}
      
        myKeys = list(res.keys())
        myKeys.sort()
        sorted_dict = {i: res[i] for i in myKeys}
        keys = []
        values = []
        items = sorted_dict.items()
        for item in items:
          keys.append(item[0]), values.append(item[1])
        with plt.style.context('dark_background'):
          plt.plot(keys, values)
        plt.axis([1, 65, 30, 0.9])
        plt.scatter(keys, values)
        plt.ylabel('Placements Over Season')
        plt.xlabel('Seasons')
        plt.title(str(wanted_artist) + "'s Placements")
        plt.savefig(fname='plot')
        await message.channel.send("Loading...")
        await message.channel.send(file=discord.File('plot.png'))
        plt.clf()
    if message.content.startswith("$last10graph"):
        everyone = []
        count10 = 0
        for numbers in data:
          if numbers['Sent By'].lower() == 'ty':
            count10 += 1
        everyone2 = []
        wanted_artist = msg.split("$last10graph ", 1)[1]
        for numbers in data:
          if int(numbers['Season'][3:]) > (count10-10):
            if numbers['Sent By'].lower() == wanted_artist.lower():
              everyone.append(int(numbers['Season'][3:]))
              everyone2.append(int(numbers['Number']))
        res = {everyone[i]: everyone2[i] for i in range(len(everyone))}
      
        myKeys = list(res.keys())
        myKeys.sort()
        sorted_dict = {i: res[i] for i in myKeys}
        keys = []
        values = []
        items = sorted_dict.items()
        for item in items:
          keys.append(item[0]), values.append(item[1])
        with plt.style.context('dark_background'):
          plt.plot(keys, values)
        plt.axis([count10-10, count10+1, 30, 0.9])
        plt.scatter(keys, values)
        plt.ylabel('Placements Over Season')
        plt.xlabel('Seasons')
        plt.title(str(wanted_artist) + "'s Placements")
        plt.savefig(fname='plot')
        await message.channel.send("Loading...")
        await message.channel.send(file=discord.File('plot.png'))
        plt.clf()
    if message.content.startswith("$nlgraph"):
        everyone = []
        everyone2 = []
        wanted_artist = msg.split("$nlgraph ", 1)[1]
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            everyone.append(int(numbers['Season'][3:]))
            everyone2.append(int(numbers['Number']))
        res = {everyone[i]: everyone2[i] for i in range(len(everyone))}
      
        myKeys = list(res.keys())
        myKeys.sort()
        sorted_dict = {i: res[i] for i in myKeys}
        keys = []
        values = []
        items = sorted_dict.items()
        for item in items:
          keys.append(item[0]), values.append(item[1])
        plt.axis([1, 60, 30, 0.9])
        plt.ylabel('Placements Over Season')
        plt.xlabel('Seasons')
        plt.scatter(keys, values)
        plt.title("Placement")
        plt.savefig(fname='plot')
        await message.channel.send("Loading...")
        await message.channel.send(file=discord.File('plot.png'))
        plt.clf()
    if message.content.startswith("$passjulissa"):
        javerage = 0
        jcount = 0
        uaverage = 0
        ucount = 0
        wanted_artist = msg.split("$passjulissa ", 1)[1]
        for numbers in data:
          if numbers['Sent By'].lower() == "julissa":
            javerage += int(numbers['Number'])
            jcount += 1
          if numbers['Sent By'].lower() == wanted_artist.lower():
            uaverage += int(numbers['Number'])
            ucount += 1
        julaverage = javerage/jcount
        winsneed = 0
        useaverage = uaverage/ucount
        while (julaverage < useaverage):
          uaverage += 1
          ucount += 1
          winsneed += 1
          useaverage = uaverage/ucount
        await message.channel.send(str(wanted_artist) + " needs " + str(winsneed) + " wins in a row to pass Julissa in season averages.")
          
          
            
    if message.content.startswith("$stats"):
        points = 0
        count = 0
        wins = 0
        winrate = 0
        count3 = 0
        points3 = 0
        top5s = 0
        top10s = 0
        outoftop20s = 0
        wanted_artist = msg.split("$stats ", 1)[1]
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            count = count + 1
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            if numbers['Number'] == 1:
              wins = wins + 1
            
            if numbers['Number'] < 6:
              top5s += 1
            if numbers['Number'] < 11:
              top10s += 1
            if numbers['Number'] > 20:
              outoftop20s += 1
        
        if wins > 0:
          winrate = wins/count*100
        if wins == 0:
          winrate = 0
        winrated = str(round(winrate, ndigits=2)) + "%"
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            count3 = count3 + 1
            points3 = points3 + numbers['Number']
        averagep = round(points3/count3, ndigits=1)
        points2 = 0
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            points2 = points2 + numbers['Points']
        points4 = 0
        count4 = 0
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            points4 = points4 + numbers['Points']
            count4 = count4 + 1
        averagepo = round(points4/count4, ndigits=1)
        count7 = 0
        inTop50 = 0
        inTop100 = 0
        inTop250 = 0
        count8 = 0
        count9 = 0
        count10 = 0
        count11 = 0
        points11 = 0
        best_song = ''
        worst_song = ''
        average10 = 0
        for numbers in data:
          if count7 <= 50:
            if numbers['Sent By'].lower() == wanted_artist.lower():
              inTop50 = inTop50 + 1
          if count7 <= 100:
            if numbers['Sent By'].lower() == wanted_artist.lower():
              inTop100 = inTop100 + 1
          if count7 <= 250:
            if numbers['Sent By'].lower() == wanted_artist.lower():
              inTop250 = inTop250 + 1
          count7 = count7  + 1
        for numbers in data:
          if count8 == 0:
            if numbers['Sent By'].lower() == wanted_artist.lower():
              best_song = numbers['Song']
              count8 = 1
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            worst_song = numbers['Song']
        for numbers in data:
          if numbers['Sent By'] == "Ty":
            count10 += 1
        for numbers in data:
          if numbers['Sent By'].lower() == wanted_artist.lower():
            if int(numbers['Season'][3:]) > (count10-10):
              count11 = count11 + 1
              points11 = points11 + numbers['Number']
              average10 = points11/count11
              average10 = round(average10, ndigits=2)
        if count11 == 0:
          average10 == 0
        count12 = 0
        if wanted_artist.lower() == "kesha":
          count12 = 1
        total_seasons = 0 
        for numbers in data:
          if numbers['Sent By'] == "Ty":
            total_seasons += 1
        participationrate = str(round(count/total_seasons*100, ndigits=2)) + "%"
        if count12 == 0:
          embed = discord.Embed(title = (str(wanted_artist) + "'s Stats"), description = "Participations: " + str(count) + "\nWins: " + str(wins) +"\nWinrate: " + str(winrated) + "\nTop 5s: " + str(top5s) + "\nTop 10s: " + str(top10s) + "\nSongs Finished 20+: " + str(outoftop20s) + "\nAverage Placement: " + str(averagep) + "\nAverage Placement Last 10: " + str(average10) + "\nTotal Points: " + str(points2) + "\nAverage Points: " + str(averagepo) + "\nSongs In Top 50 Most Points: " + str(inTop50)  + "\nSongs In Top 100 Most Points: " + str(inTop100)  + "\nSongs In Top 250 Most Points: " + str(inTop250)  + "\nSong With Most Points: " + str(best_song) + "\nSong With Least Points: " + str(worst_song) + "\nParticipations Rate: " + str(participationrate))
        if count12 == 1:
          embed = discord.Embed(title = (str(wanted_artist) + "'s Stats"), description = "Participations: " + str(count) + "\nWins: " + "Still Zero... Huh that's weird." +"\nWinrate: " + str(winrated) + "\nTop 5s: " + str(top5s) + "\nTop 10s: " + str(top10s) + "\nSongs Finished 20+: " + str(outoftop20s) + "\nAverage Placement: " + str(averagep) + "\nAverage Placement Last 10: " + str(average10) + "\nTotal Points: " + str(points2) + "\nAverage Points: " + str(averagepo) + "\nSongs In Top 50 Most Points: " + str(inTop50)  + "\nSongs In Top 100 Most Points: " + str(inTop100)  + "\nSongs In Top 250 Most Points: " + str(inTop250)  + "\nSong With Most Points: " + str(best_song) + "\nSong With Least Points: " + str(worst_song) + "\nParticipations Rate: " + str(participationrate))
        await message.channel.send(embed = embed)


  
    if message.content.startswith("$trivia"):    
      questionG = 0
      wanted_artist = ''
      if message.content == "$trivia":
        questionG = random.randint(1,3)
      if message.content != "$trivia":
          wanted_artist = msg.split("$trivia", 1)[1]
      if message.content == ("$triviawsi"):
        questionG = 1
      if message.content == ("$triviawwsc"):
        questionG = 4
      if message.content == ("$triviawp"):
        questionG = 3
      if message.content == ("$triviahol"):
        questionG = 2
      if message.content == ("$triviaholp"):
        questionG = 5
      totalentries = 0
      songandartist = ''
      sentby = ''
      counting1 = 0
      for number in data:
        totalentries += 1
      if (questionG == 1):
        await message.channel.send("Category: **Who Sent It?**")
        time.sleep(2)
        sortingentries = random.randint(0,totalentries)
        for number in data:
          if counting1 < sortingentries:
            songandartist = (str(number['Song']) + ", " + str(number['Artist']))
            sentby = number['Sent By']
          counting1 += 1
        await message.channel.send("**Who Sent This Song?**")
        await message.channel.send(">>> " + songandartist)
        time.sleep(10)
        await message.channel.send("The answer...")
        await message.channel.send(">>> **" + str(sentby) + "**")
      if (questionG == 4):
        await message.channel.send("Category: **What WSC Was It Sent In?**")
        time.sleep(2)
        sortingentries = random.randint(0,totalentries)
        for number in data:
          if counting1 < sortingentries:
            songandartist = (str(number['Song']) + ", " + str(number['Artist']) + " -  Sent By: " + str(number['Sent By']))
            sentby = number['Season']
          counting1 += 1
        await message.channel.send("What WSC Was This Submitted In?")
        await message.channel.send(">>> " + songandartist)
        time.sleep(10)
        await message.channel.send("The answer...")
        await message.channel.send(">>> **" + str(sentby) + "**")
      if (questionG == 3):
        await message.channel.send("Category: **What Placement?**")
        time.sleep(2)
        sortingentries = random.randint(0,totalentries)
        for number in data:
          if counting1 < sortingentries:
            songandartist = (str(number['Song']) + ", " + str(number['Artist']) + " - Sent By:" + str(number['Sent By']) + " In " + str(number['Season']))
            sentby = number['Placement']
          counting1 += 1
        await message.channel.send("What Placement Did This Song Get?")
        await message.channel.send(">>> " + songandartist)
        time.sleep(10)
        await message.channel.send("The answer...")
        await message.channel.send(">>> **" + str(sentby) + "**")
      if (questionG == 2):
        await message.channel.send("Category: **Higher or Lower?**")
        time.sleep(2)
        sortingentries = random.randint(0,totalentries)
        for number in data:
          if counting1 < sortingentries:
            songandartist = (str(number['Song']) + ", " + str(number['Artist']) + " - Sent By: " + str(number['Sent By']) + " In " + str(number['Season']))
            sentby = number['Points']
          counting1 += 1
        fakenumber = random.randint(sentby-12,sentby+12)
        answer = ''
        await message.channel.send("Did This Song Get Higher or Lower points than **" + str(fakenumber) + "** ?")
        if fakenumber > sentby:
          answer = 'Lower'
        if fakenumber < sentby:
          answer = 'Higher'
        if fakenumber == sentby:
          answer = 'Equal'
        await message.channel.send(">>> " + songandartist)
        time.sleep(10)
        await message.channel.send("The answer...")
        await message.channel.send(">>> **" + str(answer) + "**, the song received " + str(sentby) + " points.")
      if (questionG == 5):
        await message.channel.send("Category: **Higher or Lower? *Placement* **")
        time.sleep(2)
        totalentries=0
        for number in data:
          if number['Number'] > 2:
            totalentries += 1
        sortingentries = random.randint(0,totalentries)
        for number in data:
          if number['Number'] > 2:
            if counting1 < sortingentries:
              songandartist = (str(number['Song']) + ", " + str(number['Artist']) + " - Sent By: " + str(number['Sent By']) + " In " + str(number['Season']))
              sentby = number['Number']
          counting1 += 1
        fakenumber = random.randint(sentby-3,sentby+3)
        if fakenumber == sentby:
          fakenumber += 1
        answer = ''
        await message.channel.send("Did This Song Place Higher or Lower than **" + str(fakenumber) + "** ?")
        if fakenumber > sentby:
          answer = 'Higher'
        if fakenumber < sentby:
          answer = 'Lower'
        if fakenumber == sentby:
          answer = 'Equal'
        await message.channel.send(">>> " + songandartist)
        time.sleep(10)
        await message.channel.send("The answer...")
        await message.channel.send(">>> **" + str(answer) + "**, the song placed " + str(sentby) + ".")
        
        
    
            
          


    if message.content.startswith("$rankdownresults"):   
       embed = discord.Embed(title= "Drag Race Rankdown 2023 Results", description=  
       "1. Monet X Change (4.3 Avg)\n2. Miss Fiercelicious (5.1 Avg)\n3. Jaida Essence Hall (5.2 Avg)\n4. Symone (5.5 Avg)\n5. Priyanka(5.8 Avg)\n6. Mistress Isabelle Brooks (6.1 Avg)\n7. Raja (6.8 Avg)\n8. Alaska (7.0 Avg)\n9. Alyssa Edwards (7.2 Avg)\n10. Juriji Der Klee (7.3 Avg)\n11. Bimini Bon Boulash (7.5 Avg)\n12. Keiona (7.8 Avg)\n13. Lemon (8.0 Avg)\n14. Kylie Sonique Love (8.2 Avg)\n15. Sagittaria (12.2 Avg)")
       await message.channel.send(embed=embed)
  
    
    if message.content.startswith("$help"):   
       embed = discord.Embed(title= "All Commands", description=  
      "**$artist <Artist Name>** \nLists all submissions that included an artist \n \n**$season <Season>** \nLists all submissions for a season \n\n**$placement <Placement>**\nLists all songs that had the same placement \n\n**$submissions <Name>**\nLists all submissions by one person \n\n**$song <Title>**\nLists all songs containing a phrase entered \n\n**$points <Points>**\nShows all submissions which received a certain amount of points\n\n**$average10 <Name>**\nShows average per 10 seasons\n\n**$randomsong <Name>**\nSends a random song submitted by someone. Without including a name picks from all songs\n\n**$stats <Name>**\nDisplays a WSC stats page\n\n**$graph <Name>**\nDisplays a graph for all seasons participated\n\n**$spotify**\nLinks to the playlist's Spotify\n\n**$youtube**\nLinks to the playlist's Youtube\n\n**$due**\nSays when voting is due (adjusted to timezone)\n\n**$sorter**\nLinks to the playlist's sorter\n\n**$bestaverage**\nShows the 10 best averages in WSC\n\n**$bestlast10**\nShows the 10 best averages of the last 10 WSC\n\n**$mostap**\nShows the 10 highest average points per WSC\n\n**$mostpart**\nShows the 10 people with the most times participated\n\n**$mostwins**\nShows the 10 people with the most wins\n\n**$mostpoints**\nShows the 10 people with the most accumulated points\n\n**$simulate**\nSimulates a fake WSC season\n\n**$trivia**\nGenerates WSC Trivia\n\n")

       await message.channel.send(embed=embed)
      
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run("MTEzMDczMDQ3NDAzODM3NDQxMQ.GOJooy.KbkKWe2uLwnW8drO9RGjRHkf4XcCtwgGKJjgMQ")

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  return "Bot up and running"
if __name__ == '__main__':
  app.run(host="0.0.0.0",debug=True,port=8080)