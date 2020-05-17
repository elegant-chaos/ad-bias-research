google-ad-bias-research
==============================

Research into the effect of imbalanced classes in modeling data on Google Ad placement. Initially a group project* for CS 520 at UMass-Amherst; extended by Jenn Halbleib into a Master's research project. 

Project Organization
------------
```console

├── LICENSE
├── Makefile
├── README.md
├── background_research_and_meeting_notes
│   ├── 11-7.txt
│   ├── A_Guide_to_MTurk.pdf
│   ├── Screen\ Shot\ 2019-10-09\ at\ 5.30.27\ PM.png
│   ├── for_pooya_prevent_workers_from_doing_hit_twice.txt
│   ├── nov_11.txt
│   ├── nov_18.txt
│   ├── nov_5.txt
│   └── oct_28.txt
├── data
│   ├── external
│   ├── interim
│   ├── processed
│   └── raw
├── docs
│   ├── Makefile
│   ├── commands.rst
│   ├── conf.py
│   ├── getting-started.rst
│   ├── index.rst
│   └── make.bat
├── models
├── mturk
│   └── python
│       ├── MTurk.ipynb
│       ├── adDetail.csv
│       ├── ad_filelist.csv
│       ├── survey.html
│       └── survey_groups.csv
├── notebooks
│   └── cleaning_ad_pages_file.Rmd
├── references
├── reports
│   └── figures
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   └── make_dataset.py
│   ├── features
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── predict_model.py
│   │   └── train_model.py
│   └── visualization
│       ├── __init__.py
│       └── visualize.py
├── test_environment.py
└── tox.ini

```
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

\* Original Group Members: Jenn Halbleib, Paige Calisi, Matthew Malone, Dongxun Sun, Pooya Khaloo 
