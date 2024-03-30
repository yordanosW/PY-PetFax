from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet',__name__,url_prefix="/pets")

@bp.route('/')
def index ():
    return render_template('index.html', pets=pets)

# @bp.route('/<int:id>')
# def show_pet(id):
# 	return render_template('show_pet.html', pet=pets[id])

# @bp.route('/<int:id>')
# def show_pet(id):
# 	return render_template('show_pet.html', pet=pets[id])


@bp.route('/<int:id>')
def show_pet(id):
	return render_template('show_pet.html', pet=next(filter(lambda p: p['pet_id'] == id, pets)))

