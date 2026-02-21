"""used for implementing conditional chains where we would be using the custom logic by ourselves  """

from langchain_ollama import ChatOllama
from langchain_classic.schema.runnable import RunnableSequence,RunnableBranch,RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 





prompt_1 = PromptTemplate(template = "write a detailed report on {topic}",input_variables=['topic'])

prompt_2 = PromptTemplate(template="summarize the following text \n {text}",input_variables=['text'])

model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")


parser = StrOutputParser()

repot_gen_chain = RunnableSequence(prompt_1,model,parser)


#in runnable branch we would send the tuples and on those tuples we would write conditions


branch_chain = RunnableBranch(
    (lambda x:len(x.split())>500,RunnableSequence(prompt_2,model,parser)),

    #(condition,runnable)
    RunnablePassthrough()#this is default execute when condition failsof text count >500

)

final_chain = RunnableSequence(repot_gen_chain,branch_chain)


print(final_chain.invoke({"topic":"car"}))
print(final_chain.get_graph().print_ascii())



# ### Comprehensive Car Report

# #### Introduction
# Cars have significantly transformed transportation across civilizations, influencing economies, societies, and cultures globally. This report aims to provide an overview of car history, types, features, environmental impact, and future trends.

# ---

# #### Historical Overview
# The roots of cars date back to the 19th century when inventors like George Bidder, Nicolas-Joseph Cugnot, and Robert Baker made important advancements. Henry Ford's introduction of the Model T in 1908 marked a turning point as it popularized mass production techniques.

# - **Key Milestones**:
#   - 1896: Otto invented the first four-stroke internal combustion engine.
#   - 1893: The inaugural car race occurred, pitting cars against each other over 2 kilometers.
#   - 1908: Henry Ford introduced the Model T, popularizing mass production and setting the stage for modern auto manufacturing.        

# ---

# #### Types of Cars
# Cars are categorized into various types to cater to diverse needs, preferences, and purposes:

# - **Passenger Vehicles (PVs)**:
#   - Sedans: Comfortable and spacious designs often used for commuting and daily activities.
#   - SUVs: Popular among families for increased space and off-road capability.
#   - Coupes: Stylish and sporty, emphasizing style over practicality.

# - **Commercial Vehicles (CVs)**:
#   - Trucks/Van: Built to handle heavy loads or transport goods.    
#   - Buses: Designed for public transit systems and school use.     

# - **Electric Vehicles (EVs)**: Utilizing battery technology for zero tailpipe emissions. EVs come in various sizes, suitable for urban mobility.

# ---

# #### Features of Modern Cars
# Modern cars integrate numerous features to enhance safety, convenience, and performance:

# - **Safety Features**: Airbags, electronic stability control (ESC), traction control systems.

# - **Advanced Technologies**: Adaptive cruise control, lane departure warning, blind-spot monitoring systems.

# - **Connectivity**: On-board computers for navigation, entertainment, and communication. Some models feature smartphone integration like Apple CarPlay or Android Auto.

# - **Electricity Management**: High-efficiency engines, regenerative braking, advanced battery technology (EVs).

# ---

# #### Environmental Impact
# The automotive industry significantly impacts the environment due to its fossil fuel reliance:

# - **Emissions**: Cars contribute substantially to air pollution through tailpipe emissions of carbon dioxide, nitrogen oxides, and particulate matter.

# - **Waste Management**: Manufacturing involves waste generation from materials like steel, plastic, and rubber. Recycling rates vary by region and regulations.

# ---

# #### Future Trends
# Emerging trends are expected to transform the automotive landscape:

# - **Electrification**: Increasing adoption of electric vehicles powered by renewable energy sources.

# - **Autonomous Driving**: Advancements aiming for fully self-driving cars within the next decade.

# - **Sustainable Materials**: Use of bio-based materials and recycling initiatives to reduce environmental impact.

# ---

# #### Conclusion
# Cars have evolved from rudimentary contraptions to sophisticated mobility solutions, addressing diverse needs. Looking ahead, integrating sustainable practices and embracing innovation will be crucial in maintaining a healthy environment while improving accessibility and convenience worldwide.
#   +-------------+    
#   | PromptInput |
#   +-------------+
#           *
#           *
#           *
# +----------------+
# | PromptTemplate |
# +----------------+
#           *
#           *
#           *
#   +------------+
#   | ChatOllama |
#   +------------+
#           *
#           *
#           *
# +-----------------+
# | StrOutputParser |
# +-----------------+
#           *
#           *
#           *
#     +--------+
#     | Branch |
#     +--------+
#           *
#           *
#           *
#   +--------------+
#   | BranchOutput |
#   +--------------+
# None