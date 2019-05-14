Sentiment Analysis on Movie Reviews using Deep Neural Networks

This project aims to train the Deep Neural Networks model with movie reviews dataset from two different sources, IMDB
and Rotten Tomatoes. With the trained model, the accuracy will be measured for each dataset, and each data refinement 
methods (for Rotten Tomatoes dataset, two different data refinements will be compared). The main vision of this project
is to improve the accuracy in prediction of the model via varying the model structure (e.g. modifying the layers, hidden
units, activation functions, hyperparameters, etc.)

The codes are structured as following:
1. Loading the data
  - IMDB: from 'train' folder with 'neg' and 'pos' subfolders within the dataset, it assigns 0 and 1 to each label
    types, and put them into labels array. Accordingly, text files in each subfolders are appended to texts array.
    This process is repeated for both 'train' and 'test' folder.
  - Rotten Tomatoes: multi-class (sentiment from 0 to 4) dataset is transformed to binary-class dataset with 0 and 1 
    as labels. For one of the data refinement methods, neutral values (2) are assigned randomly to either positive or 
    positive. The other method discards the entire neutral values. 
2. Training the model 
  - After tokenizing the texts, using embeddings from GloVe, the codes train the model with 3 hidden layers. After the 
    first run of fitting, a new network from scratch are trained again, and evaluated on the test data. 
3. Evaluating the model
  - Model is evaluated to check the accuracy.

Both datasets are taken from Kaggle. The followings are the links to external sources:
IMDB: https://www.kaggle.com/iarunava/imdb-movie-reviews-dataset
Rotten Tomatoes: https://www.kaggle.com/ynouri/rotten-tomatoes-sentiment-analysis/data
Embeddings: https://nlp.stanford.edu/projects/glove/ 
