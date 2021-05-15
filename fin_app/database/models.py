from datetime import date

from fin_app import db


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    transactions = db.relationship('Finance', backref='user',
                                   lazy='joined')

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return f'User(Name:{self.first_name} Surname: {self.last_name}, ' \
               f' Email: {self.email})'


class Finance(db.Model):
    __tablename__ = 'finance'

    trans_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'),
                        nullable=False)
    sum_of_trans = db.Column(db.Float(150), nullable=False)
    trans_date = db.Column(db.Date, nullable=False,
                           default=date.today())

    def __init__(self, user_id, sum_of_trans, trans_date=date.today()):
        self.user_id = user_id
        self.sum_of_trans = sum_of_trans
        self.trans_date = trans_date

    def __repr__(self):
        return f'Transaction (User_id: {self.user_id}, Trans_id: ' \
               f'{self.trans_id}, Sum: {self.sum_of_trans}, Date:' \
               f' {self.trans_date})'
