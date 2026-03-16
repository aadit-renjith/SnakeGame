# 🐍 AI Snake Game (Python + Pygame)

An advanced implementation of the classic **Snake Game** built using Python and **Pygame**.  
This project includes an **AI-controlled snake using BFS pathfinding**, multiple difficulty levels, obstacles, and a modular project structure.

The game can run as:

- 🖥 Desktop game
- 🌐 Browser game using Pygbag (Python → WebAssembly)

---

# 🎮 Features

### Gameplay
- Classic snake mechanics
- Dynamic scoreboard UI
- Snake speed increases when food is eaten
- Randomly generated walls/obstacles
- Pause functionality

### Game Modes
- 👤 **Player Mode** – control the snake manually
- 🤖 **AI Mode** – snake automatically finds food

### Difficulty Levels
- **Easy** – slow speed, fewer walls
- **Medium** – moderate speed and obstacles
- **Hard** – fast snake with many obstacles

### AI Implementation
The AI snake uses **Breadth-First Search (BFS)** to determine the shortest safe path to food while avoiding:

- walls
- its own body
- boundaries

---

# 🧠 AI Algorithm

The AI engine performs a **grid-based BFS search**:

1. Start from the snake's head
2. Explore valid neighboring cells
3. Avoid obstacles and snake body
4. Stop when the food position is reached
5. Return the next movement step

This allows the AI snake to **navigate the board intelligently**.

---

# 📂 Project Structure

```
snake_ai_game
│
├── main.py           # Entry point
├── menu.py           # Game menu and level selection
├── game_engine.py    # Core game loop
├── ai_engine.py      # BFS pathfinding for AI snake
├── draw_utils.py     # Rendering utilities
├── level_system.py   # Difficulty levels and obstacle generation
└── settings.py       # Global constants and configurations
```

This modular architecture improves **readability, maintainability, and scalability**.

---

# 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/snake-ai-game.git
cd snake-ai-game
```

Install dependencies:

```bash
pip install pygame
```

---

# ▶️ Run the Game (Desktop)

```bash
python main.py
```

Controls:

| Key | Action |
|-----|------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| P | Pause Game |

---

# 🌐 Run in Browser

This game can be compiled to WebAssembly using **Pygbag**.

Install pygbag:

```bash
pip install pygbag
```

Build and run:

```bash
pygbag main.py
```

Then open in browser:

```
http://127.0.0.1:8000
```

---

# 🚀 Future Improvements

Possible enhancements:

- Reinforcement Learning based snake AI
- Multiplayer snake
- Particle effects and animations
- Sound effects
- High score persistence
- Online leaderboard
- Mobile deployment

---


# 👨‍💻 Author

**Aadit Renjith**    

