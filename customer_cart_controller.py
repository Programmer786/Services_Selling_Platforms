import random

from sqlalchemy.orm import joinedload
from app import app
from database_model import *
from flask import render_template, flash, session, redirect, url_for, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename


@app.route("/")
def customer_dashboard():
    try:
        # Get all necessary data from the database
        all_product_category_name = ProductCategory.query.all()
        all_products_data_retrieve = (
            Products.query
            .join(ProductCategory)
            .options(joinedload(Products.product_category))
            .all()
        )
        all_order_for_download_data_retrieve = (
            ProductDownloadVerification.query
            .join(Products)
            .options(joinedload(ProductDownloadVerification.products))
            .all()
        )

        all_artist = Users.query.filter_by(rol_name='Artist').all()

        all_reports = MakeReport.query.all()  # Retrieve all report data

        base_static_url = url_for('static', filename='')

        # Calculate the average rating for each artist
        artist_ratings = {}
        for artist in all_artist:
            feedbacks = ProductDownloadVerification.query.join(Products).filter(Products.user_id == artist.user_id).all()
            total_stars = sum(feedback.feedback_stars for feedback in feedbacks if feedback.feedback_stars is not None)
            count_stars = sum(1 for feedback in feedbacks if feedback.feedback_stars is not None)
            average_rating = total_stars / count_stars if count_stars > 0 else 0
            artist_ratings[artist.user_id] = average_rating

        # Pass the function to the template context
        return render_template('Customer/index.html',
                               all_product_category_name=all_product_category_name,
                               all_products_data_retrieve=all_products_data_retrieve,
                               base_static_url=base_static_url,
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               product_already_added=product_already_added,
                               all_artist=all_artist,
                               all_reports=all_reports,
                               artist_ratings=artist_ratings)
    except Exception as e:
        db.session.rollback()
        flash(f"Error: {str(e)}", "danger")
        return redirect('/')


@app.route("/Calligrapher")
def Calligrapher():
    try:
        # Get all necessary data from the database
        all_product_category_name = ProductCategory.query.all()
        all_products_data_retrieve = (
            Products.query
            .join(ProductCategory)
            .options(joinedload(Products.product_category))
            .all()
        )
        all_order_for_download_data_retrieve = (
            ProductDownloadVerification.query
            .join(Products)
            .options(joinedload(ProductDownloadVerification.products))
            .all()
        )

        all_artist = Users.query.filter_by(rol_name='Artist',user_name='Calligrapher').all()

        all_reports = MakeReport.query.all()  # Retrieve all report data

        base_static_url = url_for('static', filename='')

        # Calculate the average rating for each artist
        artist_ratings = {}
        for artist in all_artist:
            feedbacks = ProductDownloadVerification.query.join(Products).filter(Products.user_id == artist.user_id).all()
            total_stars = sum(feedback.feedback_stars for feedback in feedbacks if feedback.feedback_stars is not None)
            count_stars = sum(1 for feedback in feedbacks if feedback.feedback_stars is not None)
            average_rating = total_stars / count_stars if count_stars > 0 else 0
            artist_ratings[artist.user_id] = average_rating

        # Pass the function to the template context
        return render_template('Customer/Calligrapher.html',
                               all_product_category_name=all_product_category_name,
                               all_products_data_retrieve=all_products_data_retrieve,
                               base_static_url=base_static_url,
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               product_already_added=product_already_added,
                               all_artist=all_artist,
                               all_reports=all_reports,
                               artist_ratings=artist_ratings)
    except Exception as e:
        db.session.rollback()
        flash(f"Error: {str(e)}", "danger")
        return redirect('/')


