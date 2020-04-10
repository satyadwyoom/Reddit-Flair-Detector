### **STEPS PERFORMED WHILE DOING THIS PROJECT :**

1. **DATA EXTRACTION**
    * Data extraction from [**r/india**](https://www.reddit.com/r/india/) using [praw](https://github.com/praw-dev/praw)
    * Features extracted were :
        * Post Flair 
        * Post Title : It was chosen because it depicts a short description of the post itself.
    * Data was saved as a .csv file in [datasets](https://github.com/satya29m3/Reddit-Flair-Detector/tree/master/datasets)

2. **DATA VISUALIZATION AND PREPROCESSING**
    * Data was loaded
    * Data was visualised: [Here](https://github.com/satya29m3/Reddit-Flair-Detector/tree/master/Jupyter%20Notebook/Data_visualization.ipynb)

    ![Alt text](images/pie.jpg?raw=true "Title")
    ![Alt text](images/bar.jpg?raw=true "Title")
    


    * Three types of Preprocessing methods were used :
        * Simple Preprocessing : Reduced words to lowercase & and removed stopwords.
        * Stemming : Simple preprocessing + stemming the words to it's respective root form.
        * Lemmatization : Simple preprocessing + Lemmatizing the words to it's root form based upon a vocabulary.
    * Preprocessed datasets were saved.

3. **BUILDING A CLASSIFIER FOR FLAIR PREDICTION**
    * Data was loaded
    * Post Titles were converted to Tfidf features
        * Tfidf : Term Frequency Inverse Document Frequency
        * It helped us giving more weight to the words which were could be important
        ![tfidf](https://www.tmblast.com/wp-content/uploads/2018/11/TF-IDF-Report-from-Moz.jpg)

        * Models :
            * MultiNomial Naive Bayes Classifier
                * f1_score = 0.657
                * accuracy = 0.653
                * precision = 0.675
                * recall = 0.668
            * Random Forest Classifier
                * f1_score = 0.675
                * accuracy = 0.6887
                * precision = 0.6801
                * recall = 0.6886
            * Support Vector Classifier
                * f1_score = 0.687
                * accuracy = 0.684
                * precision = 0.696
                * recall = 0.688
            * Multi Layered Perceptron Classifier
                * f1_score = 0.656
                * accuracy = 0.654
                * precision = 0.662
                * recall = 0.656

4. **PREDICTION**
    * For prediction Support Vector Classifier was used because it haa the highest f1_score
        * f1_score is best metrics while performing classification tasks because it takes into account both precision and recall.

5. **DEPLOYMENT**
    * A Flask Web App was deployed on heroku.
    * [Link to Web App](https://reddit-flair-detector-api.herokuapp.com/)
    * For automated testing send the post request to :
    ```
    https://reddit-flair-detector-api.herokuapp.com/automated_testing
    ```
