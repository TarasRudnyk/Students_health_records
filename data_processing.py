import cx_Oracle


def get_configuration():
    with open("config", encoding='utf-8') as config_file:
        parameters = {}
        for line in config_file:
            parameter, value = line.split(": ")
            parameter = parameter.rstrip()
            value = value.strip()
            parameters[parameter] = value

    info = "{}/{}@{}/{}".format(parameters["name"],
                                parameters["password"],
                                parameters["server and port"],
                                parameters["database service"])
    print("Server started with parameters:", info)
    return info

info = get_configuration()
con = cx_Oracle.connect(info)
cur = con.cursor()


def authorize_user(login, password):
    global con
    global cur

    authorize_result = {"success": False,
                        "role": 'user'}

    cur.execute('SELECT user_login, user_password, user_role FROM users')
    for result in cur:
        if login == result[0] and password == result[1]:
            user_role = result[2]
            authorize_result["success"] = True
            authorize_result["role"] = user_role

    return authorize_result


def get_user_diagnoses(login):
    global con
    global cur

    diagnoses_result = {"success": True,
                        "diagnose_name": '',
                        "diagnose_date": '',
                        "diagnose_doctor": '',
                        "diagnose_time": ''}

    diagnose_name = []
    diagnose_date = []
    diagnose_time = []
    diagnose_doctor = []
    diagnose_number = []

    cur.execute('SELECT user_card_number FROM users WHERE user_login = \'{0}\''.format(login))
    for result_card_number in cur:
        user_card_number = result_card_number[0]

    try:
        cur.execute('SELECT diagnose_number FROM MEDICALCARD WHERE user_card_number = \'{0}\''.format(user_card_number))
        for result_diagnose_number in cur:
             diagnose_number.append(result_diagnose_number[0])
    except:
        pass


    if len(diagnose_number) > 1:
        diagnose_number_tuple = tuple(diagnose_number)
    elif len(diagnose_number) == 1:
        diagnose_number_tuple = diagnose_number[0]
    else:
        diagnose_number_tuple = 0

    cur.execute('SELECT disease_name, diagnose_date, diagnose_doctor, diagnose_time FROM DIAGNOSES WHERE diagnose_number IN {0}'.format(diagnose_number_tuple))
    for result_diagnose in cur:
        diagnose_name.append(result_diagnose[0])
        diagnose_date.append(str(result_diagnose[1].strftime('%d-%b-%Y')))
        diagnose_doctor.append(result_diagnose[2])
        diagnose_time.append(result_diagnose[3])

        diagnoses_result["diagnose_name"] = diagnose_name
        diagnoses_result["diagnose_date"] = diagnose_date
        diagnoses_result["diagnose_doctor"] = diagnose_doctor
        diagnoses_result["diagnose_time"] = diagnose_time

    return diagnoses_result


def get_all_users():
    global con
    global cur

    users_result = {"success": True,
                    "users_card_numbers": '',
                    "users_full_names": '',
                    "users_groups": ''}

    users_cards_numbers = []
    users_full_names = []
    users_groups = []

    cur.execute('SELECT user_card_number, user_full_name, user_group FROM users WHERE user_role != \'admin\'')
    for result in cur:
        users_cards_numbers.append(result[0])
        users_full_names.append(result[1])
        users_groups.append(result[2])

        users_result["users_card_numbers"] = users_cards_numbers
        users_result["users_full_names"] = users_full_names
        users_result["users_groups"] = users_groups

    return users_result


def add_new_user(add_users_result):
    result = {
        "success": True
    }

    global con
    global cur

    add_users_result["user_full_name"] = add_users_result["user_full_name"][0] + " " + add_users_result["user_full_name"][1]

    try:
        cur.execute('set transaction isolation level serializable')
        cur.execute('INSERT INTO users (USER_CARD_NUMBER, USER_LOGIN, USER_PASSWORD, USER_FULL_NAME,'
                    'USER_PHONE_NUMBER, USER_GROUP, USER_EMAIL, USER_ROLE)'
                    'VALUES (\'{0}\',\'{1}\', \'{2}\', \'{3}\', \'{4}\', \'{5}\', \'{6}\', \'{7}\')'.format(
                                                                            add_users_result['user_card_number'],
                                                                            add_users_result['username'],
                                                                            add_users_result['password'],
                                                                            add_users_result['user_full_name'],
                                                                            add_users_result['user_phone_number'],
                                                                            add_users_result['user_group'],
                                                                            add_users_result['user_email'],
                                                                            add_users_result['user_role']))

        con.commit()
    except:
        result["success"] = False
        con.rollback()

    return result


