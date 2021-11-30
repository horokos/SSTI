from flask import Flask, request, render_template_string, get_flashed_messages

app = Flask(__name__)

app.config['Flag'] = 'zmhCTF{Im_g000d_@t_c0nfig_h3h3}'

@app.route("/", methods=['GET', 'POST'])
def index():
    name = ""
    if request.method == 'POST':
        name = "Hello " + request.form['name']
    try:
         return render_template_string('''
         Hello, what's your name?
         <form action="{{ url_for('index') }}" method="post">
             <input name="name" size=100>
             <input type="submit">
         </form>
         %s  ''' % name)
    except Exception:
         return render_template_string('''
         Hello, what's your name?
         <form action="{{ url_for('index') }}" method="post">
             <input name="name" size=100>
             <input type="submit">
         </form>
         Coś poszło nie tak :(''')
    #return render_template_string('''
    #        Hello, what's your name? 
    #        <form action="{{ url_for('index') }}" method="post">
    #            <input name="name" size=100>
    #            <input type="submit" value="send">
    #        </form>
    #        %s  ''' % name)


if __name__ == "__main__":
    app.run()
