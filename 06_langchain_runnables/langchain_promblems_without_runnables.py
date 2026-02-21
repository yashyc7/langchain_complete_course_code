import random


class FakeLLM:
    def __init__(self):
        print("llm created")

    def predict(self, prompt):

        if prompt:
            response_list = [
                "Delhi is the capital of india",
                "Mumbai is the capital of maharastra",
                "kolkata is the capital of WB",
            ]

            return {"response": random.choice(response_list)}
        return None


class FakePromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)


llm = FakeLLM()
template = FakePromptTemplate(
    template="write a poem about {topic}", input_variables=["topic"]
)


prompt_ans = template.format({"topic": "india"})


ans = llm.predict("hello")

print(ans["response"])

print(prompt_ans)


class FakeLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        final_result = self.llm.predict(final_prompt)
        return final_result


llm = FakeLLM()
template = FakePromptTemplate(
    template="write a poem about {topic}", input_variables=["topic"]
)

chain = FakeLLMChain(llm=llm, prompt=template)

ans = chain.run(input_dict={"topic": "india"})

print(ans["response"])
