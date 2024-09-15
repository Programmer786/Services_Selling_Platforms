from requests import session
from sqlalchemy import desc
from sqlalchemy.orm import joinedload

from app import app
from sqlalchemy.exc import IntegrityError
from database_model import *
from flask import render_template, flash, session, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
import random


@app.route("/admin_dashboard")
def admin_dashboard():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        # Fetch notification data from the database
        notifications = MakeNotification.query.filter_by(status='Live').all()
        notifications_count = MakeNotification.query.filter_by(status='Live').count()

        # Get today's date
        today = date.today()
        # Fetch real count data from the database
        total_artist = Users.query.filter_by(rol_name='Artist').count()
        all_order_for_download_data_retrieve = (
            ProductDownloadVerification.query
            .join(Products)
            .options(joinedload(ProductDownloadVerification.products))  # Eager load the associated project
            .count()
        )
        print(f"all_order_for_download_data_retrieve:{all_order_for_download_data_retrieve}")
        total_delivery_boy = Users.query.filter_by(rol_name='DeliveryBoy').count()

        session_UserId = session['UserId']
        session_rol_name = session['rol_name']
        if session_rol_name == "Administrator":
            all_order_for_today_sales_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .filter(ProductDownloadVerification.is_verified == 1, ProductDownloadVerification.created_at == today)  # Filter based on Products table's attribute
                .all()
            )

            all_order_for_total_sales_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .filter(ProductDownloadVerification.is_verified == 1)  # Filter based on Products table's attribute
                .all()
            )
        else:
            all_order_for_today_sales_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .options(joinedload(ProductDownloadVerification.products))
                .filter(Products.user_id == session_UserId, ProductDownloadVerification.is_verified == 1, ProductDownloadVerification.created_at == today)  # Filter based on Products table's attribute
                .all()
            )

            all_order_for_total_sales_retrieve = (
                ProductDownloadVerification.query
                .join(Products)  # Join with Products table
                .options(joinedload(ProductDownloadVerification.products))
                .filter(Products.user_id == session_UserId, ProductDownloadVerification.is_verified == 1)  # Filter based on Products table's attribute
                .all()
            )

        # Calculate the today sale amount
        today_sale = sum(product.products.p_price for product in all_order_for_today_sales_retrieve)
        # Calculate the total sale amount
        total_sale = sum(product.products.p_price for product in all_order_for_total_sales_retrieve)

        # today_profit = today_ticket_receivable_client - today_ticket_airline_payable
        # total_profit = total_ticket_receivable_client - total_ticket_airline_payable

        return render_template('Administrator/admin_dashboard.html',
                               notifications=notifications,
                               notifications_count=notifications_count,
                               total_artist=total_artist,
                               total_delivery_boy=total_delivery_boy,
                               total_sale=total_sale,
                               today_sale=today_sale,
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve)
    else:
        return render_template('Administrator/login.html')


@app.route('/admin_login', methods=['POST', 'GET'])
def admin_login():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        session_rol_name = session['rol_name']
        if session_rol_name == "Administrator":
            return redirect('/admin_dashboard')
        elif session_rol_name == "Artist":
            return redirect('/admin_dashboard')
        else:
            return redirect('/logout')
    else:
        if request.method == 'POST':
            a_cnic = request.form['cnic']
            a_password = request.form['password']
            try:
                # query = "select 1 from Users where cnic=cnic"
                user = Users.query.filter_by(cnic=a_cnic).first()
                # If no record found by this email
                if user is not None:
                    if user.isActive == 1:
                        passwd = user.password
                        # If password decrypt and record do not match with password
                        if check_password_hash(passwd, a_password):  # if passwd == a_password: without encryption
                            session.permanent = True  # <--- makes the permanent session
                            session['user_name'] = user.user_name
                            session['full_name'] = user.full_name
                            session['cnic'] = user.cnic
                            session['email'] = user.email
                            session['ContactNo'] = user.phone
                            session['UserId'] = user.user_id
                            session['photo'] = user.photo
                            session['rol_name'] = user.rol_name

                            if user.rol_name == "Administrator":
                                return redirect('/admin_dashboard')
                            elif user.rol_name == "Artist":
                                return redirect('/admin_dashboard')
                            else:
                                return redirect('/logout')
                        else:
                            flash("Error! Invalid Detail, Please try Again!", "danger")
                            return render_template('Administrator/login.html')
                    else:
                        flash("Error! Please Contact to Administrator! Your Account is not Approve.", "warning")
                        return render_template('Administrator/login.html')
                else:
                    flash("Error! Invalid Details, Please Register your Account!", "danger")
                    return render_template('Administrator/login.html')
            except Exception as e:
                # If an error occurs during database connection, display error message
                db.session.rollback()
                flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
                return render_template('Administrator/login.html')
            # except IntegrityError:
            #     db.session.rollback()
            #     flash("Error! Please try again", "danger")
            #     return render_template('Administrator/login.html')
        return render_template('Administrator/login.html')


