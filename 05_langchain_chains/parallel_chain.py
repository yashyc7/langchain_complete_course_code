from langchain_core.output_parsers import StrOutputParser 
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema.runnable import RunnableParallel

#we will make two models then merge its results
parser = StrOutputParser()
chat_model1 = ChatOllama(model="qwen2.5-coder:7b-instruct-q4_K_M")
chat_model2 = ChatOllama(model="qwen2.5-coder:7b-instruct-q4_K_M")

prompt1= PromptTemplate(template="generate short and simple notes from the following text \n {text} ",input_variables=['text'])

prompt2 = PromptTemplate(template="generate 5 short question answers from the following text \n {text}",input_variables=['text'])

prompt3 = PromptTemplate(template="merge the provided note and quiz into single document\n notes ->notes {notes} and quiz -> {quiz}",input_variables=['quiz','notes'])

parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | chat_model1 | parser ,
        "quiz" : prompt2 | chat_model2 | parser 

    }
)


merge_chain = prompt3 | chat_model1 | parser


chain = parallel_chain | merge_chain


result = chain.invoke({"text":"support vector machines "})

print(result)

chain.get_graph().print_ascii()


# # Support Vector Machines (SVMs): A Comprehensive Guide

# Support Vector Machines (SVMs) are versatile machine learning algorithms widely used for both classification and regression tasks. These algorithms excel in high-dimensional spaces and are particularly effective when the data is non-linear.

# ## Key Concepts

# 1. **Hyperplane**: This is a decision boundary that serves as the optimal separator between different classes in feature space. The hyperplane aims to maximize the margin, which is defined as the distance from the hyperplane to the nearest data points.

# 2. **Margin**: The margin is a critical parameter in SVMs. It represents the distance between the hyperplane and the closest data points (support vectors). A larger margin generally leads to better generalization of the model.

# 3. **Kernel Trick**: This technique enables SVMs to handle non-linearly separable data by transforming it into a higher-dimensional space where linear separation becomes possible. Different kernels, such as linear, polynomial, RBF, and sigmoid, are used for this purpose.

# ## Applications

# SVMs find extensive use in various fields:      

# - **Image Recognition**: SVMs can be used to classify images based on features like edges, textures, etc.
# - **Text Analysis**: They are effective in tasks like spam detection, sentiment analysis, and topic modeling.
# - **Bioinformatics**: SVMs help in analyzing biological data for classification tasks such as protein fold prediction.

# ## Quiz Questions

# 1. **What is the main goal of using Support Vector Machines (SVM)?**
#    - To find the hyperplane that maximizes the margin between different classes in a dataset.   

# 2. **How does an SVM work for classification tasks?**
#    - It identifies the optimal boundary, known as the decision boundary or hyperplane, which separates data points into distinct classes.       

# 3. **What are Support Vectors in the context of SVMs?**
#    - These are the data points that lie closest to the hyperplane and are crucial for defining the hyperplane itself.

# 4. **How does regularization play a role in SVMs?**
#    - Regularization helps prevent overfitting by penalizing large coefficients, ensuring that the model is not too complex.

# 5. **What are some common kernels used with SVMs?**
#    - Common kernels include linear, polynomial, radial basis function (RBF), and sigmoid kernels.

# By understanding these concepts and their applications, you can effectively utilize SVMs for various machine learning tasks.
#             +---------------------------+       

#             | Parallel<notes,quiz>Input |       using runnables

#             +---------------------------+       

#                  **               **            

#               ***                   ***         

#             **                         **       

# +----------------+                +----------------+
# | PromptTemplate |                | PromptTemplate |
# +----------------+                +----------------+
#           *                               *     

#           *                               *     

#           *                               *     

#   +------------+                    +------------+
#   | ChatOllama |                    | ChatOllama |
#   +------------+                    +------------+
#           *                               *     

#           *                               *     

#           *                               *     

# +-----------------+              +-----------------+
# | StrOutputParser |              | StrOutputParser |
# +-----------------+              +-----------------+
#                  **               **            

#                    ***         ***              

#                       **     **                 

#            +----------------------------+       

#            | Parallel<notes,quiz>Output |       

#            +----------------------------+       

#                           *                     

#                           *                     

#                           *                     

#                  +----------------+             

#                  | PromptTemplate |             

#                  +----------------+             

#                           *                     

#                           *                     

#                           *                     

#                    +------------+               

#                    | ChatOllama |               

#                    +------------+               

#                           *                     

#                           *                     

#                           *                     

#                 +-----------------+             

#                 | StrOutputParser |             

#                 +-----------------+             

#                           *                     

#                           *                     

#                           *                     

#               +-----------------------+         

#               | StrOutputParserOutput |         

#               +-----------------------+         

