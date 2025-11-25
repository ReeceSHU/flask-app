import os
import json
from config import db_config
import mysql.connector
from flask import request, render_template, current_app
from . import main

@main.route('/')
def index():
    return render_template('index.html', name='World')

@main.route('/about')
def about():
    return render_template('about.html', title='About', description='This is a simple Flask web app.')

@main.route('/staffdata')
def staffdata():
    json_path = os.path.join(current_app.static_folder, 'data/staff.json')
    with open(json_path) as f:
        staff_data = json.load(f)
    return render_template('from_json.html', staffData=staff_data)

@main.route('/json_filtered', methods=['GET'])
def json_filtered():
    # Load JSON data
    json_path = os.path.join(current_app.static_folder, 'data/staff.json')
    with open(json_path) as f:
        staff_data = json.load(f)

    # Extract departments for the dropdown
    departments = sorted({entry['department'] for entry in staff_data})

    # Get selected department from URL query (GET request)
    selected_department = request.args.get('department')

    # Filter data if a department is selected
    if selected_department:
        staff_data = [
            s for s in staff_data
            if s['department'].lower() == selected_department.lower()
        ]

    return render_template(
        'json_filtered.html',
        staffData=staff_data,
        departments=departments,
        selected=selected_department
    )

@main.route('/db_data')
def db_data():
    # Establish database connection
    conn = mysql.connector.connect(**db_config)
    
    # Create a cursor that returns results as dictionaries
    cursor = conn.cursor(dictionary=True)
    
    # Execute SQL query
    cursor.execute("SELECT * FROM staff")
    
    # Fetch all rows from the query result
    data = cursor.fetchall()
    
    # Clean up resources
    cursor.close()
    conn.close()
    
    # Pass data to template
    return render_template('db_data.html', data=data)