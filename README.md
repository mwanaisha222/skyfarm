# 🌱 SkyFarm - Agricultural Management Platform

**SkyFarm** is a comprehensive agricultural management platform designed to empower farmers across Uganda with modern farming solutions, market access, and expert advice.

## ✨ Features

### 🌾 Farmers Marketplace
- Buy and sell fresh produce directly from farmers
- Product listings with images, descriptions, and pricing
- Contact farmers directly via phone
- Browse products from across Uganda

### 📱 USSD Accessibility
- Access platform features via USSD codes
- No internet required
- Available in multiple local languages (English, Luganda, Luo, Runyankole, Ateso, etc.)

### 🎯 Tailored Recommendations
- Crop-specific advice based on location
- Weather-based farming tips
- Best practices for sustainable farming

### 👥 Farmer Registration & Management
- Easy farmer registration
- Profile management
- Crop and location tracking

### 📞 Contact & Support
- Direct contact information
- Support email and phone
- Office location details

## 🚀 Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Password Hashing**: Flask-Bcrypt
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Template Engine**: Jinja2

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/skyfarm.git
   cd skyfarm
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the database**
   ```bash
   python app.py
   ```
   The database will be created automatically on first run.

6. **Add demo data (optional)**
   ```bash
   python add_demo_data.py
   ```
   This will populate the marketplace with 12 sample farmers and products.

## 🏃‍♂️ Running the Application

1. **Start the Flask development server**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to**
   ```
   http://127.0.0.1:5000
   ```

## 📱 Demo Credentials

After running `add_demo_data.py`, you can login with:
- **Email**: john.mukasa@example.com
- **Password**: password123

(Other demo accounts available - check `add_demo_data.py`)

## 📂 Project Structure

```
skyfarm/
├── app.py                 # Application factory and initialization
├── routes.py              # All route handlers
├── models.py              # Database models (User, Farmer)
├── extensions.py          # Flask extensions (db, bcrypt, login_manager)
├── logic.py               # Business logic for advice generation
├── config.py              # Configuration settings
├── add_demo_data.py       # Script to add demo data
├── requirements.txt       # Python dependencies
├── instance/              # Instance folder (contains database)
│   └── farmers.db         # SQLite database
├── static/                # Static files (CSS, JS, images)
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Landing page
│   ├── marketplace.html  # Marketplace page
│   ├── register.html     # Farmer registration
│   ├── farmers.html      # Farmers list
│   ├── signup.html       # User signup
│   ├── login.html        # User login
│   ├── about.html        # About page
│   └── contact.html      # Contact page
└── .gitignore            # Git ignore file
```

## 🌟 Key Features in Detail

### Marketplace
- **Full-width responsive grid layout** (5 products per row on desktop)
- **Real product images** from Unsplash
- **Price display** in Ugandan Shillings (UGX)
- **Farmer information** with location details
- **Direct contact** buttons with phone integration

### User Authentication
- Secure password hashing with Bcrypt
- Session management with Flask-Login
- Protected routes for authenticated users

### Farmer Registration
- Comprehensive registration form
- Optional marketplace product listing
- Location-based organization (district, sub-county)
- Multi-language support

### USSD Integration
- Accessible advice system
- No internet required
- Local language support

## 🎨 Color Scheme

SkyFarm uses an agricultural green color palette:
- Primary: `#2E7D32`
- Secondary: `#558B2F`, `#689F38`
- Accent: `#7CB342`, `#C5E1A5`
- Light: `#E8F5E9`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- Your Name - Initial work

## 🙏 Acknowledgments

- Built for Ugandan farmers
- Inspired by the need for accessible agricultural solutions
- Images courtesy of Unsplash

## 📧 Contact

- **Email**: support@skyfarm.com
- **Phone**: +256 700 000 000
- **Location**: Kampala, Uganda

---

**SkyFarm** - Cultivating a Greener Future 🌱
