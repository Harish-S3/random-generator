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


funfacts =[
    {
        "funfact": "PHP wasn't initially designed as a general-purpose language. In 1994, Rasmus Lerdorf created it to manage his personal website, calling it 'Personal Home Page Tools.'",
        "image_path": "D:/random generator/ffpics/php1.jpg"
    },
    {
        "funfact": "The iconic PHP elephant logo was inspired by a children's book 'The Elephants Who Learned to Swim,' specifically, an illustration of an elephant holding a paintbrush!",
         "image_path": "D:/random generator/ffpics/php2.jpeg"
    },
    {
        "funfact": "Over 70% of all active websites use PHP due to its ease of use and integration with popular CMS platforms like WordPress and Drupal.",
         "image_path": "D:/random generator/ffpics/php3.jpg"
    },
    {
        "funfact": "PHP is known for its fast parsing and execution speed, making it suitable for server-side web development tasks.",
         "image_path": "D:/random generator/ffpics/php4.jpg"
    },
    {
        "funfact": "PHP stands for 'Hypertext Preprocessor,' a recursive acronym that highlights its primary function of processing hypertext or dynamic web content.",
        "image_path": "D:/random generator/ffpics/php5.jpg"
    },
    {
        "funfact": "The PHP community actively maintains a vast repository of open-source libraries and frameworks, contributing to its extensive ecosystem.",
         "image_path": "D:/random generator/ffpics/php6.jpg"
    },
    {
        "funfact": "Facebook was originally built using PHP, and the language played a crucial role in the early development of the social media platform.",
         "image_path": "D:/random generator/ffpics/php7.jpg"
    },
    {
        "funfact": "PHP's flexibility allows developers to seamlessly integrate it with various databases, including MySQL, PostgreSQL, MongoDB, and more.",
         "image_path": "D:/random generator/ffpics/php8.jpeg"
    },
    {
        "funfact": "Zend Engine, the core of PHP, underwent significant improvements over the years, enhancing the language's performance and features.",
         "image_path": "D:/random generator/ffpics/php9.jpg"
    },
    {
        "funfact": "PHP's syntax draws inspiration from various programming languages, including C, Perl, and Java, contributing to its familiar and intuitive structure.",
        "image_path": "D:/random generator/ffpics/php10.jpg"
    },
	{
        "funfact": "Python was created by Guido van Rossum as a hobby project in December 1989.",
        "image_path": "D:/random generator/ffpics/py1.jpg"
    },
    {
        "funfact": "The name \"Python\" comes from the British comedy group \"Monty Python's Flying Circus,\" which was one of Guido's favorite shows.",
         "image_path": "D:/random generator/ffpics/py2.jpg"
    },
    {
        "funfact": "Python is slower than some other programming languages, like C and Java, because it is an interpreted language.",
         "image_path": "D:/random generator/ffpics/py3.jpg"
    },
    {
        "funfact": "Python is used by some of the biggest tech companies in the world, including Google, Facebook, and Netflix.",
         "image_path": "D:/random generator/ffpics/py4.jpg"
    },
    {
        "funfact": "Python is a general-purpose language that can be used in a wide range of scenarios, including web development, artificial intelligence, machine learning, data analytics, and more.",
        "image_path": "D:/random generator/ffpics/py5.jpg"
    },
    {
        "funfact": "Python has a unique \"slice\" operator that allows you to extract parts of a list, tuple, or string using a simple and intuitive syntax.",
         "image_path": "D:/random generator/ffpics/py6.jpg"
    },
    {
        "funfact": "Python is a great language for beginners due to its simplicity and readability, and has been used in primary schools to teach programming concepts to young students.",
         "image_path": "D:/random generator/ffpics/py7.jpg"
    },
    {
        "funfact": "Python's \"is\" keyword checks if two variables refer to the same object, while \"==\" checks if two variables have the same value.",
         "image_path": "D:/random generator/ffpics/py8.jpeg"
    },
    {
        "funfact": "Python's pass keyword is a placeholder that allows you to leave a block of code empty while still having valid syntax.",
         "image_path": "D:/random generator/ffpics/py9.jpg"
    },
    {
        "funfact": "Python has a built-in module called antigravity that opens a webpage with a comic about the antigravity module when imported.",
        "image_path": "D:/random generator/ffpics/py10.jpg"
    },
	  {
        "funfact": "The first computer program was written by Ada Lovelace in 1843 for Charles Babbage's proposed mechanical general-purpose computer, the Analytical Engine.",
        "image_path": "D:/random generator/ffpics/pro1.jpg"
    },
    {
        "funfact": "The first high-level programming language was developed in the 1950s. It was called FORTRAN (Formula Translation), and it was designed by John Backus for scientific and engineering calculations.",
         "image_path": "D:/random generator/ffpics/pro2.jpg"
    },
    {
        "funfact": "The most popular programming language is JavaScript, which is used by 64.9% of all websites.",
         "image_path": "D:/random generator/ffpics/pro3.jpg"
    },
    {
        "funfact": "The longest programming language is Whitespace, which is a language that uses only whitespace characters (spaces, tabs, and newlines) to encode its programs.",
         "image_path": "D:/random generator/ffpics/pro4.jpg"
    },
    {
        "funfact": "The first video game was created by a programmer named Willy Higinbotham in 1958. It was called \"Tennis for Two,\" and it was a simple tennis simulation that ran on an oscilloscope.",
        "image_path": "D:/random generator/ffpics/pro5.jpg"
    },
    {
        "funfact": "The first computer virus was created in 1982 by a programmer named Rich Skrenta. It was called \"Elk Cloner,\" and it infected Apple II computers by spreading through floppy disks.",
         "image_path": "D:/random generator/ffpics/pro6.jpg"
    },
    {
        "funfact": "There are over 700 programming languages in existence..",
         "image_path": "D:/random generator/ffpics/pro7.jpg"
    },
    {
        "funfact": "Grace Hopper and her team coined the term \"debugging\" after finding a moth inside a computer relay.",
         "image_path": "D:/random generator/ffpics/pro8.jpg"
    },
    {
        "funfact": "The first video game was created by a programmer named Willy Higinbotham in 1958. The game, called \"Tennis for Two,\" was an early computer simulation of a tennis match.",
         "image_path": "D:/random generator/ffpics/pro9.jpg"
    },
    {
        "funfact": " There are 3 very different types of Hackers, one being malicious, the other benevolent, and the last somewhere in between the two",
        "image_path": "D:/random generator/ffpics/pro10.jpg"
    },
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
    },
	{
        "funfact": "90% of the world's data was created in the last two years. ",
        "image_path": "D:/random generator/ffpics/cs1.jpeg"
    },
	{
        "funfact": " The global artificial intelligence (AI) market is expected to reach $126 billion by 2025.",
        "image_path": "D:/random generator/ffpics/cs2.jpg"
    },
	{
        "funfact": " Cybercrime is expected to cost businesses $10.5 trillion annually by 2025.",
        "image_path": "D:/random generator/ffpics/cs3.jpeg"
    },
	{
        "funfact": "The world's first electronic computer, the Colossus, was built in 1943. ",
        "image_path": "D:/random generator/ffpics/cs4.jpg"
    },
	{
        "funfact": " The first computer mouse was invented in 1964 by Douglas Engelbart.",
        "image_path": "D:/random generator/ffpics/cs5.jpeg"
    },
	{
        "funfact": " The first webcam was invented at the University of Cambridge to monitor the coffee pot in the computer science department.",
        "image_path": "D:/random generator/ffpics/cs6.jpg"
    },
	{
        "funfact": " The first website was created in 1991 by Tim Berners-Lee.",
        "image_path": "D:/random generator/ffpics/cs7.jpeg"
    },
	{
        "funfact": " The first computer network was developed in the late 1960s and was called ARPANET.",
        "image_path": "D:/random generator/ffpics/cs8.jpeg"
    },
	{
        "funfact": "The first email was sent in 1971 by Ray Tomlinson. ",
        "image_path": "D:/random generator/ffpics/cs9.jpeg"
    },
	{
        "funfact": "The first computer, known as the ENIAC, weighed 30 tons and took up an entire room. ",
        "image_path": "D:/random generator/ffpics/cs10.jpeg"
    }
]


# Insert fun facts into MongoDB
for fact in funfacts:
    image_binary = convert_image_to_binary(fact["image_path"])
    fact["image"] = image_binary
    del fact["image_path"]
    collection.insert_one(fact)

print("fun facts inserted successfully.")
