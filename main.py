from website import create_app,db
import click
import os
import csv
import datetime
from website.models import Product

app = create_app()

# Ejecutará la app y el webserver solo si
# ejecutamos este programa, no si se hace import
if __name__ == '__main__':
    app.run(debug=True)


@app.cli.command('dbdelete')
def dbdelete():
    """Borra el fichero de la base de datos sqlite del
    dir 'instance'."""
    DATABASE=os.path.join(app.instance_path, 'databaseteje.sqlite')
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        click.echo('DELETED:'+ app.instance_path+'databaseteje.sqlite') 
    else:
        click.echo("No Existe el fichero de la bdd.") 

@app.cli.command("dbreadcsv")
def dbreadcsv():
    """ Leo de catalogo-teje1.csv e inserto en la bdd
    """
    with open('catalogo-teje1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='|')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                if row[1]=="":#esta fila es una nueva categoría
                    cat=row[0]
                    continue
                print(f'\t {cat} - {row[0]} - {row[1]} - {row[2]} - {row[3]} - {row[4]}')
                p=Product(
                    nombre=row[0],
                    proveedor=row[1],
                    descripcion="",
                    tipo=cat,
                    subtipo="",
                    subsubtipo="",
                    precio=row[2],
                    precios=row[3],
                    observaciones=row[4],
                    activo=True,
                    fecha_alta=datetime.datetime.now(),
                    fecha_modificacion=datetime.datetime.now())
                db.session.add(p)
                db.session.commit()

@app.cli.command("dbaddproduct1")
def dbaddproduct1():
    """ Inserto un registro directamente a la bdd
    """
    p=Product(
        id=1,
        nombre="Juan",
        proveedor="P1",
        descripcion="D1",
        tipo="T1",
        subtipo="ST1",
        subsubtipo="SST1",
        precio="2.3",
        precios="2.2",
        observaciones="O1",
        activo=True,
        fecha_alta=datetime.datetime.now(),
        fecha_modificacion=datetime.datetime.now()
        )
    db.session.add(p)
    db.session.commit()