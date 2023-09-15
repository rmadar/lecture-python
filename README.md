# Introduction to Python for Data Analysis

This repository contains the material for a lecture on Python proposed for the [master PFA](https://www.uca.fr/formation/nos-formations/par-ufr-ecoles-et-iut/institut-des-sciences/ecole-universitaire-de-physique-et-dingenierie/master/master-physique-fondamentale-et-applications-5), the [Data Scientist University Diploma (DU)](https://www.uca.fr/formation/nos-formations/catalogue-des-formations/du-data-scientist), and the master [IMAPP](https://imapp.eu/) hosted at Université Clermont-Auvergne (UCA). Basic Python knowledge is not required but would be very valuable. However, it is better to have some basic mathematics knowledge like simple vector operations or statistics.


## General Scope of the Lecture

The main goal of this lecture is to make people familiar with Python and data analysis tools to enable them to extend their knowledge on their own. Practical exercises and small projects are also proposed to provide a few working examples of data manipulations with different levels of complexity.

**What This Lecture Is:** A basic and practical introduction to Python together with some of the most important data analysis tools, namely `numpy`, `matplotlib`, and `pandas`.

**What This Lecture Isn't:** Neither a formal introduction to Python nor an extensive demonstration of all features available in the tools mentioned above.


## Content of the Lecture -- [full PDF](https://github.com/rmadar/lecture-python/raw/master/documentation/PythonIntroductionDU.pdf)

There is a lot of information in this lecture. To help you focus on important aspects, each chapter starts with a list of expected skills that you should take away, ranked with three levels: *basic*, *medium*, *expert*.

**[0. Practical Introduction to Jupyter Notebooks.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/0-IntroductionNotebook.ipynb)** This section is not present in the final PDF but is presented during the lecture.

**[1. Practical Introduction to Python.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/1-PythonIntroduction.ipynb)** This first section is dedicated to basic object types and operations in Python. Functions will also be described, but object-oriented programming will not be covered.

**[2. Introduction to numpy.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/2-NumpyIntroduction.ipynb)** Differences between usual Python objects and numpy objects will be introduced.

**[3. Three tools to know.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/3-ToolsToKnow.ipynb)** This section gives a glimpse of `matplotlib`, `pandas`, and `scipy` packages, allowing powerful data analysis.

**[4. Multidimensional data manipulation.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/4-HighDimensionalData.ipynb)** Non-trivial operations for multidimensional data using the full power of numpy. Most of these operations can be performed with existing tools, but it is instructive to do them once with native numpy.

**[5. Introduction to image processing.](https://nbviewer.jupyter.org/github/rmadar/lecture-python/blob/master/lectures/5-ImageProcessing.ipynb)** Very first steps of image processing (definition, plotting, operation) including basic filter applications (noising, sharpening, border detection).

**Other practical examples:** Depending on the remaining time (and people's preferences), we can go through different topics among the following ones. Some of them can also be used as projects performed by students.
   + Fourier analysis
   + Principal component analysis (PCA)
   + Random Forest regression
   + Gaussian processes

## List of Previous Exams with Corrections

 + 2019: Analysis of an electric pulse ⟶ [exam](exam/2019/Examen.ipynb) / [correction](exam/2019/Examen-corrections.ipynb)
 + 2020: Ising model (more details on this topic [here](https://github.com/rmadar/isingmodel2d)) ⟶ [exam](exam/2020/Exam.ipynb) / [correction](exam/2020/ExamCorrection.ipynb)
 + 2021: Coupled harmonic oscillators (more details on this topic [here](https://github.com/rmadar/vibrating-string)) ⟶ [exam](exam/2021/exam.ipynb) / [correction](exam/2021/examCorrection.ipynb)
 + 2022: Random walk ⟶ [exam](exam/2022/exam.ipynb) / [correction](exam/2022/examCorrection.ipynb)

## How to Get Prepared

**1. Get familiar with Python.** I would recommend two links: [w3school tutorial](https://www.w3schools.com/python/) (both basic and complete) and [https://www.learnpython.org](https://www.learnpython.org) (code can be run directly within your web browser).

**2. Install Python with Anaconda.** In order to run Python on your machine, you should install it. I would recommend [Anaconda](https://www.anaconda.com/) for this, which also includes Jupyter Notebook.

**3. Install Git.** This is a versioning software that can be installed following these [instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). This whole repository can be *cloned* using the `git clone https://github.com/rmadar/lecture-python` command.

**4. Get familiar with notebooks.** This represents a nice environment combining code, notes, and plots. This is very powerful to learn something and play with it. You can check out [this video](https://www.youtube.com/watch?v=CwFq3YDU6_Y) or [this post](https://realpython.com/jupyter-notebook-introduction/).
