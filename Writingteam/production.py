import openai
from pathlib import Path

def final_blog_post(draft, editor_notes, seo_notes, photo_suggestions):
    
    current_directory = Path.cwd()
    draft_relative_path = Path("Outputs/blog_post_draft.txt")
    edit_relative_path = Path("Outputs/editor_notes.txt")
    seo_relative_path = Path("Outputs/seo_notes.txt")
    photo_relative_path = Path("Outputs/photos.txt")
    
    draft_absolute_path = current_directory / draft_relative_path
    edit_absolute_path = current_directory / edit_relative_path
    seo_absolute_path = current_directory / seo_relative_path
    photo_absolute_path = current_directory / photo_relative_path
    
    openai.api_key = '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'
    
    with open(draft_absolute_path, 'r') as f:
        draft = f.read()
    with open(edit_absolute_path, 'r') as f:
        editor_notes = f.read()
    with open(seo_absolute_path, 'r') as f:
        seo_notes = f.read()
    with open(photo_absolute_path, 'r') as f:
        photo_suggestions = f.read()
    
    system_message = "You are a skilled production editor that manages content production for a publication. You have over 10+ years of experience with proofreading, copyediting, extensive formatting checks, and more."

    # Construct a conversation with the system message and the blog post draft, editor notes, SEO notes, and photo suggestions
    conversation = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": f"Please review the following draft blog post and create a final blog post utilizing all given information. This is the first draft: {draft}"},
        {"role": "user", "content": f"Use these notes from the Editor: {editor_notes}. Try to incorporate all notes that better the post as a whole."},
        {"role": "user", "content": f"Use these notes from the SEO Exprt: {seo_notes}. Make changes to the post as necessary to fit SEO requirements."},
        {"role": "user", "content": f"Use these notes from the Photo Researcher: {photo_suggestions}. If possible, include where each photo should be placed within the final post after the sentence or paragraph that it is relevant for."}
    ]
    
    print("Generating Final Blog Post... \n")

    # Generate the suggestions using OpenAI
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo-16k",
      messages=conversation
    )

    # Extract the suggestions generated by the AI
    final_output = response['choices'][0]['message']['content']
    print("Production Editor Post Completed! \n")

    return final_output