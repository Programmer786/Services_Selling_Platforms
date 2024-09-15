import PIL
from PIL import Image
from sqlalchemy.orm import joinedload
from app import app
from sqlalchemy.exc import IntegrityError
from database_model import *
from flask import render_template, flash, session, request, redirect
import os
import random


@app.route('/add_product', methods=['POST', 'GET'])
def add_product():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Fetch notification data from the database
            notifications = MakeNotification.query.filter_by(status='Live').all()
            notifications_count = MakeNotification.query.filter_by(status='Live').count()
            # this is for get a province
            all_product_category_name = ProductCategory.query.all()

            all_products_data_retrieve = (
                Products.query
                .join(ProductCategory)
                .options(joinedload(Products.product_category))  # Eager load the associated project
                .join(Users)
                .options(joinedload(Products.users))  # Eager load the associated project
                .all()
            )

            if request.method == 'POST':
                get_p_name = request.form['p_name']
                get_p_description = request.form['p_description']
                get_p_price = request.form['p_price']
                get_category_id = request.form['get_category_id']
                # get_uploaded_p_image = request.files['p_image']  # Assuming the image is a file upload, handle it accordingly
                get_uploaded_p_original_image = request.files['p_original_image']

                session_UserId = session['UserId']
                # Check if required fields are not empty
                if not (get_p_name and get_p_price and get_category_id):
                    flash("Error. Please fill all the required fields", "danger")
                    return redirect('/add_product')

                try:
                    new_entry_save_by_products = Products(
                        p_name=get_p_name,
                        p_description=get_p_description,
                        p_price=get_p_price,
                        pc_id=get_category_id,
                        user_id=session_UserId
                    )

                    if get_uploaded_p_original_image:
                        # Get the original file extension
                        _, file_extension = os.path.splitext(get_uploaded_p_original_image.filename)
                        # Generate a random 4-digit number
                        random_number = random.randint(1000000, 9999999)
                        # UserId Get from Session
                        get_user_id = session['UserId']
                        # Combine random_number, employee ID, and file extension to create a custom filename
                        custom_filename = f"{random_number}_{get_user_id}{file_extension}"
                        # Save the file and update the database record with the file path
                        file_path_system = os.path.join(app.config['ORIGINAL_UPLOAD_FOLDER'], custom_filename)  # Set your upload folder path
                        file_full_name = os.path.join("", custom_filename)  # Set your No path for database column
                        get_uploaded_p_original_image.save(file_path_system)
                        new_entry_save_by_products.p_original_image = file_full_name

                    db.session.add(new_entry_save_by_products)
                    db.session.commit()

                    if get_uploaded_p_original_image:
                        try:
                            # Retrieve the latest product data
                            one_products_data_retrieve = (
                                Products.query
                                .join(ProductCategory)
                                .options(joinedload(Products.product_category))  # Eager load the associated project
                                .join(Users)
                                .options(joinedload(Products.users))  # Eager load the associated project
                                .order_by(Products.p_id.desc())  # Assuming 'p_id' is a unique identifier column, change it accordingly
                                .first()
                            )

                            # Construct the file path of the original image
                            file_path_system = os.path.join(app.config['ORIGINAL_UPLOAD_FOLDER'], one_products_data_retrieve.p_original_image)

                            # Open the uploaded image using Pillow
                            image = Image.open(file_path_system)

                            # Load the watermark image
                            watermark_path = 'static/img/WATERMARK.png'  # Replace 'path/to/watermark.png' with the actual path to your watermark image
                            watermark = Image.open(watermark_path)

                            # Resize the watermark image
                            watermark_width, watermark_height = watermark.size
                            image_width, image_height = image.size
                            # Adjust the scale of the watermark according to the size of the uploaded image
                            scale = min(image_width, image_height) / max(watermark_width, watermark_height)
                            new_width = int(watermark_width * scale)
                            new_height = int(watermark_height * scale)
                            watermark = watermark.resize((new_width, new_height))

                            # Calculate the position to place the watermark (e.g., bottom right corner)
                            position = (image_width - new_width, image_height - new_height)

                            # Paste the watermark onto the image
                            image.paste(watermark, position, watermark)

                            # Save the modified image
                            modified_image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"modified_{one_products_data_retrieve.p_original_image}")
                            image.save(modified_image_path)

                            # Update the database record with the modified image path
                            one_products_data_retrieve.p_image = f"modified_{one_products_data_retrieve.p_original_image}"
                            db.session.commit()

                        except PIL.UnidentifiedImageError:
                            # Handle the case when Pillow cannot identify the image file
                            flash("Error: Unable to identify the uploaded image file", "danger")
                            return redirect('/add_product')  # Redirect or display an error message as needed
                        except IOError:
                            # Handle other IO errors (e.g., file not found, permission issues)
                            flash("Error: Unable to open the uploaded image", "danger")
                            return redirect('/add_product')  # Redirect or display an error message as needed

                    flash(f"Record Successfully Saved", "success")
                    return redirect('/add_product')
                except IntegrityError:
                    db.session.rollback()
                    flash("Error. Duplicate data detected. Please do not proceed and try again.", "danger")
                    return redirect('/add_product')  # Add a return statement here
            else:
                return render_template('Administrator/add_product.html', all_product_category_name=all_product_category_name,
                                       all_products_data_retrieve=all_products_data_retrieve,
                                       notifications=notifications,
                                       notifications_count=notifications_count)
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/delete_product/<int:Product_Id>')
def delete_product(Product_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # First delete the file
            product = Products.query.get_or_404(Product_Id)
            file_path1 = None  # Initialize file_path1 with a default value
            if product.p_image is not None:
                file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], product.p_image)  # Construct the full path to the file
            # Delete the file from the directory if it exists
            if file_path1 is not None and os.path.exists(file_path1):
                os.remove(file_path1)

            # Initialize file_path2 with a default value
            file_path2 = None
            if product.p_original_image is not None:
                file_path2 = os.path.join(app.config['ORIGINAL_UPLOAD_FOLDER'], product.p_original_image)
                # Delete the file from the directory if it exists
            if file_path2 is not None and os.path.exists(file_path2):
                os.remove(file_path2)

            # get specific Product_Id from clerk Table and then check the date with Product_Id related
            select_one_products = Products.query.filter_by(p_id=Product_Id).first()
            db.session.delete(select_one_products)
            db.session.commit()
            flash("Record Successfully Deleted", "success")
            return redirect('/add_product')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: Product Cannot be deleted, because product already purchase", "danger")
            return redirect('/add_product')
    else:
        return render_template('Administrator/login.html')


