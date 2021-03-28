import os
import logging

from discord.ext import commands

class RobotCop(commands.Bot):
    def __init__(self, responses):
        """Initialisation de l'instance 

        Args:
            responses (dict): Dictionnary contained in bot.json file
        """
        super().__init__(command_prefix="-")
        self.dict_responses = responses

    async def on_ready(self):
        """Indicate if the bot is correctly connected on the server
        """
        print(f"{self.user.display_name} is connected on the server.")

    async def on_disconnect(self):
        """Indicate if the bot has been disconnected from the server
        """
        print(f"{self.user.display_name} is disconnected from the server.")

    async def on_message(self, message):
        """Reaction with messages sent by user on the server

        Args:
            message (class 'discord.message.Message'): Message get on the server
        """
        if message.author == self.user:
            return

        #Check if the message begins with one word from the bot.json file
        first_words_user_message = message.content.lower().startswith(tuple(self.dict_responses.keys()))

        if first_words_user_message:
            message_first_part = message.content.lower().split(" ")[0]

            if len(message_first_part) < 3:
                message_first_part = message.content.lower().split(" ")[0:2]
                message_first_part = " ".join(message_first_part)

            #Bot is responding with the value of the key used by the user
            try:
                await message.channel.send(self.dict_responses[message_first_part].format(username=message.author.display_name))
            except KeyError:
                logging.warning("Oh seems we lost a key? haha joking")
            else:
                print("RobotCop sent a message!")

    @commands.command(name="del")
    async def delete(self, ctx, number_of_messages: int):
        messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

        for each_message in messages:
            await each_message.delete()

