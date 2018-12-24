import json
import requests

class RESTmtds():

    def __init__(self,endpoint,**jsonval):
        self.base_url = "https://reqres.in/"
        self.endpoint = endpoint
        self.jsonval = jsonval
        self.headers = {
            'cache-control': "no-cache",
            'Accept': "application/json",
            'Content-Type' : "application/json",
        }

    def get_mthd(self):
        return requests.get(self.base_url+self.endpoint, headers= self.headers)

    def post_mtd(self):
        return requests.post(self.base_url+self.endpoint ,json = self.jsonval, headers=self.headers)

    def put_mtd(self):
        return requests.put(self.base_url+self.endpoint ,json = self.jsonval, headers=self.headers)

    def patch_mtd(self):
        return requests.patch(self.base_url+self.endpoint ,json = self.jsonval, headers=self.headers)

    def delete_mthd(self):
        return requests.delete(self.base_url+self.endpoint, headers= self.headers)

class App_REST_mtd(RESTmtds):

    def __init__(self):
        pass

    def validate_get_response(self, endpoint, status_code,comments):
        """
        function gets value from different endpoint
        :param endpoint:
        :param status_code: expected status code to be compared
        :param comments: detail about the endpoint
        :return:
        """
        try:
            print("----------------------------------")
            restObj = RESTmtds(endpoint)
            response = restObj.get_mthd()
            obj = json.loads(response.text)
            data_json = json.dumps(obj)
            if response.status_code == status_code:
                print("REST get for "+comments+" is success!"+" with status code: "+str(response.status_code)+\
                      " as expected \n Endpoint: "+endpoint
                return data_json
            else:
                print("REST get failed for "+comments+" with status code %d",response.status_code)
                return data_json
        except Exception as e:
            print(e
            return e.message
        finally:
            del restObj
            print("----------------------------------")

    def validate_post_response(self, endpoint, status_code,comments, **data):
        """
        function gets value from different endpoint
        :param endpoint:
        :param status_code: expected status code to be compared
        :param comments: detail about the endpoint
        :return:
        """
        try:
            print("----------------------------------")
            restObj = RESTmtds(endpoint,**data)
            response = restObj.post_mtd()
            obj = json.loads(response.text)
            data_json = json.dumps(obj)
            if response.status_code == status_code:
                print("REST post for "+comments+" is success!"+" with status code: "+str(response.status_code)+\
                      " as expected \n Endpoint: "+endpoint
                return data_json
            else:
                print("REST post failed for "+comments+" with status code %d",response.status_code
                return data_json
        except Exception as e:
            print(e
            return e.message
        finally:
            del restObj
            print("----------------------------------"

    def validate_put_response(self, endpoint, status_code,comments, **data):
        """
        function gets value from different endpoint
        :param endpoint:
        :param status_code: expected status code to be compared
        :param comments: detail about the endpoint
        :return:
        """
        try:
            print("----------------------------------")
            restObj = RESTmtds(endpoint,**data)
            response = restObj.put_mtd()
            obj = json.loads(response.text)
            data_json = json.dumps(obj)
            if response.status_code == status_code:
                print("REST put for "+comments+" is success!"+" with status code: "+str(response.status_code)+\
                      " as expected \n Endpoint: "+endpoint
                return data_json
            else:
                print("REST put failed for "+comments+" with status code %d",response.status_code
                return data_json
        except Exception as e:
            print(e
            return e.message
        finally:
            del restObj
            print("----------------------------------")

    def validate_patch_response(self, endpoint, status_code,comments, **data):
        """
        function gets value from different endpoint
        :param endpoint:
        :param status_code: expected status code to be compared
        :param comments: detail about the endpoint
        :return:
        """
        try:
            print("----------------------------------")
            restObj = RESTmtds(endpoint,**data)
            response = restObj.patch_mtd()
            obj = json.loads(response.text)
            data_json = json.dumps(obj)
            if response.status_code == status_code:
                print("REST patch for "+comments+" is success!"+" with status code: "+str(response.status_code)+\
                      " as expected \n Endpoint: "+endpoint
                return data_json
            else:
                print("REST patch failed for "+comments+" with status code %d",response.status_code
                return data_json
        except Exception as e:
            print(e
            return e.message
        finally:
            del restObj
            print("----------------------------------"

    def validate_delete_response(self, endpoint, status_code,comments):
        """
        function gets value from different endpoint
        :param endpoint:
        :param status_code: expected status code to be compared
        :param comments: detail about the endpoint
        :return:
        """
        try:
            print("----------------------------------")
            restObj = RESTmtds(endpoint)
            response = restObj.delete_mthd()
            if response.status_code == status_code:
                print("REST delete for "+comments+" is success!"+" with status code: "+str(response.status_code)+\
                      " as expected \n Endpoint: "+endpoint
                return True
            else:
                print("REST delete failed for "+comments+" with status code %d",response.status_code
                return False
        except Exception as e:
            print(e
            return e.message
        finally:
            del restObj
            print("----------------------------------")


    def get_list_users_details(self):
        return self.validate_get_response("api/users?page=2", 200, "list user")

    def get_single_user_detail(self):
        return self.validate_get_response("api/users/2", 200, "single user")

    def get_user_not_found(self):
        return self.validate_get_response("api/users/23", 404, "user not found")

    def get_list_resource(self):
        return self.validate_get_response("api/unknown",200,"list resource")

    def get_single_resource(self):
        return self.validate_get_response("api/unknown/2", 200, "single resource")

    def get_single_resource_not_found(self):
        return self.validate_get_response("api/unknown/23", 404, "single resource not found")

    def get_delayed_response(self):
        return self.validate_get_response("api/users?delay=3", 200, "get delayed response")

    def post_create_user(self):
        data =  {
            "name": "morpheus",
            "job": "leader"
        }
        return self.validate_post_response("api/users", 201, "create user",**data)

    def post_register_success(self):
        data =  {
            "email": "sydney@fife",
            "password": "pistol"
        }
        return self.validate_post_response("api/register", 201, "register success",**data)

    def post_register_unsuccess(self):
        data =  {
            "email": "sydney@fife"
        }
        return self.validate_post_response("api/register", 400, "register unsuccess",**data)

    def post_login_success(self):
        data =  {
                "email": "peter@klaven",
                "password": "cityslicka"
        }
        return self.validate_post_response("api/login", 200, "login success",**data)

    def post_login_unsuccess(self):
        data =  {
                "email": "peter@klaven"
        }
        return self.validate_post_response("api/login", 400, "login unsuccess",**data)

    def put_user_details(self):
        data =  {
            "name": "morpheus",
            "job": "zion resident"
        }
        return self.validate_put_response("api/users/2", 200, "update user details",**data)

    def patch_user_details(self):
        data =  {
            "name": "morpheus",
            "job": "zion resident"
        }
        return self.validate_patch_response("api/login", 200, "update user details",**data)

    def delete_users_details(self):
        return self.validate_delete_response("api/users/2", 204, "delete user")

rest_obj = App_REST_mtd()

# GET Methods
rest_obj.get_list_users_details()
rest_obj.get_single_user_detail()
rest_obj.get_user_not_found()
rest_obj.get_list_resource()
rest_obj.get_single_resource()
rest_obj.get_single_resource_not_found()
rest_obj.get_delayed_response()

# POST Methods
rest_obj.post_create_user()
rest_obj.post_register_success()
rest_obj.post_register_unsuccess()
rest_obj.post_login_success()
rest_obj.post_login_unsuccess()

# PUT Method
rest_obj.put_user_details()

# PATCH Method
rest_obj.patch_user_details()

# DELETE Method
rest_obj.delete_users_details()
