# --------------------------------------------
# Science & Technology Projects by Team Sanjana, Isha & Trisha
# Mentor: Devashish Kumar
# Flask App + Animated UI + Buttons to Run Python Projects
# --------------------------------------------

from flask import Flask, render_template_string
import subprocess
import threading

app = Flask(__name__)

# --------------------------------------------
# FUNCTION TO RUN PYTHON PROJECT
# --------------------------------------------
def run_eye_tracking():
    subprocess.run(["python", "eye_tracking_cursor.py"])

# --------------------------------------------
# HTML TEMPLATE WITH ANIMATIONS + HOVER EFFECTS
# --------------------------------------------
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Science & Technology Fair Projects</title>
    <style>
        /* BASIC STYLE */
        body {
            margin: 0;
            font-family: 'Poppins', sans-serif;
            color: white;
            scroll-behavior: smooth;
            background: linear-gradient(-45deg, #0b0c10, #1e1e2f, #2e2e4f, #0b0c10);
            background-size: 400% 400%;
            animation: gradientShift 10s ease infinite;
        }
        @keyframes gradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        header {
            background: linear-gradient(90deg, #5f27cd, #341f97);
            text-align: center;
            padding: 60px 20px;
            box-shadow: 0px 3px 15px #5f27cd;
        }
        header h1 {
            font-size: 2.8rem;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.2rem;
            color: #dcdde1;
        }
        nav {
            text-align: center;
            margin-top: 20px;
        }
        nav a {
            color: white;
            text-decoration: none;
            background-color: #341f97;
            padding: 10px 25px;
            border-radius: 25px;
            margin: 0 10px;
            transition: 0.4s;
        }
        nav a:hover {
            background-color: #5f27cd;
            transform: scale(1.1);
            box-shadow: 0px 0px 12px #5f27cd;
        }

        /* SECTIONS */
        section {
            padding: 60px 20px;
            text-align: center;
        }

        /* PROJECT CARD */
        .project-card {
            background-color: rgba(30, 30, 47, 0.9);
            padding: 30px;
            border-radius: 15px;
            margin: 20px auto;
            width: 80%;
            max-width: 800px;
            box-shadow: 0px 0px 10px #5f27cd;
            transition: 0.4s ease;
        }
        .project-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0px 0px 20px #00d2d3;
        }
        .project-card h3 {
            color: #00d2d3;
        }

        /* BUTTON */
        button {
            background-color: #00d2d3;
            color: black;
            padding: 10px 25px;
            border: none;
            border-radius: 10px;
            font-size: 1rem;
            cursor: pointer;
            transition: 0.4s;
        }
        button:hover {
            background-color: #01a3a4;
            color: white;
            transform: scale(1.1);
            box-shadow: 0px 0px 15px #00d2d3;
        }

        /* ABOUT US SECTION */
        .about-card {
            background: rgba(30, 30, 47, 0.95);
            border-radius: 25px;
            padding: 50px 30px;
            max-width: 900px;
            margin: 40px auto;
            box-shadow: 0 0 35px rgba(0, 210, 211, 0.5);
            text-align: center;
        }
        .about-card h2 {
            color: #00d2d3;
            margin-bottom: 20px;
            font-size: 2rem;
        }
        .about-card p {
            color: #dcdde1;
            font-size: 1rem;
            margin-bottom: 40px;
        }
        .team-members {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 30px;
        }
        .member {
            background: #1e1e2f;
            border-radius: 20px;
            padding: 20px;
            width: 220px;
            box-shadow: 0 0 15px rgba(95, 39, 205, 0.5);
            transition: 0.4s ease;
        }
        .member:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 0 25px #00d2d3;
        }
        .member h4 {
            color: #00d2d3;
            margin-bottom: 5px;
            font-size: 1.1rem;
        }
        .member p {
            color: #dcdde1;
            font-size: 0.9rem;
            margin: 0;
        }

        /* TECH ICONS */
        .tech-icons {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
        }
        .tech-icons div {
            background-color: #222f3e;
            padding: 15px 25px;
            border-radius: 10px;
            transition: 0.3s;
        }
        .tech-icons div:hover {
            background-color: #00d2d3;
            color: black;
            transform: scale(1.1);
        }

        /* FOOTER */
        footer {
            background-color: #1e1e2f;
            text-align: center;
            padding: 20px;
            font-size: 0.9rem;
            color: #aaa;
            box-shadow: 0px -2px 15px #5f27cd;
        }
    </style>
</head>
<body>

    <header>
        <h1>Science & Technology Projects</h1>
        <p>AI-Based Innovations by Team Sanjana, Isha & Trisha</p>
        <nav>
            <a href="#about">About Us</a>
            <a href="#projects">Projects</a>
            <a href="#tech">Technology</a>
        </nav>
    </header>

    <section id="about">
        <div class="about-card">
            <h2>About Us</h2>
            <p>We are a passionate team of innovators exploring Artificial Intelligence, Computer Vision, and creative technology.
            Our goal is to build projects that blend science, imagination, and real-world applications.</p>

            <div class="team-members">
                <div class="member">
                    <h4>Sanjana Devi</h4>
                    <p>AI Developer & Vision Analyst</p>
                </div>
                <div class="member">
                    <h4>Isha</h4>
                    <p>Research & Design Specialist</p>
                </div>
                <div class="member">
                    <h4>Trisha</h4>
                    <p>Testing & Documentation Lead</p>
                </div>
                <div class="member">
                    <h4>Mentor: Devashish Kumar</h4>
                    <p>Project Guide & Technical Mentor</p>
                </div>
            </div>
        </div>
    </section>

    <section id="projects">
        <h2>Our Projects</h2>
        <div class="project-card">
            <h3>Eye Tracking Cursor</h3>
            <p>Control your mouse cursor using eye movement with AI and webcam. Built using OpenCV and Mediapipe.</p>
            <form action="/run_eye_tracking" method="post">
                <button type="submit">▶ Run Project</button>
            </form>
        </div>
    </section>

    <section id="tech">
        <h2>Technology Used</h2>
        <div class="tech-icons">
            <div>🐍 Python</div>
            <div>📷 OpenCV</div>
            <div>🤖 Mediapipe</div>
            <div>🧠 Artificial Intelligence</div>
            <div>💻 Computer Vision</div>
        </div>
    </section>

    <footer>
        Created by Team Sanjana, Isha & Trisha | Guided by Devashish Kumar | Science Fair 2025
    </footer>

</body>
</html>
"""

# --------------------------------------------
# ROUTES
# --------------------------------------------
@app.route("/")
def home():
    return render_template_string(html_code)

@app.route("/run_eye_tracking", methods=["POST"])
def run_eye_tracking_route():
    threading.Thread(target=run_eye_tracking).start()
    return "<h2>Launching Eye Tracking Cursor...<br><a href='/'>Go Back</a></h2>"

# --------------------------------------------
# MAIN
# --------------------------------------------
if __name__ == "__main__":
    print("🚀 Running Science Projects UI at: http://127.0.0.1:5000")
    app.run(debug=True)
