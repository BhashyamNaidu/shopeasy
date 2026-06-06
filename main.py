from fastapi import FastAPI, Depends
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
import os

load_dotenv()

DB_HOST     = os.getenv("DB_HOST")
DB_NAME     = os.getenv("DB_NAME")
DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT     = os.getenv("DB_PORT", "3306")

app = FastAPI(title="ShopEasy API", version="1.0.0")
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
Base = declarative_base()
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    price = Column(Float)
    description = Column(String(500))
Base.metadata.create_all(bind=engine)
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "ShopEasy API",
        "version": "2.0"
    }
class ProductCreate(BaseModel):
    name: str
    price: float
    description: str
@app.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return {
        "message": "Product created successfully",
        "product_id": db_product.id
    }
@app.get("/products")
def get_products(
    db: Session = Depends(get_db)
):
    products = db.query(Product).all()

    return products
@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not db_product:
        return {"message": "Product not found"}

    db_product.name = product.name
    db_product.price = product.price
    db_product.description = product.description

    db.commit()

    return {
        "message": "Product updated successfully"
    }
@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    db_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not db_product:
        return {"message": "Product not found"}

    db.delete(db_product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }
