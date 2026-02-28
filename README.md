# 🍳 Annapurna - AI Cooking Assistant

Your intelligent AI-powered cooking companion that helps you cook amazing Indian dishes!
Try https://kitchenmate.streamlit.app

## ✨ Features

- **💬 AI Chat** - Ask anything about cooking with our AI assistant
- **📅 Meal Planner** - Plan your weekly meals
- **🛒 Grocery & Inventory** - Manage ingredients and shopping lists
- **🍲 Custom Recipes** - Save and organize your favorite recipes
- **🔥 Tried Recipes** - Track recipes you've made
- **❤️ Favorites** - Save your favorite recipes
- **📸 Ingredient Scanner** - Take photos of ingredients for instant identification
- **🧾 Receipt Scanner** - Scan receipts to add items to inventory
- **🥗 Diet Charts** - View nutrition and diet information
- **🎤 Voice Assistant** (local only) - Voice commands and responses on desktop

## 🚀 Quick Start

### Local Development
```bash
pip install -r requirements.txt
streamlit run hey_chef_chat.py
```

### Deploy on Streamlit Cloud
See [STREAMLIT_DEPLOYMENT.md](STREAMLIT_DEPLOYMENT.md) for detailed instructions.

## 📋 Requirements

- Python 3.9+
- Streamlit
- Firebase account
- Groq API key
- OpenRouter API key
- YouTube API key

## 🔧 Configuration

### Local Setup
Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your-key"
OPENROUTER_API_KEY = "your-key"
YOUTUBE_API_KEY = "your-key"

[firebase]
project_id = "your-project"
private_key = "your-key"
# ... other Firebase credentials

[firebase_web]
apiKey = "your-key"
# ... other Firebase web config
```

### Streamlit Cloud
Add secrets via app dashboard → Settings → Secrets

## 🗺️ Project Structure

```
annapurna/
├── hey_chef_chat.py           # Main application
├── requirements.txt           # Python dependencies
├── .streamlit/
│   ├── config.toml           # Streamlit configuration
│   └── secrets.toml          # Secrets (local only)
├── STREAMLIT_DEPLOYMENT.md   # Cloud deployment guide
├── GOOGLE_LOGIN_SETUP.md     # Google authentication setup
└── README.md                  # This file
```

## 🌟 Features in Detail

### Chat Assistant
- Powered by Groq's advanced LLMs
- Understand cooking techniques
- Provide recipes and cooking tips
- Support for Hinglish and English
- Allergies and dietary restrictions

### Meal Planning
- Plan meals day-by-day
- Select meal times (breakfast, lunch, dinner, snacks)
- Get recipe suggestions
- Check nutrition information

### Inventory Management
- Track all ingredients at home
- Monitor expiry dates
- Price tracking per ingredient
- Low stock alerts

### Recipe Discovery
- Extract recipes from YouTube videos
- Process transcripts with AI
- Create custom recipes
- Import from descriptions

### User Preferences
- Jain diet mode (no root vegetables)
- Vegan/Vegetarian options
- Unit system (metric/imperial)
- Language preferences
- Allergy tracking

## 🔐 Security & Privacy

- Firebase authentication for secure login
- Google OAuth for seamless sign-in
- Encrypted secrets management
- No sensitive data in version control
- Guest mode for quick access

## 🐛 Troubleshooting

### ModuleNotFoundError
- Install requirements: `pip install -r requirements.txt`
- On Cloud: Ensure all packages in requirements.txt

### Firebase errors
- Verify credentials in secrets
- Check Firebase project is active
- Ensure correct project ID

### Voice not working
- This is expected on Cloud - no microphone access
- Local development: Install audio dependencies
- Check microphone permissions on your device

## 📞 Support

- GitHub: [Your repository URL]
- Firebase: https://support.google.com/firebase
- Streamlit: https://discuss.streamlit.io

## 📄 License

MIT License - Feel free to use and modify!

## 🙏 Credits

Built with:
- [Streamlit](https://streamlit.io)
- [Firebase](https://firebase.google.com)
- [Groq](https://groq.com)
- [OpenRouter](https://openrouter.ai)
- ❤️ Passion for cooking!

---

**Happy Cooking! 🍳✨**

Made with ❤️ for food lovers everywhere

