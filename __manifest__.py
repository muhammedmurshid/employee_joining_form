{
    'name': 'Joining Form',
    'version': '1.0.0',
    'summary': 'Brief description of the module',
    'description': """
        A more detailed description of the module.
    """,
    'author': 'Murshid',
    'website': 'https://www.yourwebsite.com',
    'category': 'Specific Category',
    'license': 'LGPL-3',
    'depends': [
        'base',  # List of module dependencies
        'mail', 'web', 'hr'
        # Add other module dependencies here
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',  # Access rights
        'views/joining_form.xml',
        'views/web_form.xml',
        'views/employee.xml',
        'views/clarification.xml'

    ],


    'installable': True,  # Whether the module can be installed
    'application': False,  # Set to True if it's an application module
    'auto_install': False,  # Automatically install if dependencies are met

}
