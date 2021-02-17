# wordchain bot
WordChain-Bot is a discord wordchain game bot, written in Python
 - Made by Jinpyo Joo
 - DB by [kkutu](https://github.com/JJoriping/KKuTu)

### Features
 - Customizable word lists
 - Be able to use the 두음법칙

### How to use

#### Import word data
1. You can import word data from [KKuTu](https://github.com/JJoriping/KKuTu).<br>[How to load from .sql file](https://blog.naver.com/dosel1005/220935346136)
2. Install modules (psycopg2)
3. run Connect.py (Maybe you need to modify the password in the file)

#### Run
1. You can delete all the words in one letter. Run filter.py
2. Edit config.json file.
```json
{
    "token": "TOKEN", // Discord bot token
    "prefix": "!", // Prefix+끝말잇기
    "timeover" : 10 // Word input timeout (Default 10s)
}
```
3. run bot.py

## Licence
[Hangul-utils](https://github.com/kaniblu/hangul-utils) GPL-3.0 License<br>
[KKuTu](https://github.com/JJoriping/KKuTu) GPL-3.0 License
