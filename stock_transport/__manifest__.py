{
    'name': "Dispatch Management System",
    'version': '1.0',
    'depends': ['base','fleet','stock_picking_batch'],
    'author': "Bussa Vishal",
    'category': 'Category',
    'description': """
    Description text
    """,
    # # data files always loaded at installation
     'data': [
        'security/ir.model.access.csv',
        'views/fleet_inherit_category_view.xml',
        'views/batch_transfers_inherit_view.xml',
      
     
     ],
    # # data files containing optionally loaded demonstration data
      'demo': [
          
      ],
}