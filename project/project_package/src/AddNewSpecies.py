from project.project_package.src.database.database import Database

db = Database()

if __name__ == '__main__':

    db.create_users_table()
    db.create_plants_table()
    db.create_plants_table()

    db.create_species("Monstera dziurawa", "Monstera deliciosa", 7,
                      "Preferuje miejsca zacienione", "Nie należy przelewać, warto zraszać liście",
                      "Nie należę do słabych zawodników", "GUI/images/species/monstera_dziurawa.jpg")
    db.create_species("Paproć", "Nefrolepis", 3, "Lubi rozproszone światło", "Nie lubi przeciągów", "Dbam o wilgotność powietrza",
                      "GUI/images/species/paproc.jpg")
    db.create_species("Fikus", "Ficus", 7, "Lubi światło, ale nie bardzo intensywne", "Nie lubi przemieszczania",
                      "Oczyszczam powietrze i jestem raczej pozytywny", "GUI/images/species/fikus.jpg")
    db.create_species("Sensevieria gwinejska", "Sensevieria trifasciata", 10, "Lubi pełne słońce", "Bardzo odporna na złe warunki",
                      "Mówią na mnie wężownica albo język teściowej", "GUI/images/species/sans.jpg")
    db.create_species("Storczyk falenopsis", "Phalaenopsis", 10, "Lubi światło, ale nie za mocno (wschodnie okno)",
                      "Najlepiej zamiast podlewania zanurzyć mnie w wodzie na 5 minut",
                      "Jestem gwiazdą wsród storczyków", "GUI/images/species/falenopsis.jpg")

    # plant = load_plant(db.get_plant(plant_name, username)[1], species)
    # self.ids.species.text = f'Gatunek: {plant.species.name}'
    # self.ids.room.text = f'Moje lokum: {plant.room}'
    # self.ids.notes.text = f'Coś o mnie: {plant.notes}'
    # self.ids.last_water.text = f'Nie piję od: {plant.last_water}'
    # self.ids.plant_photo.source = plant.picture
