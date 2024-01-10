
#imports
import discord
import giphy_client 


from giphy_client.rest import ApiException
from discord.ext import commands
import random
from my_token import secret_token
from my_token import channelID
from my_token import api_key
from animal_library_reader import animal_names_lower 







client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
#a set to store sent GIFs' IDs 
sent_gifs = set() 

#executes when bot is ready
@client.event
async def on_ready():
     print("bot is ready")


#main function
@client.command()
async def cute(ctx, *, user_input="" ):
    global sent_gifs

    #creating an instance of the Giphy API client
    api_instance = giphy_client.DefaultApi()

    #setting user's input into lowercase 
    user_input_lower = user_input.lower()

    if user_input_lower in animal_names_lower:

        try:
            #query input
            query = (f"cute {user_input_lower}")

            #fetching multiple GIFs using query and rating 'g'
            api_response = api_instance.gifs_search_get(api_key, query, rating='g', limit=32)
            lst = list(api_response.data)
            
            #filtering out already sent GIFs to avoid same GIF being sent more than once
            new_gifs = [g for g in lst if g.id not in sent_gifs]
            
            #resetting sent GIFs set if all GIFs have been sent
            if not new_gifs:
                sent_gifs = set()  
                new_gifs = lst

            giff = random.choice(new_gifs)
            #store the sent GIF's ID in the set
            sent_gifs.add(giff.id)  
            
            #sending GIF in channel
            await ctx.channel.send(giff.embed_url)

        #handling exceptions
        except ApiException as ae:
            print("Exception when calling API")

    #if user sent an input that is not in the text library, print "invalid input :/"
    if user_input_lower not in animal_names_lower:
        await ctx.channel.send("invalid input :/")

#running discord bot with specific token
client.run(secret_token)

