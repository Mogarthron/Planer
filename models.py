from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

            # "Nazwa": "Prod_1",
            # "idop": 100,
            # "operacja_nazwa": "przegotowanie form",
            # "norma": "65min/10000szt",
            # "asortyment powiazany": "Asor_1",
            # "id_wejsciowe": 0,
            # "opuznienie startu nastepnej operacji": 0,
            # "przelicznik z poprzedniej operacji": null,
            # "id_wyjsciowe": 200,
            # "rodzaj_startu": null,
            # "start_przy_zapasie_z_porzedniej_operacji": null



class Technologia(Base):

    __tablename__ = "technologia"

    nazwa = Column("nazwa", String) #Nazawa technologii
    id_operacji = Column("id_operacji", Integer, primary_key=True)
    operacja_nazwa = Column("operacja_nazwa", String) #przypisanie do odpowiednich stanowisk
    norma = Column("norma", String)
    asortyment_powiazany = Column("asortyment_powiazany", String)
    id_wejsciowe = Column("id_wejsciowe", Integer)
    id_wyjsciowe = Column("id_wyjsciowe", Integer)
    rodzaj_startu = Column("rodzaj_startu", String, default="ES")
    przelicznik_z_poprzedniej_operacji = Column("przelicznik_z_poprzedniej_operacji",String, default="1")
    opuznienie_startu_nastepnej_operacji = Column("opuznienie startu nastepnej operacji", String)
    start_przy_zapasie_z_porzedniej_operacji = Column("start_przy_zapasie_z_porzedniej_operacji", String)


