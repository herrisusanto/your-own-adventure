# Your Own Adventure - Interactive Story Generator

A full-stack web application that generates and plays interactive "Choose Your Own Adventure" stories using AI. Users can input a theme, and the system will create a branching narrative with multiple paths and endings.

## 🚀 Features

- **AI-Powered Story Generation**: Uses OpenAI's GPT-4 to create dynamic, branching stories
- **Interactive Story Play**: Navigate through story branches with clickable choices
- **Asynchronous Processing**: Background job processing for story generation
- **Session Management**: Track user sessions and story progress
- **Multiple Endings**: Stories include both winning and losing endings
- **Real-time Status Updates**: Live polling for story generation progress
- **Responsive Design**: Modern, mobile-friendly interface

## 🏗️ Architecture

### Backend (FastAPI)

- **Framework**: FastAPI with async support
- **Database**: SQLite with SQLAlchemy ORM
- **AI Integration**: LangChain with OpenAI GPT-4
- **Background Tasks**: FastAPI BackgroundTasks for story generation
- **API Documentation**: Auto-generated OpenAPI/Swagger docs

### Frontend (React)

- **Framework**: React 19 with Vite build system
- **Routing**: React Router DOM for navigation
- **HTTP Client**: Axios for API communication
- **State Management**: React hooks (useState, useEffect)
- **Styling**: CSS with modern responsive design

## 🛠️ Tech Stack

### Backend Dependencies

- **FastAPI** (0.117.1+) - Modern, fast web framework
- **LangChain** (0.3.27+) - AI/LLM framework
- **LangChain OpenAI** (0.3.33+) - OpenAI integration
- **SQLAlchemy** (2.0.43+) - Database ORM
- **Psycopg2** (2.9.10+) - PostgreSQL adapter
- **Uvicorn** (0.36.0+) - ASGI server
- **Python-dotenv** (1.1.1+) - Environment variable management

### Frontend Dependencies

- **React** (19.1.1) - UI library
- **React DOM** (19.1.1) - React rendering
- **React Router DOM** (7.9.1) - Client-side routing
- **Axios** (1.12.2) - HTTP client
- **Vite** (7.1.7) - Build tool and dev server

### Development Tools

- **ESLint** - Code linting
- **TypeScript** - Type definitions
- **Pydantic** - Data validation and settings

## 📁 Project Structure

```
your-own-adventure/
├── backend/
│   ├── core/
│   │   ├── config.py          # Application settings
│   │   ├── models.py          # Pydantic models for AI responses
│   │   ├── promps.py          # AI prompts for story generation
│   │   └── story_generator.py # Core story generation logic
│   ├── db/
│   │   └── database.py        # Database configuration and session
│   ├── models/
│   │   ├── job.py            # Background job models
│   │   └── story.py          # Story and story node models
│   ├── routers/
│   │   ├── job.py            # Job status endpoints
│   │   └── story.py          # Story creation and retrieval endpoints
│   ├── schemas/
│   │   ├── job.py            # Job request/response schemas
│   │   └── story.py          # Story request/response schemas
│   ├── main.py               # FastAPI application entry point
│   └── pyproject.toml        # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── LoadingStatus.jsx    # Story generation progress
│   │   │   ├── StoryGame.jsx        # Interactive story player
│   │   │   ├── StoryGenerator.jsx   # Story creation interface
│   │   │   ├── StoryLoader.jsx      # Story loading component
│   │   │   └── ThemeInput.jsx       # Theme input form
│   │   ├── App.jsx            # Main application component
│   │   ├── main.jsx           # Application entry point
│   │   └── util.js            # Utility functions
│   ├── package.json           # Node.js dependencies
│   └── vite.config.js         # Vite configuration
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Node.js 18+
- OpenAI API key

### Backend Setup

1. **Navigate to backend directory**:

   ```bash
   cd backend
   ```

2. **Install dependencies**:

   ```bash
   pip install -e .
   ```

3. **Set up environment variables**:
   Create a `.env` file in the backend directory:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   DATABASE_URL=sqlite:///./database.db
   ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
   DEBUG=True
   ```

4. **Run the backend server**:
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`
   - Alternative docs: `http://localhost:8000/redoc`

### Frontend Setup

1. **Navigate to frontend directory**:

   ```bash
   cd frontend
   ```

2. **Install dependencies**:

   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`

## 🎮 How to Use

1. **Start the Application**: Open `http://localhost:5173` in your browser
2. **Enter a Theme**: Input a story theme (e.g., "space adventure", "medieval fantasy")
3. **Generate Story**: Click "Generate Story" to create your interactive adventure
4. **Play the Story**: Navigate through the story by clicking on different options
5. **Explore Endings**: Discover different paths and endings in your generated story

## 🔧 API Endpoints

### Story Management

- `POST /api/stories/create` - Create a new story (returns job ID)
- `GET /api/stories/{story_id}/complete` - Get complete story structure

### Job Management

- `GET /api/jobs/{job_id}` - Check story generation job status

## 🗄️ Database Schema

### Stories Table

- `id` - Primary key
- `title` - Story title
- `session_id` - User session identifier
- `created_at` - Creation timestamp

### Story Nodes Table

- `id` - Primary key
- `story_id` - Foreign key to stories
- `content` - Node text content
- `is_root` - Whether this is the starting node
- `is_ending` - Whether this is an ending node
- `is_winning_ending` - Whether this is a winning ending
- `options` - JSON array of available choices

## 🔐 Environment Variables

### Backend (.env)

```env
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=sqlite:///./database.db
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173
DEBUG=True
API_PREFIX=/api
```

## 🚀 Deployment

### Backend Deployment

1. Set up a PostgreSQL database for production
2. Update `DATABASE_URL` in environment variables
3. Deploy using Docker or a cloud platform like Heroku, Railway, or AWS

### Frontend Deployment

1. Build the production bundle:
   ```bash
   npm run build
   ```
2. Deploy the `dist` folder to a static hosting service like Vercel, Netlify, or AWS S3

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Troubleshooting

### Common Issues

1. **OpenAI API Key Error**: Ensure your API key is correctly set in the `.env` file
2. **CORS Issues**: Check that `ALLOWED_ORIGINS` includes your frontend URL
3. **Database Connection**: Verify the database URL is correct
4. **Port Conflicts**: Ensure ports 8000 and 5173 are available

### Debug Mode

Enable debug mode by setting `DEBUG=True` in your `.env` file for detailed error messages.

---

**Happy Storytelling!** 🎭✨
