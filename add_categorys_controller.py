from app import app
from sqlalchemy.exc import IntegrityError
from database_model import *
from flask import render_template, flash, session, request, redirect


@app.route('/add_product_category', methods=['POST', 'GET'])
def add_product_category():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Fetch notification data from the database
            notifications = MakeNotification.query.filter_by(status='Live').all()
            notifications_count = MakeNotification.query.filter_by(status='Live').count()

            product_category_data_retrieve = ProductCategory.query.all()

            if request.method == 'POST':
                get_product_category_name = request.form['product_category_name']
                if not get_product_category_name:
                    flash("Error. Please fill the product category name", "danger")
                    return redirect('/add_product_category')
                try:
                    new_entry_save_by_product_category = ProductCategory(
                        pc_name=get_product_category_name
                    )
                    db.session.add(new_entry_save_by_product_category)
                    db.session.commit()
                    flash("Record Successfully Save", "success")
                    return redirect('/add_product_category')
                except IntegrityError:
                    db.session.rollback()
                    flash("Error. Duplicate data detected. Please do not proceed and try again.", "danger")
                    return redirect('/add_product_category')  # Add return statement here
            else:
                return render_template('Administrator/add_product_category.html',
                                       product_category_data_retrieve=product_category_data_retrieve,
                                       notifications=notifications,
                                       notifications_count=notifications_count)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/delete_product_category/<int:Product_Category_Id>')
def delete_product_category(Product_Category_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # get specific user district_sno from clerk Table and then check date with District_Id related
            sel_one_product_category = ProductCategory.query.filter_by(pc_id=Product_Category_Id).first()
            db.session.delete(sel_one_product_category)
            db.session.commit()
            flash("Record Successfully Deleted", "success")
            return redirect('/add_product_category')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Please try again", "danger")
            return redirect('/add_product_category')  # Add return statement here
    else:
        return render_template('Administrator/login.html')


@app.route('/update_product_category/<int:Product_Category_Id>', methods=['GET', 'POST'])
def update_product_category(Product_Category_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            product_category_to_update = (
                ProductCategory.query
                .filter_by(pc_id=Product_Category_Id)
                .first()  # Use first() instead of all() to get a single object
            )

            if request.method == 'POST':
                new_product_category_name = request.form['product_category_name']

                if not new_product_category_name:
                    flash("Error. Please fill the product category name", "danger")
                    return redirect('/add_product_category')

                try:
                    product_category_to_update.pc_name = new_product_category_name
                    db.session.commit()
                    flash("Record Successfully Updated", "success")
                    return redirect('/add_product_category')
                except IntegrityError:
                    db.session.rollback()
                    flash("Error. Duplicate data detected. Please do not proceed and try again.", "danger")
                    return redirect('/add_product_category')
            else:
                return redirect('/add_product_category')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')
