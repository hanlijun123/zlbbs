from flask import session,redirect,url_for,g
from functools import wraps
import config


def login_requried(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if  config.CMS_USER_ID in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('cms.login'))
    return wrapper


def permission_required(permission):
    def outter(func):
        @wraps(func)
        def inner(*args,**kwargs):
            user=g.cms_user
            if user.has_permission(permission):
                return func(*args,**kwargs)
            else:
                return redirect(url_for('cms.index'))
        return inner
    return outter


