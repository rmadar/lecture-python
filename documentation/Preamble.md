# Preamble {-}


These notes contain the material for a python lecture proposed for the [master PFA](https://www.uca.fr/formation/nos-formations/par-ufr-ecoles-et-iut/institut-des-sciences/ecole-universitaire-de-physique-et-dingenierie/master/master-physique-fondamentale-et-applications-5), for the [Data scientist University Diploma (DU)](https://www.uca.fr/formation/nos-formations/catalogue-des-formations/du-data-scientist), and the master [iMAAP](https://imapp.eu/), hosted at Université Clermont-Auvergne (UCA). Basic python knowledge is not required but would be very valuable. However, it is better to know about some basic mathemtatics like simple vectorial operation or statistics.


[data scientist university degree](https://www.uca.fr/formation/nos-formations/catalogue-des-formations/du-data-scientist-23438.kjsp) proposed at Université Clermont-Auvergne (UCA). No prerequisite knowledge is assumed but being familiar with one progamming language might be useful. It is better to know about some basic mathemtatics like simple vectorial operation or statistics. All the material of this lecture can be found in this [github repository](https://github.com/rmadar/lecture-python).


**This lecture is only a support to help you doing things *yourself*. As any other language, you must practice it if you want to progress. If you don't write and test code on your own, this lecture is close to be useless.** I am available for any questions or general feedback on this lecture, so feel free to contact me: [romain.madar@clermont.in2p3.fr](mailto:romain.madar@clermont.in2p3.fr]). 


## General scope of the lecture {-}

Python offers a rapidly evolving ecosystem to perform data analysis and it is both out of scope and hopeless to be extensive in this lecture. The main goal is therefore to make people familiar with the basic of python and data analysis tools in order to *make them able to extend their knowledge on themself*. Object oriented programming is not presented in this lecture. Pratical exercises are also available to provide few working examples as a starting point.

**What this lecture is?** A *basic* and *practical* introduction to python together with some of the most important data analysis tools namely `numpy`, `matplotlib` and `pandas`.

**What this lecture isn't?** Neither a formal introduction to python, nor a extensive demonstration of all features available in the tools mentioned above.


## Content of the lecture {-}

There are a lot of information in this lecture. In order to help you to focus on important aspect, each chapter start with a list of expected skills that you should take away, ranked with three levels: *basic*, *medium*, *expert*.

**1. Introduction to Python.** This first section is dedicated to basic object type and operation in python. Fonctions will also be described but object oriented programming will not be covered -- *[online notebook](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/1-PythonIntroduction.ipynb)*

**2. Introduction to numpy**. Differences between usual python objects and numpy objects will be introduced -- *[online notebook](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/2-NumpyIntroduction.ipynb)*

**3. Three tools to know.** This section gives a glimpse of `matplotlib`, `pandas` and `scipy` packages allowing powerful data analysis -- *[online notebook](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/3-ToolsToKnow.ipynb)*

**4. Multidimensional data manipulation.** Non-trivial operation for multidimensional data using the full power of numpy. Most of these operation can be performed with existing tools but it is intructive to do it once with native numpy -- *[online notebook](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/4-HighDimensionalData.ipynb)*

**5. Introduction to image processing.** Very first steps of image processing (definition, plotting, operation) including basic filters application (noising, sharpen, border detection) -- [*online notebook*](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/5-ImageProcessing.ipynb)


**Other practical examples.** Depending on the remaining time (and the people taste), we can go through different topics among the following ones. Some of them can be also used as a project performed by students.

   + Fourier analysis
   + Principal component analysis (PCA)
   + Random Forest regression
   + Gaussian processes


## How to get prepared {-}

**1. Get familiar with python.** I would recommand two links: [w3school tutorial](https://www.w3schools.com/python/) (both basic and complete) and [https://www.learnpython.org](https://www.learnpython.org) (code can be ran directly within your web browser).

**2. Install python with anaconda.** In order to run python on your own machine, you should install it. I would recommand [anaconda](https://www.anaconda.com/) for this, which also includes jupyter-notebook.

**3. Install git.** This is a versioning software which can be installed following these [instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). This whole repository can be *cloned* using `git clone https://github.com/rmadar/lecture-python` command.

**4. Get familiar with notebooks.** This represents a nice environement combining codes, notes and plots. This is very powerful to learn something and play with it. You can checkout [this video](https://www.youtube.com/watch?v=CwFq3YDU6_Y) or [this post](https://realpython.com/jupyter-notebook-introduction/).
