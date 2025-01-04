# Contributions Repository  

This script generates custom contributions on your GitHub activity graph, creating a "HELLO GITHUB" of your activity.  

> **Disclaimer:** I want to clarify that I don’t support any form of cheating or dishonesty. My goal is simply to provide a creative way to add a visual and special touch to your GitHub profile. Plus, if the activity graph shows a message, it’s clear it was done manually, so it’s not intended to mislead anyone.

💡 **My personal take:** I don’t believe the activity graph defines a programmer’s skills or adds or subtracts value from their abilities. However, I recognize that for some people, an empty graph can represent a mental block when presenting their profile. This is why I wanted to create something fun and motivating.

🎥 I’ll soon release a video explaining how I made this, so you can customize it with other text or shapes. I’m also working on a GitHub Action to automate the script so it runs weekly, ensuring the text doesn’t break when a new week starts.

⭐ If you like this idea, check out the repository and consider giving it a star! It would mean a lot and help others discover it.

## Getting Started  

### Requirements  
- Python 3.x installed  
- Git installed and configured on your system  

### Installation  
Clone this repository:  

  ```bash
  git clone https://github.com/lolpox/contributions-repo.git
  cd contributions-repo
  ```

### Usage
Run the script:

  ```bash
  `python contribute.py`
  ```

After the script completes, a new directory called custom-contributions-repo will be created. Navigate to it:

  ```bash
  `cd custom-contributions-repo`
  ```

Push the generated repository to GitHub:

  ```bash
  `git remote add origin https://github.com/yourusername/custom-contributions-repo.git
  git push -u origin main`
  ```

Check your GitHub profile’s contribution graph to see the result. Sometimes it takes some minutes.

Follow me to get notified when the video is ready, and let me know if you have any creative ideas to add!

[LinkedIn](https://www.linkedin.com/in/mario-vicuna/)

## Inspired by

[Laurence Gellert's Blog](https://www.laurencegellert.com/software/github-graph-builder/)

[Shpota](https://github.com/Shpota/github-activity-generator)