@app.route("/Painter")
def Painter():
    try:
        # Get all necessary data from the database
        all_product_category_name = ProductCategory.query.all()
        all_products_data_retrieve = (
            Products.query
            .join(ProductCategory)
            .options(joinedload(Products.product_category))
            .all()
        )
        all_order_for_download_data_retrieve = (
            ProductDownloadVerification.query
            .join(Products)
            .options(joinedload(ProductDownloadVerification.products))
            .all()
        )

        all_artist = Users.query.filter_by(rol_name='Artist',user_name='Painter').all()

        all_reports = MakeReport.query.all()  # Retrieve all report data

        base_static_url = url_for('static', filename='')

        # Calculate the average rating for each artist
        artist_ratings = {}
        for artist in all_artist:
            feedbacks = ProductDownloadVerification.query.join(Products).filter(Products.user_id == artist.user_id).all()
            total_stars = sum(feedback.feedback_stars for feedback in feedbacks if feedback.feedback_stars is not None)
            count_stars = sum(1 for feedback in feedbacks if feedback.feedback_stars is not None)
            average_rating = total_stars / count_stars if count_stars > 0 else 0
            artist_ratings[artist.user_id] = average_rating

        # Pass the function to the template context
        return render_template('Customer/Painter.html',
                               all_product_category_name=all_product_category_name,
                               all_products_data_retrieve=all_products_data_retrieve,
                               base_static_url=base_static_url,
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               product_already_added=product_already_added,
                               all_artist=all_artist,
                               all_reports=all_reports,
                               artist_ratings=artist_ratings)
    except Exception as e:
        db.session.rollback()
        flash(f"Error: {str(e)}", "danger")
        return redirect('/')


@app.route("/Photographer")
def Photographer():
    try:
        # Get all necessary data from the database
        all_product_category_name = ProductCategory.query.all()
        all_products_data_retrieve = (
            Products.query
            .join(ProductCategory)
            .options(joinedload(Products.product_category))
            .all()
        )
        all_order_for_download_data_retrieve = (
            ProductDownloadVerification.query
            .join(Products)
            .options(joinedload(ProductDownloadVerification.products))
            .all()
        )

        all_artist = Users.query.filter_by(rol_name='Artist',user_name='Photographer').all()

        all_reports = MakeReport.query.all()  # Retrieve all report data

        base_static_url = url_for('static', filename='')

        # Calculate the average rating for each artist
        artist_ratings = {}
        for artist in all_artist:
            feedbacks = ProductDownloadVerification.query.join(Products).filter(Products.user_id == artist.user_id).all()
            total_stars = sum(feedback.feedback_stars for feedback in feedbacks if feedback.feedback_stars is not None)
            count_stars = sum(1 for feedback in feedbacks if feedback.feedback_stars is not None)
            average_rating = total_stars / count_stars if count_stars > 0 else 0
            artist_ratings[artist.user_id] = average_rating

        # Pass the function to the template context
        return render_template('Customer/Photographer.html',
                               all_product_category_name=all_product_category_name,
                               all_products_data_retrieve=all_products_data_retrieve,
                               base_static_url=base_static_url,
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               product_already_added=product_already_added,
                               all_artist=all_artist,
                               all_reports=all_reports,
                               artist_ratings=artist_ratings)
    except Exception as e:
        db.session.rollback()
        flash(f"Error: {str(e)}", "danger")
        return redirect('/')



@app.route("/contact_us", methods=['POST', 'GET'])
def contact_us():
    try:
        # Get all necessary data from the database
        all_product_category_name = ProductCategory.query.all()
        all_products_data_retrieve = (
            Products.query
            .join(ProductCategory)
            .options(joinedload(Products.product_category))
            .all()
        )
        all_order_for_download_data_retrieve = (
            ProductDownloadVerification.query
            .join(Products)
            .options(joinedload(ProductDownloadVerification.products))
            .all()
        )

        all_artist = Users.query.filter_by(rol_name='Artist').all()

        all_reports = MakeReport.query.all()  # Retrieve all report data

        base_static_url = url_for('static', filename='')

        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            message = request.form['message']

            if name and email and phone and message:
                new_contact = Contact(name=name, email=email, phone=phone, message=message)
                try:
                    db.session.add(new_contact)
                    db.session.commit()
                    flash("Message sent successfully!", "success")
                    return redirect('/contact_us')
                except Exception as e:
                    db.session.rollback()
                    flash("An error occurred while sending your message. Please try again.", "danger")
                    return redirect('/contact_us')
            else:
                flash("Please fill out all fields.", "danger")

        # Pass the function to the template context
        return render_template('Customer/contact_us.html',
                               all_product_category_name=all_product_category_name,
                               all_products_data_retrieve=all_products_data_retrieve,
                               base_static_url=base_static_url,
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               product_already_added=product_already_added,
                               all_artist=all_artist,
                               all_reports=all_reports)
    except Exception as e:
        db.session.rollback()
        flash(f"Error: {str(e)}", "danger")
        return redirect('/')


