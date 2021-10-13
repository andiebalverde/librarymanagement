import requests

def test_list_users_check_status():
     response = requests.get("http://127.0.0.1:5000/users/list")
     assert response.status_code == 200

def test_list_user_checkouts():
     response = requests.get("http://127.0.0.1:5000/users/list_by_act")
     assert response.status_code == 200

def test_list_library_checkouts():
     response = requests.get("http://127.0.0.1:5000/users/list_lib_checkout")
     assert response.status_code == 200

def test_add_library_checkouts():
     response = requests.get("http://127.0.0.1:5000/libraries/add")
     assert response.status_code == 200

def test_add_library_activity():
     response = requests.get("http://127.0.0.1:5000/library_activities/add")
     assert response.status_code == 200

