# Getting Started with CrewAI and UV

This guide provides step-by-step instructions to get started with CrewAI using UV. Follow the steps below to set up your environment and run basic examples.

---

## Prerequisites

- Python installed on your system
- UV installed ([UV documentation](https://github.com/astral-sh/uv))
- Basic understanding of Python and command-line tools

---

## Step 1: Create a New Folder

1. Create a new folder and name it `crewai`.
2. Open the folder in VS Code:

   ```bash
   code .
   ```

---

## Step 2: Initialize UV

1. Initialize UV in the folder:

   ```bash
   uv init .
   ```

2. Set up a virtual environment:

   ```bash
   uv venv
   ```

3. Confirm the interpreter:
   - Press `Ctrl + Shift + P`.
   - Search for `Python: Select Interpreter`.
   - Select the local virtual environment.

4. Delete the terminal and open a new one.

5. Run the test script to verify the setup:

   ```bash
   uv run hello.py
   ```

---

## Step 3: Get Started with CrewAI

1. Add CrewAI to your project:

   ```bash
   uv add crewai
   ```

2. Add the following files:
   - `env` file
   - `utils` file

3. Run the second example:

   ```bash
   python 2_unstructured_flow/unstructured_flow.py
   ```

---

## Step 4: Create a Flow with CrewAI

1. Create a new flow named `poem`:

   ```bash
   crewai create flow poem
   ```

2. Close VS Code and open the new `poem` folder:

   ```bash
   code .
   ```

3. Set up the environment:

   ```bash
   uv venv
   ```

4. Confirm the interpreter:
   - Press `Ctrl + Shift + P`.
   - Search for `Python: Select Interpreter`.
   - Select the local virtual environment.

5. Delete the terminal and open a new one.

6. Synchronize the flow:

   ```bash
   uv sync
   ```

---

## Step 5: Modify and Run the Flow

1. Add the following files:
   - `env` file
   - `utils` file

2. Replace the `poem_crew.py` file with your updated version.

3. Fix imports in `main.py` to ensure everything is properly configured.

4. Kick off the flow:

   ```bash
   crewai flow kickoff
   ```

5. Visualize the flow:

   ```bash
   crewai flow plot
   ```

---

## Notes

- Ensure you follow the steps in the exact order for the setup to work properly.
- If you encounter any issues, verify that the correct virtual environment is selected in VS Code.

---

Happy coding with CrewAI!
