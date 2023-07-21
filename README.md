# Tab Control

This project is meant to make navigating a browser easier and more efficient for people who might have difficulty doing so otherwise. With the correct hardware, the code will gather images from a live video stream and use PyautoGUI to open, close, or move tabs left and right by identifying specific gestures.

## The Algorithm

The original model used a pretrained Resnet18, but then was retrained on a customized data set (more details can be found in train.py). The model was trained on a NVIDIA Jetson Nano. The code depends on video or image input from the user, which would be the hand gestures. Using if statements to check if the prediction value confidence is above a certain number, a function using PyautoGUI will be called to execute unique commands depending on what the gesture was recognized as.

[Close tab hand gesture](https://imgur.com/mOvSEXV)

[Open tab hand gesture](https://imgur.com/OptjM3f)

[Switch left hand gesture](https://imgur.com/NE3tuWy)

[Switch right hand gesture](https://imgur.com/a20PGps)

## Running this project

1. Connect an NVIDIA jetson nano to your computer by SSD connection.
2. Begin to install necessary code to run:
    - Enter this into the terminal and input password.
 
    ```{bash}
    sudo apt-get update
    ```
- Install cmake with 

    ```{bash}
    sudo apt-get install git cmake
    ```
    4. Clone jetson interface project with 
    ```{bash}
    git clone --recursive 
    https://github.com/dusty-nv/jetson-inference
    cd jetson-inference
    git submodule update --init
    ```
    - Install necessary python packages with
    ```
    sudo apt-get install libpython3-dev python3-numpy
    ```

3. Begin to create directories:
    - Type
    ```
    mkdir build
    ```
    - Change directories with
    ```
    cd build
    ```
    - Build the project with
    ```
    cmake ../
    ```
    - IMPORTANT: be sure to install pyTorch along with the installation window
    - Run these commands: 
    ```
    make
    sudo make install
    sudo ldconfig
    ```


4. Open the PuTTY terminal using the nano’s IP address.

5. Get the link to the Jupyter notebook by running this and enter the password.
```{bash}
./docker_dli_run.sh
```

6. Take images of your hand open, in a fist, making a peace sign, and thumb to the side in Jupyter Notebook.

7. Take around 40 samples or more for each gesture and run 15 or more epochs. (The model I have been using has 100% accuracy in training, 71% accuracy in validation with 25 epochs)

8. Create a directory in Visual Studio Code

9. Intstall PyautoGUI (Linux) by inputting:
```{bash}
python3 -m pip install pyautogui
sudo apt-get install scrot
sudo apt-get install python3-tk
sudo apt-get install python3-dev
```

10. Save and export the trained notebook model to VS Code.
    - Download the notebook file to the computer
    - Drag the file into VS Code

11. An alternate way to train the model:
    - Gather images from the data used to train the notebook
    - Make sure you’re in the project folder and have the path to your data set in the Jetson Nano
    - Run the images through VS Code (Python3 train.py)
 
12. Write/import the PyautoGUI code.
    - Making a fist closes a tab (ctrl + w)
    - Open palm creates a tab (ctrl + t)
    - Making a peace sign switches tabs right (ctrl + tab)
    - Sticking thumb sideways switches tabs left (ctrl + shift + tab)
 
13. Connect the Jetson Nano to a separate monitor and log in.
(Pyautogui must be run on the monitor because it needs a display to properly work)

14. Run python3 camera-test.py on the monitor terminal


[Video explanation here](https://youtu.be/jvilUo7HClk)


