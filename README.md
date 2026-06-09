# ChessAI — Custom Chess Engine on PyTorch (WIP) ♟️🤖

## About the Developer & Project
Hi! I am 14 years old, and I built this custom chess engine with artificial intelligence completely from scratch. 

Instead of using ready-made chess libraries (like python-chess) or connecting standard engines (like Stockfish), I wanted to understand how neural networks work from the inside. I designed the object-oriented programming (OOP) board simulation, engineered the feature matrix, and trained the deep learning model myself using PyTorch.

Current Status: Work in Progress (WIP). The AI core, move verification, king protection, and draw tracking are 100% stable and fully operational. The graphical end-game menu is currently under development.

---

## How the AI Works
The computer doesn't play using a massive list of hardcoded if/else rules. It makes decisions based on the weight matrices of a trained deep neural network.

1. Feature Engineering (binary_array): This custom pipeline encodes the geometry of the board and any simulated move into a 10-dimensional tensor (piece value, is it under attack, is it defended, opening phase, etc.).
2. Model Architecture (ChessNet): A 3-layer fully-connected network utilizing LayerNorm for stabilization and GELU non-linear activations.
3. Loss Function Optimization: Trained using BCEWithLogitsLoss on a hand-curated dataset of 100+ unique strategic positions. This forced the model to establish a massive tactical gap between excellent positional moves (weights close to 1.00) and dangerous blunders/hanging pieces (weights crushed down to deep 0.00).

---

## Performance Optimization & Bug Fixes
During development, I encountered and solved several complex software engineering challenges:
* Circular Imports Defeated: Avoided deadly Python import loops between piece classes (Rook.py, Knight.py, etc.) and King.py by implementing highly optimized, fast class-name string reflections (v.__class__.__name__ == 'King'). This keeps the code decoupled and completely safe from NoneType crashes.
* Logits Separation: Separated training logits from raw inference probabilities, enabling the model to converge deeply over 2500 epochs without gradient saturation.
* Sharp Inference Scaling: Forced a strict mathematical hierarchy in forward by sharpening the Sigmoid slope (raw * 10.0). This guarantees the AI aggressively capitalizes on blunders while strictly protecting its own pieces.

---

## Game Features Implemented
* Tactical Threat Awareness: The AI actively scans the board, runs from attacks, and captures unprotected material instantly.
* Strict King Protection: Highly optimized filters prevent both the player and the AI from ever making illegal moves that put or leave their King under check.
* Automated Draw Rules: Fully functional 50-move rule counter (no_capture_ticks) and instant dead-material detection (King vs. King).

---

## Installation & Launch

1. Clone this repository.
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Launch the game:
```bash
python Game.py
```

---

## Roadmap (What's Coming in v2.0)
* Add the graphical End-Game pop-up menu (Checkmate / Stalemate / Draw graphics).
* Adversarial Learning Framework: Implement a replay buffer to retrain the neural network on the player's personal blunders mid-game (1 - W_move).
* Integrate a recursive Minimax search tree to allow the AI to calculate variants 2–3 moves ahead.

## License
Distributed under the MIT License. Feel free to use this code for learning purposes, but please provide a reference link to the original repository.
****