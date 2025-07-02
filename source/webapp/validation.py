def validate(data):
    errors = {}
    name = data.get('name')
    if not name:
        errors['name'] = 'Пожалуйста, заполните это поле'
    elif len(name) < 3:
        errors['name'] = 'Пожалуйста, заполните это поле на более 3 символов'
    return errors