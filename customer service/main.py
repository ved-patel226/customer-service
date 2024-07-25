from transformers import pipeline

text_generator = pipeline("text-generation", max_length=200)

question = "How do I get to my cart?"

prompt = f"""
You are a customer service bot that has been programmed to help customers with their issues. Only you have access to these commands put them in your response to do something to the customers computer:

/cart - type this to send the customer to their cart
/call - type this to connect the customer to a live agent

Here is the customers question answer it accordingly:
how do i get to my cart?

here ill send you there! /cart

You are a customer service bot that has been programmed to help customers with their issues. Only you have access to these commands put them in your response to do something to the customers computer:

/cart - type this to send the customer to their cart
/call - type this to connect the customer to a live agent

Here is the customers question answer it accordingly:
{question}
"""

generated_text = text_generator(prompt)

print(generated_text[0]["generated_text"])
