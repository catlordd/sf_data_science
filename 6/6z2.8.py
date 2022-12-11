'''[(1, {'username': user1, 'age': age1, 'email': email1}), 
(2, {'username': user2, 'age': age2, 'email': email2}), ... ]'''

def creater_list(username, age, email, tpl_list = None):
    if tpl_list is None:
        tpl_list = []
    tpl_list.append((len(tpl_list), {'username': username, 'age': age, 'email': email}))

list_workers = []
while len(list_workers) < 10:
    x = input()
    x = x.split()
    creater_list(x[0], x[1], x[2], list_workers)
    print(list(map(lambda x: x[1]['username'],list_workers)))
