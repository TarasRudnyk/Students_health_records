import cx_Oracle

def authorize_user(login, password):
    authorize_result = {"success": False}

    con = cx_Oracle.connect('taras/orcl@localhost/orcl')
    cur = con.cursor()

    cur.execute('select user_login, user_password, user_role from clients')
    for result in cur:
        if (login == result[0] and password == result[1]):
            user_role = result[2]
            authorize_result["success"] = True



    return authorize_result


    #cur.execute('select user_login, user_password from clients')

'''
    client_logins = []
    client_passwords = []
    client_roles = []

    cur.execute('select user_login from clients')
    for result_login in cur:
        client_logins.append(result_login[0])
    cur.execute('select user_password from clients')
    for result_password in cur:
        client_passwords.append(result_password[0])

    cur.execute('select user_role from clients')
    for result_role in cur:
        client_roles.append(result_role[0])

    if (login in client_logins and password in client_passwords):
        authorize_result["success"] = True
    else:
        authorize_result["success"] = False
'''


def get_user_diagnoses(username):
    database_reply = {"login": username}
    get_user_diagnoses_result = {"success": True}
    get_user_diagnoses_result.update(database_reply)
    return get_user_diagnoses_result