def edit_user_info_select_data(user_card_number):
    global con
    global cur

    user_data = {'success': True,
                 'user_full_name': '',
                 'user_group': '',
                 'user_email': '',
                 'user_phone_number': ''}

    try:
        cur.execute('SELECT user_full_name, user_group, user_email, user_phone_number '
                 'FROM users WHERE user_card_number =\'{0}\''.format(user_card_number))

        for result_user_data in cur:
            user_data['user_full_name'] = result_user_data[0]
            user_data['user_group'] = result_user_data[1]
            user_data['user_email'] = result_user_data[2]
            user_data['user_phone_number'] = result_user_data[3]
    except:
        user_data["success"] = False

    return user_data


def edit_user_info_select_diagnoses(user_card_number):
    global con
    global cur

    result = {
        "success": True
    }

    user_diagnose_numbers = []
    user_diagnose_names = []
    user_diagnose_dates = []
    user_diagnose_time = []

    # Selecting diagnose_numbers to get all users diagnoses
    cur.execute('SELECT diagnose_number FROM MEDICALCARD'
                ' WHERE user_card_number = \'{0}\''.format(user_card_number))

    for result_user_diagnose_number in cur:
        user_diagnose_numbers.append(result_user_diagnose_number[0])

    if len(user_diagnose_numbers) > 1:
        user_diagnose_numbers_tuple = tuple(user_diagnose_numbers)
    elif len(user_diagnose_numbers) == 1:
        user_diagnose_numbers_tuple = user_diagnose_numbers[0]
    else:
        user_diagnose_numbers_tuple = 0

    # Selecting users diagnoses
    try:
        cur.execute('SELECT disease_name, diagnose_date, diagnose_time FROM DIAGNOSES '
                    'WHERE diagnose_number IN {0}'.format(user_diagnose_numbers_tuple))
    except:
        result["success"] = False
    for result_diagnose in cur:
        user_diagnose_names.append(result_diagnose[0])
        user_diagnose_dates.append(result_diagnose[1])
        user_diagnose_time.append(result_diagnose[2])

    result["diagnoses"] = user_diagnose_names

    return result


def edit_user_info_update_data(user_edited_data):
    global con
    global cur


    result = {
        "success": True
    }

    if user_edited_data["user_phone_number"] == 'None':
        user_edited_data["user_phone_number"] = ""
    try:
        cur.execute('set transaction isolation level serializable')
        cur.execute('UPDATE users '
                'SET user_full_name = \'{0}\','
                'user_group = \'{1}\','
                'user_email = \'{2}\','
                'user_phone_number = \'{3}\' '
                'WHERE user_card_number = \'{4}\''.format(user_edited_data['user_full_name'],
                                                          user_edited_data['user_group'],
                                                          user_edited_data['user_email'],
                                                          user_edited_data['user_phone_number'],
                                                          user_edited_data['user_card_number']))
        con.commit()
    except:
        result["success"] = False
        con.rollback()

    return result


def edit_user_select_all_diseases():
    global con
    global cur

    disease_names = []

    result = {
        "success": True
    }

    cur.execute('SELECT disease_name FROM diseases ')

    for result_diseases in cur:
        disease_names.append(result_diseases[0])

    result["diseases"] = disease_names
    return result


def edit_user_info_add_diagnose(diagnose_data, card_number):
    global con
    global cur

    result = {
        "success": True
    }
    try:
    # print(diagnose_data['diagnose_number'])
        cur.execute('set transaction isolation level serializable')
        cur.execute('INSERT INTO DIAGNOSES (DIAGNOSE_NUMBER, DISEASE_NAME, DIAGNOSE_DATE, DIAGNOSE_DOCTOR, DIAGNOSE_TIME) '
                    'VALUES (\'{0}\',\'{1}\', \'{2}\', \'{3}\', \'{4}\')'.format(
                                                                            diagnose_data['diagnose_number'],
                                                                            diagnose_data['disease_name'],
                                                                            diagnose_data['diagnose_date'],
                                                                            diagnose_data['diagnose_doctor'],
                                                                            diagnose_data['diagnose_time']))

        cur.execute('INSERT INTO MEDICALCARD (DIAGNOSE_NUMBER, USER_CARD_NUMBER) '
                    'VALUES (\'{0}\', \'{1}\')'.format(diagnose_data['diagnose_number'], card_number))

        con.commit()
    except:
        result["success"] = False
        con.rollback()

    return result


def delete_selected_users(user_card_number):
    global con
    global cur
    result = {
        "success": True
    }

    try:
        cur.execute('set transaction isolation level serializable')
        cur.execute('DELETE FROM MEDICALCARD '
                    'WHERE user_card_number = {0}'.format(user_card_number))
        cur.execute('DELETE FROM users '
                    'WHERE user_card_number = {0}'.format(user_card_number))
        con.commit()
    except:
        result["success"] = False
        con.rollback()

    return result


def get_diagnose_number():
    global con
    global cur
    # con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    # cur = con.cursor()
    result = {
        "success": True
    }
    diagnose_number = 1

    cur.execute('SELECT MAX(diagnose_number) FROM DIAGNOSES')

    for result_diagnose_number in cur:
        diagnose_number = result_diagnose_number[0]
    result["count"] = diagnose_number
    return result


