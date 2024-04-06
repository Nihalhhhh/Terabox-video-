#!/bin/bash

# Update package repositories
pkg update

# Install Python
pkg install python

# Install pip (Python package manager)
pkg install python-pip

# Install pytube library for downloading YouTube videos
pip install pytube

# Install Node.js (if you're using a Node.js bot)
pkg install nodejs

# Install npm (Node.js package manager)
pkg install npm

# Install any Node.js dependencies (if applicable)
# Example: npm install telegram-bot-api

# Make the script executable
chmod +x requirements.sh
