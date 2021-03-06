from flask import Flask
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
from apps.ueditor import bp as ueditor_bp

import config
from exts import db,mail,alidayu
from flask_wtf import CSRFProtect
from utils.captcha import Captcha


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
alidayu.init_app(app)


app.register_blueprint(cms_bp)
app.register_blueprint(common_bp)
app.register_blueprint(front_bp)
app.register_blueprint(ueditor_bp)
CSRFProtect(app)

Captcha.gene_graph_captcha()

if __name__ == '__main__':
    app.run()