@app.route("/about")
def about():
    return render_template('Customer/about.html')


@app.route("/pos_customer_order/<int:User_Id>")
def pos_customer_order(User_Id):
    try:
        # Get all necessary data from the database
        all_product_category_name = ProductCategory.query.all()
        all_products_data_retrieve = (
            Products.query
            .filter(Products.user_id == User_Id)
            .join(ProductCategory)
            .options(joinedload(Products.product_category))
            .all()
        )
        all_order_for_download_data_retrieve = (
            ProductDownloadVerification.query
            .join(Products)
            .options(joinedload(ProductDownloadVerification.products))
            .all()
        )
        base_static_url = url_for('static', filename='')

        # Pass the function to the template context
        return render_template('Customer/pos_customer_order.html',
                               all_product_category_name=all_product_category_name,
                               all_products_data_retrieve=all_products_data_retrieve,
                               base_static_url=base_static_url,
                               all_order_for_download_data_retrieve=all_order_for_download_data_retrieve,
                               product_already_added=product_already_added)
    except Exception as e:
        db.session.rollback()
        flash(f"Error: {str(e)}", "danger")
        return render_template('Customer/pos_customer_order.html')


def product_already_added(product_id):
    # Perform the necessary query to check if the product with the given ID has been added for download
    # Return True if the product is already added, otherwise return a False
    # Example query:
    existing_verification = ProductDownloadVerification.query.filter_by(
        product_id=product_id,
        customer_id=session.get('Cust_Id')
    ).first()
    return existing_verification is not None


