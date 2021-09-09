# Mayday 

### The best way to mess with Texas

Use a [GPT-2 text generator](https://openai.com/blog/gpt-2-1-5b-release/) along with census and postal data to generate fake reports for the Handmaid's Tale of a reporting system for the 2021 Texas Heartbeat abortion law.

## Setup

You'll need `pipenv`, and you'll need space to download the GPT-2 model(s) that you'd like to use.

The default model is the smallest, called `124M`. It will work fine on CPU or GPU.

It produces [passable results](https://knowyourmeme.com/memes/they-had-us-in-the-first-half), but if you have a GPU with 8GB of RAM I recommend trying one of the larger models (`774M`) instead.

If you do, you'll need to make the corresponding change in `generator.py` - find `ai = aitextgen()` and replace it with `ai = aitextgen(tf_gpt2="774M")` or one of the other GPT-2 models.

## Speed

The text generation part is very slow. This is an estimation of performance for generating a single example on an 8GB 1070 GPU and an i7-7700k CPU:

|Model|Size|GPU   |CPU   |&Delta; |
|-----|----|------|------|--------|
|124M |0.5G|4.5s  |27.2s |6.0x    |
|355M |1.4G|9.8s  |63.4s |6.5x    |
|774M |2.9G|17.9s |118.2s|6.6x    |
|1558M|5.9G|failed|214.1s|+Inf    |

You should check your speed, but I don't recommend using any model that takes longer than 86.4s per generation - that will allow for 1000 reports per day.

