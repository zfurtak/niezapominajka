from project.project_package.src.database.database import Database
from datetime import datetime, timedelta
db = Database()

if __name__ == '__main__':
    pass
    # db.create_users_table()
    # db.create_plants_table()
    # db.create_plants_table()
    #
    # db.create_species("Monstera dziurawa", "Monstera deliciosa", 7,
    #                   "Preferuje miejsca zacienione", "Nie należy przelewać, warto zraszać liście",
    #                   "Nie należę do słabych zawodników", "GUI/images/species/monstera_dziurawa.jpg")
    # db.create_species("Paproć", "Nefrolepis", 3, "Lubi rozproszone światło", "Nie lubi przeciągów", "Dbam o wilgotność powietrza",
    #                   "GUI/images/species/paproc.jpg")
    # db.create_species("Fikus", "Ficus", 7, "Lubi światło, ale nie bardzo intensywne", "Nie lubi przemieszczania",
    #                   "Oczyszczam powietrze i jestem raczej pozytywny", "GUI/images/species/fikus.jpg")
    # db.create_species("Sensevieria gwinejska", "Sensevieria trifasciata", 10, "Lubi pełne słońce", "Bardzo odporna na złe warunki",
    #                   "Mówią na mnie wężownica albo język teściowej", "GUI/images/species/sans.jpg")
    # db.create_species("Storczyk falenopsis", "Phalaenopsis", 10, "Lubi światło, ale nie za mocno (wschodnie okno)",
    #                   "Najlepiej zamiast podlewania zanurzyć mnie w wodzie na 5 minut",
    #                   "Jestem gwiazdą wsród storczyków", "GUI/images/species/falenopsis.jpg")

    # db.create_user('test', 'test', photo_source='GUI/images/groot.jpg', last_dead_plant='2022-05-15',
    #                join_date=str(datetime.today()))
    #
    # db.create_plant('zuzia', 'normalnie', 'Fikus', '14/04/22', 'kuchnia', 'nic', '31/05/22', '')
    # db.create_plant('zuzia', '1234', 'Fikus', '14/04/22', 'kuchnia', 'nic', '29/05/22', '')
    # db.create_plant('zuzia', '1234444', 'Fikus', '14/04/22', 'kuchnia', 'nic', '05/06/22', '')
    # db.create_plant('zuzia', 'normalnie', 'Paproć', '14/04/22', 'kuchnia', 'nic', '03/06/22', '')
