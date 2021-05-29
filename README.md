# CompNeuro-VOR

Visual decoding of distributed regions of the human ventral temporal cortex, saliency and attention have been active research topics in the context of computational cognitive neuroscience. We need to construct spatio-temporal decoding algorithms to perform cognitive tasks. In this study, we investigated the functional architecture of the object vision pathway in human brain by functional magnetic resonance imaging (fMRI) methods to decode the visual stimuli viewed by a human subject. We conducted state-of-the-art explanatory echo-planar, region-of-interest (RoI), statistical map, anatomical and glass brain pre-analysis to discovery block-designed 4-D timeseries fMRI dataset, namely Haxby dataset, from the study on face and object representation. To understand geodesic relation in ventral temporal masked fMRI samples, we performed functional connectivity analysis based on the correlation, precision and partial correlation, and similarity analysis based on the cosine, minkowski and euclidean distances. Manifold learning and dimensionality reduction methods are performed on the per-subject ventral temporal masks to extract latent representations of spatio-temporal masks that will help further decoding of fMRIs. End-to-end machine learning algorithms from perceptrons to FREMs are developed to categorize the stimuli based on distributed and overlapping regions in ventral temporal cortex. We further constructed cognitive neural networks, precisely MLPs, 2D and 3D  CNNs and spatially oriented vision transformers by taking the advantage of interactions between different streams of visual representations. Our comprehensive results demonstrate that the ensembling of regularized models achieves the best performance for robust decoding and spatially oriented attention mechanism can enlighten the understanding of attention in human brains.   


## Create Project Directory 
```
mkdir CompNeuro && cd CompNeuro
git clone https://github.com/cankocagil/CompNeuro-VOR.git
cd CompNeuro-VOR
```

## Install Dependencies
```
pip install -r requirements.txt

```

Notebook is ready to run!


Note that the Haxby dataset is automatically fetching from the web, so there is no need to download and add it to the path.

Please refer paper for detailed description. 

