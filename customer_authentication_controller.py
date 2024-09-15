from sqlalchemy.orm import joinedload
from app import app
from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc
from database_model import *
# from database_model import db, Users,Rol
from flask import render_template, flash, session, request, redirect, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date


@app.route('/cust_register', methods=['POST', 'GET'])
def customer_registration_page():
    if request.method == 'POST':
        try:
            c_full_name = request.form.get('full_name')
            c_phone = request.form.get('phone_number')
            c_gender = request.form.get('gender')
            c_user_name = request.form.get('user_name')
            c_drop_address = request.form.get('drop_address')
            c_password = request.form.get('password')
            c_conform_password = request.form.get('conform_password')

            if ' ' in c_user_name:
                flash("Error! Username cannot contain spaces.", "danger")
                return redirect('/cust_register')

            if (c_full_name != "") and (c_phone != "") and (c_user_name != "") and (c_password != "") and (
                    c_conform_password != ""):
                register_customer = Customers.query.filter_by(cust_user_name=c_user_name).count()
                if c_password == c_conform_password:
                    if register_customer < 1:
                        # change_to_hashed_password = generate_password_hash(c_password, "sha256") #old method
                        change_to_hashed_password = generate_password_hash(c_password, method='scrypt')  # new method

                        new_entry_register_customer = Customers(
                            cust_user_name=c_user_name,
                            cust_full_name=c_full_name,
                            cust_phone=c_phone,
                            cust_gender=c_gender,
                            cust_rol_name="Customer",
                            cust_drop_address=c_drop_address,
                            cust_password=change_to_hashed_password,
                            cust_registrationDate=datetime.now(),
                            isActive=1
                        )
                        db.session.add(new_entry_register_customer)
                        db.session.commit()
                        flash("Successfully Register.", "success")
                        return redirect('/cust_register')
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
            return redirect('/cust_register')
    else:
        return render_template('Customer/customer_register.html')

    # Ensure to return a valid response in all cases
    return render_template('Customer/customer_register.html')


@app.route('/cust_login', methods=['POST', 'GET'])
def customer_login_page():
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        session_cust_rol_name = session['cust_RolName']
        if session_cust_rol_name == "Customer":
            return redirect('/')
        else:
            return redirect('/cust_logout')
    else:
        if request.method == 'POST':
            c_user_name = request.form['user_name']
            c_password = request.form['login_password']
            try:
                customer = Customers.query.filter_by(cust_user_name=c_user_name, isActive=1).first()
                # If no record found by this c_user_name
                if customer is not None:
                    if customer.isActive == 1:
                        passwd = customer.cust_password
                        # If password decrypt and record do not match with password
                        if check_password_hash(passwd, c_password):  # if passwd == a_password: without encryption
                            session.permanent = True  # <--- makes the permanent session
                            session['Cust_Id'] = customer.cust_id
                            session['Cust_UserName'] = customer.cust_user_name
                            session['Cust_FullName'] = customer.cust_full_name
                            session['Cust_Phone'] = customer.cust_phone
                            session['Cust_Photo'] = customer.cust_photo
                            session['cust_RolName'] = customer.cust_rol_name

                            if customer.cust_rol_name == "Customer":
                                return redirect('/')
                            else:
                                return redirect('/cust_logout')
                        else:
                            flash("Error! Invalid Detail, Please try Again!", "danger")
                            return render_template('Customer/customer_login.html')
                    else:
                        flash("Error! Please Contact to Administrator! Your Account is Looked.", "danger")
                        return render_template('Customer/customer_login.html')
                else:
                    flash("Error! Invalid Details, Please Contact to Administrator!", "danger")
                    return render_template('Customer/customer_login.html')
            except Exception as e:
                # If an error occurs during database connection, display error message
                db.session.rollback()
                flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
                return render_template('Customer/customer_login.html')
        return render_template('Customer/customer_login.html')


