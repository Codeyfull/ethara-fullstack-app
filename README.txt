Task Manager Application 

Overview: This is a full-stack task management application built using FastAPI and React. The system is designed with a clean separation between frontend and backend and demonstrates end-to-end functionality.

Features:
1. User Signup and Login
2. Project Creation
3. Task Management (pending/done)
4. Dashboard with task statistics
5. RESTful API integration between frontend and backend

Tech Stack:
1. Frontend:- React (Vite)
2. Backend:- FastAPI
3. Database:- SQLite
4. Deployment:- Vercel(Frontend), 
                Railway(Backend)

Architecture: The application follows a client-server architecture. The frontend interacts with the backend through REST APIs. The backend handles business logic, database operations, and task management using a modular structure with separate routes and models.

Functionality: Users can create tasks that are initially pending and can be updated to done. The dashboard dynamically updates based on task status.

Data Handling: Each task is associated with a user. This ensures that users can view and manage only their own tasks.

Note: Some data may appear due to testing. This can be reset easily by reset or deleted using API.

Thank you.
