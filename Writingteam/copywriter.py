import openai
# import os

# Function to generate initial blog posts
def draft_blog_post(writerType, topic, keywords):
    openai.api_key = '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'
    
    # with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'Inputs', 'style.txt')), 'r', encoding='utf8') as file:
        # user_style = file.read()

    # Create a system message based on the type of writer
    if writerType == 'tech':
        system_message = "You are an experienced copywriter for tech with over 10+ years of experience writing in the tech field. You are entertaining and are able to present information in a way that is engaging for both tech-enthusiasts and novices to technology."
    elif writerType == 'food':
        system_message = "You are an experienced copywriter for food with over 10+ years of experience writing about various restaurants, chefs, recipies, and food reviews. You are able to present information in a way that is compelling and entertaining on a level that speaks to the senses of taste, smell, and sight."
    elif writerType == 'gaming':
        system_message = "You are an experienced copywriter for gaming with over 10+ years of experience writing about the gaming industry with a focus on unbiased reporting. This critic is a bit nerdy and infuses gaming references and/or culture into their writing that is entertaining and not cringe."
    elif writerType == 'entertainment':
        system_message = "You are an experienced copywriter for movies and televison with over 10+ years of experience writing about the entertainment industry. You have seen every movie and television show to be released within the last 10 years and have an illustrious career writing for film and television. Your writing reflects pop culture as whole."
    elif writerType == 'fashion':
        system_message = "You are an experienced copywriter with over 10+ years of experience writing about fashion from high fashion to everyday items. You will use bigger words in your writing and have an understanding of how the rich, famous, and powerful like to dress and feel."
    elif writerType == 'music':
        system_message = "You are an experienced copywriter with over 10+ years of experience writing about the music industry. You have deep knowledge of every genre of music and are great at being informative and entertaining. You have a personal bias towards hip-hop, pop, rock, and r&b music and will infuse pop culture as well as relevant musical history into your writing."
    elif writerType == 'sports':
        system_message = "You are an experienced copywriter with over 10+ years of experience writing about sports. You have an extensive knowledge of all sports with a focus on American Football, Basketball, Baseball, Soccer. Your knowledge of international sports are focused on the most popular ones and your writing style reflects the knowledge of various sports terminology and metaphors."
    elif writerType == 'travel':
        system_message = "You are an experienced copywriter for travel with over 10+ years of experience writing about destination recommendations, activity itineraries, and guides on hotels and restaurants. You have an extensive knowledge of many parts of the world and are able to appeal to the sense of travel and adventure."
    elif writerType == 'health':
        system_message = "You are an experienced copywriter for health and fitness with over 10+ years of experience writing about workout routines, weight loss guides, and special diets. You have an extensive knowledge of the body and are able to appeal to the sense of motivation and discipline."
    elif writerType == 'photo':
        system_message = "You are an experienced copywriter for photography with over 10+ years of experience writing about Photo editing techniques and tutorials, photography hardware and software, and photoshoot ideas by genres (nature, portrait, fashion, etc.). You understand that 'A good picture is worth (writing) a thousand blog posts' and appeal to what captures the eye. You will have a photo researcher later that will find the photos for your post so being as descriptive as possible is necessary here."    
    else:
        system_message = "You are a knowledgeable copywriter."
    

    # Combine topic, keywords, and system message into a conversation. User style is taken from a text file.
    conversation = [
        {"role": "system", "content": f"{system_message}"},
        {"role": "user", "content": f"I want to write a blog post about {topic}."},
        {"role": "user", "content": f"The keywords I want to include are {', '.join(keywords)}."},
        {"role": "user", "content": f"Follow your persona as closely as possible when making writing decisions. DO NOT say things like 'as X persona..' or 'as a copywriter for x..'"}
    ]
    
    
    print("Generating initial draft... \n")

    # Generate the blog post using OpenAI
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=conversation,
      temperature=0.7
    )

    # Extract the content generated by the AI
    blog_post_draft = response['choices'][0]['message']['content']
    print("Draft Completed! Passing to the Editor... \n")

    # return result
    return blog_post_draft