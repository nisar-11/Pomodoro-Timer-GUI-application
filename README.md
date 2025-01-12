# Pomodoro Timer

## Overview
The Pomodoro Timer is a time management tool built with Python and Tkinter. It follows the Pomodoro Technique, where you work for focused intervals followed by short breaks to boost productivity and maintain focus. After completing four work sessions, a longer break is provided.

## Features
- **Customizable Intervals**: Work, short break, and long break durations can be modified in the code.
- **Interactive UI**: A simple and user-friendly interface with visual and textual feedback.
- **Automated Workflow**: Automatically starts the next session (work or break) after the current session ends.
- **Progress Tracking**: Displays checkmarks for completed work sessions.
- **Notifications**: Provides alerts at the start of each session.

## Requirements
- Python 3.x
- Tkinter (usually included with Python)

## How to Use
1. Clone or download the project files.
2. Ensure the `tomato.png` image is in the same directory as the script.
3. Run the script using:
   ```bash
   python <script_name>.py
   ```
4. Click **Start** to begin the timer.
5. Click **Reset** to reset the timer and progress.

## File Structure
```
project_directory/
├── pomodoro_timer.py    # Main script
├── tomato.png           # Tomato image for the UI
```

## Configuration
To change the default durations, modify the constants in the script:
```python
WORK_MIN = 25          # Work duration in minutes
SHORT_BREAK_MIN = 5    # Short break duration in minutes
LONG_BREAK_MIN = 20    # Long break duration in minutes
```

## How It Works
1. **Work Session**: Starts a 25-minute timer (default) for focused work.
2. **Short Break**: Starts a 5-minute timer (default) after a work session.
3. **Long Break**: After completing 4 work sessions, a 20-minute break is provided.
4. **Progress Display**: Checkmarks (`✓`) are added to indicate completed work sessions.


## Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## Acknowledgments
- The Pomodoro Technique was developed by Francesco Cirillo.
- Thanks to Python's Tkinter library for making GUI development accessible.

