# 🍳 Annapurna v4.0

> Your AI-Powered Cooking Assistant with Voice Commands, Recipe Management, and Smart Inventory Tracking

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

### 🤖 AI-Powered Chat
- Natural language recipe requests with Groq LLM
- Context-aware cooking assistance
- Multiple AI model support (Llama, Mixtral, Gemma)
- Conversation history with Firebase persistence

### 🎙️ Voice Interaction
- Voice input for hands-free recipe queries
- Text-to-speech recipe narration
- Real-time speech recognition

### 📚 Recipe Management
- **Smart Recipe Storage**: Save and categorize recipes
- **Favorites System**: Quick access to preferred recipes
- **Recipe Import**: Extract recipes from PDFs, images, and YouTube videos
- **YouTube Integration**: Automatic transcript extraction and recipe generation
- **Advanced Search**: Filter by cuisine, dietary restrictions, cooking time

### 🥘 Meal Planning
- Weekly meal scheduler with drag-and-drop
- Custom diet chart creator
- Nutritional tracking
- Meal prep suggestions

### 🛒 Smart Inventory & Grocery Management
- Real-time inventory tracking with expiry dates
- Price monitoring and cost analysis
- Automatic grocery list generation
- Low stock alerts
- Budget tracking

### 🌱 Dietary Preferences
- Jain mode (no onion, garlic, root vegetables)
- Allergy tracking and substitution suggestions
- Custom dietary restrictions
- Vegan/vegetarian/keto options

### 🔒 User Authentication
- Firebase Google Sign-In
- Secure user profiles
- Cloud-based data sync
- Multi-device support

### 📱 Progressive Web App (PWA)
- Install as mobile app
- Offline functionality
- Native app experience
- Cross-platform support

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
Firebase account
Groq API key
Google Cloud API key (for YouTube integration)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Annapurna-ver4.git
cd Annapurna-ver4
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.streamlit/secrets.toml` file:

```toml
[groq]
api_key = "your_groq_api_key"

[openai]
api_key = "your_openai_api_key"

[google]
youtube_api_key = "your_youtube_api_key"

[firebase]
project_id = "your_project_id"
private_key_id = "your_private_key_id"
private_key = "your_private_key"
client_email = "your_client_email"
client_id = "your_client_id"
client_x509_cert_url = "your_cert_url"

[firebase_web]
apiKey = "your_web_api_key"
authDomain = "your_auth_domain"
projectId = "your_project_id"
storageBucket = "your_storage_bucket"
messagingSenderId = "your_messaging_sender_id"
appId = "your_app_id"
```

4. **Run the application**
```bash
streamlit run hey_chef_chat.py
```

## 📖 Usage Guide

### Basic Chat Interaction

```python
# Ask for recipe suggestions
"I have chicken and broccoli, what can I make?"

# Get step-by-step instructions
"How do I make butter chicken?"

# Request dietary modifications
"Make this recipe vegan"
```

### Voice Commands

1. Click the 🎤 microphone button
2. Speak your query clearly
3. Wait for transcription and AI response
4. Use 🔊 to hear the recipe read aloud

### Recipe Management

#### Saving Recipes
- Chat with AI to get a recipe
- Click "💾 Save Recipe" button
- Add tags and categories
- Stored in Firebase cloud storage

#### Importing Recipes
- **From PDF**: Upload cooking books or printed recipes
- **From Image**: OCR extraction from recipe photos
- **From YouTube**: Paste video URL for automatic transcript extraction

### Inventory Management

```python
# Add items
Inventory Tab → Add Item → Enter details

# Track expiry
Set expiration dates → Get automatic alerts

# Price tracking
Record prices → View spending analytics

# Generate grocery list
Inventory automatically suggests items to restock
```

## 🏗️ Architecture

```
Annapurna-ver4/
├── hey_chef_chat.py        # Main application
├── requirements.txt        # Dependencies
├── .streamlit/
│   ├── secrets.toml       # API keys (gitignored)
│   └── config.toml        # Streamlit configuration
├── static/                # Static assets
│   ├── manifest.json      # PWA manifest
│   └── service-worker.js  # PWA service worker
├── docs/                  # Documentation
└── tests/                 # Unit tests
```

### Tech Stack

- **Frontend**: Streamlit
- **AI/ML**: Groq (Llama 3.3), OpenAI GPT-4
- **Database**: Firebase Firestore
- **Authentication**: Firebase Auth
- **Speech**: Google Speech Recognition, gTTS
- **OCR**: Tesseract, GPT-4 Vision
- **APIs**: YouTube Data API v3

## 🔧 Configuration

### AI Model Selection

Models available in the sidebar:
- `llama-3.3-70b-versatile` (Default, best for recipes)
- `llama-3.1-70b-versatile`
- `mixtral-8x7b-32768`
- `gemma2-9b-it`

### Customization

Edit `st.session_state` defaults in `hey_chef_chat.py`:

```python
# Change default model
st.session_state.selected_model = "llama-3.3-70b-versatile"

# Adjust conversation memory
MAX_HISTORY = 10

# Modify temperature
temperature = 0.7
```

## 📊 Features in Detail

### 1. Recipe Generation
- Context-aware AI understands cooking preferences
- Generates recipes based on available ingredients
- Suggests substitutions for missing items
- Scales recipes for different serving sizes

### 2. YouTube Recipe Extraction
```python
# Paste YouTube URL
"Extract recipe from: https://youtube.com/watch?v=..."

# AI processes transcript
# Generates formatted recipe with ingredients & steps
```

### 3. Meal Planning
- Weekly calendar view
- Drag-and-drop meal assignment
- Nutritional balance suggestions
- Shopping list auto-generation from meal plan

### 4. Inventory Intelligence
- Expiry tracking with color-coded alerts
- Price comparison over time
- Consumption patterns analysis
- Automated reorder suggestions

## 🔐 Security & Privacy

- Firebase Authentication with Google Sign-In
- Encrypted data transmission
- User data isolation in Firestore
- No data sharing with third parties
- GDPR compliant

## 🌍 Deployment

### Streamlit Cloud

1. Push to GitHub
2. Connect repository to Streamlit Cloud
3. Add secrets in Streamlit dashboard
4. Deploy with one click

### Docker (Coming Soon)

```bash
docker build -t annapurna .
docker run -p 8501:8501 annapurna
```

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Fork and clone
git clone https://github.com/yourusername/Annapurna-ver4.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

## 🐛 Known Issues

- Voice input may not work on all browsers (Chrome recommended)
- PDF extraction accuracy depends on document quality
- YouTube transcript availability varies by video

## 📝 Roadmap

- [ ] Multi-language support
- [ ] Nutritional API integration
- [ ] Barcode scanning for inventory
- [ ] Recipe sharing community
- [ ] Meal prep automation
- [ ] Integration with grocery delivery APIs
- [ ] Advanced analytics dashboard

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Manas**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Groq for fast LLM inference
- Firebase for backend infrastructure
- Streamlit for the amazing framework
- OpenAI for GPT-4 Vision
- The open-source community

## 📞 Support

- 📧 Email: support@annapurna.app
- 💬 Discord: [Join our community](https://discord.gg/annapurna)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/Annapurna-ver4/issues)

---

**Made with ❤️ by Manas** | Powered by AI | Built with Streamlit
