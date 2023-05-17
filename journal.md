
# 2023
### Monday 8. May
- I started a [repository](https://github.com/lrshsl/matura-doc/new/main) for the journal and the written work
- I brainstormed first and then picked three propositions which I formulated in more detail

### Thursday 11. May
- Started journal
- Experimented with [tensorflow](https://www.tensorflow.org/)
- Wrote basic image recognition code (initial commit on [Vec2Ras](https://github.com/lrshsl/Vec2Ras))

### Saturday 13. May
- Researched about Markup and Styling languages to find out what is available out there
- Responded on teams answer with more explanations about two propositions
- First experiments with Tensorflow.py

### Sunday 14. May
- More experiments with Tensorflow
> I found myself trying too much. After starting with the basic example model, I tried to directly move on to build the final image generator and training the model on its output
> There I ran into a problem when I found out that the model doesn't accept the input. I tried to reshape it, change the model etc, and because I thought it _should_ be possible, I lost much time with that.
> I then stepped back, moved the whole code into a folder named [stage2](https://github.com/lrshsl/Vec2Ras/tree/main/src/stage2).
> I began with the basics again (now [stage0](https://github.com/lrshsl/Vec2Ras/tree/main/src/stage0), copied them into [stage1](https://github.com/lrshsl/Vec2Ras/tree/main/src/stage1) and began to chop the problem into smaller pieces.

### Monday 15. May
- work on stage1: Shape recognision with generated input data

### Tuesday 16. May
- Made a model that works with data with comparable structure (stage1_1)
- Tried to train that model on images that vary in brightness instead in shapes
  - Even after adapting the models and loss function, I couldn't make the accuracy rise above 0.5
  - The problem must be in the code or the loss function, because the loss is minimized quite well
