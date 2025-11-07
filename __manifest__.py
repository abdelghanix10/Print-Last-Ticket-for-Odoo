{
    'name': 'POS Print Last Receipt',
    'version': '18.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Add button to print last receipt in POS',
    'description': """
        POS Print Last Receipt
        ======================
        This module adds a button in the POS interface to print the last receipt.
        
        Features:
        ---------
        * Print Last Receipt button in the action pad
        * Automatically finds the last paid order
        * Uses Odoo's default receipt template
        * Shows notifications for success/errors
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'views/pos_config_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_print_last_receipt/static/src/js/print_last_receipt.js',
            'pos_print_last_receipt/static/src/xml/print_last_receipt_button.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
