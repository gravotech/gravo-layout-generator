from ..utils import (
    write_draw_rectangle,
    write_text_left_top,
    write_text_center,
    write_draw_rectangle_style
)

def shipping_title(image, context):
    coordinate = {
        'width': 106,
        'height': 7,
        'offset_left': 190,
        'offset_top': 0,
        'left': 0,
        'top': 0,
    }
    style = {
        'fill': '#f7ffd9',
        'outline': '#000',
        'stroke': 1,
    }
    write_draw_rectangle_style(image, coordinate, style)
    value_font = 'MYRIADPRO-BOLD.OTF'
    value_font_fill = '#000'
    value_font_size = 11
    text = context['entrega']['metodo'] 
    write_text_center(image, coordinate, text, value_font, value_font_fill, value_font_size)


def shipping_body(image, context):
    coordinate = {
        'width': 106,
        'height': 20,
        'offset_left': 190,
        'offset_top': 7,
        'left': 0,
        'top': 2,
    }
    write_draw_rectangle(image, coordinate)
    # products_text = ''
    # for product in context['products']:
    #     product_text = product
    #     products_text = products_text + '\n' + product_text
    # value_text = products_text
    # value_font = 'MYRIADPRO-REGULAR.OTF'
    # value_font_fill = '#000'
    # value_font_size = 9
    # coordinate['offset_left'] = coordinate['offset_left'] + 2

# write_text_left_top(image, coordinate, value_text, value_font, value_font_fill, value_font_size)