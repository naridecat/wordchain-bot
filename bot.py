import discord, json, random, asyncio, hangulutils, jamo
client = discord.Client()

# word에 단어 데이터 넣기
word = json.loads(open('output.json', 'r', encoding='utf-8').read())
user = {}
playing = []

# config 받아오기
config = json.loads(open('config.json', 'r', encoding='utf-8').read())

# 단어 개수 가져오기
@client.event
async def on_ready():
    game = discord.Game(f"단어 {str(len(word))}개를 경험하고 있습니다")
    await client.change_presence(activity=game)
    print('ready')


# 타임오버 함수
async def wait(count, id, message):
    await asyncio.sleep(config['timeover'])
    if user[id]['count'] == count: 
        if message.author.id in playing:
            playing.remove(id)
            embed = discord.Embed(title='게임오버', description=f"{message.author.display_name}\n`{str(count)}`")
            await message.channel.send(embed=embed)    

@client.event
async def on_message(message):
    if message.author.id in playing and message.author.id != client.user.id:
        jamo_txt = str(jamo.j2hcj(jamo.h2j(user[message.author.id]['this'][-1])))
        if jamo_txt.startswith("ㄹ"):
            jamo_char = [user[message.author.id]['this'][-1], hangulutils.join_jamos("ㄴ"+str(jamo_txt[1:]))]
        else:
            jamo_char = message.content[0]
        print("jamo:"+str(jamo_char))
        print(jamo_char)
        print(user[message.author.id]['this'][-1])
        if user[message.author.id]['this'][-1] in jamo_char:
            if not message.content in user[message.author.id]['used']:
                if message.content in word:
                    temp = []
                    jamo_char = []
                    try:
                        jamo_txt = str(jamo.j2hcj(jamo.h2j(message.content[-1])))
                        if jamo_txt.startswith("ㄹ"):
                            jamo_char = [message.content[-1], hangulutils.join_jamos("ㅇ"+str(jamo_txt[1:]))]
                            for i in range(len(word)):
                                if word[i][0] in jamo_char:
                                    temp.append(word[i])
                        else:
                            for i in range(len(word)):
                                if word[i].startswith(message.content[-1]):
                                    temp.append(word[i])
                        user[message.author.id]['used'].append(message.content)
                        user[message.author.id]['this'] = temp[random.randint(0, len(temp))]
                        if message.author.id in playing:
                            await message.channel.send("`"+message.author.display_name+"`\n**"+user[message.author.id]['this']+"**")
                            user[message.author.id]['used'].append(user[message.author.id]['this'])
                            user[message.author.id]['count'] = user[message.author.id]['count'] + 1
                            await wait(user[message.author.id]['count'], message.author.id, message)
                    except Exception as ex:
                        if message.author.id in playing:
                            playing.remove(message.author.id)
                        print(ex)
                        if user[message.author.id]['count']:
                            embed = discord.Embed(title='게임승리', description=f"{message.author.display_name}\n`{str(user[message.author.id]['count'])}`")
                        await message.channel.send(embed=embed)    

            else:
                await message.channel.send("이미 사용한 단어자나요 :thinking:")

    if message.content.startswith(config['prefix']+"끝말"):
        if not message.author.id in playing:
            playing.append(message.author.id)
            user[message.author.id] = {}
            user[message.author.id]['used'] = []
            user[message.author.id]['this'] = []
            user[message.author.id]['this'] = ""
            user[message.author.id]['this'] = word[random.randint(0, len(word))]
            await message.channel.send("`"+message.author.display_name+"`\n**"+user[message.author.id]['this']+"**")
            user[message.author.id]['used'].append(user[message.author.id]['this'])
            user[message.author.id]['count'] = 0
            user[message.author.id]['status'] = 0
            await wait(user[message.author.id]['count'], message.author.id, message)
        else:
            await message.channel.send("이미 게임중이잖아요!\n뭐하는거시에오 ㅇ0ㅇㅠㅠㅠ")
        

client.run(config['token'])