@app.route('/update_customer_profile/<int:CustId>', methods=['POST', 'GET'])
def update_customer_profile(CustId):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            # Fetch notification data from the database
            notifications = MakeNotification.query.filter_by(status='Live').all()
            notifications_count = MakeNotification.query.filter_by(status='Live').count()

            customer_data_retrieve = Customers.query.filter_by(cust_id=CustId).first()

            return render_template('Customer/update_customer_profile.html',
                                   customer_data_retrieve=customer_data_retrieve,
                                   notifications=notifications,
                                   notifications_count=notifications_count)
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/customer_side_for_update/<int:CustId>', methods=['POST', 'GET'])
def customer_side_for_update(CustId):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            # get specific user SNo from clerk Table and then check date with SNo related
            get_user_name = request.form['user_name']
            get_full_name = request.form['full_name']
            get_phone = request.form['phone']
            get_gender = request.form['gender']

            update_customer = Customers.query.filter_by(cust_id=CustId).first()
            update_customer.cust_user_name = get_user_name
            update_customer.cust_full_name = get_full_name
            update_customer.cust_phone = get_phone
            update_customer.cust_gender = get_gender

            db.session.add(update_customer)
            db.session.commit()
            flash("Record Successfully Updated", "success")
            return redirect(f'/update_customer_profile/{CustId}')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/customer_side_disable_role/<int:CustId>', methods=['POST', 'GET'])
def customer_side_disable_role(CustId):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            sel_one_customer = Customers.query.filter_by(cust_id=CustId).first()
            sel_one_customer.isActive = 0
            db.session.commit()
            flash("Record Successfully Disable", "success")
            return redirect(f'/update_customer_profile/{CustId}')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/customer_side_enable_role/<int:CustId>', methods=['POST', 'GET'])
def customer_side_enable_role(CustId):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            sel_one_customer = Customers.query.filter_by(cust_id=CustId).first()
            sel_one_customer.isActive = 1
            db.session.commit()
            flash("Record Successfully Enable", "success")
            return redirect(f'/update_customer_profile/{CustId}')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/change_password_customer_side/<int:CustId>', methods=['POST', 'GET'])
def change_password_customer_side(CustId):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            # Retrieve form data
            r_password = request.form.get('password')
            r_conform_password = request.form.get('conform_password')

            if r_password == r_conform_password:
                # change_to_hashed_password = generate_password_hash(r_password, "sha256") #old method
                change_to_hashed_password = generate_password_hash(r_password, method='scrypt')  # new method

                update_customers_password = Customers.query.filter_by(cust_id=CustId).first()
                update_customers_password.password = change_to_hashed_password
                db.session.add(update_customers_password)
                db.session.commit()
                flash("Password changed successfully.", "success")
                return redirect(f'/update_customer_profile/{CustId}')
            else:
                flash("Error! Your confirm password is wrong, please try again", "danger")
                return redirect(f'/update_customer_profile/{CustId}')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    sender_id = request.form.get('sender_id')
    receiver_id = request.form.get('receiver_id')
    message = request.form.get('message')

    if not message or not sender_id or not receiver_id:
        return jsonify({'error': 'Invalid input'}), 400  # Return 400 if any required field is missing

    try:
        new_message = Chat(
            sender_id=sender_id,
            receiver_id=receiver_id,
            message=message,
            timestamp=datetime.utcnow()
        )
        db.session.add(new_message)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Message sent successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500





@app.route('/reply_message', methods=['POST'])
def reply_message():
    sender_id = request.form.get('sender_id')
    receiver_id = request.form.get('receiver_id')
    message = request.form.get('message')

    if not message or not sender_id or not receiver_id:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        new_message = Chat(
            sender_id=sender_id,
            receiver_id=receiver_id,
            receiver_message=message,
            receiver_timestamp=datetime.utcnow()
        )
        db.session.add(new_message)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Message sent successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get_messages/<int:sender_id>/<int:receiver_id>', methods=['GET'])
def get_messages(sender_id, receiver_id):
    try:
        # Fetch messages where sender and receiver match either direction
        messages = Chat.query.filter(
            ((Chat.sender_id == sender_id) & (Chat.receiver_id == receiver_id)) |
            ((Chat.sender_id == receiver_id) & (Chat.receiver_id == sender_id))
        ).order_by(Chat.timestamp.asc()).all()

        # Prepare message history for JSON response
        chat_history = []
        for msg in messages:
            chat_history.append({
                'sender_id': msg.sender_id,
                'receiver_id': msg.receiver_id,
                'message': msg.message,
                'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            })

        return jsonify({'success': True, 'messages': chat_history})
    except Exception as e:
        return jsonify({'error': str(e)}), 500





if __name__ == '__main__':
    app.run(debug=True)



@app.route("/cust_logout")
def customer_logout():
    session.pop('Cust_Id', None)
    session.pop('Cust_UserName', None)
    session.pop('Cust_FullName', None)
    session.pop('Cust_Phone', None)
    session.pop('Cust_Photo', None)
    session.pop('cust_RolName', None)
    return redirect('/cust_login')


