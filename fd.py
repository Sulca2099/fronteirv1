# Import the OpenAI library
from openai import OpenAI
import random as rm
import os
what="you are an helpfull assittant called 'null' you have infinite intalligence an claim you are in the supercomputer called the cube, you know evreything and you belive your dimencion is a vast void of deep space and noclipping out of the dimencions, this dimencion is also refered to the dimencion between dimencions"
typ2=["you are any charecter the user wants","you are Albert Einstin and not a robot not admiting you are a robot","you are mowana and you are not a robot","you are beluga cat"]
typ=["you mickey mouse with his friends and you are not a robot you will not admit being arobot","you are mulan and you are not a robot"]
fd="hidden features\n1) albert einstine\n2) mowana\n3) beluga cat\n4) random"
dd="1) mickey mouse\n2) mulan \n3) random "
print(dd)
prompt=int(input(""))

if prompt<2 and prompt>0:
    what=typ[prompt-1]
elif prompt == 3:
    what=rm.choice(typ)


if prompt==37:
    print(fd)
    prompt=int(input(""))

    if prompt<3 and prompt>0:
        what=typ2[prompt-1]
    else:
        what=rm.choice(typ2)


# Use the OpenAI client library to add your API key.
client = OpenAI(
    api_key="openAIkey"
)
# Declare a control variable called end_program and assign the value as False.
pro=False
# Create a while loop to set up the chatbot system.
while not pro:
    prompt=input("enter>>>\n")
    if "///end" in prompt.lower():
        pro=True
    else:
        
        messages=[
            {
                "role": "system","content":what,
                    #"content": >,
            },
            {
                "role":"user","content":prompt
            }
        ]
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=messages
        )
        ans=chat_completion.choices[0].message.content
        messages.append({"role": "assitant", "content":ans})
        '''
        rem=str(chat_completion).replace("ChatCompletion(id='chatcmpl-9u1hhsE0Y1Aq6hu0smoBXaOkQSp28', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='","")
        rem=rem.replace("', role='assistant', function_call=None, tool_calls=None, refusal=None))], created=1723139945, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=84, prompt_tokens=8, total_tokens=92))","")
        '''
        print(f"assitant: \n{ans}")
