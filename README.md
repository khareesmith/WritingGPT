# WritingGPT: Your AI-Powered Writing Assistant 🤖

## Overview

WritingGPT is a robust web application powered by Flask and integrated with OpenAI's GPT API. It automates the creation, editing, and optimization of articles and blog posts. Customize your writing experience with specialized teams for topics like technology 🧪, fashion 👗, or sports ⚽.

## Features 🌟

- **Article Generation**: Draft articles using OpenAI's GPT API.
- **Editing**: Revise and improve your drafts.
- **SEO Optimization**: Enhance search engine visibility.
- **Image Research**: Curate suitable visuals.
- **Final Draft**: Assemble a publish-ready article.
- **Topic-Specific Teams**: Pick writers and editors by specialization.

## Getting Started 🚀

### Prerequisites

- Python 3.x
- OpenAI API key

### Installation Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/khareesmith/WritingGPT.git
    ```

2. **Add OpenAI API Key**:

    Edit `config.json` to insert your API key:

    ```json
    {
    "API_KEY": "YOUR_API_KEY_HERE"
    }
    ```

3. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```bash
    python app.py
    ```

5. **Access the Web Interface**:

    Navigate to `http://127.0.0.1:5000/`.

### Optional: Speed Up the App

- Rebuild using pyinstaller:

    ```bash
    pyinstaller app.spec
    ```

- Run from the 'dist' directory:
  - **Windows**: Double-click `run_app.bat`
  - **Mac**: Double-click `WGPT`, then `Open Browser`

## How to Use 🛠️

1. **Setup**:
   - Specify your topic and keywords.
   - Select your preferred writer and editor types.

2. **Automate**:
   - WritingGPT handles the rest, saving the final article in the "Outputs" folder.

### Writer/Editor Categories

Choose from the following specializations to tailor your content:

- **General**: Versatile
- **Food 🍽️**: Great for recipes and restaurant reviews.
- **Tech 🖥️**: Ideal for tech-related topics.
- **Gaming 🎮**: Geared towards gaming culture.
- **Music 🎵**: Artists, genres, and more.
- **Entertainment 🎥**: Movies, TV, and pop culture.
- **Fashion 👠**: From high fashion to everyday attire.
- **Sports 🏈**: Covers American and international sports.
- **Travel 🌍**: Your guide to new destinations.
- **Photography 📷**: Where visuals tell the story.
- **Health & Fitness ⚕️💪**: Focus on well-being.

### Pro Tip 🌟

Mix and match different writer and editor types for unique and captivating articles.

## Contributing 🤝

1. Fork the Project
2. Create a Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit Changes (`git commit -m 'Add NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## License 📝

MIT License. See `LICENSE` for more details.

## Contact 💌

- K. Smith: kharee.smith@yahoo.com
- [Project Link](https://github.com/khareesmith/WritingGPT)