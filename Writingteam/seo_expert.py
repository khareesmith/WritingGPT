import openai
import os

# Set the API key
openai.api_key = ''

# Read the blog post draft from the file
with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'Outputs', 'blog_post_draft.txt')), 'r') as f:
    draft = f.read()

def seo_notes(draft):
    
    system_message = "You are an experienced SEO Specialist that understands the ins and outs and intricacies of organic search to get websites and webpages to rank well."

    # Construct a conversation with the system message and the blog post draft
    conversation = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"Please review the following blog post and provide notes to improve ranking in search engines: {draft}"}
    ]

    # Generate the SEO's notes using OpenAI
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=conversation
    )

    # Extract the suggestions generated by the AI
    seo = response['choices'][0]['message']['content']
    print("SEO Expert's Notes Completed! Passing to the Photo Researcher... \n")

    return seo