@app.route('/update_product/<int:Product_Id>', methods=['GET', 'POST'])
def update_product(Product_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # this is for table data retrieve of the Specific product
            one_product = Products.query.get_or_404(Product_Id)

            if request.method == 'POST':
                get_p_name = request.form['p_name']
                get_p_description = request.form['p_description']
                get_p_price = request.form['p_price']
                get_category_id = request.form['get_category_id']

                # Check if required fields are not empty
                if not (get_p_name and get_p_description and get_p_price and get_category_id):
                    flash("Error. Please fill all the required fields", "danger")
                    return redirect('/add_product')

                try:
                    one_product.p_name = get_p_name
                    one_product.p_description = get_p_description
                    one_product.p_price = get_p_price
                    one_product.pc_id = get_category_id

                    db.session.commit()
                    flash("Record Successfully Updated", "success")
                    return redirect('/add_product')
                except IntegrityError:
                    db.session.rollback()
                    flash("Error. Duplicate data detected. Please do not proceed and try again.", "danger")
                    return redirect('/add_product')
            else:
                return redirect('/add_product')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/update_product_image/<int:Product_Id>', methods=['GET', 'POST'])
def update_product_image(Product_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            if request.method == 'POST':
                # First delete the file
                product = Products.query.get_or_404(Product_Id)

                file_path1 = None  # Initialize file_path1 with a default value
                if product.p_image is not None:
                    file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], product.p_image)  # Construct the full path to the file
                # Delete the file from the directory if it exists
                if file_path1 is not None and os.path.exists(file_path1):
                    os.remove(file_path1)
                # Initialize file_path2 with a default value
                file_path2 = None
                if product.p_original_image is not None:
                    file_path2 = os.path.join(app.config['ORIGINAL_UPLOAD_FOLDER'], product.p_original_image)
                    # Delete the file from the directory if it exists
                if file_path2 is not None and os.path.exists(file_path2):
                    os.remove(file_path2)

                # Get Original New Image Path
                get_uploaded_p_original_image = request.files['p_original_image']

                # Initialize file_path2 with a default value
                file_path2 = None
                if product.p_original_image is not None:
                    file_path2 = os.path.join(app.config['ORIGINAL_UPLOAD_FOLDER'], product.p_original_image)
                    # Delete the file from the directory if it exists
                if file_path2 is not None and os.path.exists(file_path2):
                    os.remove(file_path2)

                if get_uploaded_p_original_image:
                    # Get the original file extension
                    _, file_extension = os.path.splitext(get_uploaded_p_original_image.filename)
                    # Generate a random 4-digit number
                    random_number = random.randint(1000000, 9999999)
                    # UserId Get from Session
                    get_user_id = session['UserId']
                    # Combine random_number, employee ID, and file extension to create a custom filename
                    custom_filename = f"{random_number}_{get_user_id}{file_extension}"
                    # Save the file and update the database record with the file path
                    file_path_system = os.path.join(app.config['ORIGINAL_UPLOAD_FOLDER'], custom_filename)  # Set your upload folder path
                    file_full_name = os.path.join("", custom_filename)  # Set your No path for database column
                    get_uploaded_p_original_image.save(file_path_system)
                    product.p_original_image = file_full_name

                    db.session.commit()

                if get_uploaded_p_original_image:
                    try:
                        # Retrieve the latest product data
                        one_products_data_retrieve = Products.query.filter_by(p_id=Product_Id).first()
                        # Construct the file path of the original image
                        file_path_system = os.path.join(app.config['ORIGINAL_UPLOAD_FOLDER'], one_products_data_retrieve.p_original_image)

                        # Open the uploaded image using Pillow
                        image = Image.open(file_path_system)

                        # Load the watermark image
                        watermark_path = 'static/img/WATERMARK.png'  # Replace 'path/to/watermark.png' with the actual path to your watermark image
                        watermark = Image.open(watermark_path)

                        # Resize the watermark image
                        watermark_width, watermark_height = watermark.size
                        image_width, image_height = image.size
                        # Adjust the scale of the watermark according to the size of the uploaded image
                        scale = min(image_width, image_height) / max(watermark_width, watermark_height)
                        new_width = int(watermark_width * scale)
                        new_height = int(watermark_height * scale)
                        watermark = watermark.resize((new_width, new_height))

                        # Calculate the position to place the watermark (e.g., bottom right corner)
                        position = (image_width - new_width, image_height - new_height)

                        # Paste the watermark onto the image
                        image.paste(watermark, position, watermark)

                        # Save the modified image
                        modified_image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"modified_{one_products_data_retrieve.p_original_image}")
                        image.save(modified_image_path)

                        # Update the database record with the modified image path
                        one_products_data_retrieve.p_image = f"modified_{one_products_data_retrieve.p_original_image}"
                        db.session.commit()

                    except PIL.UnidentifiedImageError:
                        # Handle the case when Pillow cannot identify the image file
                        flash("Error: Unable to identify the uploaded image file", "danger")
                        return redirect('/add_product')  # Redirect or display an error message as needed
                    except IOError:
                        # Handle other IO errors (e.g., file not found, permission issues)
                        flash("Error: Unable to open the uploaded image", "danger")
                        return redirect('/add_product')  # Redirect or display an error message as needed

                flash("The Product Images Successfully Updated", "success")
                return redirect('/add_product')
            else:
                return redirect('/add_product')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/add_product')
    else:
        return render_template('Administrator/login.html')


