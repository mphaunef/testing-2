from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.
    # Ticket to Ride| a cross-country train adventure
    
    # In case this is run more than once, empty out existing data
    Game.query.delete()

    # Add sample game data
    g1 = Game(name='Monopoly', description='Make your friends very angry')
    g2 = Game(name='Trouble', description='Chaotic bubble popping')
    g3 = Game(name='Life', description='Pretend you will be successful in the future')

    db.session.add_all([g1, g2, g3])
    db.session.commit()


if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    print("Connected to DB.")
