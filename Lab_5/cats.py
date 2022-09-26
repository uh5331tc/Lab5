from peewee import *

db = SqliteDatabase('cats.sqlite')

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.color}, {self.age}'

db.connect()
db.create_tables([Cat])

zoe = Cat(name='Zoe', color= 'brown', age=3)
zoe.save()  #must SAVE every item

holly = Cat(name='Holly', color= 'Tabby', age=5)
holly.save()  #must SAVE every item

cats = Cat.select()
for cat in cats:
    print(cat)

list_of_cats = list(cats)  #regular python list


"""CRUD OPPERATIONS
CREATE-  insert
READ-  select 
UPDATE- 
DELETE-
"""
# could update many rows if needed 
#assign it a variable for easy access!!
rows_modified = Cat.update(age=6).where(Cat.name == 'Holly').execute()

#viewing age change
print('After Hollys birthday')
cats = Cat.select()
for cat in cats:
    print(cat)

print(rows_modified)

## add a cat 
buzz = Cat(name='Buzz', color='Gray', age=3)
buzz.save()  # must SAVE

#variable to find cats who are three
cats_who_are_3 = Cat.select().where(Cat.age == 3)

#loop over all 3yo cats
for cat in cats_who_are_3:
    print(cat, ' is three')

#find cats with L in their name
cat_with_l_in_name = Cat.select().where(Cat.name.contains('l'))
for cat in cat_with_l_in_name:
    print(cat, ' has l in name ')


#get or none is safer 
zoe_from_db = Cat.get_or_none(name='Zoe')
print(zoe_from_db)

#get by ID
cat_1 = Cat.get_by_id(1)
print(cat_1)

#count, sort, limit
total = Cat.select().count()
print(total)

#total cats who are 5, none because it was holly birthday
total_cats_who_are_5 = Cat.select().where(Cat.age == 3).count()
print(total_cats_who_are_5)

#sorted by name
cats_by_name = Cat.select().order_by(Cat.name)
print(list(cats_by_name))

#cats  ordered by age decending then by name *desc
cats_by_age = Cat.select().order_by(Cat.age.desc(), Cat.name.desc())
print(list(cats_by_age))

#get first 3 and order by name
first_3 = Cat.select().order_by(Cat.name).limit(3)
print(list(first_3))

#### DELETE #####
rows_delete = Cat.delete().where(Cat.name == 'Holly').execute()
print(list(Cat.select()))


