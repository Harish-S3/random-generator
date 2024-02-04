from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://harish:Vny6pwFrgCtWX65y@funfact.84pnzrc.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))

# Replace <database> with your actual database name
db = client['funfact']

# Replace <collection> with your actual collection name
collection = db['funfact']

fun_facts = [
    { "fun_fact": "The concept of a 'bit' (binary digit) was introduced by Claude Shannon in his master's thesis at MIT in 1937." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The term 'bug' in computer science originated in 1947 when Grace Hopper found an actual moth causing problems in the Harvard Mark II computer." },
    { "fun_fact": "One of the earliest computer programs was written by Ada Lovelace for Charles Babbage's Analytical Engine, making her the first computer programmer." },
    { "fun_fact": "The first computer virus for Microsoft DOS was created in 1986. It was called 'Brain' and spread through infected floppy disks." },
    { "fun_fact": "The world's first computer game was 'Spacewar!' created in 1962 by Steve Russell and others at MIT." },
    { "fun_fact": "JavaScript, one of the most widely used programming languages today, was created in just 10 days by Brendan Eich in 1995." },
    { "fun_fact": "The first computer to defeat a world chess champion was IBM's Deep Blue, which defeated Garry Kasparov in 1997." },
    { "fun_fact": "The world's first website went live on August 6, 1991. It was created by Tim Berners-Lee and provided information about the World Wide Web project." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The QWERTY keyboard layout, designed in 1873, has remained the standard layout for keyboards ever since." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The first computer virus was created in 1983 and was called the 'Elk Cloner'." },
    { "fun_fact": "The world's first computer to use Wi-Fi was the Apple iBook in 1999." },
    { "fun_fact": "The Antikythera mechanism, an ancient Greek analog device, is considered the world's first computer, used to predict astronomical positions and eclipses." },
    { "fun_fact": "The world's first computer password was 'login.' It was implemented on the Compatible Time-Sharing System (CTSS) at MIT in the early 1960s." },
    { "fun_fact": "The first computer to use a floppy disk was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a hard drive was the IBM 350 in 1956." },
    { "fun_fact": "The first computer to use a keyboard was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a touchscreen was the HP-150 in 1983." },
    { "fun_fact": "The world's first computer virus was created in 1983. It was called the 'Elk Cloner' and infected Apple II computers through infected floppy disks." },
    { "fun_fact": "The first domain name ever registered was 'symbolics.com' on March 15, 1985." },
    { "fun_fact": "The most widely used programming language today, JavaScript, was created in just 10 days by Brendan Eich in 1995." },
    { "fun_fact": "The first computer to defeat a world chess champion was IBM's Deep Blue, which defeated Garry Kasparov in 1997." },
    { "fun_fact": "The world's first website went live on August 6, 1991. It was created by Tim Berners-Lee and provided information about the World Wide Web project." },
    { "fun_fact": "The world's first computer password was 'login.' It was implemented on the Compatible Time-Sharing System (CTSS) at MIT in the early 1960s." },
    { "fun_fact": "The first computer virus was created in 1983 and was called the 'Elk Cloner'." },
    { "fun_fact": "The first computer mouse was made of wood." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The first computer to use a floppy disk was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a hard drive was the IBM 350 in 1956." },
    { "fun_fact": "The first computer to use a keyboard was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a mouse was the Xerox Alto in 1973." },
    { "fun_fact": "The first computer to use a touchscreen was the HP-150 in 1983." },
    { "fun_fact": "The first computer to use Wi-Fi was the Apple iBook in 1999." },
    { "fun_fact": "The term 'bug' in computer science originated in 1947 when Grace Hopper found an actual moth causing problems in the Harvard Mark II computer." },
    { "fun_fact": "One of the earliest computer programs was written by Ada Lovelace for Charles Babbage's Analytical Engine, making her the first computer programmer." },
    { "fun_fact": "The concept of a 'bit' was introduced by Claude Shannon in his master's thesis at MIT in 1937." },
    { "fun_fact": "The first computer virus for Microsoft DOS was created in 1986. It was called 'Brain' and spread through infected floppy disks." },
    { "fun_fact": "The first electronic computer, ENIAC, weighed more than 27 tons and took up 1,800 square feet of space." },
    { "fun_fact": "The world's first computer, the Antikythera mechanism, was an ancient Greek analog device used to predict astronomical positions and eclipses." },
    { "fun_fact": "The term 'software bug' was coined by Grace Hopper in the 1940s when an actual moth caused a malfunction in the Harvard Mark II computer." },
    { "fun_fact": "The world's first computer game was 'Spacewar!' created in 1962 by Steve Russell and others at MIT." },
    { "fun_fact": "The most widely used programming language today, JavaScript, was created in just 10 days by Brendan Eich in 1995." },
    { "fun_fact": "The first computer to defeat a world chess champion was IBM's Deep Blue, which defeated Garry Kasparov in 1997." },
    { "fun_fact": "The world's first website went live on August 6, 1991. It was created by Tim Berners-Lee and provided information about the World Wide Web project." },
    { "fun_fact": "The world's first computer password was 'login.' It was implemented on the Compatible Time-Sharing System (CTSS) at MIT in the early 1960s." },
    { "fun_fact": "The first computer virus was created in 1983 and was called the 'Elk Cloner'." },
    { "fun_fact": "The first computer mouse was made of wood." },
    { "fun_fact": "The first computer to defeat a human at chess was IBM's Deep Blue in 1997." },
    { "fun_fact": "The first emoji was created in 1999 by Shigetaka Kurita." },
    { "fun_fact": "The first computer programming language was created by Ada Lovelace in the 1800s." },
    { "fun_fact": "The first computer game was created in 1947 and was called 'Cathode Ray Tube Amusement Device'." },
    { "fun_fact": "The first computer to be sold was the Kenbak-1, which was released in 1971." },
    { "fun_fact": "The first computer with a graphical user interface was the Xerox Alto, which was released in 1973." },
    { "fun_fact": "The first computer virus to infect a computer was the 'Creeper' virus in 1971." },
    { "fun_fact": "The first computer to use a floppy disk was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a hard drive was the IBM 350 in 1956." },
    { "fun_fact": "The first computer to use a keyboard was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a mouse was the Xerox Alto in 1973." },
    { "fun_fact": "The first computer to use a touchscreen was the HP-150 in 1983." },
    { "fun_fact": "The first computer to use Wi-Fi was the Apple iBook in 1999." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The world's first computer virus was created in 1983. It was called the 'Elk Cloner' and infected Apple II computers through infected floppy disks." },
    { "fun_fact": "The first domain name ever registered was 'symbolics.com' on March 15, 1985." },
    { "fun_fact": "The QWERTY keyboard layout was designed in 1873 and has remained the standard layout for keyboards ever since." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The concept of a 'bit' was introduced by Claude Shannon in his master's thesis at MIT in 1937." },
    { "fun_fact": "The first computer virus for Microsoft DOS was created in 1986. It was called 'Brain' and spread through infected floppy disks." },
    { "fun_fact": "The first electronic computer, ENIAC, weighed more than 27 tons and took up 1,800 square feet of space." },
    { "fun_fact": "The world's first computer, the Antikythera mechanism, was an ancient Greek analog device used to predict astronomical positions and eclipses." },
    { "fun_fact": "The term 'software bug' was coined by Grace Hopper in the 1940s when an actual moth caused a malfunction in the Harvard Mark II computer." },
    { "fun_fact": "The world's first computer game was 'Spacewar!' created in 1962 by Steve Russell and others at MIT." },
    { "fun_fact": "The most widely used programming language today, JavaScript, was created in just 10 days by Brendan Eich in 1995." },
    { "fun_fact": "The first computer to defeat a world chess champion was IBM's Deep Blue, which defeated Garry Kasparov in 1997." },
    { "fun_fact": "The world's first website went live on August 6, 1991. It was created by Tim Berners-Lee and provided information about the World Wide Web project." },
    { "fun_fact": "The world's first computer password was 'login.' It was implemented on the Compatible Time-Sharing System (CTSS) at MIT in the early 1960s." },
    { "fun_fact": "The first computer virus was created in 1983 and was called the 'Elk Cloner'." },
    { "fun_fact": "The first computer mouse was made of wood." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The first computer to use a floppy disk was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a hard drive was the IBM 350 in 1956." },
    { "fun_fact": "The first computer to use a keyboard was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a mouse was the Xerox Alto in 1973." },
    { "fun_fact": "The first computer to use a touchscreen was the HP-150 in 1983." },
    { "fun_fact": "The first computer to use Wi-Fi was the Apple iBook in 1999." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The world's first computer virus was created in 1983. It was called the 'Elk Cloner' and infected Apple II computers through infected floppy disks." },
    { "fun_fact": "The first domain name ever registered was 'symbolics.com' on March 15, 1985." },
    { "fun_fact": "The QWERTY keyboard layout was designed in 1873 and has remained the standard layout for keyboards ever since." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The first computer to use a floppy disk was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a hard drive was the IBM 350 in 1956." },
    { "fun_fact": "The first computer to use a keyboard was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a mouse was the Xerox Alto in 1973." },
    { "fun_fact": "The first computer to use a touchscreen was the HP-150 in 1983." },
    { "fun_fact": "The first computer to use Wi-Fi was the Apple iBook in 1999." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The world's first computer virus was created in 1983. It was called the 'Elk Cloner' and infected Apple II computers through infected floppy disks." },
    { "fun_fact": "The first domain name ever registered was 'symbolics.com' on March 15, 1985." },
    { "fun_fact": "The QWERTY keyboard layout was designed in 1873 and has remained the standard layout for keyboards ever since." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The concept of a 'bit' was introduced by Claude Shannon in his master's thesis at MIT in 1937." },
    { "fun_fact": "The first computer virus for Microsoft DOS was created in 1986. It was called 'Brain' and spread through infected floppy disks." },
    { "fun_fact": "The first electronic computer, ENIAC, weighed more than 27 tons and took up 1,800 square feet of space." },
    { "fun_fact": "The world's first computer, the Antikythera mechanism, was an ancient Greek analog device used to predict astronomical positions and eclipses." },
    { "fun_fact": "The term 'software bug' was coined by Grace Hopper in the 1940s when an actual moth caused a malfunction in the Harvard Mark II computer." },
    { "fun_fact": "The world's first computer game was 'Spacewar!' created in 1962 by Steve Russell and others at MIT." },
    { "fun_fact": "The most widely used programming language today, JavaScript, was created in just 10 days by Brendan Eich in 1995." },
    { "fun_fact": "The first computer to defeat a world chess champion was IBM's Deep Blue, which defeated Garry Kasparov in 1997." },
    { "fun_fact": "The world's first website went live on August 6, 1991. It was created by Tim Berners-Lee and provided information about the World Wide Web project." },
    { "fun_fact": "The world's first computer password was 'login.' It was implemented on the Compatible Time-Sharing System (CTSS) at MIT in the early 1960s." },
    { "fun_fact": "The first computer virus was created in 1983 and was called the 'Elk Cloner'." },
    { "fun_fact": "The first computer mouse was made of wood." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The first computer to use a floppy disk was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a hard drive was the IBM 350 in 1956." },
    { "fun_fact": "The first computer to use a keyboard was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a mouse was the Xerox Alto in 1973." },
    { "fun_fact": "The first computer to use a touchscreen was the HP-150 in 1983." },
    { "fun_fact": "The first computer to use Wi-Fi was the Apple iBook in 1999." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The world's first computer virus was created in 1983. It was called the 'Elk Cloner' and infected Apple II computers through infected floppy disks." },
    { "fun_fact": "The first domain name ever registered was 'symbolics.com' on March 15, 1985." },
    { "fun_fact": "The QWERTY keyboard layout was designed in 1873 and has remained the standard layout for keyboards ever since." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The concept of a 'bit' was introduced by Claude Shannon in his master's thesis at MIT in 1937." },
    { "fun_fact": "The first computer virus for Microsoft DOS was created in 1986. It was called 'Brain' and spread through infected floppy disks." },
    { "fun_fact": "The first electronic computer, ENIAC, weighed more than 27 tons and took up 1,800 square feet of space." },
    { "fun_fact": "The world's first computer, the Antikythera mechanism, was an ancient Greek analog device used to predict astronomical positions and eclipses." },
    { "fun_fact": "The term 'software bug' was coined by Grace Hopper in the 1940s when an actual moth caused a malfunction in the Harvard Mark II computer." },
    { "fun_fact": "The world's first computer game was 'Spacewar!' created in 1962 by Steve Russell and others at MIT." },
    { "fun_fact": "The most widely used programming language today, JavaScript, was created in just 10 days by Brendan Eich in 1995." },
    { "fun_fact": "The first computer to defeat a world chess champion was IBM's Deep Blue, which defeated Garry Kasparov in 1997." },
    { "fun_fact": "The world's first website went live on August 6, 1991. It was created by Tim Berners-Lee and provided information about the World Wide Web project." },
    { "fun_fact": "The world's first computer password was 'login.' It was implemented on the Compatible Time-Sharing System (CTSS) at MIT in the early 1960s." },
    { "fun_fact": "The first computer virus was created in 1983 and was called the 'Elk Cloner'." },
    { "fun_fact": "The first computer mouse was made of wood." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The first computer to use a floppy disk was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a hard drive was the IBM 350 in 1956." },
    { "fun_fact": "The first computer to use a keyboard was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a mouse was the Xerox Alto in 1973." },
    { "fun_fact": "The first computer to use a touchscreen was the HP-150 in 1983." },
    { "fun_fact": "The first computer to use Wi-Fi was the Apple iBook in 1999." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The world's first computer virus was created in 1983. It was called the 'Elk Cloner' and infected Apple II computers through infected floppy disks." },
    { "fun_fact": "The first domain name ever registered was 'symbolics.com' on March 15, 1985." },
    { "fun_fact": "The QWERTY keyboard layout was designed in 1873 and has remained the standard layout for keyboards ever since." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The concept of a 'bit' was introduced by Claude Shannon in his master's thesis at MIT in 1937." },
    { "fun_fact": "The first computer virus for Microsoft DOS was created in 1986. It was called 'Brain' and spread through infected floppy disks." },
    { "fun_fact": "The first electronic computer, ENIAC, weighed more than 27 tons and took up 1,800 square feet of space." },
    { "fun_fact": "The world's first computer, the Antikythera mechanism, was an ancient Greek analog device used to predict astronomical positions and eclipses." },
    { "fun_fact": "The term 'software bug' was coined by Grace Hopper in the 1940s when an actual moth caused a malfunction in the Harvard Mark II computer." },
    { "fun_fact": "The world's first computer game was 'Spacewar!' created in 1962 by Steve Russell and others at MIT." },
    { "fun_fact": "The most widely used programming language today, JavaScript, was created in just 10 days by Brendan Eich in 1995." },
    { "fun_fact": "The first computer to defeat a world chess champion was IBM's Deep Blue, which defeated Garry Kasparov in 1997." },
    { "fun_fact": "The world's first website went live on August 6, 1991. It was created by Tim Berners-Lee and provided information about the World Wide Web project." },
    { "fun_fact": "The world's first computer password was 'login.' It was implemented on the Compatible Time-Sharing System (CTSS) at MIT in the early 1960s." },
    { "fun_fact": "The first computer virus was created in 1983 and was called the 'Elk Cloner'." },
    { "fun_fact": "The first computer mouse was made of wood." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." },
    { "fun_fact": "The first computer to use a floppy disk was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a hard drive was the IBM 350 in 1956." },
    { "fun_fact": "The first computer to use a keyboard was the IBM 704 in 1956." },
    { "fun_fact": "The first computer to use a mouse was the Xerox Alto in 1973." },
    { "fun_fact": "The first computer to use a touchscreen was the HP-150 in 1983." },
    { "fun_fact": "The first computer to use Wi-Fi was the Apple iBook in 1999." },
    { "fun_fact": "The world's first computer programmer was Ada Lovelace, who wrote the first algorithm for Charles Babbage's Analytical Engine in the mid-1800s." },
    { "fun_fact": "The world's first computer virus was created in 1983. It was called the 'Elk Cloner' and infected Apple II computers through infected floppy disks." },
    { "fun_fact": "The first domain name ever registered was 'symbolics.com' on March 15, 1985." },
    { "fun_fact": "The QWERTY keyboard layout was designed in 1873 and has remained the standard layout for keyboards ever since." },
    { "fun_fact": "The average computer mouse travels over 1.5 miles (2.4 kilometers) on a weekly basis." },
    { "fun_fact": "One gigabyte (GB) of storage in the 1950s cost approximately $10 million. Today, it's incredibly cheap and widely available." },
    { "fun_fact": "The first computer mouse was made of wood and had two wheels. It was invented by Douglas Engelbart in 1964." },
    { "fun_fact": "The term 'hack' originated from MIT's Tech Model Railroad Club (TMRC), where it referred to creative tinkering and problem-solving." }
]

# Insert the documents into the collection
result = collection.insert_many(fun_facts)

# Print the inserted document IDs
print(result.inserted_ids)

# Close the MongoDB connection
client.close()

