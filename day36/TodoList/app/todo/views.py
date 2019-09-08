from app.todo import todo

@todo.route('/add/')
def add():
    return  'todo add'

@todo.route('/delete/')
def delete():
    return  'todo delete'