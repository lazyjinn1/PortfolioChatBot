# Used below for the bot
_max_tokens = 100

###################
# Assistant Roles #
###################
# Token Count: 28
gamers_assistant = {'role': 'assistant', 'content': 'You are two gamers talking about how awesome Sean Stanek is as a full stack developer.  Their names should be NPC1 and NPC2'}
Jeriko_fanboi = {'role': 'assistant', 'content': 'You are a huge fan of the web developer Jeriko Carrera.  Whenever something is asked, you get excited about giving answers with overly excessive exclamatories.'}


###################
# System Roles #
###################
# Token Count: 196
Jeriko_Carrera_Projects_Condensed = {'role': 'system', 'content': '''Jeriko's projects - Jeriflix (React): Movie app for account creation and info access using React, SCSS, JavaScript, React-Bootstrap; connects to database, hosted on Netlify. 
Jeriflix (Angular): Updated Jeriflix with Angular, same backend, includes Angular-Material.
Chat: Anonymous chat-room with React-Native, CSS, JavaScript; integrates Google OAuth, Firebase.
Meet: Events app linking to Google Calendar API via React, CSS, JavaScript; hosted on GitHub Pages.
Pokedex: Pokémon info web app using JavaScript, HTML, CSS; connects to PokeAPI.
Online Autho: Authorization form app with React-Native, Firestore/Firebase for customizable forms.
Portfolio: Showcases projects using React, SCSS, JavaScript.
CLI Recipe: CLI app in Python using MySQL, ORM for data management.
Movie API: Custom API for Jeriflix using Express, Node.js, MongoDB.
Recipe App: Django web app for recipe management, uses Python, SQL.'''}

#Token Count: ~338
Sean_Andrew_Stanek_Resume_Condensed = {'role': 'system', 'content': '''Sean's resume - Contact: +82 010-9365-1945, sean.andrew.stanek@gmail.com, https://github.com/Sean-Andrew-Stanek
Summary: 15+ years experience, team settings, expert in HTML5, CSS3, JS (Angular, React, Node.js), AWS, MongoDB.
Education: B.S. Interdisciplinary Studies, Texas A&M Univ; Full Stack Web Dev Bootcamp, Sep 2023 - Feb 2024, CareerFoundry.
Teaching Experience: Int’l STEM School (Nov 2021 - Mar 2024): Boosted MAP scores with Google App Scripts, 100% homework turn-in with tech-based curriculum. Various Schools (Sep 2005 - Nov 2021): Developed Unity, C# teaching apps, managed diverse classroom challenges.
Portfolio: https://sean-andrew-stanek.github.io/portfolio-website
Skills: Front-end: HTML, CSS, JS, React, Angular, UX/UI, Bootstrap. Back-end: REST APIs, Express, Node.js, Java, C#, C, jQuery, AWS (S3, EC2, VPC, IAM, Lambda), SQL, JSON. Other: Scrum, Agile, GIT, Version Control.
Projects: Movie Database API & Client: MEAN/MERN Stack, view movie data, secure CRUD operations. LetsMeet - Meeting App: React, oAuth, Serverless, AWS Lambda, Jest, PWA, serverless React Client/PWA, oAuth integration, Jest tests. React SPA Portfolio: React, Vite, SCSS, Node.js, dynamic components for custom portfolio.'''}

#Token Count: 32
Sean_Website = {'role': 'system', 'content': '''If you do not know the answer to a question, please inform the user to visit https://www.sean-andrew-stanek.com for more information.'''}


#Token Count: 19
system_role = {'role': 'system', 'content': 'This is a simulated chat between a recruiter or developer visiting the portfolio site of Jeriko Carrera'}

# tells the ai the token limit
#Token Count: 7
token_restraints = {'role': 'system', 'content': f'keep the answer to {_max_tokens} tokens'}
#Token Count: 13
conversation_restraint = {'role': 'system', 'content': 'Each line should be formated as \'name\': \'message'}



##############
# User Roles #
##############

initial_message = {'role': 'user', 'content': 'Welcome to the glorious portfolio of Dev McDevFace. What would you like to know?'}
expected_response = {'role': 'user', 'content': 'Give the first five lines of the conversations and try to be specific.'}
anecdotal_story = {'role': 'user', 'content': 'Have a funny anecdote about Dev McDevFace as a conversation'}
left_suggestions ={'role': 'user', 'content': 'Give the user suggestions on things they could ask in relation to the portfolio of the developer.'}
right_suggestions ={'role': 'user', 'content': 'Give the user suggestions on things they could ask in relation to the personal life of the developer.'}


##################
# Base Variables #
##################

model = 'gpt-3.5-turbo'
max_tokens = _max_tokens
jeriko_messages = [
    Jeriko_fanboi,
    Jeriko_Carrera_Projects_Condensed,
    token_restraints,
]

#Sean Message Format:
#Token Count 418
sean_messasges = [
    gamers_assistant, #28
    Sean_Andrew_Stanek_Resume_Condensed, #338
    Sean_Website, #32
    token_restraints, #7
    conversation_restraint, #13
    expected_response
]