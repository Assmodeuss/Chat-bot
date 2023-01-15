# AI CHAT BOT
## _Latest, easy, fast, customizable_

This template is for a simple ai chat bot for a custom channel, it's easy to customize, use, and setup.
## Bot made by [Asmodeus#8700](https://discord.com/users/634343118384398347)
Star for support 

## API

- API used is provided by [random-stuff-api](https://rapidapi.com/pgamerxdev/api/random-stuff-api)
- Created by [PGamerX#2809](https://discord.com/users/587663056046391302)
- Support Server for api [click here](https://discord.com/invite/4TeGKpSkdN)
- [Website](https://development.pgamerx.com)
- [Docs](https://api-docs.pgamerx.com/)





## IMPORTANT LINKS


| |  |
| ------ | ------ |
| API | [link](https://rapidapi.com/pgamerxdev/api/random-stuff-api) |
| Bot dev| [link](https://discord.com/users/634343118384398347) |
| API dev | [link](https://discord.com/users/587663056046391302) |
| API KEY | [link](https://api-info.pgamerx.com/manage-key) |
| Support server (API) | [link](https://discord.com/invite/4TeGKpSkdN) |


##Setup
```py

@bot.command()
async def setup(ctx):
	async with aiohttp.ClientSession(headers=headervar) as session:
		param_var = {"BotName":"Indigo", "BotMaster":"CannonBall Chris", "BotAge":69}#....You can find all customizations at: https://rsa-api.xyz > Documentation
		async with session.post(url=CUSTOMIZATION_URL, params = param_var) as sess:
			output = await sess.json()
			await ctx.send(output["message"])
#Use this command only once. THis command will help your bot to be registered on your api key in the db of api. So, you don't have to pass this information everytime. Its just one time only.
```
_Latest as per 2023_
