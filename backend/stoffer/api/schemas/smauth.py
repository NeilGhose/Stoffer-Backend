from stoffer.models import SMAuth
from stoffer.extensions import ma, db


class SMAuthSchema(ma.SQLAlchemyAutoSchema):
    id = ma.Int(dump_only=True)
    class Meta:
        model = SMAuth
        sqla_session = db.session
        load_instance = True
