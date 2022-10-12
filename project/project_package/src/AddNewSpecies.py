from project.project_package.src.database.database import Database
from datetime import datetime, timedelta
db = Database()

if __name__ == '__main__':
    pass
    #db.delete_user(1)
    # print(db.get_users())
    # db.create_species("Monstera dziurawa", "Monstera deliciosa", 7,
    #                   "Preferuje miejsca zacienione", "Nie należy przelewać, warto zraszać liście",
    #                   "Nie należę do słabych zawodników", "images/species/monstera_dziurawa.jpg")
    # db.create_species("Paproć", "Nefrolepis", 3, "Lubi rozproszone światło", "Nie lubi przeciągów", "Dbam o wilgotność powietrza",
    #                   "images/species/paproc.jpg")
    # db.create_species("Fikus", "Ficus", 7, "Lubi światło, ale nie bardzo intensywne", "Nie lubi przemieszczania",
    #                   "Oczyszczam powietrze i jestem raczej pozytywny", "images/species/fikus.jpg")
    # db.create_species("Sensevieria gwinejska", "Sensevieria trifasciata", 10, "Lubi pełne słońce", "Bardzo odporna na złe warunki",
    #                   "Mówią na mnie wężownica albo język teściowej", "images/species/sans.jpg")
    # db.create_species("Storczyk falenopsis", "Phalaenopsis", 10, "Lubi światło, ale nie za mocno (wschodnie okno)",
    #                   "Najlepiej zamiast podlewania zanurzyć mnie w wodzie na 5 minut",
    #                   "Jestem gwiazdą wsród storczyków", "images/species/falenopsis.jpg")

    # db.create_user('test', 'test', photo_source='images/groot.jpg', last_dead_plant='2022-05-15',
    #                join_date=str(datetime.today()))
    #
    db.create_plant('user', 'okay', 'Fikus', '05/10/22', 'bathroom', 'nic', '05/10/22', '')
    db.create_plant('user', 'forget', 'Fikus', '05/10/22', 'bathroom', 'nic', '01/10/22', '')
    db.create_plant('user', 'forget2', 'Fikus', '05/10/22', 'bedroom', 'nic', '20/09/22', '')
    # db.create_plant('test', 'plant7', 'Fikus', '14/04/22', 'living room', 'nic', '05/10/22', '')
    # db.create_plant('test', 'plant8', 'Paproć', '14/04/22', 'kitchen', 'nic', '03/10/22', '')
