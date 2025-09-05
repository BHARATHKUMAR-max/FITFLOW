import os
import shutil
from pathlib import Path

# Source and destination directories
static_dir = Path('static/images')
products_dir = Path('media/products')
categories_dir = Path('media/categories')

# Create directories if they don't exist
os.makedirs(products_dir, exist_ok=True)
os.makedirs(categories_dir, exist_ok=True)

# Copy product images
product_images = [
    'Whey Protein Isolate - Chocolate.jpeg',
    'Whey Protein Isolate - Vanilla.jpeg',
    'Plant-Based Protein - Mixed Berry.jpeg',
    'Casein Protein - Chocolate.jpeg',
    'Daily Multivitamin.jpeg',
    'Vitamin D3 + K2.jpeg',
    'Omega-3 Fish Oil.jpeg',
    'Vitamin B Complex.jpeg',
    'Extreme Energy Pre-Workout - Blue Raspberry.jpeg',
    'Stimulant-Free Pre-Workout.jpeg',
    'Creatine Monohydrate.jpeg',
    'BCAA + Electrolytes - Lemon Lime.jpeg',
    'Thermogenic Fat Burner.jpeg',
    'Meal Replacement Shake - Chocolate.jpeg',
    'CLA Softgels.jpeg',
    'Apple Cider Vinegar Gummies.jpeg'
]

# Copy category images
category_images = [
    'Protein category image .png',
    'Vitamins category image .png',
    'Pre-Workout category image.jpeg',
    'Weight Management category image.png'
]

# Process product images
for image in product_images:
    src = static_dir / image
    dest = products_dir / image
    
    if src.exists():
        shutil.copy2(src, dest)
        print(f"Copied {image} to {dest}")
    else:
        print(f"Warning: {image} not found in {static_dir}")

# Process category images
for image in category_images:
    src = static_dir / image
    
    # Create a simplified name for the destination
    if 'Protein' in image:
        dest_name = 'protein.png'
    elif 'Vitamins' in image:
        dest_name = 'vitamins.png'
    elif 'Pre-Workout' in image:
        dest_name = 'pre-workout.jpeg' if image.endswith('.jpeg') else 'pre-workout.png'
    elif 'Weight Management' in image:
        dest_name = 'weight-management.png'
    else:
        dest_name = image
    
    dest = categories_dir / dest_name
    
    if src.exists():
        shutil.copy2(src, dest)
        print(f"Copied {image} to {dest}")
    else:
        print(f"Warning: {image} not found in {static_dir}")

print("Image copying complete!") 