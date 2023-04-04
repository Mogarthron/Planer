import json
from sqlalchemy.orm import sessionmaker
from models import *

with open("technologia.json", "r") as f:
    tehnologia = json.loads(f.read())["tech"]

print(tehnologia)

# engine = create_engine("sqlite:///planer.db", echo=True)
# Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# prod1 = "Szklanka Caffe Latte 200ml kpl 6 szt"
# asor1 = "xxx"
# # op1 = Technologia("Szklanka Caffe Latte 200ml kpl 6 szt",100, "przygotowanie form",
# #                   "65min/10000", "Forma Latte 200", 0, 
# #                   200)

# # session.add(op1)
# session.query(Technologia)

# session.commit()