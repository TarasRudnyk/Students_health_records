import cx_Oracle

def authorize_user(login, password):
    authorize_result = {"success": True}

    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('select user_login from clients')
    for result_login in cur:
        client_login = result_login[0]
    cur.execute('select user_password from clients')
    for result_password in cur:
        client_password = result_password[0]

    if (client_login == login and client_password == password):
        authorize_result["success"] = True
    else:
        authorize_result["success"] = False

    return authorize_result


def get_user_diagnoses(username):
    database_reply = {"login": username}
    get_user_diagnoses_result = {"success": True}
    get_user_diagnoses_result.update(database_reply)
    return get_user_diagnoses_result


