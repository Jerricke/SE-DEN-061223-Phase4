#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models
from app import app
from models import db, Production

# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

with app.app_context():


# 8.✅ Create a query to delete all existing records from Production    
   Production.query.delete()

   productions = []
# 9.✅ Create some seeds for production and commit them to the database. 
   p1 = Production(title="Hamlet", genre="Drama", director="Bill Shakespeare",description="The tragedy of Hamlet, Prince of Denmark",budget="100000.00", image="https://upload.wikimedia.org/wikipedia/commons/6/6a/Edwin_Booth_Hamlet_1870.jpg", ongoing=True)

   productions.append(p1)

   p2 = Production(title="Cats", genre="Muscial", director="Andrew Lloyd Webber",description="Cats and dogs sing",budget="200000.00", image="https://upload.wikimedia.org/wikipedia/en/3/3e/CatsMusicalLogo.jpg", ongoing=True)

   productions.append(p2)

   p3 = Production(title="carmen", genre="Opera", director="Georges Bizet",description="Set in southern Spain this is the story of the downfall of Don José, a naïve soldier who is seduced by the wiles of the fiery and beautiful Carmen.",budget="200000.00", image='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Prudent-Louis_Leray_-_Poster_for_the_premi%C3%A8re_of_Georges_Bizet%27s_Carmen.jpg/300px-Prudent-Louis_Leray_-_Poster_for_the_premi%C3%A8re_of_Georges_Bizet%27s_Carmen.jpg', ongoing=False)

   productions.append(p3)

   p4 = Production(title="Hamilton", genre="Musical", director="Lin-Manuel Miranda",description="An American Musical is a sung-and-rapped-through musical by Lin-Manuel Miranda. It tells the story of American Founding Father Alexander Hamilton.",budget="400000.00", image='https://upload.wikimedia.org/wikipedia/en/thumb/8/83/Hamilton-poster.jpg/220px-Hamilton-poster.jpg', ongoing=False)

   productions.append(p4)

   db.session.add_all(productions)
   db.session.commit()

# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  
    
    