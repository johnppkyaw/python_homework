import sqlite3

def add_publisher(cursor, name):
  try:
    cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
  except sqlite3.IntegrityError:
    print(f"{name} is already in the database.")

def add_magazine(cursor, name, publisher_Id):
  try:
    cursor.execute("INSERT INTO Magazines (name, publisher_Id) VALUES (?,?)", (name, publisher_Id))
  except sqlite3.IntegrityError:
    print(f"{name} is already in the database.")

def add_subscribers(cursor, name, address):
  try:
    cursor.execute("INSERT INTO Subscribers (name, address) VALUES (?,?)", (name, address))
  except sqlite3.IntegrityError:
    print(f"The subscriber {name} with the address ({address}) is already in the database.")

def add_subscriptions(cursor, expiration_date, subscriber_id, magazine_id):
  try:
    cursor.execute("INSERT INTO Subscriptions (expiration_date, subscriber_id, magazine_id) VALUES (?,?,?)", (expiration_date, subscriber_id, magazine_id))
  except sqlite3.IntegrityError:
    print(f"The subscriber with the id {subscriber_id} is already subscribed to the magazine with the id {magazine_id} in the database.")

try:
  #Task 1: Create a New SQLite Database
  #sqlite3 can create a new db file if not exist but not a new folder
  with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
        
    #Task 2: Define Database Structure
    #Publishers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    #Magazines Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines(
        magazine_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
    )
    """)

    #Subscribers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers(
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        CONSTRAINT Uni_Subscriber UNIQUE (name, address)
    )
    """)

    #Subscriptions Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions(
        subscription_id INTEGER PRIMARY KEY,
        expiration_date TEXT NOT NULL,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines(magazine_id)
        CONSTRAINT Uni_Subscription UNIQUE (magazine_id, subscriber_id)
    )
    """)

    print("Database created and connected successfully.")

    #Task 3: Populate Tables with Data
    add_publisher(cursor, 'TechForge Publishing')
    add_publisher(cursor, 'ByteStream Media')
    add_publisher(cursor, 'NextGen Tech Press')

    add_magazine(cursor, "AI News", 1)
    add_magazine(cursor, "CloudTech", 1)
    add_magazine(cursor, "IoT News", 1)
    add_magazine(cursor, "TechHQ", 1)
    add_magazine(cursor, "ByteStream Weekly", 2)
    add_magazine(cursor, "NextGen Innovator", 3)

    add_subscribers(cursor, 'Alice Johnson', '123 Maple Street, Springfield, IL')
    add_subscribers(cursor, 'Alice Johnson', '456 Oak Avenue, Denver, CO')
    add_subscribers(cursor, 'Brian Smith', '456 Oak Avenue, Denver, CO')
    add_subscribers(cursor, 'Carla Martinez', '789 Pine Road, Austin, TX')

    add_subscriptions(cursor, 'Feb 8, 2026', 1, 2)
    add_subscriptions(cursor, 'Feb 8, 2026', 2, 2)
    add_subscriptions(cursor, 'Feb 8, 2026', 3, 1)
  
    conn.commit()

    #Task 4: Write SQL Queries
    #Write a query to retrieve all information from the subscribers table.
    cursor.execute("SELECT * FROM Subscribers")
    subscribers = cursor.fetchall()
    for subscriber in subscribers:
      print(subscriber)
    
    #Write a query to retrieve all magazines sorted by name.
    cursor.execute("SELECT * FROM Magazines ORDER BY name")
    magazines = cursor.fetchall()
    for magazine in magazines:
      print(magazine)
    
    #Write a query to find magazines for a particular publisher, one of the publishers you created. This requires a JOIN.
    cursor.execute("SELECT * FROM Magazines JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id WHERE Publishers.name = 'TechForge Publishing'")
    selected_magazines = cursor.fetchall()
    for magazine in selected_magazines:
      print(magazine)

  conn.close()  

except sqlite3.OperationalError as e:
  print(e) 
