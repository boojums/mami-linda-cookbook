# mami-linda-cookbook

Some install notes
- clone repo
- mkvirtualenv cookbook -p `which python3`
- pip install -r requirements.txt
- generate secret_key.txt with secret-key-gen.py
- fix the registration import lines:
from django.contrib.sites.models import RequestSite
should be:
from django.contrib.sites.requests import RequestSite


TODO:
- Imbeded recipes (like in many Desserts). Dessert should be able to be marked as part of another, won't show up independently but can search, will show up as part of the correct recipe in the 'instructions' section
- In addition, when a recipe is selected, show all recipes from the same page (receipe_set?)
- add basic recipe formatting
- implement fancy wysiwyg editing
- add formatting inside recipes
- shift all page numbers if a new recipe is inserted
- add edition attribute
- tags
- user favorites
- user comments
- Export to PDF
- Send a link to someone who doesn't have an account