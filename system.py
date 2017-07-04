system_active = false;

def toggle():
    print('Toggled')
    if not system_active:
        system_active = True
    else:
        system_active = False
