import os
import django
from decimal import Decimal
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitflow.settings')
django.setup()

from core.models import Category, Product, User
from django.contrib.auth.models import User

def create_sample_data():
    # Create a superuser if none exists
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        print("Superuser created successfully.")
    
    # Create categories
    categories = [
        {
            'name': 'Protein',
            'description': 'High-quality protein supplements for muscle building and recovery.',
        },
        {
            'name': 'Vitamins',
            'description': 'Essential vitamins and minerals for overall health and wellbeing.',
        },
        {
            'name': 'Pre-Workout',
            'description': 'Boost your energy and focus for intense workout sessions.',
        },
        {
            'name': 'Weight Management',
            'description': 'Products to help with weight loss and management goals.',
        },
    ]
    
    category_objects = {}
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data['name'],
            defaults={
                'slug': slugify(category_data['name']),
                'description': category_data['description'],
            }
        )
        
        category_objects[category_data['name']] = category
        if created:
            print(f"Created category: {category.name}")
        else:
            print(f"Category already exists: {category.name}")
    
    # Create products
    products = [
        # Protein products
        {
            'name': 'Whey Protein Isolate - Chocolate',
            'category': 'Protein',
            'description': 'Premium whey protein isolate with 27g of protein per serving. Low in fat and carbs, perfect for muscle building and recovery. Delicious chocolate flavor.',
            'price': Decimal('49.99'),
            'sale_price': Decimal('44.99'),
            'stock': 100,
        },
        {
            'name': 'Whey Protein Isolate - Vanilla',
            'category': 'Protein',
            'description': 'Premium whey protein isolate with 27g of protein per serving. Low in fat and carbs, perfect for muscle building and recovery. Smooth vanilla flavor.',
            'price': Decimal('49.99'),
            'sale_price': Decimal('44.99'),
            'stock': 85,
        },
        {
            'name': 'Plant-Based Protein - Mixed Berry',
            'category': 'Protein',
            'description': 'Vegan-friendly plant-based protein with 24g protein per serving. Made from pea, rice, and hemp proteins. Delicious mixed berry flavor.',
            'price': Decimal('54.99'),
            'sale_price': None,
            'stock': 75,
        },
        {
            'name': 'Casein Protein - Chocolate',
            'category': 'Protein',
            'description': 'Slow-digesting casein protein, perfect for overnight recovery. 24g of protein per serving with minimal fat and carbs.',
            'price': Decimal('52.99'),
            'sale_price': Decimal('47.99'),
            'stock': 60,
        },
        
        # Vitamins products
        {
            'name': 'Daily Multivitamin',
            'category': 'Vitamins',
            'description': 'Complete daily multivitamin with essential vitamins and minerals for overall health. Contains vitamins A, B, C, D, E, and essential minerals.',
            'price': Decimal('24.99'),
            'sale_price': None,
            'stock': 120,
        },
        {
            'name': 'Vitamin D3 + K2',
            'category': 'Vitamins',
            'description': 'High-potency Vitamin D3 (5000 IU) with K2 for optimal calcium absorption and bone health.',
            'price': Decimal('19.99'),
            'sale_price': Decimal('17.99'),
            'stock': 90,
        },
        {
            'name': 'Omega-3 Fish Oil',
            'category': 'Vitamins',
            'description': 'Premium fish oil supplement rich in EPA and DHA omega-3 fatty acids for heart, brain, and joint health.',
            'price': Decimal('29.99'),
            'sale_price': None,
            'stock': 85,
        },
        {
            'name': 'Vitamin B Complex',
            'category': 'Vitamins',
            'description': 'Complete B-complex with all essential B vitamins for energy production, nervous system health, and cell metabolism.',
            'price': Decimal('22.99'),
            'sale_price': Decimal('19.99'),
            'stock': 70,
        },
        
        # Pre-Workout products
        {
            'name': 'Extreme Energy Pre-Workout - Blue Raspberry',
            'category': 'Pre-Workout',
            'description': 'High-intensity pre-workout formula with caffeine, beta-alanine, and creatine. Boosts energy, focus, and pumps during training.',
            'price': Decimal('39.99'),
            'sale_price': Decimal('34.99'),
            'stock': 65,
        },
        {
            'name': 'Stimulant-Free Pre-Workout',
            'category': 'Pre-Workout',
            'description': 'Caffeine-free pre-workout with pump-enhancing ingredients like citrulline malate, betaine, and nitric oxide boosters.',
            'price': Decimal('37.99'),
            'sale_price': None,
            'stock': 50,
        },
        {
            'name': 'Creatine Monohydrate',
            'category': 'Pre-Workout',
            'description': 'Pure micronized creatine monohydrate for increased strength, power, and muscle recovery. 5g per serving.',
            'price': Decimal('29.99'),
            'sale_price': Decimal('24.99'),
            'stock': 110,
        },
        {
            'name': 'BCAA + Electrolytes - Lemon Lime',
            'category': 'Pre-Workout',
            'description': '2:1:1 ratio of branched-chain amino acids with added electrolytes for hydration and recovery during training.',
            'price': Decimal('34.99'),
            'sale_price': None,
            'stock': 75,
        },
        
        # Weight Management products
        {
            'name': 'Thermogenic Fat Burner',
            'category': 'Weight Management',
            'description': 'Advanced thermogenic formula to boost metabolism and support fat loss. Contains green tea extract, caffeine, and L-carnitine.',
            'price': Decimal('44.99'),
            'sale_price': Decimal('39.99'),
            'stock': 60,
        },
        {
            'name': 'Meal Replacement Shake - Chocolate',
            'category': 'Weight Management',
            'description': 'Complete meal replacement with balanced macros, vitamins, and minerals. 20g protein, 5g fiber, and only 200 calories per serving.',
            'price': Decimal('42.99'),
            'sale_price': None,
            'stock': 85,
        },
        {
            'name': 'CLA Softgels',
            'category': 'Weight Management',
            'description': 'Conjugated Linoleic Acid to support fat metabolism and lean muscle maintenance. 1000mg per softgel.',
            'price': Decimal('32.99'),
            'sale_price': Decimal('27.99'),
            'stock': 70,
        },
        {
            'name': 'Apple Cider Vinegar Gummies',
            'category': 'Weight Management',
            'description': 'Delicious apple cider vinegar gummies with "the mother" for digestive health and metabolism support.',
            'price': Decimal('24.99'),
            'sale_price': None,
            'stock': 95,
        },
    ]
    
    for product_data in products:
        category = category_objects[product_data['category']]
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'slug': slugify(product_data['name']),
                'category': category,
                'description': product_data['description'],
                'price': product_data['price'],
                'sale_price': product_data['sale_price'],
                'stock': product_data['stock'],
                'is_available': True,
            }
        )
        
        if created:
            print(f"Created product: {product.name}")
        else:
            print(f"Product already exists: {product.name}")

if __name__ == '__main__':
    print("Starting data creation...")
    create_sample_data()
    print("Sample data creation completed!") 