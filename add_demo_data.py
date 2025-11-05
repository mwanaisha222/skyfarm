"""
Demo Data Script for SkyFarm Marketplace
This script adds sample farmers with products for demonstration purposes
Run this script: python add_demo_data.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from extensions import db
from models import User, Farmer

# Demo data with real images from Unsplash
demo_farmers = [
    {
        "email": "john.mukasa@example.com",
        "password": "password123",
        "name": "John Mukasa",
        "district": "Kampala",
        "sub_county": "Rubaga",
        "crop": "Maize",
        "language": "English",
        "product_name": "Fresh Yellow Maize",
        "product_description": "High-quality yellow maize, freshly harvested from organic farms. Perfect for posho and animal feed.",
        "product_price": 150000,
        "product_image": "https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=800&q=80",
        "phone_number": "+256700123456"
    },
    {
        "email": "mary.nakato@example.com",
        "password": "password123",
        "name": "Mary Nakato",
        "district": "Mbale",
        "sub_county": "Bududa",
        "crop": "Coffee",
        "language": "Luganda",
        "product_name": "Arabica Coffee Beans",
        "product_description": "Premium Arabica coffee beans from the slopes of Mount Elgon. Sun-dried and carefully sorted.",
        "product_price": 25000,
        "product_image": "https://images.unsplash.com/photo-1447933601403-0c6688de566e?w=800&q=80",
        "phone_number": "+256701234567"
    },
    {
        "email": "peter.okello@example.com",
        "password": "password123",
        "name": "Peter Okello",
        "district": "Gulu",
        "sub_county": "Bungatira",
        "crop": "Beans",
        "language": "Luo",
        "product_name": "Red Kidney Beans",
        "product_description": "Organic red kidney beans, rich in protein. Grown without chemical fertilizers.",
        "product_price": 8000,
        "product_image": "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=800&q=80",
        "phone_number": "+256702345678"
    },
    {
        "email": "sarah.namukasa@example.com",
        "password": "password123",
        "name": "Sarah Namukasa",
        "district": "Masaka",
        "sub_county": "Kyanamukaaka",
        "crop": "Bananas",
        "language": "Luganda",
        "product_name": "Sweet Bananas (Bogoya)",
        "product_description": "Fresh sweet bananas, perfect for eating raw or making juice. Harvested daily.",
        "product_price": 5000,
        "product_image": "https://images.unsplash.com/photo-1603833665858-e61d17a86224?w=800",
        "phone_number": "+256703456789"
    },
    {
        "email": "david.walusimbi@example.com",
        "password": "password123",
        "name": "David Walusimbi",
        "district": "Mbarara",
        "sub_county": "Kashari",
        "crop": "Tomatoes",
        "language": "Runyankole",
        "product_name": "Fresh Red Tomatoes",
        "product_description": "Juicy red tomatoes, perfect for cooking. Pesticide-free and vine-ripened.",
        "product_price": 3500,
        "product_image": "https://images.unsplash.com/photo-1546470427-227e4bc6ed17?w=800&q=80",
        "phone_number": "+256704567890"
    },
    {
        "email": "grace.akello@example.com",
        "password": "password123",
        "name": "Grace Akello",
        "district": "Lira",
        "sub_county": "Adekokwok",
        "crop": "Groundnuts",
        "language": "Lango",
        "product_name": "Raw Groundnuts (Peanuts)",
        "product_description": "Fresh groundnuts from Northern Uganda. High oil content, perfect for paste or roasting.",
        "product_price": 12000,
        "product_image": "https://images.unsplash.com/photo-1582033043894-d4f89ff73b7f?w=800&q=80",
        "phone_number": "+256705678901"
    },
    {
        "email": "james.ssemakula@example.com",
        "password": "password123",
        "name": "James Ssemakula",
        "district": "Jinja",
        "sub_county": "Butembe",
        "crop": "Rice",
        "language": "Lusoga",
        "product_name": "Upland Rice",
        "product_description": "Quality upland rice from Jinja wetlands. Polished and ready for cooking.",
        "product_price": 4500,
        "product_image": "https://images.unsplash.com/photo-1516684732162-798a0062be99?w=800&q=80",
        "phone_number": "+256706789012"
    },
    {
        "email": "alice.nabirye@example.com",
        "password": "password123",
        "name": "Alice Nabirye",
        "district": "Soroti",
        "sub_county": "Asuret",
        "crop": "Cassava",
        "language": "Ateso",
        "product_name": "Fresh Cassava Tubers",
        "product_description": "Fresh cassava roots, perfect for making flour or cooking. Sweet and starchy.",
        "product_price": 2000,
        "product_image": "https://images.unsplash.com/photo-1591192350348-c76f9e3e2f7b?w=800",
        "phone_number": "+256707890123"
    },
    {
        "email": "robert.tumwine@example.com",
        "password": "password123",
        "name": "Robert Tumwine",
        "district": "Kabale",
        "sub_county": "Rubaya",
        "crop": "Irish Potatoes",
        "language": "Rukiga",
        "product_name": "Irish Potatoes",
        "product_description": "Fresh Irish potatoes from the highlands of Kabale. Perfect for chips and cooking.",
        "product_price": 3000,
        "product_image": "https://images.unsplash.com/photo-1518977825259-1573e93f5e78?w=800&q=80",
        "phone_number": "+256708901234"
    },
    {
        "email": "rebecca.nalongo@example.com",
        "password": "password123",
        "name": "Rebecca Nalongo",
        "district": "Wakiso",
        "sub_county": "Nangabo",
        "crop": "Pineapples",
        "language": "Luganda",
        "product_name": "Sweet Pineapples",
        "product_description": "Sweet and juicy pineapples, perfect for fresh juice or eating. Naturally grown.",
        "product_price": 6000,
        "product_image": "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?w=800",
        "phone_number": "+256709012345"
    },
    {
        "email": "samuel.kato@example.com",
        "password": "password123",
        "name": "Samuel Kato",
        "district": "Hoima",
        "sub_county": "Kyangwali",
        "crop": "Sweet Potatoes",
        "language": "Runyoro",
        "product_name": "Orange-Fleshed Sweet Potatoes",
        "product_description": "Vitamin A-rich orange sweet potatoes. Nutritious and delicious for the whole family.",
        "product_price": 2500,
        "product_image": "https://images.unsplash.com/photo-1589927986089-35812378b6a3?w=800",
        "phone_number": "+256710123456"
    },
    {
        "email": "florence.namazzi@example.com",
        "password": "password123",
        "name": "Florence Namazzi",
        "district": "Mukono",
        "sub_county": "Nama",
        "crop": "Passion Fruits",
        "language": "Luganda",
        "product_name": "Fresh Passion Fruits",
        "product_description": "Ripe passion fruits with high juice content. Perfect for juice making and desserts.",
        "product_price": 8000,
        "product_image": "https://images.unsplash.com/photo-1502389369948-ad0ba9e432e9?w=800",
        "phone_number": "+256711234567"
    }
]

def add_demo_data():
    """Add demo farmers to the database"""
    app = create_app()
    
    with app.app_context():
        print("\n" + "="*60)
        print("SkyFarm Marketplace - Demo Data Setup")
        print("="*60)
        print("\nStarting to add demo data...\n")
        
        # Check if demo data already exists
        existing_demo = User.query.filter_by(email="john.mukasa@example.com").first()
        if existing_demo:
            print("⚠️  Demo data already exists in the database!")
            print("Demo data has already been added previously.")
            print("\nYou can:")
            print("1. Visit the marketplace: http://127.0.0.1:5000/marketplace")
            print("2. Login with demo credentials:")
            print("   Email: john.mukasa@example.com")
            print("   Password: password123")
            return
        
        print("Adding 12 demo farmers with products...")
        
        # Add demo farmers
        added_count = 0
        for i, farmer_data in enumerate(demo_farmers, 1):
            try:
                # Create user account
                user = User(email=farmer_data['email'])
                user.set_password(farmer_data['password'])
                db.session.add(user)
                db.session.flush()  # Get the user ID
                
                # Create farmer profile with product
                farmer = Farmer(
                    name=farmer_data['name'],
                    district=farmer_data['district'],
                    sub_county=farmer_data['sub_county'],
                    crop=farmer_data['crop'],
                    language=farmer_data['language'],
                    user_id=user.id,
                    product_name=farmer_data['product_name'],
                    product_description=farmer_data['product_description'],
                    product_price=farmer_data['product_price'],
                    product_image=farmer_data['product_image'],
                    phone_number=farmer_data['phone_number']
                )
                db.session.add(farmer)
                added_count += 1
                print(f"  [{i}/12] ✓ {farmer_data['name']} - {farmer_data['product_name']}")
                
            except Exception as e:
                print(f"  [{i}/12] ✗ Error adding {farmer_data['name']}: {str(e)}")
                db.session.rollback()
                continue
        
        # Commit all changes
        try:
            db.session.commit()
            print("\n" + "="*60)
            print(f"🎉 SUCCESS! Added {added_count} demo farmers to the marketplace!")
            print("="*60)
            print("\n✅ Your marketplace is now ready for demo!")
            print("\n📋 Next Steps:")
            print("   1. Make sure Flask is running: python app.py")
            print("   2. Visit: http://127.0.0.1:5000/marketplace")
            print("   3. You should see 12 products with images!")
            print("\n🔑 Demo Login Credentials (you can use any):")
            print("   Email: john.mukasa@example.com")
            print("   Email: mary.nakato@example.com")
            print("   Email: peter.okello@example.com")
            print("   Password: password123")
            print("\n" + "="*60 + "\n")
            
        except Exception as e:
            db.session.rollback()
            print(f"\n✗ Error committing to database: {str(e)}")
            print("Please make sure the database schema is up to date.")

if __name__ == "__main__":
    add_demo_data()
