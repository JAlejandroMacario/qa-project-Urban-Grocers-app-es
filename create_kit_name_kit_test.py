import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201

def negative_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400

def test_1_create_kit_1_character_in_name_get_success_response():
    positive_assert(data.kit_body_1)

def test_2_create_kit_511_characters_in_name_get_success_response():
    positive_assert(data.kit_body_2)

def test_3_create_kit_0_characters_in_name_get_error_response():
    negative_assert(data.kit_body_3)

def test_4_create_kit_512_characters_in_name_get_error_response():
    negative_assert(data.kit_body_4)

def test_5_create_kit_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_5)

def test_6_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(data.kit_body_6)

def test_7_create_kit_has_number_in_first_name_get_success_response():
    positive_assert(data.kit_body_7)

def test_8_create_kit_no_name_get_error_response():
    negative_assert(None)

def test_9_create_kit_number_type_name_get_error_response():
    negative_assert(data.kit_body_9)
