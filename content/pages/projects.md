Title: Projects
Category: Projects
Slug: projects

## ohia.ai
- Competition: Hawaii Annual Code Challenge 2018
- Placement: 4th, two points away from 2nd place, out of over 20 teams that registered and 19 that presented
- Problem: Plant classification
- Type: Multiclass classification
- Task: To identify photos of native and invasive plants in Hawaii
- Dataset: Custom data collection
- Project: <a href="https://github.com/HACC2018/ohia.ai" target="_blank">GitHub repository</a>, <a href="https://devpost.com/software/ohia-ai" target="_blank">Devpost</a>

Hawaii’s nature is beautiful and powerful. Unfortunately, almost one-third of native Hawaiian plants are endangered or threatened on some level. Motivated by the effort to protect native Hawaii plants, we chose to take on the Plant Identification challenge by building a mobile application that empowers citizen-scientists and official researchers to help protect the nature of the islands for the entire community. Users of the ohia.ai app can take part in this effort by capturing photos of plants and uploading them to our server. Via a TensorFlow.js MobileNet model, our app then returns the top three genus predictions to the user.

## Spooky Author Identification
- Problem: Authorship attribution
- Type: Multiclass classification
- Task: To identify authors based on samples of their writings
- Dataset: <a href="https://www.kaggle.com/c/spooky-author-identification/data" target="_blank">Kaggle Spooky Author Identification</a>
- Project: <a href="https://github.com/mrbarbasa/kaggle-spooky-author" target="_blank">GitHub repository</a>

This is my capstone project work for <a href="https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009t" target="_blank">Udacity's Machine Learning Engineer Nanodegree</a> program, in which I applied machine learning and NLP techniques to solve an authorship attribution problem. The task was to identify the horror authors Edgar Allan Poe, H.P. Lovecraft, and Mary Wollstonecraft Shelley from samples of their writings. 60 iterations of 10-fold cross validation random search was run for each of the following six models: an MLP with the top 20,000 most common n-gram features, an MLP with all n-gram features, a CNN with GloVe embeddings, an RNN with GloVe embeddings, a CNN with fastText embeddings, and an RNN with fastText embeddings. Using multiclass logarithmic loss, or logloss, as the evaluation metric, it was the tuned MLP with all n-gram features that scored the lowest validation logloss, therefore performing the best. I have published the results in a project report, accessible <a href="https://github.com/mrbarbasa/kaggle-spooky-author/blob/master/report/report.pdf" target="_blank">here</a>.

## Lazy Chef Bot
- Problem: Recipe recommendation
- Type: POS tagging, API usage
- Task: To create a Twitter bot that shares recipes with users, given ingredients
- Dataset: spoonacular's Recipe API, user's Twitter tweets
- Project: <a href="https://2016.nodeknockout.com/entries/248-learning-name-processing" target="_blank">Node Knockout 2016</a>, <a href="https://twitter.com/lazychefbot" target="_blank">Lazy Chef Bot on Twitter</a>

A Twitter bot that responds with recipes if you tweet it ingredients. For our Node Knockout 2016 project, I learned how to run the POS tagger from spaCy (and therefore Python) on a Node.js server.

## W.A.T.E.R.S.
- Competition: NASA Space Apps Challenge 2016
- Award: Global Nominee
- Type: Data visualization web application
- Project: <a href="http://lauragonzalezzz.github.io/waters/" target="_blank">Deployed project</a>, <a href="https://github.com/lauragonzalezzz/hi20_nasa_hackathon" target="_blank">GitHub repository</a>, <a href="https://2016.spaceappschallenge.org/challenges/earth/earth-live/projects/w.a.t.e.r.s." target="_blank">Project video and details page</a>

We created an interactive animation that visually displays the rise of sea levels as users mouse over a range of years. The purpose of We All Track Earth's Rising Sea levels (W.A.T.E.R.S.) is to provide a platform for individuals of any age around the world to easily access NASA's and NOAA's extensive data to bring more awareness to the impact of rising sea levels.

## HOME
- Competition: AT&T University of Hawaii Mobile Tech Hackathon 2016
- Award: Best Smart City Application
- Type: Data visualization web application
- Project: <a href="https://github.com/DaDataDudes/HOME" target="_blank">GitHub repository</a>, <a href="https://www.hawaii.edu/news/2016/03/14/uh-tech-students-among-the-winners-at-att-uh-hackathon/" target="_blank">News article on hackathon winners</a>

We developed the Homeless Observation & Mapping Engine (HOME) to log data about the homeless and visualize homeless populations within the different counties of Hawaii.

## Werewolf
- Type: Mobile multiplayer game
- Project: <a href="https://github.com/mrbarbasa/werewolf" target="_blank">GitHub repository</a>, <a href="https://medium.com/@mrbarbasa/project-werewolf-c1b1fc7bcacd" target="_blank">Medium post on project inspiration</a>

An 8-player mobile-responsive game based on Werewolf and Town of Salem, powered by Meteor.

## Committed
- Type: Data visualization web application

A web app powered by the GitHub API that displays each DevLeague student's number of commits, repos created, and repos forked for the previous week. A progress bar represents the number of commits a student has made relative to the student with the highest number of commits for the previous week. Built while I was a student at DevLeague.

## HI Mobility
- Type: Hybrid mobile application
- Project: <a href="https://github.com/hitraffic/mobile" target="_blank">GitHub repository</a>, <a href="https://github.com/hitraffic" target="_blank">HI Traffic GitHub organization</a>

A hybrid mobile app powered by the Ionic Framework. Utilizes the HI Traffic API to provide traffic incident reports on Oahu. I worked on the incidents list and saving settings to local storage.

## WTF*Do I Do!?!
- Type: Two-player iPad game
- Project: <a href="https://globalgamejam.org/2015/games/wtfdo-i-do" target="_blank">Project details page</a>

A two-player iPad game built over a weekend using Haxe. Player one is a bunny in a cute dream-like world but finds he or she must escape, led by the voice of player two, who is trapped in a world of darkness. I focused on implementing portions of the game logic, such as picking up and dropping items, as well as positioning assets on the background.

## Legistates
- Competition: Startup Weekend Honolulu 2014
- Placement: 3rd
- Type: Web application
- Project: <a href="https://twitter.com/legistates" target="_blank">Legistates on Twitter</a>

Legistates is a startup whose goal is to transform the way our generation engages with issues and topics they care about, starting with making Hawaii State Legislature bills more accessible to the community. My primary role was to design and implement the front page of the app using Bootstrap, HTML, and CSS.

## JavaScript Zombies
- Type: JavaScript OOP programming exercise
- Project: <a href="https://github.com/mrbarbasa/js-zombies" target="_blank">Original GitHub repository</a>, <a href="https://github.com/devleague/js-zombies" target="_blank">DevLeague GitHub repository (most up-to-date)</a>

A JavaScript object-oriented programming exercise modeling a simple player vs. zombie game that I created for DevLeague students. My instructors helped in writing tests and contributing to the README.
