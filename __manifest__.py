{
    'name': 'Gestión de Salud del Cliente',
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'version': '1.0',
    'summary': 'Gestión de Salud del Cliente',
    'description': 'Módulo para gestionar la información de salud de los clientes.',
    'author': 'Jose Maria Lozano Banqueri',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cliente_salud_views.xml',
    ],
    'installable': True,
    'application': True,
}