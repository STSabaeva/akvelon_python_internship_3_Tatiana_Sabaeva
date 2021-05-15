from fin_app import db
from fin_app.database.models import User, Finance
from datetime import date


def create_info():
    # tom = User(
    #     first_name='Tom',
    #     last_name='Riddle',
    #     email='tommy@gmail.com'
    # )
    #
    # harry = User(
    #     first_name='Harry',
    #     last_name='Potter',
    #     email='theboywhosurvived@gmail.com'
    # )
    # ron = User(
    #     first_name='Ron',
    #     last_name='Weasley',
    #     email='redhead@mail.ru'
    # )
    # hermione = User(
    #     first_name='Hermione',
    #     last_name='Granger',
    #     email='clevergirl@mail.ru'
    # )

    tr1 = Finance(
        user_id=1,
        sum_of_trans=-2000,
        trans_date=date(2021, 5, 11)

    )

    tr2 = Finance(
        user_id=1,
        sum_of_trans=500,
        trans_date=date(2019, 7, 12)

    )
    tr3 = Finance(
        user_id=1,
        sum_of_trans=-700,
        trans_date=date(2020, 1, 1)

    )
    tr4 = Finance(
        user_id=2,
        sum_of_trans=100,
        trans_date=date(2020, 1, 1)

    )
    tr5 = Finance(
        user_id=2,
        sum_of_trans=500,
        trans_date=date(2019, 7, 30)

    )
    tr6 = Finance(
        user_id=2,
        sum_of_trans=-200,
        trans_date=date(2019, 7, 30)

    )
    tr7 = Finance(
        user_id=2,
        sum_of_trans=100,
        trans_date=date(2021, 4, 30)

    )
    #
    # db.session.add(tom)
    # db.session.add(harry)
    # db.session.add(ron)
    # db.session.add(hermione)

    db.session.add(tr1)
    db.session.add(tr2)
    db.session.add(tr3)
    db.session.add(tr4)
    db.session.add(tr5)
    db.session.add(tr6)
    db.session.add(tr7)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    print('Creating...')
    create_info()
    print('Successfully created!')
