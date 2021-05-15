from flask_restful import Resource, request
from marshmallow import ValidationError
from fin_app import db, api
from fin_app.database import models
from fin_app.schemas.finance import FinanceSchema
from fin_app.schemas.user import UserSchema


class UserApi(Resource):
    user_schema = UserSchema()

    def get(self, user_id=None):
        """ Function for getting information about user """
        if not user_id:
            users = db.session.query(models.User).all()
            return self.user_schema.dump(users, many=True), 200
        user = db.session.query(models.User).filter_by(user_id=user_id).first()
        if not user:
            return 'User does not exist yet', 404
        return self.user_schema.dump(user), 200

    def post(self):
        """ Function for creating a new user"""
        try:
            user = self.user_schema.load(request.json, session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(user)
        db.session.commit()
        return self.user_schema.dump(user), 200

    def put(self, user_id):
        """ Function for updating information about an existing user """
        user = db.session.query(models.User).filtered_by(
            user_id=user_id).first()
        if not user:
            return {'message': 'Wrong data'}, 400
        try:
            user = self.user_schema.load(request.json, instance=user,
                                         session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(user)
        db.session.commit()
        return self.user_schema.dump(user), 200

    def delete(self, user_id):
        """ Function to completely delete information about user"""
        user = db.session.query(models.User).filter_by(user_id=user_id).first()
        if not user:
            return 'User does not exist yet', 404
        db.session.delete(user)
        db.session.commit()
        return 'User deleted successfully', 200


class FinanceApi(Resource):
    finance_schema = FinanceSchema()

    def get(self, user_id=None):
        """ Function for getting information about transaction """
        user_json = request.json
        budget = user_json.get('budget')
        sort = user_json.get('sort')
        day_s = user_json.get('day_start')
        day_e = user_json.get('day_end')
        one_day_stat = user_json.get('one_day_stat')
        if one_day_stat and sort:
            try:
                user_query = db.session.query(models.Finance).filter(
                    models.Finance.user_id == user_id).order_by(
                    models.Finance.trans_date.asc()).all()
                return self.finance_schema.dump(user_query)
            except ValidationError:
                return 'Transaction does not exist', 404

        elif budget and sort:
            try:
                user_query = db.session.query(models.Finance).filter(
                    models.Finance.user_id == user_id).order_by(
                    models.Finance.sum_of_trans.asc()).all()
                return self.finance_schema.dump(user_query)
            except ValidationError:
                return 'Transaction does not exist', 404

        elif one_day_stat and budget:
            try:
                user_query = db.session.query(models.Finance).filter(
                    models.Finance.user_id == user_id, models.Finance.trans_date
                    == one_day_stat).all()
                plus = sum(
                    [user_query[s].sum_of_trans for s in
                     range(0, len(user_query))
                     if user_query[s].sum_of_trans > 0])
                minus = sum(
                    [user_query[s].sum_of_trans for s in
                     range(0, len(user_query))
                     if user_query[s].sum_of_trans < 0])
                return f'Day: {one_day_stat}, "+": {plus}, "-":{minus}'
            except ValidationError:
                return 'Transaction does not exist', 404

        elif day_s and day_e:
            try:
                user_query = db.session.query(models.Finance).filter(
                    models.Finance.user_id == user_id).filter(
                    models.Finance.trans_date.in_([day_s, day_e])).all()
                return self.finance_schema.dump(user_query)
            except ValidationError:
                return 'Transaction does not exist', 404

    def post(self):
        """ Function for creating a new transaction"""
        try:
            trans = self.finance_schema.load(request.json,
                                             session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(trans)
        db.session.commit()
        return self.finance_schema.dump(trans), 200

    def put(self, trans_id):
        """ Function for updating information about an existing transaction"""
        trans = db.session.query(models.Finance).filtered_by(
            trans_id=trans_id).first()
        if not trans:
            return {'message': 'Wrong data'}, 400
        try:
            trans = self.finance_schema.load(request.json,
                                             instance=trans,
                                             session=db.session)
        except ValidationError as e:
            return {'message': str(e)}, 400
        db.session.add(trans)
        db.session.commit()
        return self.user_schema.dump(trans), 200

    def delete(self, trans_id):
        """ Function to completely delete information about transaction"""
        trans = db.session.query(models.Finance).filter_by(
            trans_id=trans_id).first()
        if not trans:
            return 'Transaction does not exist', 404
        db.session.delete(trans)
        db.session.commit()
        return 'Transaction deleted successfully', 200


api.add_resource(UserApi, '/user', '/user/<user_id>', strict_slashes=False)
api.add_resource(FinanceApi, '/trans', '/trans/<trans_id>',
                 strict_slashes=False)
