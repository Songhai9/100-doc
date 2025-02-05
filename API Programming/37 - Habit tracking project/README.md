# Habit Tracking Project

This project uses the Pixela API to track habits, such as coding hours, by creating graphs and updating pixel data daily.

## Overview

- **User Registration:** Registers a new Pixela user using a token specified in the `.env` file.
- **Graph Creation:** Sets up a coding graph where each pixel represents the number of hours spent coding.
- **Pixel Update:** Updates the graph with daily coding hours.

## Setup

1. Install the required packages:
     ```
     pip install -r requirements.txt
     ```
2. Create a `.env` file in the project root and set your user token:
     ```
     USER_TOKEN='your-token-here'
     ```
3. Run the main script:
     ```
     python main.py
     ```
    and enter the amount of time of the day

## Project Goals

- Learn how to interact with REST APIs using Python.
- Utilize environment variables for secure token management.
- Build a habit tracking mechanism integrating external APIs.