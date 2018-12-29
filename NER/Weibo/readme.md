## readme for Weibo NER dataset
### Task
Named Entity Recognition
### Description
**Tags**: PER(人名), LOC(地点名), GPE(行政区名), ORG(机构名)   

|Label|Tag|Meaning|
|:-:|:-:|:--|
|PER|PER.NAM|名字（张三）|
||PER.NOM|代称、类别名（穷人）|
|LOC|LOC.NAM|特指名称（紫玉山庄）|
||LOC.NOM|泛称（大峡谷、宾馆）|
|GPE|GPE.NAM|行政区的名称（北京）|
|ORG|ORG.NAM|特定机构名称（通惠医院）|
||ORG.NOM|泛指名称、统称（文艺公司）|

**Tag Strategy**：BIO  
**Split**:   
'\t' in raw data (北\tB-LOC)  
'*space*'in transformed data (北 B-LOC)  
**Data Size**:  
Train data set ( [weiboNER.conll.train](weiboNER.conll.train) ):  

|句数|字符数|PER.NAM数|PER.NOM数|LOC.NAM数|LOC.NOM数|GPE.NAM数|ORG.NAM数|ORG.NOM数|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1350|73778|574|766|56|51|205|183|42|

Dev data set ( [weiboNER.conll.dev](weiboNER.conll.dev) ):  

|句数|字符数|PER.NAM数|PER.NOM数|LOC.NAM数|LOC.NOM数|GPE.NAM数|ORG.NAM数|ORG.NOM数|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|270|14509|90|208|6|6|26|47|5|

Test data set ( [weiboNER.conll.test](weiboNER.conll.test) )

|句数|字符数|PER.NAM数|PER.NOM数|LOC.NAM数|LOC.NOM数|GPE.NAM数|ORG.NAM数|ORG.NOM数|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|270|14842|111|170|19|9|47|39|17|

**Note**:  
the raw data contains segmentation information, like:
```
她0	O
和0	O
现0	B-PER.NOM
任1	I-PER.NOM
男0	B-PER.NOM
友1	I-PER.NOM
交0	O
往1	O
时0	O
``` 
the sample conll file should not contain segmentation, like:
```
她 O
和 O
现 B-PER.NOM
任 I-PER.NOM
男 B-PER.NOM
友 I-PER.NOM
交 O
往 O
时 O
``` 
a script was provided to transform the raw data, in which segmentation 
was deleted, '\t' was transformed to '*space*', you can use following 
command.
```bash
python3 transform_data.py
```

**Reference**:   
[Named Entity Recognition for Chinese Social Media
with Jointly Trained Embeddings
](http://aclweb.org/anthology/D15-1064)  
[Improving Named Entity Recognition for Chinese Social Media
with Word Segmentation Representation Learning](http://www.aclweb.org/anthology/P16-2025)  
<https://github.com/hltcoe/golden-horse>  