@app.route('/role', methods=['POST', 'GET'])
def role():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Fetch notification data from the database
            notifications = MakeNotification.query.filter_by(status='Live').all()
            notifications_count = MakeNotification.query.filter_by(status='Live').count()

            # role_with_Cnic_data_retrieve = Users.query.order_by(Users.user_id).all()
            cell_values = ["Administrator", "Artist"]
            role_with_cnic_data_retrieve = Users.query.filter(
                Users.rol_name.in_(cell_values)
            ).all()

            if request.method == 'POST':
                try:
                    r_user_name = request.form.get('user_name')
                    r_full_name = request.form.get('full_name')
                    r_email = request.form.get('email')
                    r_phone = request.form.get('phone')
                    r_cnic = request.form.get('cnic')
                    r_gender = request.form.get('gender')
                    r_password = request.form.get('password')
                    r_conform_password = request.form.get('conform_password')
                    if (r_user_name != "") and (r_full_name != "") and (r_email != "") and (r_phone != "") and (r_cnic != "") and (r_password != "") and (
                            r_conform_password != ""):
                        register_user = Users.query.filter_by(cnic=r_cnic).count()
                        if r_password == r_conform_password:
                            if register_user < 1:
                                # change_to_hashed_password = generate_password_hash(r_password, "sha256") #old method
                                change_to_hashed_password = generate_password_hash(r_password, method='scrypt')  # new method

                                new_entry_register_user = Users(
                                    user_name=r_user_name,
                                    full_name=r_full_name,
                                    email=r_email,
                                    phone=r_phone,
                                    cnic=r_cnic,
                                    gender=r_gender,
                                    rol_name="Artist",
                                    password=change_to_hashed_password,
                                    registrationDate=datetime.now(),
                                    isActive=1
                                )
                                db.session.add(new_entry_register_user)
                                db.session.commit()
                                flash("Successfully Register.", "success")
                                return redirect('/role')
                            else:
                                flash(
                                    "Error! The Account is Already Registered So goto Login otherwise Contact to your Administrator. "
                                    "Thank you",
                                    "danger")
                        else:
                            flash("Error! Your conform password is wrong please try again", "danger")
                    else:
                        flash("Error! Please fill out this field.", "danger")
                except Exception as e:
                    # If an error occurs during database connection, display error message
                    db.session.rollback()
                    flash(f"Error: {str(e)}" "", "danger")
                    return redirect('/role')
            else:
                return render_template('Administrator/role.html', role_with_Cnic_data=role_with_cnic_data_retrieve,
                                       notifications=notifications,
                                       notifications_count=notifications_count)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/disable_role_user/<int:UserId>')
