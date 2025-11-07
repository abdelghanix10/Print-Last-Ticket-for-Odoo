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
    'author': 'Abdelghani X',
    'website': 'https://www.AbdelghaniX.com',
    'price': 19.99,
    'currency': 'USD',
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
        'static/description/screenshots/Register Without Button \'Print Last Receipt\' - 1.png',
        'static/description/screenshots/Button Edit Settings Register - 2.png',
        'static/description/screenshots/PopUp Settings Register - 3.png',
        'static/description/screenshots/Register With Button Print Last Receipt - 4.png',
        'static/description/screenshots/Register With Button Print Last Receipt - 5.png',
    ],
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
