#!/usr/bin/env python3

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 
# stopwords is a collection of words that dont convey meaning. mostly pronouns such as he she etc.

#generate word cloud
text = '''
    Description
    Reporting directly to the Engineering Manager, you will dive in and take ownership of our existing codebase, helping extend and scale our bespoke recommendations engine, order management, inventory, shipping, and reporting components.
    This is a great opportunity to lead the engineering team of a startup that is already profitable, already a well-known brand for women, but is still growing fast even in COVID times. We need someone who can not only build our existing codebase, but also push the envelope, as we are developing some sophisticated data science capabilities, similar to Netflix, Amazon, and Stitch Fix.
    Founded in 2014, Nadine West sends personalized outfits to our customers’ doorsteps every month. We are based in Austin TX, but we are a remote-first company, so you can live and work anywhere.
    Requirements
    You partner with stakeholders to understand the business needs and design right-sized solutions, able to move from open-minded design thinking to breaking problems down and iterating to create working software.
    You have built, launched, extended, and maintained a business-critical Rails app long enough to learn from your decisions, and love sharing those stories.
    You are comfortable directing and mentoring other engineers with humility.
    You have time-tested beliefs about code quality, testing, architecture, database design, ORMs, and build vs. buy tradeoffs, and enjoy articulating those beliefs to your colleagues.
    You’re at home owning the entire product development cycle (design, dev, testing, release, monitoring).
    You’ve managed CI/CD pipelines and love auto-deploying to production after your well-honed tests pass.
    You cherish focused, low-interruption deep work like we do (See 37 Signals’ “Group Chat is Making you Sweat”).
    You’re excited to work remotely, but also excited to share a US timezone and let us host you in Austin one day!
    Benefits
    1) This position pays somewhere between your local pay and Austin pay (Google “Austin senior software engineer salary”.) 
    2) You can work and live anywhere that makes you happy. 
    3) We have always been a remote work company, collaborating across multiple continents. We believe you should be free to work whenever and wherever you choose. 
    ''' # the input of the wordcloud generator

#generate the wordcloud object, set the height and width, set the random_state parameter to ensure reproducibility of results and set the stopwords parameter so that the irrelevant words such as pronouns are discarded.
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='white', collocations=False, stopwords = STOPWORDS).generate(text)

# text is the input to the generate() method
#draw the figure
#Set figure size
plt.figure(figsize=(40, 30))

# Display image
plt.imshow(wordcloud) 

# No axis 
plt.axis("off")
plt.show()
