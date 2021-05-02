# CompNeuro-VOS


This repo is placeholder for upcoming Computational Neuroscience project of Bilkent University in 2020-2021.




## Create Project Directory 
```
mkdir CompNeuro && cd CompNeuro
git clone https://github.com/cankocagil/CompNeuro-VOS.git
cd CompNeuro-VOS
```

## Install Dependencies
```
pip install -r requirements.txt

```

Notebook is ready to run!


Note that the Haxby dataset is automatically fetching from the web, so there is no need to download and add it to the path.

(For Colloborater)
##  Push to Remote CompNeuro-VOS
```
git init
git add -all
git commit -m "added ML algo"
git branch -M main
git remote add origin https://github.com/cankocagil/CompNeuro-VOS.git
git push -u origin main
```


### 


Filename : CompNeuro_2021-2022_Final_Project.ipynb

Authors : Arman Vural Budunoğlu and Can Kocagil

Institution : Bilkent University Departmant of Electric & Electronical Enginering

Class : EEE482/582 - Computational Neuroscience

Project Goal : Implement multi-voxel pattern analyses methods (based on some type of classifier) to decode the category of visual stimuli viewed by a human subject based on their recorded brain activity

Dataset Link : https://openfmri.org/dataset/ds000105.

Related Papers : Distributed and overlapping representations of faces and objects in ventral temporal cortex

Abstract:

The functional architecture of the object vision pathway in the human brain was
investigated using functional magnetic resonance imaging to measure patterns
of response in ventral temporal cortex while subjects viewed faces, cats, Þve
categories of man-made objects, and nonsense pictures. A distinct pattern of
response was found for each stimulus category. The distinctiveness of the
response to a given category was not due simply to the regions that responded
maximally to that category, because the category being viewed also could be
identiÞed on the basis of the pattern of response when those regions were
excluded from the analysis. Patterns of response that discriminated among all
categories were found even within cortical regions that responded maximally
to only one category. These results indicate that the representations of faces
and objects in ventral temporal cortex are widely distributed and overlapping.

Pipeline:

1) Necessary Installations (If necessary)
2) Imports
3) Visual Stimuli and Category Loading
4) Visual Stimuli Transformations
5) Explanatory Visual Stimuli Analysis

    * PCA
    * T-Stochastic Neighboor Embedding (t-SNE)
    * Linear Discriminate Analysis
    * Uniform Manifold Approximation and Projection (UMAP)
    * Independent Component Analysis (ICA)
    * Non-Negative Matrix Factorization
    * Masking

6) Visual Stimuli Similarity Analysis

    * Euclidean Similarity
    * Cosine Similarity
    * Pearson Correlation             

7) Classical ML Algorithms:

    * LinearSVC
    * SGDClassifier
    * MLPClassifier
    * Perceptron
    * LogisticRegression
    * LogisticRegressionCV
    * SVC
    * CalibratedClassifierCV
    * PassiveAggressiveClassifier
    * LabelPropagation
    * LabelSpreading
    * RandomForestClassifier
    * GradientBoostingClassifier
    * QuadraticDiscriminantAnalysis
    * RidgeClassifierCV
    * RidgeClassifier
    * AdaBoostClassifier
    * ExtraTreesClassifier
    * KNeighborsClassifier
    * BaggingClassifier
    * BernoulliNB
    * LinearDiscriminantAnalysis
    * GaussianNB
    * NuSVC
    * DecisionTreeClassifier
    * NearestCentroid
    * ExtraTreeClassifier
    * CheckingClassifier
    * DummyClassifier

7) Reported Metrics
    * Accuracy
    * Balanced Accuracy
    * ROC AUC
    * F1-Score
    * Time Taken

8) Deep Learning Algorithms
    * 3-D Convolutional Neural Networks
    * Visual Transformers
    * ...

9) Results Interpretation
