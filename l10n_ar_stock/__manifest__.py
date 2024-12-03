{
    'name': 'Remitos, COT y demas ajustes de stock para Argentina',
    'version': "18.0.1.0.0",
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'l10n_ar',
        'stock',
        'stock_voucher',  # por la clase receiptbooks y demas
        'l10n_ar_ux',
        'stock_picking_invoice_link',
    ],
    'data': [
        'security/l10n_ar_stock_security.xml',
        'wizards/arba_cot_wizard_views.xml',
        'wizards/res_config_settings_view.xml',
        'views/stock_picking_views.xml',
        'views/stock_book_views.xml',
        'views/product_template_views.xml',
        'views/uom_uom_views.xml',
        'views/stock_lot_views.xml',
        'views/report_deliveryslip.xml',
        'views/report_invoice.xml',
        'data/ir_sequence_data.xml',
        'data/product_uom_data.xml',
        'data/document_type_data.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/stock_book_demo.xml',
        'demo/stock_picking_demo.xml',
    ],
    'installable': True,
    'auto_install': ['stock', 'l10n_ar'],
    'application': False,
}