@app.route('/update_stock', methods=['POST', 'GET'])
def update_stock():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Fetch notification data from the database
            notifications = MakeNotification.query.filter_by(status='Live').all()
            notifications_count = MakeNotification.query.filter_by(status='Live').count()
            # this is for get a province
            all_product_category_name = ProductCategory.query.all()

            all_products_data_retrieve = (
                Products.query
                .join(ProductCategory)
                .options(joinedload(Products.product_category))  # Eager load the associated project
                .all()
            )

            if request.method == 'POST':
                get_p_name = request.form['p_name']
                get_p_description = request.form['p_description']
                get_p_price = request.form['p_price']
                get_category_id = request.form['get_category_id']
                get_uploaded_p_image = request.files['p_image']  # Assuming the image is a file upload, handle it accordingly

                # Check if required fields are not empty
                if not (get_p_name and get_p_price and get_category_id):
                    flash("Error. Please fill all the required fields", "danger")
                    return redirect('/update_stock')

                try:
                    new_entry_save_by_products = Products(
                        p_name=get_p_name,
                        p_description=get_p_description,
                        p_price=get_p_price,
                        pc_id=get_category_id
                    )

                    if get_uploaded_p_image:
                        # Get the original file extension
                        _, file_extension = os.path.splitext(get_uploaded_p_image.filename)
                        # Generate a random 4-digit number
                        random_number = random.randint(1000000, 9999999)
                        # UserId Get from Session
                        get_user_id = session['UserId']
                        # Combine random_number, employee ID, and file extension to create a custom filename
                        custom_filename = f"{random_number}_{get_user_id}{file_extension}"
                        # Save the file and update the database record with the file path
                        file_path_system = os.path.join(app.config['UPLOAD_FOLDER'], custom_filename)  # Set your upload folder path
                        file_full_name = os.path.join("", custom_filename)  # Set your No path for database column
                        get_uploaded_p_image.save(file_path_system)
                        new_entry_save_by_products.p_image = file_full_name

                    db.session.add(new_entry_save_by_products)
                    db.session.commit()
                    flash(f"Record Successfully Saved", "success")
                    return redirect('/update_stock')
                except IntegrityError:
                    db.session.rollback()
                    flash("Error. Duplicate data detected. Please do not proceed and try again.", "danger")
                    return redirect('/update_stock')  # Add a return statement here
            else:
                return render_template('Administrator/update_stock.html', all_product_category_name=all_product_category_name,
                                       all_products_data_retrieve=all_products_data_retrieve,
                                       notifications=notifications,
                                       notifications_count=notifications_count)
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/update_stock')  # Add a return statement here
    else:
        return render_template('Administrator/login.html')


