# Chinese-NLP-Corpus
Collections of Chinese NLP corpus

## Open Domain
Corpus for open domain, including: law, social media, comments
### Word Segmentation and Part-of-Speech
|Name|Description|Link|
|:-:|---|:-:|
|ZhuXian(诛仙)|小说《诛仙》的POS和分词标注数据|[zhuxian](https://github.com/hankcs/OpenCorpus/tree/master/zhuxian)|
|CNLC|国家语言委员会的数据，train: dev: test=8: 1: 1|[CNLC](https://github.com/hankcs/OpenCorpus/tree/master/cncorpus)|

\* the url in the table is out-of-date, you can find the data from the following reference.  
**Reference**:<https://github.com/hankcs/multi-criteria-cws/tree/master/data>  
the details of the corpus  
![](https://camo.githubusercontent.com/8dfcf9fb2ea026c1e178ec9f70efea038fa4ca20/687474703a2f2f7778332e73696e61696d672e636e2f6c617267652f303036466d6a6d636c7931666d366a74686133746d6a33313872306c343078392e6a7067)


### Named Entity Recognition (NER)
|Name|Description|Link|
|:-:|:-:|:-:|
|MSRA|中文NER任务最常用数据之一|[MSRA](NER/MSRA)|
|People's Daily|中文NER任务最常用数据之二|[People's Daily](NER/People%27s%20Daily)|
|Weibo Data|中文NER任务最常用数据之三|[Weibo](NER/Weibo)|

### Text Classification
|Name|Description|Link|notes|
|:-:|---|:-:|---|
|CAIL2018|2018中国‘法研杯’法律智能挑战赛（任务：罪名预测、法条推荐、刑期预测）的数据，数据集共包括**268万**刑法法律文书，共涉及**183条**罪名，**202条**法条，刑期长短包括0-25年、无期、死刑。|[CAIL2018](https://cail.oss-cn-qingdao.aliyuncs.com/CAIL2018_ALL_DATA.zip)|[比赛官网](http://cail.cipsc.org.cn/), [github](https://github.com/thunlp/CAIL2018)|
|CSL - Classification|[中文科学文献数据集(CSL)](https://github.com/P01son6415/CSL)中，选取自然科学相关学报的论文摘要根据[国家自然科学基金](http://www.nsfc.gov.cn/nsfc/cen/xmzn/2019xmzn/15/index.html)进行学科分类。|[CSL - Classification](https://github.com/P01son6415/CSL#3学科分类)||

### Sentiment Analysis and Rating
|Name|Description|Link|notes|
|:-:|---|:-:|---|
| ChnSentiCorp_htl_all | **7000**多条酒店评论数据，**5000**多条正面评论，**2000**多条负面评论 | [ChnSentiCorp_htl_all](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/ChnSentiCorp_htl_all) |
| waimai_10k | 某外卖平台收集的用户评价，正面**4000**条，负面约**8000**条 | [waimai_10k](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/waimai_10k) |
| online_shopping_10_cats | **10**个类别（书籍、平板、手机、水果、洗发水、热水器、蒙牛、衣服、计算机、酒店），共**6万**多条评论数据，正、负面评论各约**3万**条 | [online_shopping_10_cats](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/online_shopping_10_cats) |
| weibo_senti_100k | **10万**多条，带情感标注的新浪微博，正负面评论约**各5万**条 | [weibo_senti_100k](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/weibo_senti_100k) |参考[页面](https://github.com/SophonPlus/ChineseNlpCorpus/issues/1)，这个数据集里包含大量emoji，效果可能与emoji相关，训练之前最好去除emoji|
| simplifyweibo_4_moods | **36万**多条，带情感标注的新浪微博，包含**4**种情感，其中喜悦约**20万**条，愤怒、厌恶、低落**各约5万**条 | [simplifyweibo_4_moods](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/simplifyweibo_4_moods) |
| dmsc_v2 | **28**部电影，超**70万**用户，超 **200万**条评分/评论数据 | [dmsc_v2](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/dmsc_v2) |
| yf_dianping | **24万**家餐馆，**54万**用户，**440万**条评论/评分数据 | [yf_dianping](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/yf_dianping) |
| yf_amazon | **52万**件商品，**1100**多个类目，**142万**用户，**720万**条评论/评分数据 | [yf_amazon](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/yf_amazon) |
| ez_douban | **5万**多部电影（**3万**多有电影名称，**2万**多没有电影名称），**2.8万**用户，**280万**条评分数据 | [ez_douban](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/ez_douban) |

### Other Github Repo
|Description|Link|notes|
|:-:|:-:|---|
|Chinese NLP Corpus|<https://github.com/SophonPlus/ChineseNlpCorpus>||
|awesome-chinese-nlp/Corpus 中文语料|https://github.com/crownpku/Awesome-Chinese-NLP#corpus-中文语料||
|Large Scale Chinese Corpus for NLP|https://github.com/brightmart/nlp_chinese_corpus||
|中文自然语言处理数据集|https://github.com/InsaneLife/ChineseNLPCorpus||
|funNLP|<https://github.com/fighting41love/funNLP>||


## Medical Domain
collect corpus for Chinese medical domain, including medical terminology, QA, clinical NER

### Word Segmentation
|Name|Description|Link|notes|
|:-:|---|:-:|---|
|AMTTL|医学语言的分词数据集，来源应该是医学论坛，所以数据还是偏向open，与医学文本中的语言描述有差异。|[AMTTL](https://github.com/adapt-sjtu/AMTTL/tree/master/medical_data)|[Adaptive Multi-Task Transfer Learning for Chinese Word Segmentation in Medical Text](http://aclweb.org/anthology/C18-1307)|

### Clinical NER
|Name|Description|Link|notes|
|:-:|---|:-:|---|
|CNMER|中文医学实体识别数据集，实体包括身体部位、症状体征、检查、疾病以及治疗。|[CNMER](https://github.com/yhzbit/CNMER/tree/master/data)|应该是CCKS2017的数据。|
|CNMER|识别疾病和诊断、解剖部位、影像检查、实验室检验、手术和药物6种命名实体|[CCKS2018数据](https://github.com/MenglinLu/Chinese-clinical-NER/tree/master/data)||
|CNMER|识别中文医学命名实体|[CCKS2019数据](http://openkg.cn/dataset/yidu-s4k)|来自[OpenKG](http://openkg.cn)的分享|

### Question Answer (QA)
|Name|Description|Link|notes|
|:-:|---|:-:|---|
|cMedQA|医学在线论坛的数据，包含**5.4万**个问题，及对应的**约10万**个回答。|[cMedQA](https://github.com/zhangsheng93/cMedQA)|[Chinese Medical Question Answer Matching Using End-to-End Character-Level Multi-Scale CNNs](https://www.mdpi.com/2076-3417/7/8/767)|
|cMedQA2|cMedQA的扩展版，包含**约10万**个医学相关问题，及对应的**约20万**个回答。|[cMedQA2](https://github.com/zhangsheng93/cMedQA2)|[Multi-Scale Attentive Interaction Networks for Chinese Medical Question Answer Selection](https://ieeexplore.ieee.org/abstract/document/8548603)|
|webMedQA|又一个医学在线问答数据集，包含**6万**个问题和**31万**个回答，而且包含问题的类别。|[webMedQA](https://github.com/hejunqing/webMedQA)|[Applying deep matching networks to Chinese medical question answering: A study and a dataset](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-019-0761-8)|

### Others
|Name|Description|Link|notes|
|:-:|---|:-:|---|
|medical-books|Open sourece medical books in LaTeX|[medical-books](https://github.com/scienceasdf/medical-books)|       |
| awesome_Chinese_medical_NLP | 中文医学NLP公开资源整理|[awesome_Chinese_medical_NLP](https://github.com/GanjinZero/awesome_Chinese_medical_NLP) |       |
|Chinese_medical_NLP|医疗NLP领域（主要关注中文）评测数据集与论文等相关资源。|[Chinese_medical_NLP](https://github.com/lrs1353281004/Chinese_medical_NLP) |       |

