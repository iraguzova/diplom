import request_order

def test_get_order_by_track():
    track = request_order.create_new_order().json()['track']
    requests = request_order.order_track_info(str(track)).status_code
    code = 200
    assert requests == code

test_get_order_by_track()

# Рагузова Ирина, 10-я когорта — Финальный проект. Инженер по тестированию плюс