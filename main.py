from input import get_copywrite, get_editor
from copywriter import draft_blog_post
from editor import edit_blog_post
from seo_expert import seo_notes
from photo import photo_suggestions
from production import final_blog_post

# Get user input for the copywriter
topic, keywords, writer_type = get_copywrite()

# Generate the blog post draft
draft = draft_blog_post(topic, keywords, writer_type)

# Save the draft to a text file
f = open('blog_post_draft.txt', 'w')
f.write(draft)


# Get the type of editor from the user
editor_type = get_editor()

# Generate the Editor's suggestions
editor_notes = edit_blog_post(draft, editor_type)

# Save the Editor's notes to a text file
f = open('editor_notes.txt', 'w')
f.write(editor_notes)

# Generate the SEO Expert's suggestions
seo = seo_notes(draft)

# Save the SEO Expert's notes to a text file
f = open('seo_notes.txt', 'w')
f.write(seo)

# Generate the Photo Researcher's suggestions
photos = photo_suggestions(draft)

# Save the SEO Expert's notes to a text file
f = open('photos.txt', 'w')
f.write(photos)

# Generate the Production Editor's Final Draft
final = final_blog_post(draft, editor_notes, seo, photos)

# Save the final blog post to a text file
f = open('final_blog_post.txt', 'w')
f.write(final)

# Print the Final Post
print("Completed Blog Post: \n", final)
print("View the draft and all notes for this blog post in this folder under: \n blog_post_draft.txt \n editor_notes.txt \n seo_notes.txt \n photos.txt \n final_blog_post.txt")

