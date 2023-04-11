
from flask import Flask, render_template, redirect, request, session
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate, migrate
# from flask_sqlalchemy import SQLAlchemy, model, table

from flask_bcrypt import Bcrypt

# from sqlalchemy import create_engine, Column, Integer, String, MetaData
# # from sqlalchemy.orm import session, sessionmaker, base
# from sqlalchemy.types import Date
# from db import Base, SessionLocal, Calendar, engine

 
app = Flask(__name__)
from sqlalchemy import create_engine, ForeignKey, Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
Base = declarative_base()


class Calendar(Base):
    __tablename__ = "calendar"
    #id = Column('id',Integer, primary_key=True)
    title = Column('title',String(100), primary_key=True, nullable=False)
    start = Column('start',Date, nullable=True)
    end = Column('end',Date, nullable=True)

    def __init__(self,title,start,end):
        #self.id = id
        self.title = title
        self.start = start
        self.end = end

    def __repr__(self):
         return '<Event %>' % self.title
         #return f"({self.id}) {self.title} {self.start} {self.end}"
    
engine = create_engine('sqlite:///test.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session() 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test4.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'SECRETKEYKD4'
# db = SQLAlchemy()
# migrate = Migrate(app, db)
# Bootstrap(app)
# bcrypt = Bcrypt(app)
# db.init_app(app)

# events = [
#      {
#          'title' : 'TestEvent', 
#          'start' : '2023-03-28',
#          'end' : ''
        
#      },
#      {
#          'title' : 'Another TestEvent',
#          'start' : '2023-03-29',
#          'end' : '2023-03-30' 
#      }
#  ]



# class Calendar(db.Model):
#    # __tablename__ = "calendar"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     start = db.Column(db.Date, default=date, nullable=True)
#     end = db.Column(db.Date, default=date, nullable=True)  

#     def __repr__(self):
#         return '<Calendar %r>' % self.id
    
    # def __init__(self,title,start,end):
    #     self.title = title
    #     self.start = start
    #     self.end = end

        # return '<Calendar %r>' % self.id 

@app.route('/') 
def helloworld():
    return 'bad bitch w a sun tan' 

@app.route('/cal', methods=['GET','POST'])
def calendar():
    
    #event = session.get(ident=)
    return render_template("call.html") 


# @app.route('/test', methods=['GET', 'POST'])
# def test():
#     if request.method == "POST":
#            event_title = request.form['title']
#            event_end = request.form['end']
#            event_start = request.form['start']
#            db_event = Calendar(title=event_title,start=event_start, end=event_end)

#            event = {
#                "title": event_title,
#                "start": event_start,
#                "end": event_end
#            }
           
        #    try:  
        #     db.session.add(db_event)
        #     db.session.commit()
        #    except:
        #     return 'Foo'
    # else:
        # db_thing = Calendar.query.order_by(Calendar.title).all() 
        # event = query db and grab all events
    # return render_template("test.html", test=db_event)
 

@app.route('/add', methods=['GET', 'POST'])
def add():
    # if request.method == "GET":
    #      return render_template('add.html', events=events)

    if request.method == "POST":
        events_end = request.form['end']
        events_start = request.form['start']
        events_title = request.form['title']
        new_event = Calendar(title=events_title, start=events_start,end=events_end)
        title = Calendar(title)
        #(1, "Kareem OOO", "04/08/2023", "04/11/2023")
        #(title=events_title, start=events_start,end=events_end )
        # new_start = Calendar(start=event_start)
        # new_end = Calendar(end=event_end)
        


        # if events_end == '':
        #     events_end=events_start
        #     session.add({
        #      'title' : events_title,
        #      'start' : events_start,
        #      'end' : events_end
        #  },
        #  )
        try:  
            session.add(new_event)
            session.commit()
            return redirect('/add')
        except:
            return "there was a problem updating OOO date"
    else:
        event = session.query.__get__(Calendar)

        return render_template('add.html', new_event=event)


if __name__ == '__main__':
    app.run(debug=True)