from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion
import os

load_dotenv()

class ExampleFlow(Flow):
    gemini_api_key = os.environ['GEMINI_API_KEY']
    model = "gemini-1.5-flash"

    @start()
    def generate_city(self):
        print("Starting flow")

        response = completion(
            model=self.model,
            api_key=self.gemini_api_key,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world.",
                },
            ],
        )
        random_city = response["choices"][0]["message"]["content"]
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_city)
    def generate_fun_fact(self, random_city):
        print("Received random city:", random_city)
        response = completion(
            model=self.model,
            api_key=self.gemini_api_key,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {random_city}",
                },
            ],
        )
        fun_fact = response["choices"][0]["message"]["content"]
        return fun_fact

flow = ExampleFlow()
result = flow.kickoff()

print(f"Generated fun fact: {result}")