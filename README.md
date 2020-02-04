# 2019nCov_Data_Analysis
分析新型冠状病毒感染的肺炎疫情数据

项目大致分为四个部分：

- 数据获取
- 数据可视化
- 数据分析
- 结论

大致技术路线：

- 数据来源主要为[国家疾控中心官网](http://www.chinacdc.cn/)公布的[新型冠状病毒感染的肺炎疫情分布数据](http://2019ncov.chinacdc.cn/2019-nCoV/)，目前数据不够完善，更详细的数据可以搜寻各省发布的公告。

- 从目前公布的数据可以分析包括传播模型、潜伏期、发病率、确诊率、治愈率和死亡率，这些分析不涉及新型冠状病毒的致病机理，但需要考虑疫情发展过程中的主要事件的影响，包括春运、隔离措施、医疗投入等等，主要目标是分析疫情发展的过程，希望能对疫情发展的趋势进行大致的预测。

- 特别注意，需要将湖北与其他地区分别进行分析，湖北疫情较为复杂，数据有可能存在失真，其他地区情况相对简单，数据基本可靠，另外本项目为学习性项目，不具有实际应对疫情的效果~

主要使用的工具：

- [Python](https://www.python.org/)
- 数据获取工具：[requests](https://github.com/psf/requests), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), [PhantomJS](https://phantomjs.org/), [Selenium](https://github.com/baijum/selenium-python), [pyquery](https://github.com/gawel/pyquery), 人工(终极武器)
  
- 数据分析与可视化工具：[NumPy](https://numpy.org/), [SciPy](https://www.scipy.org/), [Matplotlib](https://matplotlib.org/), [Pandas](https://pandas.pydata.org/)