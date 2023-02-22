import sqlite3
from bottle import route,run,template,request,error
import json as js

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table',rows=result)
    return output

@route('/new',method='GET')
def new_task():
    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)",(new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()
        
        return '<p>成功添加数据，ID为：%s</p>'%new_id
    
    else:
        return template('new_task.tpl')

@route('/edit',method="get")
def edit_task():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.exectue("SELECT task FROM todo WHERE id LIKE ?",(str(no),))
    cur_data = fetchone()
    return template('edit_task',old=cur_data,no=no)

@route('/edit/<no:int>',method="GET")
def edit_item(no):
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?,status = ? WHERE id LIKE ?",(edit,status,no))
        conn.commit()
        #c.close()

        return '<p>成功提交计划 id：%s </p>'%no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?",(str(no),))
        cur_data = c.fetchone()

        return template('edit_task',old= cur_data,no=no)


@route('/json<json:re:[0-9]+>')
def show_json(json):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?",(json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task':'This item number does not exist!'}
    else:         
        #json_result = js.dumps(result[0],ensure_ascii=False)
        return {'task':result[0]}

@error(404)
def mistake404(code):
    return 'Sorry,你要的网页不存在！'

run(reload=True,host='localhost',port='8888')
