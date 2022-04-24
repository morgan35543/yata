import os
import platform

from sre_constants import SRE_FLAG_DEBUG
from django.contrib.auth.models import User
from player.models import Player
from player.models import PlayerData
from faction.models import Faction
from setup.models import APIKey
from awards.models import AwardsData
from faction.models import FactionData
from bazaar.models import BazaarData
from company.models import CompanyDescription
from loot.models import NPC
from bot.models import Bot
from decouple import config

class Configuration:
    reset_db_question = "Do you want to reset the database?"
    fill_db_question = "Do you want to fill the database?"
    key = config('SECRET_KEY')

    def yes_or_no(self, question):
        reply = str(input(question + ' (y/n): ')).lower().strip() 

        confirmation = [ "yes", "ye", "y" ]

        if (reply in confirmation or [ 'no', 'n']):
            return reply in confirmation
        else:
            return self.yes_or_no("Invalid input. Please enter")

    def reset_db(self):
        if (self.yes_or_no(self.reset_db_question) is False):
            return

        if (config("DATABASE") == "postgresql"):
            print('Remove local database')
            cmd = 'python manage.py reset_db'
            r = os.system(cmd)
        else:
            # remove local database
            print('Remove local database')
            cmd = 'rm -vf db.sqlite3'
            r = os.system(cmd)

        # migrate
        cmd = 'python manage.py migrate'
        r = os.system(cmd)

        # create cache table
        cmd = 'python manage.py createcachetable'
        r = os.system(cmd)

        # create db super user
        if not len(User.objects.all()):
            print('create superuser')
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')

        # create required objects
        if not len(PlayerData.objects.all()):
            print('Create Players stats')
            cmd = 'python manage.py players_stats'
            r = os.system(cmd)

        if not len(Player.objects.filter(tId=-1)):
            print('Create Player')
            Player.objects.create(tId=-1, name="Anonymous", validKey=False)

        if not len(Faction.objects.filter(tId=-1)):
            print('Create Faction')
            Faction.objects.create(tId=-1, name="Faction Anonymous")

        if not len(APIKey.objects.all()) and self.key:
            print('Create API Key')
            APIKey.objects.create(key=self.key)

        if not len(AwardsData.objects.all()):
            print('Create Awards data')
            AwardsData.objects.create()

        if not len(BazaarData.objects.all()):
            print('Create Bazaar data')
            BazaarData.objects.create()

        if not len(FactionData.objects.all()):
            print('Create Faction data')
            FactionData.objects.create()
            cmd = 'python manage.py init_faction_tree'
            r = os.system(cmd)

        if not len(NPC.objects.all()):
            print('Create NPC')
            NPC.objects.create(tId=4, show=True)
            NPC.objects.create(tId=15, show=True)
            NPC.objects.create(tId=19, show=True)

        if not len(CompanyDescription.objects.all()):
            print('Create NPC')
            cmd = 'python manage.py init_companies'
            r = os.system(cmd)

        if not len(Bot.objects.all()) >= 3:
            print('Create Bots')
            for i in range(3):
                Bot.objects.create(token=f"Token {i + 1}", name=f"Bot {i + 1}")
    
    def fill_db(self):
        if (self.yes_or_no(self.fill_db_question) is False):
            return

        cmd = 'python manage.py check_keys'
        r = os.system(cmd)
        cmd = 'python manage.py awards'
        r = os.system(cmd)
        cmd = 'python manage.py territories'
        r = os.system(cmd)
        cmd = 'python manage.py items'
        r = os.system(cmd)
        cmd = 'python manage.py players'
        r = os.system(cmd)
        cmd = 'python manage.py loot'
        r = os.system(cmd)
        cmd = 'python manage.py factions'
        r = os.system(cmd)
        cmd = 'python manage.py companies'
        r = os.system(cmd)

    def static_files(self):
        # Has its own yes/no
        cmd = 'python manage.py collectstatic'
        r = os.system(cmd)