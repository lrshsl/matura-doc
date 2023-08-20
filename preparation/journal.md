
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
- Tried to train that model on images that vary in brightness instead in shapes [stage1_2](https://github.com/lrshsl/Vec2Ras/tree/main/src/stage1_2)
  - Even after adapting the models and loss function, I couldn't make the accuracy rise above 0.5
  - The problem must be in the code or the loss function, because the loss is minimized quite well

### On and before June 17th
I couldn't work that much on the project anymore, since I'm in a phase of many exams right now. Though I could do some more experimentation and research during the last weeks. This is where I'm at right now:

The problem with the brightness could not be easily solved, it may not be possible with the same model. I'm planning to take a closer look at [multitask learning](https://en.wikipedia.org/wiki/Multi-task_learning), and maybe use a model with shared layers but different branches to detect several features of the same object.

I've now been researching about existing approaches to tackle the problems I encountered. After searching on [google scholar](https://scholar.google.com/), I found several papers and works that could potentially be helpful:
- [Vectorization of Raster Manga by Deep Reinforcement Learning](https://arxiv.org/abs/2110.04830)
  - Successful ([very precise](https://arxiv.org/pdf/2110.04830.pdf)) raster to vector converter for mangas
  - A subtask of what I try to accomplish
    - interesting pipeline and *model*
  - Can't solve the shape-color problem though
- [Im2Vec](https://arxiv.org/abs/2102.02798)
  - A try to synthesizing vector graphics without vector supervision
  - *Could maybe also be useful for generating train/test vector images*

