🐍 AI Snake Game (Python + Pygame)

An advanced implementation of the classic Snake Game built using Python and Pygame.
This version includes an AI-controlled snake using BFS pathfinding, multiple difficulty levels, obstacles, and a modular project structure.

The project can run as:

🖥 Desktop game

🌐 Browser game using Pygbag

🎮 Features
Gameplay

Classic snake mechanics

Dynamic scoreboard UI

Snake speed increases as food is eaten

Randomly generated walls/obstacles

Pause functionality

Game Modes

👤 Player Mode – control the snake manually

🤖 AI Mode – snake automatically finds food

Difficulty Levels

Easy – slow speed, fewer walls

Medium – moderate speed and obstacles

Hard – fast snake with many obstacles

AI Implementation

The AI snake uses Breadth-First Search (BFS) to determine the shortest safe path to food while avoiding:

walls

its own body

boundaries

🧠 AI Algorithm

The AI engine performs a grid-based BFS search:

Start from the snake's head

Explore valid neighboring cells

Avoid obstacles and snake body

Stop when the food position is reached

Return the next movement step

This allows the AI snake to navigate the board intelligently.

📂 Project Structure
snake_ai_game
│
├── main.py           # Entry point
├── menu.py           # Game menu and level selection
├── game_engine.py    # Core game loop
├── ai_engine.py      # BFS pathfinding for AI snake
├── draw_utils.py     # Rendering utilities
├── level_system.py   # Difficulty levels and obstacle generation
└── settings.py       # Global constants and configurations

This modular architecture improves readability, maintainability, and scalability.

🛠 Installation

Clone the repository:

git clone https://github.com/yourusername/snake-ai-game.git
cd snake-ai-game

Install dependencies:

pip install pygame
▶️ Run the Game (Desktop)
python main.py

Controls:

Key	Action
⬆	Move Up
⬇	Move Down
⬅	Move Left
➡	Move Right
P	Pause Game
🌐 Run in Browser

This game can be compiled to WebAssembly using Pygbag.

Install pygbag:

pip install pygbag

Build and run:

pygbag main.py

Then open in browser:

http://127.0.0.1:8000
