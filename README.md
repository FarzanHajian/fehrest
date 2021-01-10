Fehrest
============

Introduction
------------

Fehrest is a static site generator written in Python that creates lists from your local files allowing them to be shared on network.

The application uses Pelican site generator under the hood so having a basic knowledge about Pelican can be helpful.

Getting Started
---------------
- Make sure you you have Python 3.8+ installed.
- Get the source:
    - git remote add origin https://github.com/FarzanHajian/fehrest.git
- Navigate to the source folder and install the package:
    - pip install -e .
- Create a brand new site using the following command:
    - fehrest --init --name [my site name] --ouptput [output path]
- The result of the above command is a Pelican regular empty site (with a couple of modifications) which is created by pelican-quickstart command.
- Navigate to [output path]/content/files. Here is the place where you must put your files. Create some subfolders (each subfolder matches one list) and copy your files inside them.
- Use the following command to publish your site:
    - fehrest --publish [output path]

- When successful, Fehrest create the folder [output path]/output. Deploy this folder on your web server of choice and enjoy.
- If  you want to preview your result before final deployment, you can use Pelican internal web server.
    - cd [output path]
    - pelican --listen