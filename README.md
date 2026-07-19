🏏 AI Cricket Coach
An AI-powered cricket coaching system built with Python and Computer Vision.

The goal of this project is to analyse a batsman's technique in real time using a webcam, providing instant feedback on movement, balance, shot execution, and overall batting performance.

Features
Current Features
✅ Live webcam feed
✅ Cricket ball detection
✅ Object tracking
✅ Ball speed estimation
✅ Modular project architecture
✅ Git version control
Planned Features
🔄 Full-body pose detection using MediaPipe
🔄 Bat speed calculation
🔄 Wrist speed analysis
🔄 Head movement tracking
🔄 Front leg angle analysis
🔄 Shoulder rotation analysis
🔄 Balance scoring
🔄 Shot detection
🔄 Automatic technique feedback
🔄 Confidence scoring
🔄 Video recording and replay
🔄 Shot history and progress tracking
🔄 Mobile support
Project Structure
AI Cricket Coach/
│
├── main.py
├── config.py
│
├── tracking/
│   ├── pose_tracker.py
│   ├── ball_detector.py
│   ├── tracker.py
│   └── speed.py
│
├── analysis/
│   ├── technique.py
│   ├── scoring.py
│   └── shot_detector.py
│
├── ui/
│   └── draw.py
│
├── tests/
│   ├── check_mediapipe.py
│   └── motion_detector.py
│
└── README.md
Technologies
Python 3.12
OpenCV
MediaPipe
NumPy
Git
Project Pipeline
Camera
   │
   ▼
Frame Capture
   │
   ▼
Ball Detection
   │
   ▼
Pose Detection
   │
   ▼
Technique Analysis
   │
   ▼
Shot Detection
   │
   ▼
Scoring Engine
   │
   ▼
Live Feedback Dashboard
Future Vision
The long-term goal is to create an intelligent cricket coach capable of:
 
Analysing batting technique automatically
Comparing shots against professional players
Detecting technical flaws
Tracking improvement over time
Providing personalised coaching feedback
Running on desktop and mobile devices
Installation
Clone the repository:

git clone <repository-url>
Navigate into the project:

cd AI-Cricket-Coach
Install dependencies:

pip install -r requirements.txt
Run the application:

python main.py
Development Roadmap
Phase 1
Ball tracking
Pose tracking
Basic feedback
Phase 2
Technique analysis
Bat speed
Shot detection
Performance scoring
Phase 3
AI coaching
Professional shot comparison
Video recording
Session history
Phase 4
Mobile application
Cloud analytics
Personalised training plans
Author
Aaron

Built as a computer vision project to explore how machine learning can improve cricket coaching.

License
This project is for educational and personal development purposes.
