## Intro
Measuring the reading difficulty of a particular text is a common problem in the educational world, assigning an appropriate reading level metric to new resources remains challenging. We aim to classify each text according to its difficulty level. A text with rating 1000 or more imply that the text is academic and needs prior knowledge while a text with rating 100 or below shows that the text is for beginner readers and primary school students. According to that way we could match each reader with the most suitable book. By the most suitable book we mean that the reader will complete it with an acceptable reading accuracy.

**Case study**:\
Current systems have been widely criticized for  misrepresenting the difficulty of texts which causes frustration for students and educators alike. Currently the most popular metric is the Lexile Reading Measure which is both proprietary and expensive. One of the Lexile’s naive approach problems is using quantitative classifying methods like mean sentence length, word count and mean log word frequency which could produce errors in the score. 

**Target**:\
Reproducing the results of the Lexile Measure and hopefully improve it.

## Plan:
### 1. Building our Deep Learning model.
The whole graduation project is mainly about building our deep learning model using recurrent neural network. 
		
**I. Data set:** One of the biggest problems of the whole learning process is collecting the data that would be fed to the learning model. Our data set input is basically a large list of books titles.\
			X = The text or the book\
			Y = Lexile Score
		
**II. NLP:** Our data set will pass on a natural language processing phase where each word of our text will be converted to its root. Play, Player, played are all having the same root. This process will help us to reduce the amount of words for a better performance. Also we have to deal with compound words like Chicago bulls which has a literal meaning and also it is the name of basketball team.
		
**III. Parsing data set:** After defining our data set, We need now to parse the our text that are gonna to be evaluated in a regular form to be fed by our network. One approach is to map each word in the text into a single integer. This step is important because neural networks cannot be fed by characters. The need to be only fed by numbers.
		
**IV. Building Neural Network:** Our Neural network will consist of several layers. The first layer will have the mapped numbers that reflect to each word. The last layer will output one number which is the measure of difficulty. Between these two layers there are several layers. We are going to choose the most suitable layers to achieve our goal.
		
**V. Choosing algorithm:** It seems like it is a supervised learning model. I think the problems we need to solve is a linear regression. As we need to output a continuous value of levels for each text.

**VI. Validation and Testing:** There is a good portion of our data set we have not fed in our learning model. That’s because we need some data in order to validate the 	correctness and the reliability of our model. Also this portion is not constant. 

### 2. Building our business model
After making sure that our model is functioning correctly. We have to present our 		product in a fancy way. 
**I. Design Website:** A simple interface for a normal user to interact with our precious	learning model. In this website we are going to apply our software engineering	experiences from the past years with latest full stack web development tools and technologies.

**II. Deploy Website:** Our precious model will have to experience being on the cloud and deal with real users, accept reviews and learn from mistakes. It also depends on our data set license.

**III. Explain our tool:** A short video will allow users to understand what is it all about and how to register and use that tool.



## Tool and Technologies that will be used:
Python: Python will be our main programming  and scientific language for both our learning model and our website. Python is a flexible and easy syntax language.

Tensorflow-Keras: The famous deep learning environment that has been developed by Google. It will be imported as module within python interpreter.

[Mini-Conda](https://conda.io/miniconda.html): The famous python environment for scientific programming. What special about it is that it isolates the scientific environment from the normal python environment which gives an area for trying various libraries without crashing everything. 

[NLTK](https://www.youtube.com/playlist?list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL): Will also be imported within python. Its a useful library for all needed natural language processes.

Matplotlib: Plotting data is crucial for visualizing and decide many things in the learning model. Matplolib gives us a lot flexibility in plotting data within python.

Flask: Flask is a famous python back end framework for developing functional websites.

MVC: A well known design pattern that is used in many websites. What special about it is that it isolates the view from the logic and database.

React or Angular: We will use one of those to develop the front end of the website. Both are well known javascript framework.

SQLAlchemy: Writing sql queries as strings is an old school technique that has a lot of problems. This tool will provide an abstract access to our database using functions that make the 4 basic database orders Create, Read, Update, Delete.

Git & Github: Collaborating with my 2 colleagues will be impossible without version control software. 

Heroku: Online platform that offers hosting websites.

[Trello](https://trello.com/b/MFXsyvpR/getting-ready-for-gp): Online platform that is mainly an online sticky notes so that I can set goals and All my colleagues can see them. 

Scrum: One of the most famous agile ways that we are going to follow through our project. We will divide our project to several sprints. Every sprint will take one or two weeks to complete and ends by a sprint review.

Whatsapp: Our main communication method to contact each other and our beloved supervisor Dr. Ali Fahmy..