@app.route('/update_product_stock_active/<int:Product_Id>', methods=['GET', 'POST'])
def update_product_stock_active(Product_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            one_product = Products.query.get_or_404(Product_Id)
            if request.method == 'POST':
                get_p_stock = request.form.get('p_stock')

                # Check if p_isActive key exists in form data and if you get_p_stock is not equal to 0
                if 'p_isActive' in request.form and get_p_stock != '0':
                    # Checkbox is checked and stock is not 0
                    get_p_is_active = True
                    stock = get_p_stock
                else:
                    # Checkbox is unchecked or stock is 0
                    get_p_is_active = False
                    stock = 0

                # Check if required fields are not empty
                if not get_p_stock:
                    flash("Error. Please fill all the required fields", "danger")
                    return redirect('/update_stock')

                one_product.p_stock = stock
                one_product.p_isActive = get_p_is_active

                db.session.commit()
                flash(f"{one_product.p_name} Record Successfully Updated", "success")
                return redirect('/update_stock')
            else:
                return redirect('/update_stock')
        except Exception as e:
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/take_order', methods=['POST', 'GET'])
def take_order():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        # Fetch notification data from the database
        notifications = MakeNotification.query.filter_by(status='Live').all()
        notifications_count = MakeNotification.query.filter_by(status='Live').count()

        # UserId Get from Session rol_name
        get_user_id = session['UserId']
        get_rol_name = session['rol_name']
        if get_rol_name == 'Administrator':
            all_order_for_download_data_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .options(joinedload(ProductDownloadVerification.products))  # Eager load the associated project
                .all()
            )
        else:
            all_order_for_download_data_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .filter(Products.user_id == get_user_id)  # Filter based on Products table's attribute
                .options(joinedload(ProductDownloadVerification.products))  # Eager load the associated project
                .all()
            )
        return render_template('Administrator/take_order.html',
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               notifications=notifications,
                               notifications_count=notifications_count)
    else:
        return render_template('Administrator/login.html')


