from textblob import TextBlob
import random

# Create lists of questions and responses
questions = [
  "What brings you to therapy today?", "How are you feeling right now?", "What do you hope to get out of this session?", "What challenges have you been facing lately?", "What are some goals you have for yourself?", "How is your mood and energy level?", "How have you been sleeping lately?", "How is your appetite and eating habits?", "How are things going socially and interpersonally?", "What hobbies or activities do you enjoy?", "What accomplishments are you proud of recently?", "What worries or anxieties have you been experiencing?", "What are some stresses you've been dealing with lately?", "What are some ways you cope with stress or difficult emotions?", "Who are the supportive people in your life right now?", "What do you do for self-care and to recharge?", "How do you feel about your work or career?", "How satisfied do you feel in your relationships?", "What is something you've always wanted to try or pursue?", "How do you feel about your living situation?", "What does a typical day look like for you?", "What are some things you wish you could change?", "How do you feel about your physical health?", "How confident do you feel in yourself lately?", "What is something that brings you joy or relaxation?",

  "Tell me about your family and your relationships with them.", "Do you have any big events or changes coming up in your life?", "What are your beliefs or values that guide you?", "In what ways do you feel fulfilled or unfulfilled?", "Whatobstacles stand in the way of your progress or happiness?", "What negative habits would you like to change?", "How do you handle feelings of anger or frustration?", "What are you proud of about yourself? ", "Do you feel supported by friends or family?", "What do you feel passionate and excited about?", "What anxieties or fears hold you back?", "How do you respond when someone upsets or hurts you?", "In what situations do you feel happiest or most comfortable?", "How do you define success or progress for yourself?", "What would your ideal day look like if you had no limitations?", "When have you felt truly understood or cared for by someone else?", "What are your core needs that must be met in relationships?", "How do you balance caring for yourself vs. caring for others?", "What do you think your purpose or calling in life might be?",

  "Tell me about some of your role models or influencers.", "What qualities do you admire most in other people?", "Whose approval or praise do you desire the most?", "In what ways do you compare yourself to other people?", "When do you feel insecure around others and why?", "What makes someone worthy of your trust and loyalty?", "Whose opinions about you make the biggest impact on how you feel?", "Do you feel pressure to meet the expectations of others?", "In what ways do you feel competitive or jealous towards others?", "How do you handle constructive criticism or feedback from others?", "Do you ask others for help when you need it?", "Do you feel deserving of the good things you want?", "How are you impacted by rejection or disapproval from others?", "What do you wish other people understood about you?",

  "What activities energize you?", "What obstacles or stressors drain your energy?", "How do you maintain balance among work, family, and lifestyle?", "What are some ways you can be more mindful each day?", "How do you envision your ideal lifestyle five years from now?", "What brings meaning and purpose into your life right now?", "Do you feel aligned with your own core values and motivations?", "What legacy or impact do you want to leave on the world?", "How do you define happiness, progress, and success for yourself?", "What might you regret not doing if you don't make needed changes?", "How do you rise after setbacks or failures?", "What gifts do you have to share with the world?", "How do you stay motivated when faced with challenges?", "What inspires and excites you about the future?", "What does your inner critic say to you?", "How can you quiet your inner critic?", "How do you cultivate more self-compassion?",
]

responses = [
  "Thank you for sharing that with me today.", "I appreciate you opening up about this sensitive topic.", "It's understandable that you would feel that way.", "I'm glad you felt comfortable discussing that.", "It takes courage to be vulnerable about your struggles.", "I'm here to support you without judgement.", "I'd like to better understand your perspective.", "Tell me more about why you feel that way.", "I sense this is really bothering you right now.", "Your feelings are valid. There's nothing wrong with you.", "Let's explore some ways to cope with those emotions.", "I see you have a lot of inner strength even in hard times.", "I think talking this through will be helpful for you.", "My role is to listen without telling you what to do.", "How do you think you might be able to overcome this?", "You seem to have some good insight into what will help.",

  "I appreciate you sharing your story with me. I can tell this is important.", "Let's take some time to unpack what you've told me.", "I want to make sure I understand fully. Can you tell me more?", "Your perspective gives me greater insight into your experiences.", "I understand why you would feel upset about that.", "It sounds like you're being really hard on yourself.", "I hear how much this is impacting you. We will figure it out together.", "While the problem seems big now, I know you have strength to get through this.", 

  "I empathize with how difficult this is for you right now.", "Let's think through what meaningful actions you could take.", "Your needs matter. Don't neglect taking care of yourself.", "What small step could you take today to improve the situation?", "You are not defined by your mistakes. How can you move forward?", "I appreciate you confiding in me. How can I support you through this?", "I believe in you, even if you don't believe in yourself right now.", "You've shown resilience before. You can tap into that strength again.",

  "I can tell you put a lot of thought into what you want to get out of our discussion today.", "I appreciate you being so open and honest with me about this sensitive topic.", "It sounds like these realizations took a great deal of courage and self-reflection on your part.", "I'm glad we're able to have such an in-depth dialogue. Please let me know if talking about any of this becomes overwhelming or uncomfortable."

]

while True:

  user_input = input("You: ")

  sentiment = TextBlob(user_input).sentiment

  if sentiment.polarity < 0:
    response = random.choice(responses)
  else:
    response = random.choice(questions)

  print("Therapist: " + response)

  if user_input == "end":
    break
    
print("Session complete!")
