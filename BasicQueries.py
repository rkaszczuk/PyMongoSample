from pymongo import MongoClient

db_name = 'pySamples'
collection_name = 'basicQueries'
client = MongoClient('localhost', 27017)

db = client[db_name]
collection = db[collection_name]

user = {
    'name': 'Ann',
    'age': 32
}


# 1. Dodaj warunek sprawdzajacy czy w bazie istnieje uzytkownik o imieniu Ann
if 1 is None:

    new_id = 1 #2. Dodaj do bazy użytkownika w zmiennej user. new_id będzie ObjectId nowo dodanego obiektu
    print("Added new record " + str(new_id))
#koniec warunku

#3. Pobierz do zmiennej uzytkownika o imieniu Ann
user_ann = None
print(user_ann)

#4. Zwieksz wiek uzytkownika o 10

#5. Do zmiennej user_ann ponownie przypisz użytkownika o imieniu Ann
user_ann = None
print(user_ann)

#6. Usuń użytkownika Ann z bazy

#7. Sprawdź czy użytkownik nie istnieje w bazie (zapytanie powinno zwrócić None)
user_ann = None
print(user_ann)