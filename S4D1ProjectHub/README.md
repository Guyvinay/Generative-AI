ProjectHub - Comprehensive Project Management Application
Objective
ProjectHub is a comprehensive project management application designed to help teams efficiently collaborate on projects, track tasks, and manage resources.

Platform Access
Access ProjectHub at https://projecthub-demo.com

Video Walkthrough
Watch our guided video walkthrough: Link to Feature Walkthrough

Key Features
User Management

Register, log in, and manage distinct roles:
Admin: Highest level of access, manages users, projects, and teams.
Project Manager: Oversees specific projects, assigns tasks, and manages project details.
Team Member: Collaborates on projects, receives task assignments, and updates task statuses.
User profiles with Name, Email, and Profile Picture.
Project Management

Create projects with details like Name, Description, Start Date, End Date, and Project Manager.
Assign multiple users to a project, and team members collaborate on tasks within the project.
Task Management

Create, edit, and delete tasks within projects.
Detailed task attributes: Title, Description, Due Date, Priority, Status, Assigned Team Members, and Sub-tasks.
Team Management

Create and manage teams with Team Name and Team Members.
Team assignments facilitate collaboration within projects, and users can belong to multiple teams.
Dashboard

Provides an overview of a user's tasks, project statuses, and team information.
Quick access to pending tasks and project updates.
Notifications

Implement real-time or email notifications to keep users informed of task assignments, updates, and changes to projects and teams.
Ensures users stay updated without constant manual checks.
Project and Task Analytics

Visual representations of project progress, task completion rates, and relevant metrics.
Helps users and project managers make informed decisions and track project performance.
Design Approach and Assumptions
Designed for usability and a seamless user experience.
Assumption: Simplified user authentication for the sake of this demo.
Installation & Getting Started
Clone the repository: git clone <https://github.com/yourusername/projecthub.git>
Install dependencies: npm install
Start the application: npm start
User Journey
Register or log in using provided credentials.
Create and manage projects, tasks, and teams.
Collaborate with team members on project tasks.
Use the dashboard to track progress and access pending tasks.
Receive notifications for task assignments and updates.
Explore project and task analytics for insights.
API Endpoints
Authentication
POST /api/auth/register - Register a new user.
POST /api/auth/login - Log in an existing user.
Projects
GET /api/projects - Retrieve all projects.
GET /api/projects/:id - Retrieve project details.
Tasks
GET /api/tasks - Retrieve all tasks.
GET /api/tasks/:id - Retrieve task details.
Teams
GET /api/teams - Retrieve all teams.
GET /api/teams/:id - Retrieve team details.
... (include more API endpoints as needed)

Technology Stack
Front-end: Angular
Back-end: Node.js with Express.js
Database: PostgreSQL or MySQL for storing user data, project details, tasks, teams, and notifications.
Deliverables
A fully functional web application with all specified features.
Detailed documentation, including setup instructions, database schema, and API endpoints.
The complete source code hosted on a public repository like GitHub.
Evaluation
The project will be evaluated based on:

Correctness and completeness of the application.
Quality of code (cleanliness, efficiency, modularity).
UI/UX design (responsiveness, user-friendliness).
Quality of documentation (setup, database, API).