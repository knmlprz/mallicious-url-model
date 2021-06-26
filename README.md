<p align="center">
  <img src="./Poster/README-version-100dpi.png" alt="Suspicious URL detection">
</p>

# Hackathon: Suspicious URL detection

*By RTFD team*

The phenomenon of phishing has been around for many years. However, the last year has shown how important internet security is among other things. Over a year ago, the world stopped: everybody and everything was moved to the Internet. That motivated us to analyse the topic of Phishing. Phishers usually use email or SMS messages to deceive and force users to act according to their expectations. In our research we tried to implement some machine learning analysis of the URL in order to prevent the deception.

## Setting up the environment

First of all you need to clone or download this repository.

### What is a `conda` environment and why is it the easiest choice?

Conda environments allow multiple incompatible versions of the same package to coexist on your system. An environment is simply a file path containing a collection of mutually compatible packages. 

There are a large number of reasons why it is best practice to use environments, but two of them we believe to be the most important in this project are:
 - an ability to both install and uninstall all the necessary libraries with one command;
 - a certainty that all packages are going to be installed correctly with least effort.

You can download Miniconda from Anaconda's [official documentation](https://docs.conda.io/en/latest/miniconda.html). If you prefer installing all the necessary packages manually than please jump to the following section: <a href="#using-pip"><em>Using `pip`</em></a>.

### Using `conda`:

Assuming this Git repository is already cloned to your local machine and Miniconda is installed the next task you would probably like to accomplish is to create a separate Conda-environment specially for this project. To do so please use the following commands inside the project's directory:
```bash
conda env create --file env.yml
```
You may like to change the default environment name `Hackathon2021` or path to environment location using `--name ENVIRONMENT` and `--prefix PATH` flags respectively. 

If everything goes according to plan a question similar to the one shown below should appear. When conda asks you to proceed, type `y`:
```bash
The following NEW packages will be INSTALLED:

  anyio              conda-forge/win-64::anyio-3.1.0-py39hcbf5309_0
  argon2-cffi        conda-forge/win-64::argon2-cffi-20.1.0-py39hb82d6ee_2
  async_generator    conda-forge/noarch::async_generator-1.10-py_0
  attrs              conda-forge/noarch::attrs-21.2.0-pyhd8ed1ab_0
  babel              conda-forge/noarch::babel-2.9.1-pyh44b312d_0
  ...

Proceed ([y]/n)?
```

If the environment has been installed correctly than the similar message should appear in your console:
```bash
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate Hackathon2021
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```
Note: the environment name (*in our case it is "Hackathon2021"*) may differ if you changed the `--name` flag in 
the previous command. 

To activate your environment:
```bash
conda activate Hackathon2021
```

If everything seems to work as expected than you can jump to the following section: <a href="#opening-jupyterlab-notebook-interface"><em>Opening JupyterLab Notebook Interface</em></a>.

### Using `pip`:

If you anyway prefer installing modules using `pip` than the following command has to be used:
```bash
pip install pandas, numpy, matplotlib, flask, sklearn, urllib3, nltk, seaborn, Pillow, joblib, jupyterlab
```

### Opening JupyterLab Notebook Interface

To open `JupyterLab` Notebook Interface use one of the following commands:
```bash
jupyter-lab
```
or 
```bash
python -m jupyterlab
```

If there were no problems with installing or running the stuff, you are ready to go. You can start from opening the file `Notebooks/Second_model.ipynb`, where we have covered the basics of our analysis. 


## References

### Data sets:
 - [CERT Polska : Lista ostrzeżeń przed niebezpiecznymi stronami](https://hole.cert.pl/schema/certpl_lista_ostrzezen_api_v1.pdf)

### Used articles: 
- [*Malicious URL Filtering – A Big Data Application*](https://www.semanticscholar.org/paper/Malicious-URL-filtering-%E2%80%94-A-big-data-application-Lin-Chiu/c46092506e36d8d5e4bea3c7bf507b2bb3c079d1#paper-header)
- [*Phishing detection based Associative Classification data mining*](https://www.sciencedirect.com/science/article/abs/pii/S0957417414001481?via%3Dihub)

### Documentations and code examples:
- [StackOverflow](https://stackoverflow.com/)
- [R & Python Graph Gallery](https://www.r-graph-gallery.com/about.html)

### Icons and poster: 
- Inspiration - [r-lab-project](https://github.com/FrightenedFox/r-lab-project)
- [Free SVG](https://freesvg.org/)
- [Pixel perfect](https://www.flaticon.com/authors/pixel-perfect), [Freepik](https://www.freepik.com), [Becris](https://creativemarket.com/Becris), [bqlqn](https://www.flaticon.com/authors/bqlqn)  from [Flaticon](https://www.flaticon.com/)