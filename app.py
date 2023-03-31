from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/favorite-course')
def favorite_course():
    return render_template('favorite-course.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        message = request.form['message']
        return render_template('contact.html', first_name=first_name, last_name=last_name, email=email, message=message)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
