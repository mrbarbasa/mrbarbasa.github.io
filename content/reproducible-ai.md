Title: AAAI 2019 Reproducible AI Workshop Takeaways
Date: 2019-01-30 12:50
Modified: 2019-01-30 12:50
Category: Machine Learning
Tags: ai machine-learning
Slug: reproducible-ai
Authors: Marifel Barbasa
Summary: Takeaways from the Reproducible AI workshop that I attended at the AAAI 2019 Conference.

AI is a science, and reproducible experiments are key to validating results. However, the field of AI is not known for its reproducibility. I've experienced this firsthand over the past months as a newcomer to the field. For example, while [Kaggle](https://www.kaggle.com/) is generally agreed upon as a great learning tool for modern machine learning techniques, I find it difficult to learn from. Competitors often fork Kaggle kernels with mediocrely-structured code and either don't change any code or change a few numerical parameters, just to score higher on the leaderboard and publish "their work" as a new high-scoring kernel. Hence, one has to look elsewhere for good coding practices, decent documentation, and reproducibility (such kernels are rare gems on Kaggle). These experiences, along with my background in software engineering and attempting to get used to reading code in Jupyter Notebooks, has led to my interest in the Reproducible AI workshop.

The full-day Reproducible AI workshop was held at the Association for the Advancement of Artificial Intelligence (AAAI) 2019 Conference on January 27th. The workshop chairs were Yolanda Gil (University of Southern California), Odd Erik Gundersen (Norwegian University of Science and Technology), Satinder Singh (University of Michigan), and Joelle Pineau (McGill University). The purpose of the workshop was to discuss and gather ideas "to make a roadmap for improving the reproducibility of research result[s] presented at future AAAI conferences and other AAAI publications" [[1](https://www.idi.ntnu.no/~odderik/RAI-2019/)]. It is admirable that AAAI and workshop chairs are working on creating strides, no matter how small, towards reproducibility in AI research and focusing on practical solutions rather than attempting to solve the whole problem at once. While actionable results in AAAI conferences and publications were the goal, much of the material presented and ideas discussed are relevant to all AI researchers, engineers, and decision makers. More information about the workshop, including the full list of presentation topics and speakers, can be found [here](https://www.idi.ntnu.no/~odderik/RAI-2019/).

There are many contributing factors that make reproducibility within AI research difficult. The popular usage of Jupyter Notebooks within the AI and data science communities might be one of them. Notebooks hardcode their parameters and allow for cells to be run out of order. They don't help enforce dependencies, and once you use them, you are pretty much locked into using them. They combine library with experiment code and lump together code and data; overall, that is a recipe for poorly factored code. Notebooks complicate code reviews and make unit testing the code within them difficult. They also do not allow for easy separation of tests from experiments (such as when using assertions in the notebook). Furthermore, it is difficult to build upon code written in notebooks; this is terrible for advancing science. As Joel Grus stated at the workshop, "'Notebooks as a source of reproducibility' presupposes a static view of AI as a science" [[2](https://www.idi.ntnu.no/~odderik/RAI-2019/presentations/if_not_notebooks.pdf)]. In my view, the main advantage of notebooks are that they are good for their interactiveness, constructing and consuming conceptual tutorials, and trying something out quickly. But perhaps they should not be used, at least entirely, for AI research code.

Another contributing factor to irreproducible AI research is that machine learning development is much harder than traditional software development. While software is built to meet certain functional specifications, machine learning systems are built to optimize metrics. While software requires quality code, machine learning requires much more than that: quality input data, quality methods, quality metrics, and quality tuning. Production machine learning is even harder since it requires consistent data input; design, retraining, and inference are often carried out by different people; and software must work across different environments. Traditional software development, on the other hand, became faster through development lifecycle tools, and these tools are useful enough that a team of developers can work effectively with one another. It is also not as difficult for a software developer to jump across different teams and projects, due to these tools. Another problem with reproducibility, especially in AI, is that it takes a lot more time and effort to implement. For many, if the benefits of reproducibility are not immediate, then it might not be worth the extra time and effort, since it is the nature of research to publish first or iterate quickly on ideas that might not make it into a paper.

Now that we've established that reproducibility in AI research is difficult, what can we do to strive towards reproducibility? Proposed solutions are to start with simpler models, then only if behavior is good enough, try to scale up. Proper documentation can go a long way with clearly explained experiments, results, and how to execute the project.

We can assign responsibilities to the following groups of people: paper publishers, reviewers, authors, and the AI community. The main idea is that, if we require authors to do certain things, they will do them if it means that their paper is more likely to get accepted or published.

We can assign publishers any of the following tasks:

- Have a reproducibility track at conferences and establish guidelines around that
- Provide reproducibility guidelines or requirements to paper authors; instead of accomplishing this per publisher, all publishers around the world should agree on a specific set of reproducibility criteria, not for a reproducibility track but for acceptance into publications and conferences
- Create a reward mechanism for original authors whose work has been reproduced by other researchers, such as a Most Reproducible Paper Award or a badge system on published papers
- Find a lightweight way for graduate students to reproduce work
- Require that paper authors have multiple sections to their experiments, such as working with toy problems (if their dataset is too huge for the average researcher to reproduce their experiments and results) and then large-scale problems
- Publishers should provide private data and code repositories for published papers

We can assign reviewers any of the following tasks:

- Publishers can set a budget and reviewers can then vote on which papers to reproduce; this might help in assessing the reproducibility of certain papers

We can assign authors any of the following tasks:

- Write an explicit paragraph in the paper itself about reproducibility of the paper's experiments and results
- Document everything about the code, data, methods, parameters, and results
- Anonymize data if necessary so that they can share it with the public

Other tasks that the AI community can accomplish:

- Some sort of recognition or public system in which publishers or the community can explicitly ask authors whether they think that their work is reproducible; then we can have a web application to crowdsource publisher or community ratings

In conclusion, in order to achieve reproducibility in AI research, we need to standardize how we measure reproducibility and make extensiblility of AI software systems a focus. The next steps for workshop attendees are to await an email from the workshop chairs to cast our vote on the tasks that should be carried out first. It was suggested that we start small and vote on pressing matters or those that have a higher chance of being carried out.
