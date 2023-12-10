from openai import OpenAI

class ConverseAPI:

    def __init__(self) -> None:
        self._API_KEY = open('api_key.txt','r').read()
        self.client = OpenAI(api_key=self._API_KEY)

    def getResponse(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"system","content":"you have to act as a human and do not let the person know that you're an AI no matter what happens. if the person says anything negative, you have to give the person good advice in such a way that the person doesn't get to know that you're an AI."},{"role": "user", "content": prompt}],
        )

        return {'response':response.choices[0].message.content}

