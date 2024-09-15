from datetime import date

from app import app
from database_model import *
from flask import render_template, flash, session, request, redirect


@app.route('/notification', methods=['POST', 'GET'])
def notification():
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Fetch notification data from the database
            notifications = MakeNotification.query.filter_by(status='Live').all()
            notifications_count = MakeNotification.query.filter_by(status='Live').count()

            session_user_id = session['UserId']
            notification_data_retrieve = MakeNotification.query.all()

            # Check the status of each notification
            if notification_data_retrieve:
                for entry in notification_data_retrieve:
                    if entry.end_date >= date.today():
                        entry.status = "Live"
                    else:
                        entry.status = "Ended"
                db.session.commit()

            if request.method == 'POST':
                message = request.form['message']
                end_date = request.form['end_date']

                if message and end_date:
                    new_notification = MakeNotification(
                        user_id=session_user_id,
                        notification_info=message,
                        end_date=end_date
                    )
                    db.session.add(new_notification)
                    db.session.commit()
                    flash("Notification added successfully.", "success")
                    return redirect('/notification')
                else:
                    flash("Error! Please fill out all fields.", "danger")
            else:
                return render_template('Administrator/notification.html', notification_data_retrieve=notification_data_retrieve, notifications=notifications, notifications_count=notifications_count)
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/admin_dashboard')
    else:
        return render_template('Administrator/login.html')


@app.route('/update_notification/<int:Notification_Id>', methods=['POST'])
def update_notification(Notification_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            if request.method == 'POST':
                # Get the data from the form
                message = request.form['message']
                end_date = request.form['end_date']

                # Retrieve the notification from the database
                get_notification = MakeNotification.query.get(Notification_Id)

                # Update the notification attributes
                get_notification.notification_info = message
                get_notification.end_date = end_date

                # Commit the changes to the database
                db.session.commit()

                notification_data_retrieve = MakeNotification.query.all()
                # Check the status of each notification
                if notification_data_retrieve:
                    for entry in notification_data_retrieve:
                        if entry.end_date >= date.today():
                            entry.status = "Live"
                        else:
                            entry.status = "Ended"
                    db.session.commit()

                flash("Notification updated successfully.", "success")
                return redirect('/notification')
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            db.session.rollback()
            return redirect('/notification')
    else:
        return render_template('Administrator/login.html')


@app.route('/delete_notification/<int:Notification_Id>', methods=['GET'])
def delete_notification(Notification_Id):
    if 'cnic' and 'user_name' and 'rol_name' in session:
        try:
            # Retrieve the notification from the database
            get_notification = MakeNotification.query.get(Notification_Id)

            # Check if the notification exists
            if get_notification:
                # Delete the notification
                db.session.delete(get_notification)
                db.session.commit()

                notification_data_retrieve = MakeNotification.query.all()
                # Check the status of each notification
                if notification_data_retrieve:
                    for entry in notification_data_retrieve:
                        if entry.end_date >= date.today():
                            entry.status = "Live"
                        else:
                            entry.status = "Ended"
                    db.session.commit()

                flash("Notification deleted successfully.", "success")
            else:
                flash("Notification not found.", "danger")

            return redirect('/notification')
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            db.session.rollback()
            return redirect('/notification')
    else:
        return render_template('Administrator/login.html')
