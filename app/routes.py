import os
from .stylegan2 import projector

from flask import Blueprint, render_template

routes_blueprint = Blueprint("routes_blueprint", __name__)


@routes_blueprint.route("/")
def index():
    return render_template("index.html")


@routes_blueprint.route("/run_projector")
def run_projector():
    sample_image = "/sample_images/me.jpg"
    img_path = os.path.abspath(os.path.dirname(__file__) + sample_image)
    model_ckpt = "/model_checkpoints/stylegan-128px.model"
    ckpt_path = os.path.abspath(os.path.dirname(__file__) + model_ckpt)
    projector.project([img_path], ckpt_path)

    return render_template("projector.html")
