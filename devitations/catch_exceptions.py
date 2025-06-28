
# devitations/catch_exceptions.py

"""
🧘 Devitation 03: Catch the Exceptions
Reason: Mindfulness lets you intercept reactivity before it causes bugs in behaviour.
"""

from time import sleep

def handle_emotion(emotion):
    try:
        print(f"// Observing: {emotion}")
        if emotion == "anger":
            raise Exception("🔥 Uncaught Reaction")
        elif emotion == "fear":
            raise Exception("❄️ Freeze Stack Overflow")
        else:
            print("// Emotion logged. Letting it pass.")
    except Exception as e:
        print(f"// Exception caught: {str(e)}")
        print("// Initiating breath handler...")
        breath_sequence()

def breath_sequence():
    print("Breathing through stack trace...")
    sleep(4)
    print("Clearing mental cache...")
    sleep(3)

if __name__ == "__main__":
    print("// Monitoring internal state...")
    handle_emotion("anger")
    handle_emotion("joy")
