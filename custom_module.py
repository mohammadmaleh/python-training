from random import choice

capital = "Tokyo"
flower = "Sakura"
bird = "Parrot"
song = "Kiss"


def random_fun_fact():
    fun_facts = [
        "Tokyo is the most populous metropolitan area in the world, with over 37 million people.",
        "Tokyo was originally a small fishing village called Edo, which means 'estuary'.",
        "Tokyo is home to the busiest train station in the world, Shinjuku Station, which serves over 3.5 million people daily.",
        "The city has a café where you can cuddle with hedgehogs, called Harry Hedgehog Café.",
        "Tokyo Tower was inspired by the Eiffel Tower and stands taller at 333 meters.",
        "The Shibuya Crossing is one of the busiest pedestrian crossings in the world, with as many as 3,000 people crossing at once.",
        "Tokyo Disneyland was the first Disney park to be built outside of the United States, opening in 1983.",
        "In Tokyo, vending machines are everywhere, with approximately one machine for every 23 people.",
        "Tokyo has over 100 Michelin-starred restaurants, making it the city with the most Michelin stars in the world.",
        "The Tsukiji Market in Tokyo was the largest fish market in the world until it moved to a new location in 2018.",
    ]
    index = choice(range(len(fun_facts)))
    return fun_facts[index]
