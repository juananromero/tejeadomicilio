from . import db
from dataclasses import dataclass
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from flask_login import UserMixin

# Decorator @dataclass para añadir jsonify() a la clase.
@dataclass
class Product(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    proveedor: Mapped[str] = mapped_column(String(100), nullable=False)
    descripcion: Mapped[str] = mapped_column(String(100))
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)
    subtipo: Mapped[str] = mapped_column(String(50))
    subsubtipo: Mapped[str] = mapped_column(String(50))
    precio: Mapped[str] = mapped_column(String(10), nullable=False)
    precios: Mapped[str] = mapped_column(String(10))
    observaciones: Mapped[str] = mapped_column(String(100))
    activo: Mapped[bool] = mapped_column(Boolean(100), default=True, nullable=False)
    fecha_alta: Mapped[DateTime] = mapped_column(DateTime)
    fecha_modificacion: Mapped[DateTime] = mapped_column(DateTime)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    nombre = db.Column(db.String(100))

tipos=[
    "ALIMENTACIÓN",
    "ACCESORIOS/COMPLEMENTOS",
    "BEBIDAS",
    "COSMÉTICA",
    "DECORACIÓN",    
    "DROGUERÍA/LIMPIEZA",
    "ENTRETENIMIENTO/JUEGOS",
    "LIBROS/PAPELERÍA",
    "MÚSICA",
    "TEXTIL"
    ]
subtipos=[
    "ACEITES Y VINAGRES",
    "ALIMENTACIÓN INFANTIL",
    "AZÚCAR, MIEL Y DERIVADOS",
    "BEBIDAS CON ALCOHOL",
    "BEBIDAS NO ALCOHÓLICAS",
    "CAFÉ Y TÉ",
    "CHOCOLATES Y CACAOS",
    "CONDIMENTOS",
    "CONSERVAS Y PATÉS",
    "FRESCOS (HUEVOS LÁCTEOS OTROS)",
    "GALLETAS, CEREALES Y OTROS DESAYUNO",
    "HARINA, PAN, BOLLERÍA Y DERIVADOS",
    "LEGUMBRES, ARROZ Y OTROS",
    "PASTA",
    "SNACKS, FRUTOS SECOS, SEMILLAS Y DERIVADOS"
    ]