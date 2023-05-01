from datetime import datetime as dt
from resources.db import db

startDate = dt.now()

db().createTables()

endDate = dt.now()
print("Tabelas criadas em seconds " + str((endDate - startDate).total_seconds()))
