### **STEPS PERFORMED WHILE DOING THIS PROJECT :**

1. **DATA EXTRACTION**
    * Data extraction from [**r/india**](https://www.reddit.com/r/india/) using [praw](https://github.com/praw-dev/praw)
    * Features extracted were :
        * Post Flair 
        * Post Title : It was chosen because it depicts a short description of the post itself.
    * Almost equal sample were extracted, So that when we train our model, It does not get biased towards a single class.
    * Data was saved as a .csv file in [datasets](https://github.com/satya29m3/Reddit-Flair-Detector/tree/master/datasets)


2. **DATA VISUALIZATION AND PREPROCESSING**
    * Data was loaded
    * Data was visualised: [Here](https://github.com/satya29m3/Reddit-Flair-Detector/tree/master/Jupyter%20Notebook/Data_visualization.ipynb)

    ![Alt text](images/pie.jpg?raw=true "Title")
    ![Alt text](images/bar.jpg?raw=true "Title")
    * General word features include :

        ![Alt text](images/new_wordcloud.jpg?raw=true "Title")


    


    * Three types of Preprocessing methods were used :
        * Simple Preprocessing : Reduced words to lowercase & and removed stopwords.
        * Stemming : Simple preprocessing + stemming the words to it's respective root form.
        * Lemmatization : Simple preprocessing + Lemmatizing the words to it's root form based upon a vocabulary.
    * We try to train on models on each of these features, and try to which type of preprocessing works the best for our goal.
    * Preprocessed datasets were saved.

3. **BUILDING A CLASSIFIER FOR FLAIR PREDICTION**
    * Data was loaded
    * Post Titles were converted to Tfidf features
        * Tfidf : Term Frequency Inverse Document Frequency
        * It helped us giving more weight to the words which were could be important
        ![tfidf](https://www.tmblast.com/wp-content/uploads/2018/11/TF-IDF-Report-from-Moz.jpg)

        * Models :
            * MultiNomial Naive Bayes Classifier (M_nb)
            * Random Forest Classifier (Rf)
            * Support Vector Classifier (svc)
            * Multi Layered Perceptron Classifier (Mlp)
            
        * Reason for Choosing these Models:
            * these are some of the best models for Classification tasks using textual features as input.

        * Results:

                * Using Stemmed Features :

                    | model | f1_Score | accuracy | precision | recall |
                    |-------|----------|----------|-----------|--------|
                    | M_nb  | 0.657    | 0.653    | 0.675     | 0.668  |
                    | Rf    | 0.675    | 0.6887   | 0.6801    | 0.6886 |
                    | svc   | 0.687    | 0.684    | 0.696     | 0.688  |
                    | Mlp   | 0.656    | 0.654    | 0.662     | 0.656  |

                * Using Lemmetized Features :

                    | model | f1_Score | accuracy | precision | recall |
                    |-------|----------|----------|-----------|--------|
                    | M_nb  | 0.583    | 0.579    | 0.607     | 0.610  |
                    | Rf    | 0.643    | 0.649    | 0.641     | 0.669  |
                    | svc   | 0.657    | 0.649    | 0.667     | 0.676  |
                    | Mlp   | 0.597    | 0.591    | 0.589     | 0.621  |

                * Using Simple Preprocessed Features :

                    | model | f1_Score | accuracy | precision | recall |
                    |-------|----------|----------|-----------|--------|
                    | M_nb  | 0.595    | 0.622    | 0.621     | 0.608  |
                    | Rf    | 0.625    | 0.649    | 0.624     | 0.637  |
                    | svc   | 0.619    | 0.622    | 0.657     | 0.609  |
                    | Mlp   | 0.602    | 0.610    | 0.614     | 0.599  |

        * **OUTCOME :**
            * Best results were obtained using:
                * Stemmed Features
                * Support Vector Classifier
                

4. **PREDICTION**
    * For prediction Support Vector Classifier was used because it haa the highest f1_score
        * f1_score is best metrics while performing classification tasks because it takes into account both precision and recall.
        * macro averaging was chosen while calculating f1_score so that each class is taken into account individually.

5. **DEPLOYMENT**
    * A Flask Web App was deployed on heroku.
    * [Link to Web App](https://reddit-flair-detector-api.herokuapp.com/)
    * For automated testing send the post request to :
    ```
    https://reddit-flair-detector-api.herokuapp.com/automated_testing
    ```
6. **NOTE :**
   * Results obtained while using a GRU based RNN were not good enough due to dataset Limitations. But these limitations can be overcomed with a Larger dataset because Deep-Learning approaches tends to deliver far better accuracies as compared to normal approaches as the amount of data increases.
