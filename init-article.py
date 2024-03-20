#!/usr/bin/env python

import os
from datetime import datetime
from googletrans import Translator, LANGUAGES
# pip install googletrans

title_fr = input("[?] Titre article : ")

translator = Translator()
title_en = translator.translate(title_fr, src='fr', dest='en').text

title_fr_transformed = title_fr.replace("-", "").replace(" ", "-").replace("'", "").replace("?", "").replace("!", "").lower()
title_en_transformed = title_en.replace("-", "").replace(" ", "-").replace("'", "").replace("?", "").replace("!", "").lower()

current_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+01:00")

folder_path = f"content/posts/{title_fr_transformed}"
folder_image_path = f"static/images/{title_fr_transformed}"
os.makedirs(folder_path, exist_ok=True)
os.makedirs(folder_image_path, exist_ok=True)

template_path = "./template.md"
new_fr_file_path = f"{folder_path}/{title_fr_transformed}.fr.md"
new_en_file_path = f"{folder_path}/{title_en_transformed}.en.md"

with open(template_path, 'r') as file:
    template_fr = file.read()
    template_en = template_fr

template_fr = template_fr.replace("FIXME_TITLE", title_fr)
template_en = template_en.replace("FIXME_TITLE", title_en)
template_fr = template_fr.replace("FIXME_DESCRIPTION", "FIXME description à remplir")
template_en = template_en.replace("FIXME_DESCRIPTION", "FIXME description à remplir")
template_fr = template_fr.replace("FIXME_DATE", current_datetime)
template_en = template_en.replace("FIXME_DATE", current_datetime)
template_fr = template_fr.replace("FIXME_T_TRANSFORMED", f"{title_fr_transformed}")
template_en = template_en.replace("FIXME_T_TRANSFORMED", f"{title_en_transformed}")

with open(new_fr_file_path, 'w') as fr_file:
    fr_file.write(template_fr)

with open(new_en_file_path, 'w') as en_file:
    en_file.write(template_en)

print(f"[+] Article vierge : {new_fr_file_path}")
