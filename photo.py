import openai

# Set the API key
openai.api_key = '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'

# Read the blog post draft from the file
with open('blog_post_draft.txt', 'r') as f:
    draft = f.read()

def photo_suggestions(draft):
    
    system_message = "You are an experienced photographer and understand the intracacies of composition, exposure, focusing, depth of field and other concepts to create engaging images"

    # Construct a conversation with the system message and the blog post draft
    conversation = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"Please review the following blog post and provide image suggestions for any relevant content: {draft}"}
    ]

    # Generate the photo researcher's notes using OpenAI
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=conversation
    )

    # Extract the suggestions generated by the AI
    photos = response['choices'][0]['message']['content']
    print("Photo Researchers's Notes Completed! Passing to the Production Editor for Final Content... \n")

    return photos