from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from extensions import db, bcrypt, login_manager
from models import Farmer, User
from logic import get_advice

routes = Blueprint('routes', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"error": "Email already registered"}), 400
        
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return jsonify({"message": "Signed up successfully!"})
    
    return render_template('signup.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return jsonify({"message": "Logged in successfully!"})
        return jsonify({"error": "Invalid email or password"}), 401
    
    return render_template('login.html')

@routes.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('routes.login'))

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Check if user is authenticated for POST requests
        if not current_user.is_authenticated:
            return jsonify({'error': 'Please sign up or log in first'}), 401
        
        try:
            data = request.get_json()
            farmer = Farmer(
                name=data['name'],
                district=data['district'],
                sub_county=data['sub_county'],
                crop=data['crop'],
                language=data['language'],
                user_id=current_user.id,
                product_name=data.get('product_name'),
                product_description=data.get('product_description'),
                product_price=data.get('product_price'),
                product_image=data.get('product_image'),
                phone_number=data.get('phone_number')
            )
            db.session.add(farmer)
            db.session.commit()
            return jsonify({'message': 'Farmer registered successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        # For GET requests, show the page even if not authenticated
        return render_template('register.html')

@routes.route('/get-advice')
@login_required
def get_advice_route():
    district = request.args.get('district')
    crop = request.args.get('crop')
    if not district or not crop:
        return redirect(url_for('home'))

    advice = get_advice(district, crop)
    return render_template('advice.html',
                           district=district,
                           crop=crop,
                           advice=advice)

@routes.route('/api/advice')
def advice_api():
    district = request.args.get('district')
    crop = request.args.get('crop')
    if not district or not crop:
        return jsonify({'error': 'Missing parameters'}), 400

    return jsonify({
        'district': district,
        'crop': crop,
        'advice': get_advice(district, crop)
    })

@routes.route('/farmers')
@login_required
def farmers():
    all_farmers = Farmer.query.filter_by(user_id=current_user.id).all()
    return render_template('farmers.html', farmers=all_farmers)

@routes.route('/about')
def about():
    return render_template('about.html')

@routes.route('/marketplace')
def marketplace():
    # Get only specific farmers whose images are working for demo
    allowed_farmers = ['Rebecca Nalongo', 'Robert Tumwine', 'David Walusimbi', 'Sarah Namukasa', 'James Ssemakula']
    products = Farmer.query.filter(
        Farmer.product_name.isnot(None),
        Farmer.name.in_(allowed_farmers)
    ).all()
    return render_template('marketplace.html', products=products)

@routes.route('/contact')
def contact():
    return render_template('contact.html')

@routes.route('/ussd', methods=['POST'])
def ussd():
    print('calling this function from at ussd')
    session_id = request.form.get("sessionId", None)
    service_code = request.form.get("serviceCode", None)
    phone_number = request.form.get("phoneNumber", None)
    text = request.form.get("text", "")

    response = ""
    text_list = text.split("*")

    if text == "":
        response = "CON Welcome to SkyFarm\n1. Register\n2. Get Advice"
    elif text == "1":
        response = "CON Enter your District:"
    elif len(text_list) == 2 and text_list[0] == "1":
        response = "CON Enter your Crop (e.g., Maize):"
    elif len(text_list) == 3 and text_list[0] == "1":
        response = "CON Enter your Preferred Language:"
    elif len(text_list) == 4 and text_list[0] == "1":
        district = text_list[1].strip()
        crop = text_list[2].strip()
        language = text_list[3].strip()

        # For USSD, assign to a default user or handle differently
        default_user = User.query.first()  # Use a default user for USSD registrations
        if not default_user:
            # Create a default user if none exists
            default_user = User(email="ussd@skyfarm.com")
            default_user.set_password("defaultpassword")
            db.session.add(default_user)
            db.session.commit()

        farmer = Farmer(
            name="USSD User",
            district=district,
            crop=crop,
            sub_county="N/A",
            language=language,
            user_id=default_user.id
        )
        db.session.add(farmer)
        db.session.commit()

        response = "END You have been registered successfully!"
    elif text == "2":
        response = "CON Enter your District:"
    elif len(text_list) == 2 and text_list[0] == "2":
        response = "CON Enter Crop:"
    elif len(text_list) == 3 and text_list[0] == "2":
        district = text_list[1]
        crop = text_list[2]
        advice = get_advice(district, crop)
        advice_text = "\n".join(advice[:2])
        response = f"END Advice for {crop} in {district}:\n{advice_text}"
    else:
        response = "END Invalid input. Try again."

    return response