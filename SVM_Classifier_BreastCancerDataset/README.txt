Author: Girish Srinivas
Email: gsrinivas@unomaha.edu
Class: CSCI 8456 Artificial Intelligence.

Author: Siddesh Southekal
Email: siddesh.southekal@unmc.edu
Class: CSCI 8456 Artificial Intelligence.

INSTRUCTIONS
-------------------------------------------------------------------------------------

1. This file specifies the instruction on running the programs on loki.
2. All the source files for the question are in the submission directory
3. To run the programs in this assignment, you need to have python3, numpy, scikit-learn,
    and matplotlib to be installed.
4. Installation Instruction are given in the below section.
5. to run the program, the commad is:
    syntax := python3 <file_name.py>
    (Please Execute the driver file which is mentioned in the below section)
6. For providing the user input to the program, follow the instructions as prompted by
    the program

    To View results:
    ----------------
7. As soon as after running the program, if a graph is generated, please close the graph window
    because, other results will be displayed once a graph window is closed.
    if you dont close the graph window, you cannot see the subsequent results of other classifiers.
    because they are running one after the other.

P.S. 
----
For more information about the results, please refer the project report. Screen shots of
the results are added in the report.

-------------------------------------------------------------------------------------

FILES IN THE SUBMISSION DIRECTORY:
---------------------------------
All the source code is under the directory CSCI-4450-DG-F17-Project/SVM

1. svm_driver.py (Execute this file)
2. TestData1.csv (Test dataset)        
3. TrainingData1.csv (Training dataset)
4. svm_package (Python Package)
   |- __init__.py
   |- cancer_svm.py
   |- DataSet.py


Here, TestData1.csv and TrainingData1.csv are the datafiles for the program where it 
reads the data for training and test the classifiers.
-------------------------------------------------------------------------------------

Installation Instruction:
-------------------------
To install these packages, you need to have pip3 since all these packages are 
installed on python3

1. To install pip3:
    cmd: sudo apt-get install python3-pip
    Reference: https://docs.bigchaindb.com/projects/server/en/latest/appendices/install-latest-pip.html

2. To install scikit-learn:
    cmd: pip3 install -U scikit-learn
    Reference: http://scikit-learn.org/stable/install.html

3. To install matplotlib:
    cmd: python3 -mpip install -U matplotlib
    Reference: https://matplotlib.org/faq/installing_faq.html

4. To install Numpy:
    cmd: sudo pip3 install numpy
    Reference: https://scipy.org/install.html
               https://askubuntu.com/questions/765494/how-to-install-numpy-for-python3

-------------------------------------------------------------------------------------

