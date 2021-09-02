# MusicSourceSep
***Bachelor Thesis** - Separación de Fuentes Musicales en Conjuntos de Cámara de Música Clásica*

Music source separation is the task of recovering the audio signals from the isolated music sources that conform a musical mix. Generally, in chamber music pieces, it is common to associate each musical source to each instrument present in the piece.

<!-- ![Repo image](https://github.com/andrezg98/MusicSourceSep/blob/main/Images/source_separation_training.png?raw=true) -->
<img align="center" src="https://github.com/andrezg98/MusicSourceSep/blob/main/Images/source_separation_training.png?raw=true" width="700" height="300">

This repository present the contents developed for my Bachelor Thesis, titled: ***"Separación de Fuentes Musicales en Conjuntos de Cámara de Música Clásica"***.
***
## Repository Structure
This repository is organized in the following folders:
- **_Notebooks_**: Include Python notebooks developed in Google Colaboratory with `.ipynb` format.
- **_Models_**: Contains the trained models for this project with the _Mask Inference_ model implemented by the Nussl library.
- **_Results_**: It contains the tables (in `.csv` format) with the results obtained in all the tests performed for each model.
- **_Images_**: Include the images used in the `README.md` of this repository.
***
## How to obtain the Bach10 Dataset
The Bach10 dataset will contain the audio mixes of each part and the ensemble of ten pieces of four-part J.S. Bach chorales. The audio mixes of the four parts (Soprano, Alto, Tenor and Bass) of each piece are performed by violin, clarinet, saxophone and bassoon, respectively.

To download the dataset for the first time, you can access [here](https://https://docs.google.com/forms/d/e/1FAIpQLSfJ1IdB7Ws2_m0wkkvS1hGm5GevGS3QmqBIoxiGDbw93yoPLQ/viewform?embedded=true&formkey=dGU3cmRlb1Q4RU5zTGNZeHUyRGFwaWc6MQ). The authors ask you to fill in a short form in order to keep track of the use of the dataset. Once downloaded, you can easily unzip and access it as follows. The dataset will be saved in the path you have specified.
```
!unzip bach10_dataset_compressed.zip
```

If you want to use the pre-processed datasets tailored to the input of each model, which have been used during this project, you can access to the public folder [Datasets](https://drive.google.com/drive/folders/1IuS0YSDNNGp7i7t-RdARWlmmaOEOPD9k?usp=sharing) in Google Drive (enabled for this purpose).
***
## Evaluation metrics and results
### Overall results: Comparison of models 
The next table shows the overall results for each different model training configuration for the **violin**.

_Metrics_: mean of the leave-one-out experiments together with their corresponding standard deviations.

|  Model | _Avg+-Std_<br>SI-SAR | _Avg+-Std_<br>SI-SDR | _Avg+-Std_<br>SI-SIR | _Avg+-Std_<br>SNR |
|:-------:|:------------------:|:------------------:|:------------------:|:---------------:|
| _Model A_ |   7.8156 ± 1.5922  |  -3.9426 ± 0.5993  |  -3.6211 ± 0.6726  | 1.0507 ± 0.3363 |
| _Model B_ |   6.526 ± 1.6632   |  -4.1932 ± 0.6887  |  -3.7908 ± 0.6488  | 1.1823 ± 0.2568 |
| _Model C_ |   3.6319 ± 2.3592  |   -3.085 ± 1.1161  |  -1.8411 ± 1.3898  | 1.6863 ± 0.4115 |
| _Model D_ |    2.62 ± 1.3366   |   0.2325 ± 1.3618  |   3.9965 ± 1.5079  | 3.1463 ± 0.6905 |
| _Model E_ |   2.6605 ± 1.2927  |   0.581 ± 1.5047   |   4.9995 ± 2.3326  | 3.3059 ± 0.7757 |
| _Model F_ |  -3.3146 ± 2.0966  |  -4.4473 ± 2.0246  |   2.4107 ± 2.6533  | 1.1831 ± 0.5565 |

From the table above we obtain that the best model that offers the best results for the evaluation metrics is the _Model E_.

Let's see the result offered by the best model for each instrument:

| Target_instrument | _Avg+-Std_<br>SI-SAR | _Avg+-Std_<br>SI-SDR | _Avg+-Std_<br>SI-SIR |  _Avg+-Std_<br>SNR |
|:-----------------:|:------------------:|:------------------:|:------------------:|:----------------:|
|       _violin_      |   2.6605 ± 1.2927  |   0.581 ± 1.5047   |   4.9995 ± 2.3326  |  3.3059 ± 0.7757 |
|      _bassoon_      |  10.2911 ± 1.8588  |  -6.0057 ± 0.5351  |   -5.897 ± 0.5121  | -3.8291 ± 0.1437 |
|      _clarinet_     |   1.8281 ± 1.4409  |  -1.2837 ± 1.6222  |   1.677 ± 1.9212   |  2.3862 ± 0.7532 |
|      _saxphone_     |   4.0214 ± 0.622   |   -2.179 ± 0.7487  |  -0.9612 ± 0.9328  |  1.7026 ± 0.2956 |

### Visualizing estimated separated piece
