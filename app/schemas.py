from flask_marshmallow import Marshmallow
from app.models import *
ma = Marshmallow()

class PlayKeySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PlayKey
        include_relationships = False
        load_instance = True
        include_fk = True

class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        include_relationships = False
        load_instance = True
        include_fk = True

    play_key = ma.Nested(PlayKeySchema)


class AccountInvitationSchema(ma.SQLAlchemyAutoSchema): #  noqa
    class Meta:
        model = AccountInvitation
        include_relationships = True
        load_instance = True
        include_fk = True

    invite_by_user = ma.Nested(AccountSchema)

