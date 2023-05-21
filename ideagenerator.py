import os
import openai
import config


openai.api_key = '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'


def generateTopics(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Generate topics on: {}. \n \n 1.  ".format(prompt1),
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']

def generateSections(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the title in to high level sections: {} \n\n- Introduction: ".format(prompt1),
      temperature=0.6,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def sectionExpander(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the section in to a detailed professional , witty and clever explanation.\n\n {}".format(prompt1),
      temperature=0.7,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return response['choices'][0]['text']
