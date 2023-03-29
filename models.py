from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

    nazwa = Column("nazwa", String)
    id_operacji = Column("id_operacji", Integer, primary_key=True)
    operacja_nazwa = Column("operacja_nazwa", String)
    norma = Column("norma", String)
    asortyment_powiazany = Column("asortyment_powiazany", String)
    id_wejsciowe = Column("id_wejsciowe", Integer)
    id_wyjsciowe = Column("id_wyjsciowe", Integer)
    rodzaj_startu = Column("rodzaj_startu", String)
    przelicznik_z_poprzedniej_operacji = Column("przelicznik_z_poprzedniej_operacji",String)
    opuznienie_startu_nastepnej_operacji = Column("opuznienie startu nastepnej operacji", String)
    start_przy_zapasie_z_porzedniej_operacji = Column("start_przy_zapasie_z_porzedniej_operacji", String)

    def __init__(self, nazwa, id_operacji, operacja_nazwa, 
                 norma, asortyment_powiazany, id_wejsciowe, id_wyjsciowe,
                 rodzaj_startu="ES", przelicznik_z_poprzedniej_operacji="1",
                 opuznienie_startu_nastepnej_operacji=None, start_przy_zapasie_z_porzedniej_operacji=None
                 ) -> None:
        
        self.nazwa = nazwa
        self.id_operacji = id_operacji
        self.operacja_nazwa = operacja_nazwa
        self.norma = norma
        self.asortyment_powiazany = asortyment_powiazany
        self.id_wejsciowe = id_wejsciowe
        self.id_wyjsciowe = id_wyjsciowe
        self.rodzaj_startu = rodzaj_startu
        self.przelicznik_z_poprzedniej_operacji = przelicznik_z_poprzedniej_operacji
        self.opuznienie_startu_nastepnej_operacji = opuznienie_startu_nastepnej_operacji
        self.start_przy_zapasie_z_porzedniej_operacji = start_przy_zapasie_z_porzedniej_operacji

    def __repr__(self) -> str:
        return f"({self.id_operacji}), {self.operacja_nazwa}, {self.id_wejsciowe}, {self.id_wyjsciowe}"
    


engine = create_engine("sqlite:///planer.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

op1 = Technologia("Szklanka Caffe Latte 200ml kpl 6 szt",100, "przygotowanie form",
                  "65min/10000", "Forma Latte 200", 0, 
                  200)

session.add(op1)
session.commit()