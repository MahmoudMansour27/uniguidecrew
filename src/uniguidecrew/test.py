from google import genai

client = genai.Client(api_key="AIzaSyA2Xm4ZNEbkvlctbUEJCg8KqvGHyfdLTIw")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="What is the capital of France?",
)

print(response.text)