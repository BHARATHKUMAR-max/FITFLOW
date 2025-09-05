import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitflow.settings')
django.setup()

from core.models import Product, Category
from django.core.files import File
from pathlib import Path

# Paths to the image directories
products_dir = Path('media/products')
categories_dir = Path('media/categories')

def update_product_images():
    # Map product names to their image files
    image_mapping = {
        'Whey Protein Isolate - Chocolate': 'Whey Protein Isolate - Chocolate.jpeg',
        'Whey Protein Isolate - Vanilla': 'Whey Protein Isolate - Vanilla.jpeg',
        'Plant-Based Protein - Mixed Berry': 'Plant-Based Protein - Mixed Berry.jpeg',
        'Casein Protein - Chocolate': 'Casein Protein - Chocolate.jpeg',
        'Daily Multivitamin': 'Daily Multivitamin.jpeg',
        'Vitamin D3 + K2': 'Vitamin D3 + K2.jpeg',
        'Omega-3 Fish Oil': 'Omega-3 Fish Oil.jpeg',
        'Vitamin B Complex': 'Vitamin B Complex.jpeg',
        'Extreme Energy Pre-Workout - Blue Raspberry': 'Extreme Energy Pre-Workout - Blue Raspberry.jpeg',
        'Stimulant-Free Pre-Workout': 'Stimulant-Free Pre-Workout.jpeg',
        'Creatine Monohydrate': 'Creatine Monohydrate.jpeg',
        'BCAA + Electrolytes - Lemon Lime': 'BCAA + Electrolytes - Lemon Lime.jpeg',
        'Thermogenic Fat Burner': 'Thermogenic Fat Burner.jpeg',
        'Meal Replacement Shake - Chocolate': 'Meal Replacement Shake - Chocolate.jpeg',
        'CLA Softgels': 'CLA Softgels.jpeg',
        'Apple Cider Vinegar Gummies': 'Apple Cider Vinegar Gummies.jpeg'
    }
    
    # Update each product
    for product_name, image_file in image_mapping.items():
        try:
            product = Product.objects.get(name=product_name)
            image_path = products_dir / image_file
            
            if image_path.exists():
                with open(image_path, 'rb') as img_file:
                    product.image.save(image_file, File(img_file), save=True)
                print(f"Updated image for {product_name}")
            else:
                print(f"Image file not found: {image_path}")
        except Product.DoesNotExist:
            print(f"Product not found: {product_name}")

def update_category_images():
    # Map category names to their image files
    image_mapping = {
        'Protein': 'protein.png',
        'Vitamins': 'vitamins.png',
        'Pre-Workout': 'pre-workout.jpeg',
        'Weight Management': 'weight-management.png'
    }
    
    # Update each category
    for category_name, image_file in image_mapping.items():
        try:
            category = Category.objects.get(name=category_name)
            image_path = categories_dir / image_file
            
            if image_path.exists():
                with open(image_path, 'rb') as img_file:
                    category.image.save(image_file, File(img_file), save=True)
                print(f"Updated image for {category_name} category")
            else:
                print(f"Image file not found: {image_path}")
        except Category.DoesNotExist:
            print(f"Category not found: {category_name}")

if __name__ == "__main__":
    update_product_images()
    update_category_images()
    print("Database update complete!") 