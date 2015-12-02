import cx_Oracle


def authorize_user(login, password):
    authorize_result = {"success": False,
                        "role": 'user'}

    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('SELECT user_login, user_password, user_role FROM clients')
    for result in cur:
        if login == result[0] and password == result[1]:
            user_role = result[2]
            authorize_result["success"] = True
            authorize_result["role"] = user_role

    return authorize_result


def get_user_diagnoses(login):
    diagnoses_result = {"success": True,
                        "diagnose_name": '',
                        "diagnose_date": '',
                        "diagnose_doctor": ''}

    diagnose_name = []
    diagnose_date = []
    diagnose_doctor = []
    diagnose_number = []

    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('SELECT user_card_number FROM clients WHERE user_login = \'{0}\''.format(login))
    for result_card_number in cur:
        user_card_number = result_card_number[0]

    cur.execute('SELECT diagnose_number FROM MEDICALCARD WHERE user_card_number = \'{0}\''.format(user_card_number))
    for result_diagnose_number in cur:
        diagnose_number.append(result_diagnose_number[0])

    if len(diagnose_number) > 1:
        diagnose_number_tuple = tuple(diagnose_number)
    elif len(diagnose_number) == 1:
        diagnose_number_tuple = diagnose_number[0]
    else:
        diagnose_number_tuple = 0

    cur.execute('SELECT diagnose_name, diagnose_date, diagnose_doctor FROM DIAGNOSES WHERE diagnose_number IN {0}'.format(diagnose_number_tuple))
    for result_diagnose in cur:
        diagnose_name.append(result_diagnose[0])
        diagnose_date.append(str(result_diagnose[1]))
        diagnose_doctor.append(result_diagnose[2])

        diagnoses_result["diagnose_name"] = diagnose_name
        diagnoses_result["diagnose_date"] = diagnose_date
        diagnoses_result["diagnose_doctor"] = diagnose_doctor

    return diagnoses_result


def get_all_users():
    users_result = {"success": True,
                    "users_card_numbers": '',
                    "users_full_names": '',
                    "users_groups": ''}

    users_cards_numbers = []
    users_full_names = []
    users_groups = []

    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('SELECT user_card_number, user_full_name, user_group FROM clients WHERE user_role != \'admin\'')
    for result in cur:
        users_cards_numbers.append(result[0])
        users_full_names.append(result[1])
        users_groups.append(result[2])

        users_result["users_card_numbers"] = users_cards_numbers
        users_result["users_full_names"] = users_full_names
        users_result["users_groups"] = users_groups

    return users_result


def add_new_user():
    add_users_result = {"user_card_number": '77777777',
                        "user_full_name": 'Anton Badovskiy',
                        "user_group": 'kw11',
                        "user_phone_number": '0951111111',
                        "username": 'anton',
                        "password": 'anton',
                        "user_email": 'email@gmail.com',
                        "user_role": 'user'}


    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('INSERT INTO CLIENTS (USER_CARD_NUMBER, USER_FULL_NAME, USER_GROUP,'
                ' USER_PHONE_NUMBER, USER_LOGIN, USER_PASSWORD, USER_EMAIL, USER_ROLE)'
                'VALUES (\'{0}\',\'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', \'{6}\', \'{7}\')'.format(
                                                                        add_users_result['user_card_number'],
                                                                        add_users_result['user_full_name'],
                                                                        add_users_result['user_group'],
                                                                        add_users_result['user_phone_number'],
                                                                        add_users_result['username'],
                                                                        add_users_result['password'],
                                                                        add_users_result['user_email'],
                                                                        add_users_result['user_role']))



def edit_user_info():
    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    user_card_number = '11111111'
    user_diagnose_numbers = []
    user_edited_data = {} #TODO recieve this dictionari from server

    # Selecting card_number
    cur.execute('SELECT user_full_name, user_group, user_email, user_phone_number'
                'FROM CLIENTS WHERE user_card_number =\'{0}\''.format(user_card_number))

    for result_user_data in cur:
        user_full_name = result_user_data[0]
        user_group = result_user_data[1]
        user_email = result_user_data[2]
        user_phone_number = result_user_data[3]

    # Selecting diagnose_numbers to get all users diagnoses
    cur.execute('SELECT diagnose_number FROM MEDICALCARD'
                'WHERE user_card_number = \'{0}\''.format(user_card_number))

    for result_user_diagnose_number in cur:
        user_diagnose_numbers.append(result_user_diagnose_number[0])

    if len(user_diagnose_numbers) > 1:
        user_diagnose_numbers_tuple = tuple(user_diagnose_numbers)
    elif len(user_diagnose_numbers) == 1:
        user_diagnose_numbers_tuple = user_diagnose_numbers[0]
    else:
        user_diagnose_numbers_tuple = 0

    # Selecting users diagnoses
    cur.execute('SELECT diagnose_name FROM DIAGNOSES '
                'WHERE diagnose_number IN {0}'.format(user_diagnose_numbers_tuple))

    cur.execute('UPDATE CLIENTS '
                'SET user_full_name = \'{0}\','
                'user_group = \'{1}\','
                'user_email = \'{2}\','
                'user_phone_number = \'{3}\''
                'WHERE user_card_number = \'{4}\''.format(user_edited_data['user_full_name'],
                                                          user_edited_data['user_group'],
                                                          user_edited_data['user_email'],
                                                          user_edited_data['user_phone_number'],
                                                          user_card_number))
    # TODO  finish this function: add operations with updating and deleting diagnoses


def delete_selected_users(user_card_number):
    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('DELECTE * FROM CLIENTS'
                'WHERE user_card_number IN {0}'.format(user_card_number))
