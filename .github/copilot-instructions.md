<!-- Copilot / AI agent instructions for the CodeLab workspace -->

# Purpose
This file gives concise, actionable guidance to an AI coding agent working in this repository so it can be immediately productive. The repository is a collection of teaching exercises (C#, C++, Java, NodeJS, Python, Arduino, small Flask apps). Changes should be minimal, well-scoped, and preserve the exercise-oriented structure.

# Big picture
- **Repo structure:** top-level folders group languages and course materials (examples: `03_C#`, `04_C++`, `05_java`, `06_NodeJS`, `07_Python`, `01_IFSP`).
- **Primary intent:** learning examples and exercises, not a production app. Most files are single-file exercises or small lesson projects.
- **C# area:** `CodeLab.sln` at repo root and per-lesson projects under `03_C#/aulaX` (example: `03_C#/aula2/aula2.csproj`). Use the solution/project files for builds.
- **Python area:** `07_Python/` contains many single-file exercises (filenames like `exercicio 23.py`). Treat these as isolated scripts — run locally to verify behavior.
- **Flask examples:** `01_IFSP/LP2/Flask/` contains `app.py` and `MoreSimpleFlaskAPI.py` — small web examples. Run them directly with Python to test.
- **NodeJS:** `06_NodeJS` contains standalone JS examples (e.g. `06_NodeJS/Sintax/Helloword.js`). There is no `package.json` in these subfolders; run files with `node` unless a package manifest exists.
- **Arduino & Java:** Arduino sketches (`.ino` in `02_Arduino`) are for the Arduino IDE; Java samples in `05_java` are standalone source files under `05_java/Sintax`.

# How to build / run / debug (explicit, reproducible commands)
- C# (solution/project):
  - Build solution: `dotnet build CodeLab.sln`
  - Run a project: `dotnet run --project 03_C#/aula2/aula2.csproj` (replace path as needed).
- Python scripts and Flask:
  - Run a script: `python "07_Python/exercicio 23.py"`
  - Run Flask example: `python "01_IFSP/LP2/Flask/app.py"` (use venv if available).
- NodeJS examples (no package.json in `06_NodeJS/Sintax`):
  - Run a file: `node "06_NodeJS/Sintax/Helloword.js"`.
- Java examples (standalone .java files):
  - Compile: `javac 05_java/Sintax/HelloWord.java`
  - Run: `java HelloWord`
- Arduino sketches: open `02_Arduino/Aula2.ino` (or others) in the Arduino IDE and upload to hardware.

# Project-specific conventions & patterns
- Filenames and directories follow course/lesson naming: `aulaN/` for C# lessons, `exercicio XX.py` for Python exercises. When modifying, keep naming consistent.
- Many files are intentionally minimal and educational — prefer focused edits that do not rewrite entire lessons.
- Tests are not present in this repo; verification is usually running the script or project directly.
- Keep changes local to the exercise you are modifying unless asked to update cross-cutting infrastructure (e.g., `CodeLab.sln`).

# Integration points and external dependencies
- C# uses the .NET SDK (use `dotnet --version` to detect environment). `CodeLab.sln` may reference projects under `03_C#`.
- Flask examples expect a Python environment; check for `requirements.txt` in the same folder before adding dependencies.
- NodeJS examples are single-file and do not require npm unless a `package.json` is added.

# What to do and what to avoid (practical guidance)
- Do: make small, reversible edits; run the related script or project to validate; prefer adding a short README or comment in the folder when adding non-trivial changes.
- Do: preserve exercise intent — if improving code quality, keep pedagogical structure and add brief notes explaining refactors.
- Avoid: sweeping refactors across many lesson files in a single PR; avoid adding heavy infra (CI, linting) without explicit permission.

# Files to reference when working
- Root solution: `CodeLab.sln`
- Example C# project: `03_C#/aula2/aula2.csproj` and `03_C#/aula2/Program.cs`
- Flask examples: `01_IFSP/LP2/Flask/app.py`, `01_IFSP/LP2/Flask/MoreSimpleFlaskAPI.py`
- Python exercises: `07_Python/` (many `exercicio *.py` files)
- NodeJS examples: `06_NodeJS/Sintax/Helloword.js`, `06_NodeJS/Sintax/input.js`

# If you need more context
- Ask for the target lesson/file to change and whether you may update the surrounding lesson materials (README, comments). I can also add small runnable tests or example invocations where appropriate.

-- End of instructions --
