# WritingGPT: An A.I. Generated Writing Team

## Overview

This web application is a powerful tool that leverages the capabilities of OpenAI's GPT-3.5 to generate, edit, and optimize articles and blog posts. Users can select from a variety of specialized writing teams based on the topic of their content, such as tech, fashion, or sports. The AI writing team will create a draft, edit it, provide SEO notes, research relevant images, and compile a final draft using all of the available information.

---

## Features

- **Article Generation**: Create drafts for articles and blog posts using the OpenAI API.
- **Editing**: Refine and polish the generated drafts.
- **SEO Optimization**: Provide notes and suggestions for better SEO.
- **Image Research**: Find suitable images for the article or blog post.
- **Final Draft Creation**: Combine all the information to create a final, polished piece of content.
- **Specialized Writing Teams**: Choose a specific type of copywriter and editor based on the content topic.

---

## Getting Started

### Prerequisites

- Python
- OpenAI API key

### Installation

1. Clone the repository

```
git clone https://github.com/khareesmith/WritingGPT.git
```

2. Add your API key from OpenAI. The API key will need to be added to every file in the "Writingteam" directory

```
openai.api_key = 'ENTER API KEY HERE'
```


2. In the main folder, run the program

```
python main.py
```

---

## Usage

Before running the program, you can input a sample for the AI to try to follow. Very useful if you want to mimic your style of writing. The sample will be added to the "style.txt" file in the "Inputs" folder.

After running the program using main.py, enter the topic of the blog post. The topic is the general idea for the AI to start, it will create a title.

Next, enter the keywords for the blog post and use a comma ( , ) to separate multiple keywords. The AI will use these keywords either somewhere in the blog post or use them to influence the overall content.

Next, select the type of writer that will create the inital blog post. The type of copywriter will influence the writing style of the blog itself. Writing a blog post/article about an album review? Try the Music writer. You can even try weird combinations to generate unique ideas (What would a post about the history of American Baseball written by a Tech writer look like?) Entering "avail_types" will display all types available for the copywriter. The available types are:

- General (The default copywriter with general knowledge in various fields)
- Food (Knowledgable with restaurants, recipies, etc.)
- Tech (Knowledgable with various technologies)
- Gaming (Knowledgable with video games and gaming culture)
- Music (Knowledgable with different musical artists and genres)
- Entertainment (Knowledgeable with movies, tv, and general pop culture)
- Fashion (Knowledgeable with both high fashion and everyday clothing)
- Sports (Knowledgeable with various sports, American and International)

Once the initial draft has been completed, you are able to select the type of editor that will review the intital blog post and give notes for how to improve the content. The available selections are the same as the copywriter. Maybe use a gaming writer and editor to hyperfocus on the perfect article about a particular game or use a different writer and editor to generate unique articles.

The program will automatically run through the Photo Reseacher, SEO Expert, and Production Manager to generate the remaining notes and final blog post. Final outputs are found within the "Outputs" folder.

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

K. Smith - kharee.smith@yahoo.com

Project Link: [https://github.com/khareesmith/WritingGPT](https://github.com/khareesmith/WritingGPT)
