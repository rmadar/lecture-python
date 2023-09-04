# Introduction to Python for Data Analysis

This repository contains the material for a lecture of python proposed for the [master PFA](https://www.uca.fr/formation/nos-formations/par-ufr-ecoles-et-iut/institut-des-sciences/ecole-universitaire-de-physique-et-dingenierie/master/master-physique-fondamentale-et-applications-5), for the [Data scientist University Diploma (DU)](https://www.uca.fr/formation/nos-formations/catalogue-des-formations/du-data-scientist), and the master [iMAAP](https://imapp.eu/), hosted at Université Clermont-Auvergne (UCA). Basic python knowledge is not required but would be very valuable. However, it is better to know about some basic mathemtatics like simple vectorial operation or statistics.


## General scope of the lecture

The main goal of this lecture is to make people familiar with python and data analysis tools in order to make them able to extend their knowledge on *themself*. Pratical exercises and small projects are also proposed to provide a few working examples of data manipulations with different level of complexity.

**What this lecture is?** A *basic* and *practical* introduction to python together with some of the most important data analysis tools namely `numpy`, `matplotlib` and `pandas`.

**What this lecture isn't?** Neither a formal introduction to python, nor a extensive demonstration of all features available in the tools mentioned above.


## Content of the lecture -- [full PDF](https://github.com/rmadar/lecture-python/raw/master/documentation/PythonIntroductionDU.pdf)

There are a lot of information in this lecture. In order to help you to focus on important aspect, each chapter start with a list of expected skills that you should take away, ranked with three levels: *basic*, *medium*, *expert*.

**[0. Practical Introduction to Jupyter Notebooks.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/0-IntroductionNotebook.ipynb)** This section is not present in the final PDF but is presented during the lecture.

**[1. Practical Introduction to Python.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/1-PythonIntroduction.ipynb)** This first section is dedicated to basic object type and operation in python. Fonctions will also be described but object oriented programming will not be covered.

**[2. Introduction to numpy.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/2-NumpyIntroduction.ipynb)** Differences between usual python objects and numpy objects will be introduced.

**[3. Three tools to know.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/3-ToolsToKnow.ipynb)** This section gives a glimpse of `matplotlib`, `pandas` and `scipy` packages allowing powerful data analysis.

**[4. Multidimensional data manipulation.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/4-HighDimensionalData.ipynb)** Non-trivial operation for multidimensional data using the full power of numpy. Most of these operation can be performed with existing tools but it is intructive to do it once with native numpy.

**[5. Introduction to image processing.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/5-ImageProcessing.ipynb)** Very first steps of image processing (definition, plotting, operation) including basic filters application (noising, sharpen, border detection).


**Other practical examples.** Depending on the remaining time (and the people taste), we can go through different topics among the following ones. Some of them can be also used as a project performed by students.
   + Fourier analysis
   + Principal component analysis (PCA)
   + Random Forest regression
   + Gaussian processes


## List of previous exams with corrections

 + 2019 : Analysis of an electric pulse --> [exam](exam/2019/Examen.ipynb) / [correction](exam/2019/Examen-corrections.ipynb)
 + 2020 : Ising model (more details on this topic [here](https://github.com/rmadar/isingmodel2d)) --> [exam](exam/2020/Exam.ipynb) / [correction](exam/2020/ExamCorrection.ipynb)
 + 2021 : Coupled harmonic oscillators (more details on this topic [here](https://github.com/rmadar/vibrating-string)) --> [exam](exam/2021/exam.ipynb) / [correction](exam/2021/examCorrection.ipynb)
 + 2022 : Random walk --> [exam](exam/2022/exam.ipynb) / [correction](exam/2022/examCorrection.ipynb)
 

## How to get prepared

**1. Get familiar with python.** I would recommand two links: [w3school tutorial](https://www.w3schools.com/python/) (both basic and complete) and [https://www.learnpython.org](https://www.learnpython.org) (code can be ran directly within your web browser).

**2. Install python with anaconda.** In order to run python on your own machine, you should install it. I would recommand [anaconda](https://www.anaconda.com/) for this, which also includes jupyter-notebook.

**3. Install git.** This is a versioning software which can be installed following these [instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). This whole repository can be *cloned* using `git clone https://github.com/rmadar/lecture-python` command.

**4. Get familiar with notebooks.** This represents a nice environement combining codes, notes and plots. This is very powerful to learn something and play with it. You can checkout [this video](https://www.youtube.com/watch?v=CwFq3YDU6_Y) or [this post](https://realpython.com/jupyter-notebook-introduction/).
