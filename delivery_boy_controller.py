from sqlalchemy.orm import joinedload
from werkzeug.security import generate_password_hash

from app import app
from sqlalchemy.exc import IntegrityError
from database_model import *
from flask import render_template, flash, session, request, redirect


@app.route('/all_delivery_boy', methods=['POST', 'GET'])
def all_delivery_boy():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Retrieve the parent data where view_request is False
            # all_delivery_boy_data_retrieve = Users.query.filter_by(rol_name='DeliveryBoy').all()
            all_delivery_boy_data_retrieve = (
                Users.query
                .filter_by(rol_name='DeliveryBoy')
                .all()
            )

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
                                    rol_name="DeliveryBoy",
                                    password=change_to_hashed_password,
                                    registrationDate=datetime.now(),
                                    isActive=1
                                )
                                db.session.add(new_entry_register_user)
                                db.session.commit()
                                flash("Successfully Register.", "success")
                                return redirect('/all_delivery_boy')
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
                    # If an error occurs during database connection, display an error message
                    db.session.rollback()
                    flash(f"Error: {str(e)}" "", "danger")
                    return redirect('/all_delivery_boy')
            return render_template('Administrator/all_delivery_boy.html', all_delivery_boy_data_retrieve=all_delivery_boy_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Administrator/login.html')

