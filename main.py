#Author:  Prof. Candido
#Purpose: SQL Basics for the class to learn

import sqlite3

dbConnection = sqlite3.connect("InClassPracticed.db")
dbCursor =     dbConnection.cursor()

# Create Tables...
dbConnection.execute("CREATE TABLE IF NOT EXISTS Dogs(dog_name text, dog_owner_id integer, dog_age real)")


sInsertStatement = "insert into Dog_Owners(dog_owner_id, dog_owner_name) values(1,'Brian Candido')"
print(sInsertStatement)
dbConnection.execute(sInsertStatement)
dbConnection.commit()


sInsertStatement = "insert into Dog_Owners(dog_owner_id, dog_owner_name) values(2,'Daniel Candido')"
print(sInsertStatement)
dbConnection.execute(sInsertStatement)

sInsertStatement = "insert into Dog_Owners(dog_owner_id, dog_owner_name) values(3,'Joseph Candido')"
print(sInsertStatement)
dbConnection.execute(sInsertStatement)

dbConnection.commit()


sName = 'Moose Kuaui Comet'
iOwnerID = 1
fAge =  14.25
sSQLStatememt = f"INSERT into Dogs(dog_name, dog_owner_id, dog_age) values('{sName}',{iOwnerID},{fAge})"

print(sSQLStatememt)
dbConnection.execute(sSQLStatememt)
dbConnection.commit()


sName = 'Bentley Louis'
iOwnerID = 1
fAge =  2.5
sSQLStatememt = f"INSERT into Dogs(dog_name, dog_owner_id, dog_age) values('{sName}',{iOwnerID},{fAge})"

print(sSQLStatememt)
dbConnection.execute(sSQLStatememt)


# Add Values:
sName = 'Sora'
iOwnerID = 2
fAge =  2.85
sSQLStatememt = f"INSERT into Dogs(dog_name, dog_owner_id, dog_age) values('{sName}',{iOwnerID},{fAge})"

print(sSQLStatememt)
dbConnection.execute(sSQLStatememt)
dbConnection.commit()


# Add Values:
sName = 'Bingo'
iOwnerID = 3
fAge =  2.85
sSQLStatememt = f"INSERT into Dogs(dog_name, dog_owner_id, dog_age) values('{sName}',{iOwnerID},{fAge})"

print(sSQLStatememt)
dbConnection.execute(sSQLStatememt)
dbConnection.commit()

# Show Output....

sSQLSelect = "SELECT dog_owner_id, dog_owner_name FROM Dog_Owners ORDER BY dog_owner_id"
print(sSQLSelect)
dbCursor.execute(sSQLSelect)

        
print(f"{'Owner ID':<20} {'Owner Name':<25}")
for tupSQLRows in dbCursor.fetchall():
  print(f"{tupSQLRows[0]:<20} {tupSQLRows[1]:<25}")


# Output the Dog Data...
sSQLSelect = "SELECT * FROM Dogs ORDER BY dog_name"
print(sSQLSelect)
dbCursor.execute(sSQLSelect)

        
print(f"{'Dog':<20} {'Age':>15}")
for tupSQLRows in dbCursor.fetchall():
  print(f"{tupSQLRows[0]:<20} {tupSQLRows[2]:>15,.2f}")


# Output the Dog and Owner Data...
#Dog_Owners(dog_owner_id, dog_owner_name)
sSQLSelect = "SELECT Dog_Owners.dog_owner_name, Dogs.dog_name, Dogs.dog_age FROM Dogs, Dog_Owners WHERE Dogs.dog_owner_id =  Dog_Owners.dog_owner_id ORDER BY dog_owner_name"
print(sSQLSelect)
dbCursor.execute(sSQLSelect)

        
print(f"{'Dog Owner':<30} {'Dog Name':<30} {'Age':>15}")
for tupSQLRows in dbCursor.fetchall():
  print(f"{tupSQLRows[0]:<30} {tupSQLRows[1]:<30} {tupSQLRows[2]:>15,.2f}")