@app.route('/order_deliver', methods=['POST', 'GET'])
def order_deliver():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        # Fetch notification data from the database
        get_delivery_boy = Users.query.filter_by(rol_name='DeliveryBoy').all()
        notifications = MakeNotification.query.filter_by(status='Live').all()
        notifications_count = MakeNotification.query.filter_by(status='Live').count()

        # UserId Get from Session rol_name
        get_user_id = session['UserId']
        get_rol_name = session['rol_name']
        if get_rol_name == 'Administrator':
            all_order_for_download_data_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .filter(ProductDownloadVerification.is_verified == 1)
                .options(joinedload(ProductDownloadVerification.products))  # Eager load the associated project
                .all()
            )
        else:
            all_order_for_download_data_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .filter(Products.user_id == get_user_id, ProductDownloadVerification.is_verified == 1)  # Filter based on Products table's attribute
                .options(joinedload(ProductDownloadVerification.products))  # Eager load the associated project
                .all()
            )
        return render_template('Administrator/order_deliver.html',
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               notifications=notifications,
                               notifications_count=notifications_count,
                               get_delivery_boy=get_delivery_boy)
    else:
        return render_template('Administrator/login.html')


@app.route('/delivery_on_the_way/<int:OrderId>', methods=['POST', 'GET'])
def delivery_on_the_way(OrderId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            get_select_delivery_boy = request.form.get('select_delivery_boy')
            sel_one_delivery = ProductDownloadVerification.query.get_or_404(OrderId)
            sel_one_delivery.delivery_boy_id = get_select_delivery_boy
            sel_one_delivery.delivery_status = 'OnTheWay'
            db.session.commit()
            flash("Record Successfully Received", "success")
            return redirect('/order_deliver')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Error: {str(e)}" "", "danger")
            return redirect('/order_deliver')
    else:
        return render_template('Administrator/login.html')


@app.route('/view_feedback', methods=['POST', 'GET'])
def view_feedback():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        # Fetch notification data from the database
        notifications = MakeNotification.query.filter_by(status='Live').all()
        notifications_count = MakeNotification.query.filter_by(status='Live').count()

        # UserId Get from Session rol_name
        get_user_id = session['UserId']
        get_rol_name = session['rol_name']
        if get_rol_name == 'Administrator':
            all_order_for_download_data_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .filter(ProductDownloadVerification.feedback_submitted == 1)
                .options(joinedload(ProductDownloadVerification.products))  # Eager load the associated project
                .all()
            )
        else:
            all_order_for_download_data_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .filter(Products.user_id == get_user_id, ProductDownloadVerification.feedback_submitted == 1)  # Filter based on Products table's attribute
                .options(joinedload(ProductDownloadVerification.products))  # Eager load the associated project
                .all()
            )
        return render_template('Administrator/view_feedback.html',
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               notifications=notifications,
                               notifications_count=notifications_count)
    else:
        return render_template('Administrator/login.html')


@app.route('/view_report', methods=['POST', 'GET'])
def view_report():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        # Fetch notification data from the database
        notifications = MakeNotification.query.filter_by(status='Live').all()
        notifications_count = MakeNotification.query.filter_by(status='Live').count()

        all_report_data_retrieve = MakeReport.query.all()

        return render_template('Administrator/view_report.html',
                               all_report_data_retrieve=all_report_data_retrieve,
                               notifications=notifications,
                               notifications_count=notifications_count)
    else:
        return render_template('Administrator/login.html')


