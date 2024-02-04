from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import os,random

app = Flask(__name__, template_folder='templates', static_folder='static')

# Your MongoDB Atlas URI
uri = "mongodb+srv://harish:Vny6pwFrgCtWX65y@funfact.84pnzrc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

# Replace 'funfact' with your actual database name
db = client['funfact']
collection = db['funfact']

@app.route('/', endpoint='home')
def home():
    return render_template('home.html')

@app.route('/random', methods=['GET', 'POST'])
def random_number_generator():
    if request.method == 'POST':
        min_value = int(request.form.get('min', default=1))
        max_value = int(request.form.get('max', default=100))
        random_number = random.randint(min_value, max_value)

        return render_template('random_number_generator.html', random_number=random_number, min_value=min_value, max_value=max_value)
    else:
        return render_template('random_number_generator.html')

@app.route('/fun-fact-generator')
def fun_fact_generator():
    # Fetch random fun fact from MongoDB
    random_fun_fact = collection.aggregate([{'$sample': {'size': 1}}]).next()
    fun_fact_text = random_fun_fact['fun_fact']

    return render_template('fun_fact_generator.html', fun_fact=fun_fact_text)

# Add the /api/fun-facts route
@app.route('/api/fun-facts')
def get_fun_facts_api():
    random_fun_fact = collection.aggregate([{'$sample': {'size': 1}}]).next()
    if random_fun_fact:
        return jsonify({'fun_fact': random_fun_fact['fun_fact']})
    else:
        return jsonify({'fun_fact': None})
    
meme_folder = os.path.join(os.path.dirname(__file__), 'static', 'memes')
meme_files = [f for f in os.listdir(meme_folder) if os.path.isfile(os.path.join(meme_folder, f))]


@app.route('/meme-generator')
def meme_generator():
    selected_meme = random.choice(meme_files)
    return render_template('meme_generator.html', meme=dict(src=selected_meme))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
