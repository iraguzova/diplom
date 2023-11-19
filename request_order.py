import configuration
import data
import requests

def create_new_order():
    order_track_response = requests.post(configuration.URL+configuration.CREATE_NEW_ORDER, json=data.order_body)
    return order_track_response

def order_track_info(order_track):
    order_info_response = requests.get(configuration.URL+configuration.ORDER_TRACK_INFO+order_track)
    return order_info_response
