from flask import jsonify

class HttpCode(object):
    ok=200
    unautherror = 401
    paramaserror = 400
    servererror = 500

def restful_code(code,message,data):
    return jsonify({'code':code,'message':message,'data':data or {}})

def success(message='',data=None):
    return restful_code(code=HttpCode.ok,message=message,data=data)

def unauth_error(message=''):
    return restful_code(code=HttpCode.unautherror,message=message,data=None)

def paramas_error(message: object = '') -> object:
    return restful_code(code=HttpCode.paramaserror,message=message,data=None)

def server_error(message=''):
    return restful_code(code=HttpCode.servererror,message=message or '服务器内部错误',data=None)