def disable_role_user(UserId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 0
            db.session.commit()
            flash("Record Successfully Disable", "success")
            return redirect('/role')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/enable_role_user/<int:UserId>')
def enable_role_user(UserId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 1
            db.session.commit()
            flash("Record Successfully Enable", "success")
            return redirect('/role')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/user_for_update/<int:UserId>', methods=['POST', 'GET'])
def user_for_update(UserId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # get specific user SNo from clerk Table and then check date with SNo related
            get_user_name = request.form['user_name']
            get_full_name = request.form['full_name']
            get_email = request.form['email']
            get_cnic = request.form['cnic']
            get_phone = request.form['phone']
            get_gender = request.form['gender']

            update_user = Users.query.filter_by(user_id=UserId).first()
            update_user.user_name = get_user_name
            update_user.full_name = get_full_name
            update_user.email = get_email
            update_user.cnic = get_cnic
            update_user.phone = get_phone
            update_user.gender = get_gender

            db.session.add(update_user)
            db.session.commit()
            flash("Record Successfully Updated", "success")
            return redirect('/role')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC Not Acceptable", "danger")
            return redirect('/role')  # Add return statement here
    else:
        return render_template('Administrator/login.html')


@app.route('/update_profile/<int:UserId>', methods=['POST', 'GET'])
def update_profile(UserId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Fetch notification data from the database
            notifications = MakeNotification.query.filter_by(status='Live').all()
            notifications_count = MakeNotification.query.filter_by(status='Live').count()

            role_with_cnic_data_retrieve = Users.query.filter_by(user_id=UserId).first()
            return render_template('Administrator/update_profile.html', role_with_cnic_data=role_with_cnic_data_retrieve, notifications=notifications,
                                   notifications_count=notifications_count)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/change_password/<int:UserId>', methods=['POST', 'GET'])
def change_password(UserId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Retrieve form data
            r_password = request.form.get('password')
            r_conform_password = request.form.get('conform_password')

            if r_password == r_conform_password:
                # change_to_hashed_password = generate_password_hash(r_password, "sha256") #old method
                change_to_hashed_password = generate_password_hash(r_password, method='scrypt')  # new method

                update_user_password = Users.query.filter_by(user_id=UserId).first()
                update_user_password.password = change_to_hashed_password
                db.session.add(update_user_password)
                db.session.commit()
                flash("Password changed successfully.", "success")
                return redirect(f'/update_profile/{UserId}')
            else:
                flash("Error! Your confirm password is wrong, please try again", "danger")
                return redirect(f'/update_profile/{UserId}')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        # Render the form for GET requests
        return render_template('Administrator/login.html')


@app.route('/manage_customers', methods=['POST', 'GET'])
def manage_customers():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Fetch notification data from the database
            notifications = MakeNotification.query.filter_by(status='Live').all()
            notifications_count = MakeNotification.query.filter_by(status='Live').count()

            customer_data_retrieve = Customers.query.order_by(desc(Customers.cust_id)).all()
            return render_template('Administrator/manage_customers.html', customer_data_retrieve=customer_data_retrieve, notifications=notifications,
                                   notifications_count=notifications_count)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/disable_role_customer/<int:CustId>')
def disable_role_customer(CustId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            sel_one_customer = Customers.query.filter_by(cust_id=CustId).first()
            sel_one_customer.isActive = 0
            db.session.commit()
            flash("Record Successfully Disable", "success")
            return redirect('/manage_customers')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/enable_role_customer/<int:CustId>')
def enable_role_customer(CustId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            sel_one_customer = Customers.query.filter_by(cust_id=CustId).first()
            sel_one_customer.isActive = 1
            db.session.commit()
            flash("Record Successfully Enable", "success")
            return redirect('/manage_customers')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/customer_for_update/<int:CustId>', methods=['POST', 'GET'])
def customer_for_update(CustId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # get specific user SNo from clerk Table and then check date with SNo related
            get_user_name = request.form['user_name']
            get_full_name = request.form['full_name']
            get_phone = request.form['phone']
            get_gender = request.form['gender']
            get_drop_address = request.form['drop_address']

            update_customer = Customers.query.filter_by(cust_id=CustId).first()
            update_customer.cust_user_name = get_user_name
            update_customer.cust_full_name = get_full_name
            update_customer.cust_phone = get_phone
            update_customer.cust_gender = get_gender
            update_customer.cust_drop_address = get_drop_address

            db.session.add(update_customer)
            db.session.commit()
            flash("Record Successfully Updated", "success")
            return redirect('/manage_customers')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate Data Not Acceptable", "danger")
            return redirect('/manage_customers')  # Add return statement here
    else:
        return render_template('Administrator/login.html')


@app.route('/update_artist_image/<int:UserId>', methods=['GET', 'POST'])
def update_artist_image(UserId):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            if request.method == 'POST':
                # First delete the file
                user = Users.query.get_or_404(UserId)
                file_path1 = None  # Initialize file_path1 with a default value
                if user.photo is not None:
                    file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], user.photo)  # Construct the full path to the file
                # Delete the file from the directory if it exists
                if file_path1 is not None and os.path.exists(file_path1):
                    os.remove(file_path1)
                session.pop('photo', None)

                # Get WaterMart New Image Path
                get_uploaded_p_original_image = request.files['p_original_image']

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
                    file_path_system = os.path.join(app.config['UPLOAD_FOLDER'], custom_filename)  # Set your upload folder path
                    file_full_name = os.path.join("", custom_filename)  # Set your No path for database column
                    get_uploaded_p_original_image.save(file_path_system)
                    user.photo = file_full_name
                    session['photo'] = file_full_name

                db.session.commit()
                flash("The Artist Images Successfully Updated", "success")
                return redirect(f'/update_profile/{UserId}')
            else:
                return redirect(f'/update_profile/{UserId}')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect(f'/update_profile/{UserId}')
    else:
        return render_template('Administrator/login.html')


@app.route('/artist_register', methods=['POST', 'GET'])
def artist_register():
    if request.method == 'POST':
        try:
            r_user_name = request.form.get('user_name')
            r_full_name = request.form.get('full_name')
            r_email = request.form.get('email')
            r_phone = request.form.get('phone')
            r_cnic = request.form.get('cnic')
            r_gender = request.form.get('gender')
            r_password = request.form.get('password')
            r_conform_password = request.form.get('conform_password')
            if (r_user_name != "") and (r_full_name != "") and (r_email != "") and (r_phone != "") and (r_cnic != "") and (r_password != "") and (
                    r_conform_password != ""):
                register_user = Users.query.filter_by(cnic=r_cnic).count()
                if r_password == r_conform_password:
                    if register_user < 1:
                        # change_to_hashed_password = generate_password_hash(r_password, "sha256") #old method
                        change_to_hashed_password = generate_password_hash(r_password, method='scrypt')  # new method

                        new_entry_register_user = Users(
                            user_name=r_user_name,
                            full_name=r_full_name,
                            email=r_email,
                            phone=r_phone,
                            cnic=r_cnic,
                            gender=r_gender,
                            rol_name="Artist",
                            password=change_to_hashed_password,
                            registrationDate=datetime.now(),
                            isActive=0
                        )
                        db.session.add(new_entry_register_user)
                        db.session.commit()
                        flash("Successfully Register.", "success")
                        return redirect('/artist_register')
                    else:
                        flash(
                            "Error! The Account is Already Registered So goto Login otherwise Contact to your Administrator. "
                            "Thank you",
                            "danger")
                else:
                    flash("Error! Your conform password is wrong please try again", "danger")
            else:
                flash("Error! Please fill out this field.", "danger")
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash("Error: Your Contact Number is Already Attached to Another Account, So Please Try with Another Contact Number.", "danger")
            return redirect('/artist_register')
    else:
        return render_template('Administrator/artist_register.html')

    # Ensure to return a valid response in all cases
    return render_template('Administrator/artist_register.html')


@app.route("/error_404")
def error_404():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        return render_template('Administrator/error_404.html')
    else:
        return render_template('Administrator/login.html')


@app.route("/logout")
def logout():
    session.pop('user_name', None)
    session.pop('full_name', None)
    session.pop('cnic', None)
    session.pop('email', None)
    session.pop('ContactNo', None)
    session.pop('UserId', None)
    session.pop('photo', None)
    session.pop('district', None)
    session.pop('rol_name', None)
    return redirect('/')
