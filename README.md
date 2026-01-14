# MindMapAI ![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-MIT-yellowgreen)

## Project Description
MindMapAI is an innovative web application that allows users to create interactive mind maps enhanced by AI. Users can brainstorm ideas collaboratively in real-time, with the AI providing suggestions and context from integrated knowledge bases. The app supports exporting mind maps in multiple formats and offers customizable templates for various use cases.

## Features
- 🧠 Interactive mind mapping with AI-generated suggestions
- 🤝 Real-time collaboration for multiple users
- 📚 Integration with external knowledge bases for enhanced context
- 📥 Export mind maps to various formats (PDF, image, etc.)
- 🎨 Customizable templates for different brainstorming sessions

## Tech Stack
### Frontend
- **Next.js** 🌐

### Backend
- **FastAPI** 🚀
- **LangChain** 🔗
- **OpenAI** 🤖

### Database
- **PostgreSQL** 🗄️

## Installation
To set up MindMapAI locally, follow these steps:

- Clone the repository
bash
git clone https://github.com/Rahul-Khera-Codes/mindmapai
- Navigate to the project directory
bash
cd mindmapai
- Install the backend dependencies
bash
cd backend
pip install -r requirements.txt
- Install the frontend dependencies
bash
cd ../frontend
npm install
- Set up the PostgreSQL database and update the configuration
- Run the backend server
bash
cd ../backend
uvicorn main:app --reload
- Run the frontend development server
bash
cd ../frontend
npm run dev
## Usage
1. Open your browser and navigate to `http://localhost:3000`.
2. Create a new mind map or join an existing one.
3. Start brainstorming with AI-generated suggestions and collaborate in real-time.

## API Documentation
For detailed API documentation, please refer to the [API Docs](https://github.com/Rahul-Khera-Codes/mindmapai/docs/api.md).

## Testing
To run tests for the backend, follow these steps:

- Navigate to the backend directory
bash
cd backend
- Run the tests
bash
pytest
## Deployment
To deploy MindMapAI, follow these steps:

- Build the frontend for production
bash
cd frontend
npm run build
- Deploy the backend using your preferred cloud service (e.g., AWS, Heroku).
- Ensure the PostgreSQL database is accessible from your deployment environment.

## Contributing
We welcome contributions! Please follow these guidelines:

- Fork the repository
- Create a new branch for your feature or bug fix
- Make your changes and commit them
- Open a pull request with a clear description of your changes

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Rahul-Khera-Codes/mindmapai/LICENSE) file for details.

## Acknowledgments
- Special thanks to the contributors and the open-source community for their support and resources.