"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3
from peewee import *
db = SqliteDatabase('chainsaw_jugglers.sqlite')

class Players(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.country}, {self.catches}'

db.connect()
db.create_tables([Players])

JaM = Players(name='Janne Mustonen', country= 'Finland', catches = 98)
JaM.save()  #must SAVE every item

IaS = Players(name='Ian Stewart', country= 'Canada', catches = 94)
IaS.save()  #must SAVE every item

AaG = Players(name='Aaron Grett', country= 'Canada', catches = 88)
AaG.save()  #must SAVE every item

ChT = Players(name='Chad Taylor', country= 'USA', catches = 78)
ChT.save()  #must SAVE every item



#name 
# country 
# number of catches
def main():
    menu_text = """
    1. Display all records
    2. Add new record
    3. Edit existing record
    4. Delete record 
    5. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            add_new_record()
        elif choice == '3':
            edit_existing_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    players = Players.select()
    for player in players:
        print(player)

    list_of_players = list(players)  #regular python list   
    print(list_of_players)

##todo add new record. What if user wants to add a record that already exists?'
def add_new_record():

    print('Enter the information of the new player: ')
    
    new_player_name = input('Enter the name of the new player: ')
    new_player_country = input('Enter the country ')
    new_player_catches = input('Enter the players catches ')

    #new_player_info = new_player_name, new_player_country, new_player_catches 
    new_player_to_save = Players(name={new_player_name}, country={new_player_country}, catches ={new_player_catches})
    new_player_to_save.save()  #must SAVE every item



def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?') 


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 


if __name__ == '__main__':
    main()