@app.route('/add_to_download_verification', methods=['POST'])
def add_to_download_verification():
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            product_id = request.form.get('product_id')
            customer_id = session['Cust_Id']
            if not product_id or not customer_id:
                return jsonify({'error': 'Missing product ID or customer ID'}), 400

            # Check if the combination of product_id and customer_id already exists
            existing_verification = ProductDownloadVerification.query.filter_by(
                product_id=product_id,
                customer_id=customer_id
            ).first()

            if existing_verification:
                return jsonify({'message': 'Product already added to download verification'}), 200

            # If not exists, add the entry
            verification = ProductDownloadVerification(
                product_id=product_id,
                customer_id=customer_id
            )
            db.session.add(verification)
            db.session.commit()

            return jsonify({'message': 'Product added to download verification'}), 201
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/download_product_image/<int:P_Id>')
def download_product_image(P_Id):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            # Fetch the document information from the database
            document = Products.query.filter_by(p_id=P_Id).first_or_404()
            # Send the file using send_from_directory
            if document.p_original_image:
                return send_from_directory(app.config['ORIGINAL_UPLOAD_FOLDER'], document.p_original_image, as_attachment=True)
            else:
                return redirect('/')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash("The Contact to Admin", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/submit_transaction/<int:OrderId>', methods=['GET', 'POST'])
def submit_transaction(OrderId):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            one_Order = ProductDownloadVerification.query.get_or_404(OrderId)
            if request.method == 'POST':
                get_select_payment_method = request.form.get('select_payment_method')
                uploaded_file = request.files['receipt_file']

                # Check if required fields are not empty
                if not get_select_payment_method or not uploaded_file or not allowed_file(uploaded_file.filename):
                    flash("Error. Please fill all the required fields and upload a valid receipt", "danger")
                    return redirect('/')

                # Save the uploaded receipt file
                if uploaded_file:
                    # Get the original file extension
                    _, file_extension = os.path.splitext(uploaded_file.filename)
                    # Generate a random 4-digit number
                    random_number = random.randint(1000000, 9999999)
                    # Combine random_number, employee ID, and file extension to create a custom filename
                    custom_filename = f"{random_number}_{OrderId}{file_extension}"
                    # Save the file and update the database record with the file path
                    # filename = secure_filename(uploaded_file.filename)
                    file_path_system = os.path.join(app.config['UPLOAD_FOLDER'], custom_filename)  # Set your upload folder path
                    file_full_name = os.path.join("", custom_filename)  # Set your No path for database column
                    uploaded_file.save(file_path_system)
                    one_Order.receipt_file_path = file_full_name

                # Update the order with a select method and receipt file path
                one_Order.select_payment_method = get_select_payment_method
                one_Order.transaction_no = True
                db.session.commit()

                flash(f"{one_Order.products.p_name} :- Transaction Recept Successfully Submitted, Now Waiting For Confirmation. Thank You!", "success")
                return redirect('/')
            else:
                return redirect('/')
        except Exception as e:
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/download_recept_document/<int:OrderId>')
def download_recept_document(OrderId):
    try:
        # Fetch the document information from the database
        document = ProductDownloadVerification.query.filter_by(id=OrderId).first_or_404()

        # Send the file using send_from_directory
        return send_from_directory(app.config['UPLOAD_FOLDER'], document.receipt_file_path, as_attachment=True)
    except Exception as e:
        # If an error occurs during database connection, display an error message
        db.session.rollback()
        flash(f"Error: {str(e)}", "danger")
        flash("The Documents are Not Available in the database", "danger")
        return render_template('Administrator/login.html')


@app.route('/submit_feedback/<int:OrderId>', methods=['GET', 'POST'])
def submit_feedback(OrderId):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            feedback = request.form.get('feedback')
            give_stars = request.form.get('give_stars')

            # Retrieve the order from the database using the order_id
            one_Order = ProductDownloadVerification.query.get_or_404(OrderId)

            # Update the feedback and stars for the order
            one_Order.feedback_description = feedback
            one_Order.feedback_stars = give_stars
            one_Order.feedback_submitted = True

            # Commit the changes to the database
            db.session.commit()

            flash(f"{one_Order.products.p_name} :- Feedback Successfully Submitted, Thank You!", "success")
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/delivery_received/<int:OrderId>')
def delivery_received(OrderId):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            sel_one_delivery = ProductDownloadVerification.query.get_or_404(OrderId)
            sel_one_delivery.delivery_status = 'Deliver'
            db.session.commit()
            flash("Record Successfully Received", "success")
            return redirect('/')
        except Exception as e:
            # If an error occurs during database connection, display an error message
            db.session.rollback()
            flash(f"Error: {str(e)}" "", "danger")
            return render_template('Customer/customer_login.html')
    else:
        return render_template('Customer/customer_login.html')


@app.route('/make_report/<int:Report_Id>', methods=['POST'])
def make_report(Report_Id):
    if 'Cust_Id' and 'Cust_Phone' and 'Cust_UserName' in session:
        try:
            # Retrieve the form data
            select_reason = request.form['select_reason']
            report_message = request.form['report_message']

            # Check if the form data is valid
            if select_reason and report_message:
                # Create a new report entry
                new_report = MakeReport(
                    user_id=Report_Id,
                    customer_id=session['Cust_Id'],
                    select_reason=select_reason,
                    send_report_message=report_message,
                    is_check_by_admin=False  # Default value
                )
                db.session.add(new_report)
                db.session.commit()

                flash("Report submitted successfully.", "success")
            else:
                flash("Error! Please fill out all fields.", "danger")

            return redirect('/')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/')
    else:
        return render_template('Customer/customer_login.html')
