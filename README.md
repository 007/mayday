# Mayday 

### The best way to mess with Texas

Use a [GPT-2 text generator](https://openai.com/blog/gpt-2-1-5b-release/) along with census and postal data to generate fake reports for the Handmaid's Tale of a reporting system for the 2021 Texas Heartbeat abortion law.

## Setup

You'll need `pipenv`, and then you'll need to download the GPT-2 model(s) that you'd like to use.

The default model is the smallest, called `124M`. It will work fine on CPU or GPU.

It produces [passable results](https://knowyourmeme.com/memes/they-had-us-in-the-first-half), but if you have a GPU with 8GB of RAM I recommend trying one of the larger models instead:
```bash
screen -dmS download.774 pipenv run python3 ./download_model.py 774M
```

You'll need to make the corresponding change in `generator.py` - `interact_model` has a parameter for `model_name` that should match whichever one you download.
