from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.binary import Binary

uri = "mongodb+srv://harish:Vny6pwFrgCtWX65y@funfact.84pnzrc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

# Replace <database> with your actual database name
db = client['funfact']

# Replace <collection> with your actual collection name
collection = db['funfact']

def convert_image_to_binary(image_path):
    with open(image_path, 'rb') as f:
        image_binary = Binary(f.read())
    return image_binary

funfacts = [ 
    {
        "funfact": "Java wasn't always Java! It was originally named Oak, inspired by the tree outside James Gosling's office. But due to trademark issues, it was later changed to Java, a nod to the Indonesian island known for its coffee. ",
        "image_path": "D:/random generator/ffpics/java1.jpg"
    },
    {
        "funfact": "Java's mascot, Duke, is a coffee cup character with sunglasses and a cool attitude. He embodies the energy and fun of the Java community. ",
         "image_path": "D:/random generator/ffpics/java2.jpg"
    },
    {
        "funfact": "The popular game Minecraft was built using Java! This showcases the language's power in creating interactive and engaging experiences.",
         "image_path": "D:/random generator/ffpics/java3.jpg"
    },
    {
        "funfact": "Most Android apps are powered by Java bytecode. So, the next time you use an Android app, remember the Java magic behind it! .",
         "image_path": "D:/random generator/ffpics/java4.jpg"
    },
    {
        "funfact": "Java is downloaded over a BILLION times each year, solidifying its position as one of the most popular programming languages worldwide. ",
        "image_path": "D:/random generator/ffpics/java5.jpg"
    },
    {
        "funfact": "Java's power extends beyond apps and websites. It's even used to power supercomputers, tackling complex scientific simulations! ",
         "image_path": "D:/random generator/ffpics/java6.jpg"
    },
    {
        "funfact": "One of Java's biggest strengths is its portability. \"Write Once, Run Anywhere\" means you can code once and run your program on various platforms.",
         "image_path": "D:/random generator/ffpics/java7.jpg"
    },
    {
        "funfact": "James Gosling, fondly known as the \"father of Java,\" wasn't aiming to create a new language initially. He and his team were working on an interactive TV project and ended up developing Java in the process!",
         "image_path": "D:/random generator/ffpics/java8.jpg"
    },
    {
        "funfact": "Java wasn't just limited to Earth. It played a crucial role in developing software for the Mars Pathfinder mission, helping explore the Red Planet! ",
         "image_path": "D:/random generator/ffpics/java9.jpg"
    },
    {
        "funfact": " Java was originally developed by Sun Microsystems, which later became Oracle. In 2017, Java became open-source, making it freely accessible and even more widely adopted. ",
        "image_path": "D:/random generator/ffpics/java10.jpg"
    }
]


# Insert fun facts into MongoDB
for fact in funfacts:
    image_binary = convert_image_to_binary(fact["image_path"])
    fact["image"] = image_binary
    del fact["image_path"]
    collection.insert_one(fact)

print("fun facts inserted successfully.")
