'''
This script seeds the database with sample project data.
It creates a list of sample projects with names and descriptions, and then inserts them into the database.
'''


from sqlmodel import Session
from app.database import get_engine
from app.models import Project


# Function to seed the database with sample project data
def seed_projects():
    sample_projects = [
        ("AI-Powered Chatbot",
         "A virtual assistant that uses natural language processing to help users with FAQs."),
        ("E-Commerce Store", "An online platform for selling electronics with real-time inventory and payment gateway."),
        ("Weather Dashboard",
         "A responsive app showing weather forecasts using public APIs."),
        ("Task Manager", "A to-do list app with project-based task grouping and due dates."),
        ("Fitness Tracker",
         "Mobile-first app that logs workouts, meals, and progress with charts."),
        ("Budget Planner", "A web app for tracking income, expenses, and financial goals."),
        ("Portfolio Website", "A personal portfolio site for showcasing work and projects."),
        ("Blog CMS", "A content management system for creating, editing, and publishing blog posts."),
        ("Recipe App", "An app to save, share, and discover recipes with ingredient filters."),
        ("Event Scheduler",
         "An app to create and manage events with calendar and RSVP system."),
        ("Crypto Tracker",
         "Tracks prices of major cryptocurrencies and shows historical trends."),
        ("Online Quiz System",
         "A system for creating timed quizzes and auto-grading results."),
        ("Job Board", "A portal where companies can post jobs and users can apply with resumes."),
        ("Language Learning App",
         "An interactive app that helps users learn new languages."),
        ("News Aggregator", "Fetches and categorizes news headlines from multiple sources."),
        ("Movie Recommendation Engine",
         "Suggests movies based on user ratings and genre preferences."),
        ("Remote Work Dashboard",
         "Tracks productivity, meetings, and tasks for remote teams."),
        ("Music Streaming Service", "Streams curated playlists and user-uploaded music."),
        ("Inventory System",
         "Manages stock levels, orders, and suppliers for small businesses."),
        ("Online Voting System",
         "A secure, anonymous voting platform with user authentication.")
    ]

    engine = get_engine()
    with Session(engine) as session:
        for name, description in sample_projects:
            project = Project(name=name, description=description)
            session.add(project)
        session.commit()
        print("✅ 20 projects added successfully.")


# Function to run the seeder script
if __name__ == "__main__":
    seed_projects()
