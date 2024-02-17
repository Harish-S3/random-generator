from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
from bson.binary import Binary
from pymongo.server_api import ServerApi
import random, base64, boto3

app = Flask(__name__, template_folder='templates', static_folder='static')

# Your MongoDB Atlas URI
uri = "mongodb+srv://harish:Vny6pwFrgCtWX65y@funfact.84pnzrc.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

# Replace 'funfact' with your actual database name
db = client['funfact']
collection = db['funfact']


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/home')
def home_page():
    # Render the home page
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
    # Fetch random fun fact and image from MongoDB
    random_fun_fact = collection.aggregate([{'$sample': {'size': 1}}]).next()
    fun_fact_text = random_fun_fact['funfact']
    
    # Extract image data from MongoDB
    image_data = random_fun_fact.get('image', None)
    if image_data:
        # If the image data is stored as binary, convert it to base64
        image_base64 = base64.b64encode(image_data).decode('utf-8')
    else:
        # Provide a default image if no image data is found
        image_base64 = None

    return render_template('fun_fact_generator.html', fun_fact=fun_fact_text, image_data=image_base64)

@app.route('/api/fun-facts')
def get_fun_facts_api():
    num_facts = int(request.args.get('num_facts', default=1))
    random_fun_facts = collection.aggregate([{'$sample': {'size': num_facts}}])
    
    # Extract fun facts and images from MongoDB documents
    fun_facts = []
    for fact in random_fun_facts:
        fun_fact = {
            'fun_fact': fact['funfact'],  # Use 'funfact' instead of 'fun_fact'
            'image': base64.b64encode(fact['image']).decode('utf-8')  # Encode image as Base64
        }
        fun_facts.append(fun_fact)

    return jsonify({'fun_facts': fun_facts})



# Initialize S3 client
s3 = boto3.client('s3')

@app.route('/meme-generator')
def meme_generator():
    # List all files in the meme folder
    meme_files = s3.list_objects_v2(Bucket='simphell')['Contents']

    # Select a random meme image
    selected_meme = random.choice(meme_files)['Key']

    # Construct the URL of the selected meme image
    meme_url = s3.generate_presigned_url('get_object', Params={'Bucket': 'simphell', 'Key': selected_meme}, ExpiresIn=3600)

    return render_template('meme_generator.html', meme=dict(src=meme_url))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
