# MusicSourceSep
***Bachelor Thesis** - Separación de Fuentes Musicales en Conjuntos de Cámara de Música Clásica*

Music source separation is the task of recovering the audio signals from the isolated music sources that conform a musical mix. Generally, in chamber music pieces, it is common to associate each musical source to each instrument present in the piece.

<!-- ![Repo image](https://github.com/andrezg98/MusicSourceSep/blob/main/Images/source_separation_training.png?raw=true) -->
<p align="center">
  <img src="https://github.com/andrezg98/MusicSourceSep/blob/main/Images/source_separation_training.png?raw=true" width="650" height="280" align="middle">
</p>

This repository present the contents developed for my Bachelor Thesis, titled: ***"Separación de Fuentes Musicales en Conjuntos de Cámara de Música Clásica"***.
***
## Repository Structure
This repository is organized in the following folders:
- **_Notebooks_**: Include Python notebooks developed in Google Colaboratory with `.ipynb` format.
- **_Models_**: Contains the trained models for this project with the Mask Inference model implemented by the Nussl library.
- **_Images_**: Include the images used in the `README.md` of this repository.
***
## How to obtain the Bach10 Dataset
The Bach10 dataset will contain the audio mixes of each part and the ensemble of ten pieces of four-part J.S. Bach chorales. The audio mixes of the four parts (Soprano, Alto, Tenor and Bass) of each piece are performed by violin, clarinet, saxophone and bassoon, respectively.

To download the dataset for the first time, you can access [here](https://https://docs.google.com/forms/d/e/1FAIpQLSfJ1IdB7Ws2_m0wkkvS1hGm5GevGS3QmqBIoxiGDbw93yoPLQ/viewform?embedded=true&formkey=dGU3cmRlb1Q4RU5zTGNZeHUyRGFwaWc6MQ). The authors ask you to fill in a short form in order to keep track of the use of the dataset. Once downloaded, you can easily unzip and access it as follows. The dataset will be saved in the path you have specified.
```
!unzip bach10_dataset_compressed.zip
```
***
## Evaluation metrics and results

### Overall results: Comparison of models 
The next table shows the overall results for each different model training configuration.
Metrics: mean of the leave-one-out experiments together with their corresponding standard deviations.

|      Model     |    SI-SAR    |    SI-SDR    |    SI-SIR    |      SNR     |
|:---------------:|:------------:|:------------:|:------------:|:------------:|
|  Model Aum. A  | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 |
|  Model Aum. B  | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 |
|  Model Aum. C  | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 |
|  Model Aum. D  | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 |
| Model NoAum. D | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 | 3.60 +- 0.03 |

### Visualizing estimated separated piece
