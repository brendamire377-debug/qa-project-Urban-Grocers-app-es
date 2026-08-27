import data
import sender_stand_request

def get_kit_body(kit_name):
    currents_kit_body= data.kit_body.copy()
    currents_kit_body["name"] = kit_name
    return currents_kit_body

def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert kit_body["name"] == response.json()["name"]

def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def negative_assert_no_kit_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400
    assert response.json()["code"] == 400


def test_1_kit_name_1_character():
    current_kit_body = get_kit_body("a")
    positive_assert(current_kit_body)

def test_2_kit_name_511_characters():
    current_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(current_kit_body)

def test_3_kit_without_name():
    current_kit_body = get_kit_body("")
    negative_assert_code_400(current_kit_body)

def test_4_kit_name_512_characters():
    current_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(current_kit_body)

def test_5_kit_name_with_special_characters():
    current_kit_body = get_kit_body("№%@")
    positive_assert(current_kit_body)

def test_6_kit_name_with_spaces():
    current_kit_body = get_kit_body( " A Aaa ")
    positive_assert(current_kit_body)

def test_7_kit_name_with_numbers():
    current_kit_body = get_kit_body("123")
    positive_assert(current_kit_body)

def test_8_get_kit_body_no_name():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_kit_name(kit_body)

def test_9_get_kit_body_kit_name_type_number():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400





