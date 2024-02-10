import discord
from discord import app_commands
from . import Guilds

class MyCommandTree(app_commands.CommandTree):

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        guild = Guilds.getGuild(interaction.guild_id)

        print(f'Guild: {guild.guild}')

        print(f'Required: {guild.required_role}')
        print(f'Roles: {interaction.user.roles}')

        for role in interaction.user.roles:
            print(role.name)
            if str(role.name) == str(guild.required_role):
                print(role.name)
                print("You have permission")
                return True

        print("You cannot Access This Bot")
        await interaction.response.send_message(f'Sorry, you are not allowed to use this bot. Request: {guild.required_role}')    
        return False