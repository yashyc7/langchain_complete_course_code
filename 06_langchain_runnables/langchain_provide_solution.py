# all runnables have common method for standardization

# we would make the abstract class to force developers for standardization of the method like invoke etc etc


from abc import ABC, abstractmethod
import random


class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass


class FakeLLM(Runnable):
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

    def invoke(self, prompt):
        if prompt:
            response_list = [
                "Delhi is the capital of india",
                "Mumbai is the capital of maharastra",
                "kolkata is the capital of WB",
            ]

            return {"response": random.choice(response_list)}
        return None


class FakePromptTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    # TypeError: Can't instantiate abstract class FakeLLM without an implementation for abstract method 'invoke'
    # we must have to create the invoke method


llm = FakeLLM()
template = FakePromptTemplate(
    template="write a poem about {topic}", input_variables=["topic"]
)


class RunnableConnector(Runnable):
    def __init__(self, runnables_list):
        self.runnables_list = runnables_list

    def invoke(self, input_data):
        for runnable in self.runnables_list:
            input_data = runnable.invoke(
                input_data
            )  # output data will be the input of the next component
            return input_data  # which is the input data


class FakeStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data["response"]


llm = FakeLLM()
template = FakePromptTemplate(
    template="write a poem about {topic}", input_variables=["topic"]
)
parser = FakeStrOutputParser()


chain = RunnableConnector([template, llm, parser])
answer = chain.invoke({"topic": "india"})
print(answer)


template1 = FakePromptTemplate(
    template="write a joke about {topic} ", input_variables=["topic"]
)

template2 = FakePromptTemplate(
    template="explain the following joke {response}", input_variables=["response"]
)

llm = FakeLLM()

parser = FakeStrOutputParser()

chain1 = RunnableConnector([template1, llm])
chain2 = RunnableConnector([template2, llm, parser])


final_chain = RunnableConnector(
    [chain1, chain2]
)  # like an lego piece the ouput will be an runnable too

ans = final_chain.invoke({"topic": "Cricket"})

print(ans)  # write a joke about Cricket
