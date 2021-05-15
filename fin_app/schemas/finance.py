from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from fin_app.database.models import Finance


class FinanceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Finance
        load_instance = True
        include_fk = True
    user = Nested('UserSchema', exclude=('finance',))
