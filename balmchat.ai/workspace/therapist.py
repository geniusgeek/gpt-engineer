import random

class Therapist:
    def analyze_sentiment(self, message: str) -> str:
        # Placeholder sentiment analysis
        positive_words = ["happy", "good", "great"]
        negative_words = ["sad", "bad", "depressed"]

        if any(word in message.lower() for word in positive_words):
            return "positive"
        elif any(word in message.lower() for word in negative_words):
            return "negative"
        else:
            return "neutral"

    def generate_response(self, sentiment: str, message: str) -> str:
        # Placeholder response generation
        if sentiment == "positive":
            return random.choice(["That's great to hear!", "I'm glad you're feeling good."])
        elif sentiment == "negative":
            return random.choice(["I'm sorry to hear that.", "Let's talk about why you're feeling this way."])
        else:
            return random.choice(["Tell me more.", "How can I help you?"])