@app.route('/reply_report/<int:Report_Id>', methods=['POST'])
def reply_report(Report_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Retrieve the form data
            received_report_message = request.form['received_report_message']

            # Check if the form data is valid
            if received_report_message:
                # Retrieve the MakeReport from the database
                get_make_report = MakeReport.query.get(Report_Id)

                # Update the MakeReport attributes
                get_make_report.received_report_message = received_report_message
                get_make_report.is_check_by_admin = True

                # Commit the changes to the database
                db.session.commit()

                flash("Report Reply submitted successfully.", "success")
            else:
                flash("Error! Please fill out all fields.", "danger")

            return redirect('/view_report')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/view_report')
    else:
        return render_template('Administrator/login.html')


@app.route('/sale_report', methods=['POST', 'GET'])
def sale_report():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        notifications = MakeNotification.query.filter_by(status='Live').all()
        notifications_count = MakeNotification.query.filter_by(status='Live').count()

        get_user_id = session['UserId']
        get_rol_name = session['rol_name']

        from_date = request.form.get('from_date')
        to_date = request.form.get('to_date')

        # Convert form date inputs to datetime objects
        from_date = datetime.strptime(from_date, '%Y-%m-%d') if from_date else None
        to_date = datetime.strptime(to_date, '%Y-%m-%d') if to_date else None

        query = ProductDownloadVerification.query.join(Products)

        # Filter by date range if provided
        if from_date and to_date:
            query = query.filter(ProductDownloadVerification.created_at.between(from_date, to_date))

        if get_rol_name != 'Administrator':
            query = query.filter(Products.user_id == get_user_id)

        query = query.filter(ProductDownloadVerification.is_verified == 1)

        all_order_for_download_data_retrieve = query.all()

        total_sale = sum(product.products.p_price for product in all_order_for_download_data_retrieve)

        return render_template('Administrator/sale_report.html',
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               notifications=notifications,
                               notifications_count=notifications_count,
                               total_sale=total_sale)
    else:
        return render_template('Administrator/login.html')


@app.route('/verify_payment', methods=['POST', 'GET'])
def verify_payment():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        # Fetch notification data from the database
        notifications = MakeNotification.query.filter_by(status='Live').all()
        notifications_count = MakeNotification.query.filter_by(status='Live').count()

        all_order_for_download_data_retrieve = (
            ProductDownloadVerification.query
            .join(Products)
            .options(joinedload(ProductDownloadVerification.products))  # Eager load the associated project
            .all()
        )
        return render_template('Administrator/verify_payment.html',
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               notifications=notifications,
                               notifications_count=notifications_count)
    else:
        return render_template('Administrator/login.html')


@app.route('/payment_verification_success/<int:O_Id>')
def payment_verification_success(O_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            sel_one_download_verify = ProductDownloadVerification.query.filter_by(id=O_Id).first()
            sel_one_download_verify.is_verified = 1
            sel_one_download_verify.delivery_status = 'OnTheWay'
            db.session.commit()
            flash("Record Successfully Verified", "success")
            return redirect('/verify_payment')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/chat_messages', methods=['POST', 'GET'])
def chat_messages():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        # Fetch notification data from the database
        notifications = MakeNotification.query.filter_by(status='Live').all()
        notifications_count = MakeNotification.query.filter_by(status='Live').count()

        seller_id = session['UserId']

        # Retrieve all unique users who have sent messages to the seller
        users_who_sent_messages = db.session.query(Customers).join(Chat, Customers.cust_id == Chat.sender_id).filter(
            Chat.receiver_id == seller_id).distinct().all()

        # Retrieve chat messages between seller and each user
        all_chats = {}
        for user in users_who_sent_messages:
            chat_messages = Chat.query.filter(
                (Chat.sender_id == user.cust_id) & (Chat.receiver_id == seller_id)
            ).all()
            all_chats[user.cust_id] = chat_messages  # Dictionary storing all messages per user

        return render_template('Administrator/chat_messages.html',
                               users_who_sent_messages=users_who_sent_messages,
                               all_chats=all_chats,
                               notifications=notifications,
                               notifications_count=notifications_count)
    else:
        return render_template('Administrator/login.html')

