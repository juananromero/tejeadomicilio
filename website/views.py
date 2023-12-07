from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Product, tipos, subtipos

views = Blueprint('views', __name__)

@views.route("/")
def home():
    products=[]
    length=[]
    for t in tipos:
        products.extend(Product.query.filter_by(tipo=t).order_by(Product.subtipo, Product.nombre).all())
        length.append(len(products))
    length.insert(0,0)
    return render_template('home.html', products=products, tipos=tipos, user=current_user, length=length)

@views.route("/api/products", methods=('GET', 'POST'))
def list_products():
    products=Product.query.all()
    return jsonify(products)

@views.route("/addproduct", methods=('GET', 'POST'))
@login_required
def add_product():
    if request.method == 'POST':
        nombre = request.form['nombre']
        proveedor = request.form['proveedor']
        descripcion = request.form['descripcion']
        tipo = request.form['tipo']
        subtipo = request.form['subtipo']
        subsubtipo = request.form['subsubtipo']
        observaciones = request.form['observaciones']
        precio = request.form['precio']
        precios = request.form['precios']
        activo= request.form['activo']
        p=Product(
            nombre=nombre,
            proveedor=proveedor,
            descripcion=descripcion,
            tipo=tipo,
            subtipo=subtipo,
            subsubtipo=subsubtipo,
            precio=precio,
            precios=precios,
            observaciones=observaciones,
            activo= True if activo=="Si" else False,
            fecha_alta=datetime.datetime.now(),
            fecha_modificacion=datetime.datetime.now()
            )
        db.session.add(p)
        db.session.commit()
        flash("Producto añadido con id =" + str(p.id))
        return render_template('addproduct.html')

    return render_template('addproduct.html', tipos=tipos, subtipos=subtipos, user=current_user)

@views.route("/editproduct/<id>", methods=('GET', 'POST'))
def edit_product(id):

    if request.method == 'GET':
        product=Product.query.get(id)
        return render_template('editproduct.html', product=product, tipos=tipos, subtipos=subtipos)
    else: #POST
        product=Product.query.get(id)
        product.nombre=request.form['nombre']
        product.proveedor=request.form['proveedor']
        product.descripcion=request.form['descripcion']
        product.tipo=request.form['tipo']
        product.subtipo=request.form['subtipo']
        product.subsubtipo=request.form['subsubtipo']
        product.precio=request.form['precio']
        product.precios=request.form['precios']
        product.observaciones=request.form['observaciones']
        print("request.form['activo']", request.form['activo'])
        product.activo= True if request.form['activo']=="Si" else False
        product.fecha_modificacion=datetime.datetime.now()
        try:
            db.session.commit()
            flash("Producto actualizado con id =" + str(product.id))
            return render_template('editproduct.html', product=product, tipos=tipos, subtipos=subtipos)
        except:
            return "Problema actualizando/Editando un producto " + product.id
