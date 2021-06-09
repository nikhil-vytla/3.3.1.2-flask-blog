
from random import randint, random


scss_files = ['bubbles.scss', 'purple.scss', 'stars.scss']

def get_random_background():
    random_index = randint(0, len(scss_files) - 1)
    return "{{ url_for('static',filename='styles/backgrounds/{" + scss_files[random_index] +  "}') }}"

print(get_random_background())