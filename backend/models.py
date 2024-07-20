from config import db

class entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(80), unique=False, nullable=False)
    userName = db.Column(db.String(80), unique=False, nullable=True)
    password = db.Column(db.String(80), unique=False, nullable=False)
    
    def to_json(self):
        return {
            "id" : self.id,
            "platform" : self.platform,
            "value":self.userName,
            "status":self.password
        }