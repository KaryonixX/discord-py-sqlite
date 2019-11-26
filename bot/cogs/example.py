import os
import sqlite3
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        DB_NAME = "example"
        db_path = os.path.join(os.path.abspath(os.getcwd()), DB_NAME + ".db")
        self.db = sqlite3.connect(db_path)
        self.db_cursor = self.db.cursor()
        self.db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            discriminator TEXT
        )
        """)

    @commands.command(name="whoami")
    async def whoami(self, ctx):
        self.db_cursor.execute("SELECT * FROM users WHERE id=?". (ctx.author.id,))
        response = self.db_cursor.fetchone()

        if not response:
            self.db_cursor.execute("INSERT INTO users VALUE (?,?,?)",
                (ctx.author.id, ctx.author.name, ctx.author.discriminator,))
            self.db.commit()

        uid, name, discriminator = response
        await ctx.send("<@{}>, you are {}#{}.".format(uid, name, discriminator))

def setup(bot):
    bot.add_cog(Example(bot))