## readme for MSRA dataset
### Task
Named Entity Recognition
### Description
**Tags**: LOC(地名), ORG(机构名), PER(人名)   
**Tag Strategy**：BIO  
**Split**: '\t' (北\tB-LOC)  
**Data Size**:  
Train data set ( [msra_train_bio.txt](msra_train_bio.txt) ):  

|句数|字符数|LOC数|ORG数|PER数|
|:-:|:-:|:-:|:-:|:-:|
|45000|2171573|36860|20584|17615|

Test data set ( [msra_test_bio.txt](msra_test_bio.txt) )

|句数|字符数|LOC数|ORG数|PER数|
|:-:|:-:|:-:|:-:|:-:|
|3442|172601|2886|1331|1973|

**Reference**:   
[The third international Chinese
language processing bakeoff: Word segmentation
and named entity recognition](https://faculty.washington.edu/levow/papers/sighan06.pdf)   
<https://github.com/dox1994/nlp_datasets>