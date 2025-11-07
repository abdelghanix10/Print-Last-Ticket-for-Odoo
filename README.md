# POS Print Last Receipt - Odoo 18

## Description

This module adds a "Print Last Receipt" button to the Odoo 18 Point of Sale interface, allowing users to quickly reprint the last receipt from the current session.

## Features

- **Print Last Receipt Button**: Adds a button in the POS action pad
- **Automatic Order Detection**: Finds the last paid order automatically
- **Default Receipt Template**: Uses Odoo's standard receipt format
- **User Notifications**: Shows success or error messages
- **Easy to Use**: One-click printing of the last receipt

## Installation

1. Copy the `pos_print_last_receipt` folder to your Odoo addons directory
2. Update the apps list in Odoo (Apps menu > Update Apps List)
3. Search for "POS Print Last Receipt"
4. Click Install

## Usage

1. Open the Point of Sale application
2. Complete at least one sale
3. Look for the "Print Last" button in the action pad (right side panel)
4. Click the button to reprint the last receipt

## Technical Details

- **Odoo Version**: 18.0
- **Dependencies**: point_of_sale
- **License**: LGPL-3

## Module Structure

```
pos_print_last_receipt/
├── __init__.py
├── __manifest__.py
├── README.md
└── static/
    └── src/
        ├── js/
        │   └── print_last_receipt.js
        └── xml/
            └── print_last_receipt_button.xml
```

## Support

For issues or questions, please contact your Odoo administrator.

## Credits

- Developer: Abdelghani X
- Maintainer: Abdelghani X
