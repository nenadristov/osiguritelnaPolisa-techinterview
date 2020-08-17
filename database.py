import sqlite3
conn = sqlite3.connect('osiguruvanje.db')
c=conn.cursor()

#kreiranje tabeli
def kreiranje_tabeli():
    c.execute("""CREATE TABLE polisa 
    (polisa_broj VARCHAR(12) UNIQUE PRIMARY KEY,
    polisa_pod_broj VARCHAR(2) UNIQUE,
    sif_filijala VARCHAR(3),
    agent_id VARCHAR(10),
    osigurenik VARCAHR(10),
    dogovarac VARCHAR(10),
    klasa VARCHAR(2),
    tarifa VARCHAR(2),
    skadenca_datum_od timestamp,
    skadenca_datum_do timestamp,
    datum_izgotvuvanje timestamp,
    datum_potpis timestamp,
    premija_denari FLOAT)
    """)

    c.execute("""CREATE TABLE agent 
    (agent_id VARCHAR(10) UNIQUE PRIMARY KEY,
    sif_filijala VARCHAR(3),
    ime VARCHAR(30),
    prezime VARCHAR(30),
    edb VARCHAR(13),
    adresa_ulica VARCHAR(60),
    adresa_broj VARCHAR(60),
    datum_pocetok timestamp,
    datum_prestanok timestamp)
    """)

try:
    kreiranje_tabeli()
    conn.commit()
    print("Tabelite se uspesno kreirani")
except sqlite3.OperationalError :
    print("Ne se kreiraat tabeli bidejki postojat, programata prodoluzva \n\n")

#Queries

#quering agent_id
c.execute('SELECT agent_id from agent where edb="0000000000000"')
id_agent=c.fetchone()
#print(id_agent[0])

#quering polisi 
c.execute("SELECT * FROM polisa WHERE agent_id=?", (id_agent[0],))
polisi=c.fetchall()

#for loop za query polisi
for i in polisi:
    print("""
    Polisa_broj: {}
    Polisa_pod_broj: {}
    sif_filijala: {}
    agent_id: {}
    klasa: {}
    tarifa: {}
    """.format(i[0], i[1], i[2], i[3], i[6], i[7]))








