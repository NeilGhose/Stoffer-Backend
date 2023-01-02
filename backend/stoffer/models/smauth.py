from stoffer.extensions import db


class SMAuth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sm_type = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer)
    refresh_key = db.Column(db.String(255))
    author_key = db.Column(db.String(255))
    active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User %s> <Social Media %s>" % (self.user_id, self.sm_type)