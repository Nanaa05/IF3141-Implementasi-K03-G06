{
    'name': "KYZN Sales",
    'summary': 'Module Odoo untuk sistem pencatatan sales terpusat KYZN.',
    'description': 'Module Odoo untuk memusatkan pencatatan, validasi, dan pelaporan penjualan membership pada PT Akademi Fambam Indonesia (KYZN).',
    'sequence': -100,
    'author': "Kelompok 06-K03",
    'category': 'Sales',
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/kyzn_menus.xml',
        'views/kyzn_trees.xml',
        'views/kyzn_forms.xml',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/product_views.xml',
        'views/report_views.xml',
        'views/menus.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
