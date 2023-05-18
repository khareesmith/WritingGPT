import Inputs
import Writingteam
import os


# Get user input for the copywriter
topic, keywords, writer_type = Inputs.get_copywrite()

# Generate the blog post draft
draft = Writingteam.draft_blog_post(topic, keywords, writer_type)

# Save the draft to a text file
f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'Outputs', 'blog_post_draft.txt')), 'w')
f.write(draft)


# Get the type of editor from the user
editor_type = Inputs.get_editor()

# Generate the Editor's suggestions
editor_notes = Writingteam.edit_blog_post(draft, editor_type)

# Save the Editor's notes to a text file
f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'Outputs', 'editor_notes.txt')), 'w')
f.write(editor_notes)

# Generate the SEO Expert's suggestions
seo = Writingteam.seo_notes(draft)

# Save the SEO Expert's notes to a text file
f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'Outputs', 'seo_notes.txt')), 'w')
f.write(seo)

# Generate the Photo Researcher's suggestions
photos = Writingteam.photo_suggestions(draft)

# Save the Photo Researcher's suggestions to a text file
f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'Outputs', 'photos.txt')), 'w')
f.write(photos)

# Generate the Production Editor's Final Draft
final = Writingteam.final_blog_post(draft, editor_notes, seo, photos)

# Save the final blog post to a text file
f = open(os.path.realpath(os.path.join(os.path.dirname(__file__), 'Outputs', 'final_blog_post.txt')), 'w')
f.write(final)

# Print the Final Post
print("Completed Blog Post: \n", final, "\n")
print("View the draft and all notes for this blog post in the 'Outputs' folder under: \n blog_post_draft.txt \n editor_notes.txt \n seo_notes.txt \n photos.txt \n final_blog_post.txt")

