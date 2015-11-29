import cx_Oracle

def authorize_user(login, password):
    authorize_result = {"success": False}
    authorize_result["role"] = 'user'

    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('select user_login, user_password, user_role from clients')
    for result in cur:
        if (login == result[0] and password == result[1]):
            user_role = result[2]
            authorize_result["success"] = True
            authorize_result["role"] = user_role


    return authorize_result


def get_user_diagnoses(username):
    database_reply = {"login": username}
    get_user_diagnoses_result = {"success": True}
    get_user_diagnoses_result.update(database_reply)
    return get_user_diagnoses_result


