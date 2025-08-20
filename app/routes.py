from flask import Blueprint, render_template, url_for, current_app
import os
import re

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Base gallery directory for images used in before/after showcase
    gallery_dir = os.path.join(current_app.static_folder, 'pictures', 'gallery')
    
    # Before/After Projects
    before_after_projects = []
    
    # Door Project
    door_folder = os.path.join(gallery_dir, 'before and after door')
    if os.path.exists(door_folder):
        door_images = {}
        for img in os.listdir(door_folder):
            if img.lower().endswith((".jpg", ".jpeg", ".png")):
                rel_path = os.path.join('pictures', 'gallery', 'before and after door', img)
                rel_path = rel_path.replace("\\", "/")
                if 'before' in img.lower():
                    door_images['before'] = rel_path
                elif 'after' in img.lower():
                    door_images['after'] = rel_path
        
        if 'before' in door_images and 'after' in door_images:
            before_after_projects.append({
                'title': 'Deur schilderen',
                'description': 'Professioneel schilderwerk van een deur',
                'before': door_images['before'],
                'after': door_images['after']
            })
    
    # NY Pizza Project
    pizza_folder = os.path.join(gallery_dir, 'before and after 3 examples NY PIZZA')
    if os.path.exists(pizza_folder):
        pizza_images = {'before': [], 'after': []}
        for img in os.listdir(pizza_folder):
            if img.lower().endswith((".jpg", ".jpeg", ".png")):
                rel_path = os.path.join('pictures', 'gallery', 'before and after 3 examples NY PIZZA', img)
                rel_path = rel_path.replace("\\", "/")
                if 'before' in img.lower():
                    pizza_images['before'].append(rel_path)
                elif 'after' in img.lower():
                    pizza_images['after'].append(rel_path)
        
        # Sort to match pairs (before1 with after1, etc.)
        pizza_images['before'].sort()
        pizza_images['after'].sort()
        
        # Only include the first pair to avoid showing multiple NY Pizza items
        if pizza_images['before'] and pizza_images['after']:
            before_after_projects.append({
                'title': 'NY Pizza Renovatie 1',
                'description': 'Volledige transformatie van restaurant exterieur',
                'before': pizza_images['before'][0],
                'after': pizza_images['after'][0]
            })
    
    # Additional root-level before/after pairs (e.g. before6/after6) in gallery root
    root_pairs = {}
    if os.path.exists(gallery_dir):
        for f in os.listdir(gallery_dir):
            file_path = os.path.join(gallery_dir, f)
            if os.path.isfile(file_path) and f.lower().endswith((".jpg", ".jpeg", ".png")):
                match = re.match(r'^(before|after)(\d+)\.(jpg|jpeg|png)$', f.lower())
                if match:
                    kind = match.group(1)  # 'before' or 'after'
                    num = int(match.group(2))
                    rel_path = os.path.join('pictures', 'gallery', f).replace("\\", "/")
                    pair_entry = root_pairs.setdefault(num, {})
                    pair_entry[kind] = rel_path
    
    for num in sorted(root_pairs.keys()):
        pair = root_pairs[num]
        if 'before' in pair and 'after' in pair:
            if num == 6:
                title = 'Deur renovatie'
                description = 'Professionele restauratie van een deur'
            elif num == 7:
                title = 'Terras schilderwerk'
                description = 'Professioneel schilderwerk van een terras'
            else:
                title = f'Project {num}'
                description = 'Nieuwe transformatie uitgelicht'

            before_after_projects.append({
                'title': title,
                'description': description,
                'before': pair['before'],
                'after': pair['after']
            })

    return render_template('index.html', before_after_projects=before_after_projects)

@main.route('/about')
def about():
    # Logos for the about page
    logo_dir = os.path.join(current_app.static_folder, 'pictures', 'logos')
    logos = []
    for f in os.listdir(logo_dir):
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".svg")):
            rel_path = os.path.join('pictures', 'logos', f)
            logos.append(rel_path.replace("\\", "/"))
    return render_template('about.html', logos=logos) 

@main.route('/contact')
def contact():
    # Logos for the contact page (favicon)
    logo_dir = os.path.join(current_app.static_folder, 'pictures', 'logos')
    logos = []
    for f in os.listdir(logo_dir):
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".svg")):
            rel_path = os.path.join('pictures', 'logos', f)
            logos.append(rel_path.replace("\\", "/"))
    return render_template('contact.html', logos=logos)