from flask import Blueprint, render_template, url_for, current_app
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Gather gallery images (excluding before/after folders to avoid duplicates)
    gallery_dir = os.path.join(current_app.static_folder, 'pictures', 'gallery')
    gallery = []
    
    # Folders to exclude from main gallery (these are used in before/after showcase)
    excluded_folders = {
        'before and after door',
        'before and after 3 examples NY PIZZA'
    }
    
    for folder in os.listdir(gallery_dir):
        folder_path = os.path.join(gallery_dir, folder)
        if os.path.isdir(folder_path) and folder not in excluded_folders:
            for img in os.listdir(folder_path):
                if img.lower().endswith((".jpg", ".jpeg", ".png")):
                    # Store relative path for url_for and fix path separators for web URLs
                    rel_path = os.path.join('pictures', 'gallery', folder, img)
                    gallery.append(rel_path.replace("\\", "/"))
    
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
                'title': 'Deur Renovatie',
                'description': 'Professionele restauratie van een voordeur',
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
        
        # Create pairs
        for i in range(min(len(pizza_images['before']), len(pizza_images['after']))):
            before_after_projects.append({
                'title': f'NY Pizza Renovatie {i+1}',
                'description': 'Volledige transformatie van restaurant exterieur',
                'before': pizza_images['before'][i],
                'after': pizza_images['after'][i]
            })
    
    # Hero images
    hero_dir = os.path.join(current_app.static_folder, 'pictures', 'hero')
    hero_images = []
    for f in os.listdir(hero_dir):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            rel_path = os.path.join('pictures', 'hero', f)
            hero_images.append(rel_path.replace("\\", "/"))
    # Logos
    logo_dir = os.path.join(current_app.static_folder, 'pictures', 'logos')
    logos = []
    for f in os.listdir(logo_dir):
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".svg")):
            rel_path = os.path.join('pictures', 'logos', f)
            logos.append(rel_path.replace("\\", "/"))
    return render_template('index.html', gallery=gallery, hero_images=hero_images, logos=logos, before_after_projects=before_after_projects)

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