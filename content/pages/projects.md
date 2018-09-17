Title: Projects
Category: Projects
Slug: projects

## Spooky Author Identification
- Problem: Authorship attribution
- Type: Multiclass classification
- Task: To identify authors based on samples of their writings
- Dataset: <a href="https://www.kaggle.com/c/spooky-author-identification/data" target="_blank">Kaggle Spooky Author Identification</a>
- Project: <a href="https://github.com/mrbarbasa/kaggle-spooky-author" target="_blank">GitHub repository</a>

This is my capstone project work for <a href="https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t" target="_blank">Udacity's Machine Learning Engineer Nanodegree</a> program, in which I applied machine learning and NLP techniques to solve an authorship attribution problem. The task was to identify the horror authors Edgar Allan Poe, H.P. Lovecraft, and Mary Wollstonecraft Shelley from samples of their writings. 60 iterations of 10-fold cross validation random search was run for each of the following six models: an MLP with the top 20,000 most common n-gram features, an MLP with all n-gram features, a CNN with GloVe embeddings, an RNN with GloVe embeddings, a CNN with fastText embeddings, and an RNN with fastText embeddings. Using multiclass logarithmic loss, or logloss, as the evaluation metric, it was the tuned MLP with all n-gram features that scored the lowest validation logloss, therefore performing the best. I have published the results in a project report, accessible <a href="https://github.com/mrbarbasa/kaggle-spooky-author/blob/master/report/report.pdf" target="_blank">here</a>.
