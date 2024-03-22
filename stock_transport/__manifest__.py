{
    'name': "Dispatch Management System",
    'version': '1.0',
    'depends': ['base','fleet','stock_picking_batch','web_gantt'],
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
        'views/stock_picking_inherit_view.xml',
      
     
     ],
    # # data files containing optionally loaded demonstration data
      'demo': [
          
      ],
      'assets': {
        'web.assets_backend': [
            'stock_transport/static/src/views/stockTransport/stock_transport_gantt_renderer.xml',
            'stock_transport/static/src/views/stockTransport/stock_transport_gantt_renderer.js',
            'stock_transport/static/src/views/stockTransport/stock_transport_gantt_view.js',
        ]
    }
}