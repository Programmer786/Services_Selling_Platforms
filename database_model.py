from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, datetime
from sqlalchemy import create_engine, Numeric
import os
from flask_migrate import Migrate

# Session configuration
app.permanent_session_lifetime = timedelta(hours=5)

# Database configuration for the online MySQL database on cPanel
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/services_selling_platforms_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# Set the upload folder
UPLOAD_FOLDER = 'static/uploaded_files'
# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# Configure the Flask app with the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the upload folder
ORIGINAL_UPLOAD_FOLDER = 'original_uploaded_files'
# Ensure the upload folder exists
if not os.path.exists(ORIGINAL_UPLOAD_FOLDER):
    os.makedirs(ORIGINAL_UPLOAD_FOLDER)
# Configure the Flask app with the upload folder
app.config['ORIGINAL_UPLOAD_FOLDER'] = ORIGINAL_UPLOAD_FOLDER

db = SQLAlchemy(app)
# Model Migrate into database tables Automatically
# First initialize only one time command (flask db init)
# apply those command Step:1(flask db migrate)Step:2 (flask db upgrade)
migrate = Migrate(app, db)


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=False, nullable=True)
    full_name = db.Column(db.String(50), unique=False, nullable=True)
    email = db.Column(db.String(50), unique=True, nullable=True)
    phone = db.Column(db.String(50), unique=True, nullable=True)
    cnic = db.Column(db.String(20), unique=True, nullable=True)
    gender = db.Column(db.String(20), unique=False, nullable=True)
    rol_name = db.Column(db.String(20), unique=False, nullable=True)
    delivery_status = db.Column(db.String(20), default='Available', nullable=True)  # e.g., 'Available', 'Pending', 'OutOfDelivery', 'NotAvailable'
    password = db.Column(db.String(256))
    photo = db.Column(db.String(256))  # e.g., db.Column(db.LargeBinary) for LONGBLOB).
    isActive = db.Column(db.Boolean, nullable=False)
    registrationDate = db.Column(db.Date, nullable=False, default=datetime.utcnow)


class ProductCategory(db.Model):
    __tablename__ = 'product_category'
    pc_id = db.Column(db.Integer, primary_key=True)
    pc_name = db.Column(db.String(50), unique=True, nullable=False)


class Products(db.Model):
    __tablename__ = 'products'
    p_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    pc_id = db.Column(db.Integer, db.ForeignKey('product_category.pc_id'), nullable=False)
    p_name = db.Column(db.String(100), nullable=False)
    p_description = db.Column(db.Text, nullable=True)
    p_price = db.Column(Numeric(precision=20, scale=1), nullable=False)
    p_image = db.Column(db.String(255), nullable=True)
    p_original_image = db.Column(db.String(255), nullable=True)
    p_isActive = db.Column(db.Boolean, nullable=False, default=True)
    p_registrationDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    p_stock = db.Column(db.Integer, default=1, nullable=True)
    # Define the relationships
    product_category = db.relationship('ProductCategory', backref=db.backref('products', lazy=True))
    users = db.relationship('Users', backref=db.backref('products', lazy=True))


class Customers(db.Model):
    __tablename__ = 'customers'
    cust_id = db.Column(db.Integer, primary_key=True)
    cust_user_name = db.Column(db.String(50), unique=True, nullable=False)
    cust_full_name = db.Column(db.String(50), unique=False, nullable=False)
    cust_phone = db.Column(db.String(50), unique=True, nullable=False)
    cust_gender = db.Column(db.String(20), unique=False, nullable=False)
    cust_rol_name = db.Column(db.String(20), unique=False, nullable=False)
    cust_drop_address = db.Column(db.String(255), nullable=True)
    cust_password = db.Column(db.String(256), nullable=False)
    cust_photo = db.Column(db.String(256))  # e.g., db.Column(db.LargeBinary) for LONGBLOB).
    cust_registrationDate = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    isActive = db.Column(db.Boolean, nullable=False)


class ProductDownloadVerification(db.Model):
    __tablename__ = 'product_download_verification'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.p_id'), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    transaction_no = db.Column(db.Boolean, default=False)
    select_payment_method = db.Column(db.String(100), nullable=True)
    receipt_file_path = db.Column(db.String(255), nullable=True)  # New column to store the receipt file path
    feedback_description = db.Column(db.String(255), nullable=True)
    feedback_stars = db.Column(db.Integer, nullable=True)
    feedback_submitted = db.Column(db.Boolean, default=False)
    delivery_boy_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    delivery_status = db.Column(db.String(50), nullable=True)  # e.g., 'OnTheWay', 'Deliver', 'Return'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Define the relationships
    products = db.relationship('Products', backref=db.backref('product_download_verification', lazy=True))
    customers = db.relationship('Customers', backref=db.backref('product_download_verification', lazy=True))
    users = db.relationship('Users', backref=db.backref('product_download_verification', lazy=True))


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.p_id'), nullable=False)
    price = db.Column(db.Numeric(precision=20, scale=1), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    isActive = db.Column(db.Boolean, nullable=False)


class MakeNotification(db.Model):
    __tablename__ = 'make_notification'
    n_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    notification_info = db.Column(db.String(50), nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    is_check_by_manager = db.Column(db.Boolean, default=False, nullable=True)
    is_check_by_employee = db.Column(db.Boolean, default=False, nullable=True)
    is_check_by_parent = db.Column(db.Boolean, default=False, nullable=True)
    is_check_by_delivery_boy = db.Column(db.Boolean, default=False, nullable=True)
    status = db.Column(db.String(50), default='Live', nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Define relationships if needed
    user = db.relationship('Users', backref=db.backref('make_notification', lazy=True))


class MakeReport(db.Model):
    __tablename__ = 'make_report'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    customer_id = db.Column(db.Integer, nullable=True)
    select_reason = db.Column(db.String(100), nullable=True)
    send_report_message = db.Column(db.String(255), nullable=True)
    is_check_by_admin = db.Column(db.Boolean, default=False, nullable=True)
    received_report_message = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Define relationships if needed
    users = db.relationship('Users', backref=db.backref('make_report', lazy=True))


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Chat(db.Model):
    __tablename__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # Define relationships
    sender = db.relationship('Customers', backref=db.backref('sent_messages', lazy=True))
    receiver = db.relationship('Users', backref=db.backref('received_messages', lazy=True))
