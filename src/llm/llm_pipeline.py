from groq import Groq
import streamlit as st
class LLMPipeline:

    def __init__(self):
        self.client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama3-8b-8192"
        )

        return response.choices[0].message.content