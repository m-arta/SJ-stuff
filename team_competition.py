import random

print('Who will win the team competition?')

messages = ['Poland',
            'Norway',
            'Austria',
            'Germany',
            'Japan',
            'Czech Republic',
            'Slovenia',
            'Russia',
            'Finland',
            'Switzerland',
            'Competition cancelled due to wind conditions']

print(messages[random.randint(0, len(messages) - 1)])
