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

'''
def get_users():
    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('SELECT user_card_number, user_full_name, user_group FROM clients')
    for result in cur:

            user_role = result[2]
            authorize_result["success"] = True
            authorize_result["role"] = user_role

    return authorize_result
'''
