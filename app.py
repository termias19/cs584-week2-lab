"""
Health Dashboard - Flask Application Starter
Your task: Follow LAB_GUIDE.md to add form handling!
"""

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage for user data (we'll add to this during the lab!)
user_data = {}


@app.route('/')
def index():
    """Home page with time/weekend counter"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    day_num = datetime.now().weekday()  # Monday=0, Sunday=6
    days_to_weekend = 5 - day_num if day_num < 5 else 0
    
    return render_template('index.html', 
                         time=current_time, 
                         days_to_weekend=days_to_weekend,
                         user_data=user_data)


# TODO: Add /submit route here (see LAB_GUIDE.md Part 3)
@app.route('/submit', methods = ['POST'])
def submit():
    #handle form submission
    #Get data
    name = request.form.get('name', '')
    sleep_hours = request.form.get('sleep_hours', '')
    water_glasses = request.form.get('water_glasses', '') 
    exercise_minutes = request.form.get('exercise_minutes', '')

    #store it
    user_data['name'] = name
    user_data['sleep_hours'] = sleep_hours
    user_data['water_glasses'] = water_glasses
    user_data['exercise_minutes'] = exercise_minutes

    #generate feedback
    #sleep feedback
    try:
        hours = float(sleep_hours)
        if hours < 7:
            user_data['feedback'] = "⚠️ Try to get more sleep!"
            user_data['sleep_class'] = "warn"
        else:
            user_data['feedback'] = "✅ Great sleep!"
            user_data['sleep_class'] = "good"
    except ValueError:
        user_data['feedback'] = "Please enter valid hours."
        user_data['sleep_class'] = "bad"

    #water feedback
    try:
        water = int(water_glasses)
        if water < 8:
            user_data['water_feedback'] = "💧 Try to drink more water (goal: 8 glasses)."
            user_data['water_feedback'] = "warn"
        else:
            user_data['water_feedback'] = "💧 Great hydration today!"
            user_data['water_feedback'] = "good"
    except ValueError:
        user_data['water_feedback'] = "Enter a valid number of glasses."
        user_data['water_feedback'] = "bad"
    #Exercise Feedback
    try:
        ex = int(exercise_minutes)  
        if ex < 20:
            user_data['exercise_feedback'] = "🏃 Try to get at least 20 minutes of movement today."
            user_data['exercise_feedback'] = "warn"
        else:
            user_data['exercise_feedback'] = "🏃 Nice! You got solid movement in today."
            user_data['exercise_feedback'] = "good"
    except ValueError:
        user_data['exercise_feedback'] = "Enter a valid number of exercise minutes."
        user_data['exercise_feedback'] = "bad"


    print("DEBUG - Data stored:", user_data) # <-- Show your collected variable in terminal.
    # ... it's being stored as an in-memory Python dict... it's not going to an API or database yet! We'll work on that in a future lecture.

    # Redirect back to home
    return redirect(url_for('index'))

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True) 
=======
    app.run(debug=True) 
>>>>>>> 119ba25 (Initial Lab 2 health dashboard)
