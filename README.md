Asteroid Game
A simple arcade-style game implemented in Python using object-oriented principles. The player controls a spaceship, shoots asteroids, and avoids collisions. The game tracks and displays the player's score.

Project Structure

.
├── main.py              # Game entry point and main loop
├── asteroid.py          # Asteroid behavior
├── asteroidfield.py     # Asteroid spawning and management
├── circleshape.py       # Circle-based collision detection
├── constants.py         # Configuration values
├── player.py            # Spaceship logic and controls
├── shot.py              # Bullet behavior
├── pyproject.toml       # Poetry-based dependency management
└── uv.lock              # Dependency lock file

Gameplay
Move the spaceship using arrow keys or WASD.

Press spacebar to shoot.

Destroy asteroids to score points.

Avoid collisions with asteroids. Collisions reduce lives.

Game ends when all lives are lost. Final score is displayed.

Installation
Requirements
Python 3.10 or later

Poetry for dependency management

Running the Game

git clone https://github.com/prateekdhar/asteroid-game
cd asteroid-game
poetry install
poetry run python main.py
Alternatively, if using pip (after generating a requirements.txt):

bash
Copy
Edit
pip install -r requirements.txt
python main.py
Features
Real-time score tracking

Simple and readable object-oriented design

Circle-based collision detection

Modular code for easy extension
