admin_username = 'admin'
admin_password_var = 'DJANGO_ADMIN_PASSWORD'

default_users = {
    admin_username: {
        'password_var': admin_password_var,
        'data': {
            'is_active': True,
            'is_superuser': True,
        }
    }
}

selectable_user_permissions = [
    'add_client',
    'add_group',
    'add_product',
    'add_visit',
    'add_payment',
]
