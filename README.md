<h1 align= "center"> PONG! </h1>

## Description:
  In the following repository, will be done the refactoring and debugging the PONG project, authored by  Jucimar Silva Jr.
In addition there will be the insertion of new features to improve gameplay in general.

Next, the link to the original repository will available [clicking right here](https://github.com/jucimarjr/lpc_2021-2.git.).

## Table of Contents
<!--ts-->
   * [Description](#Description)
   * [Table of Contents](#table-of-Contents);
   * [Changes](#Changes);
   * [How to play](#How-to-play);
   * [Recomendation](#Recommendation-for-Windows-users);
   * [Observations](#Observations);
   * [Developers](#Developers);
<!--te-->

## Changes:
Compared to the original, the following code has some differentials:
<!--ts-->
  - ✅ Corretion of the paddle bug;
  - ✅ Paddle inprovement;
  - ✅ Developing a game speed;
  - ✅ Inserting a winning condition; 
  - ✅ Optimization and formatting the code to PEP-8.
<!--te-->

## How to play:
  |Player 1|Player 2|Movement|
  |:---:|:---:|:---:|
  |"w"|Up|⬆️|
  |"s"|Down|⬇️|
  
## Recommendation for Windows users:
The game is to be played in co-op, but if you are without someone to play with, don't worry, the **Parsec** app will solve this problem. Parsec is a tool that allows you to use a friend's desktop from your own computer, opening up the possibility of online multiplayer.

### **Parsec tutorial**:
  - **Passo 1:** Install the parsec application [clicking right here](https://parsec.app/downloads), choose the per user installation type;
  - **Passo 2:** Create an account in the parsec;
  - **Passo 3:** In the application, add your friends to gain access to their desktops, when they open it;
  - **Passo 4:** In Computers, press share and will be disponibilize one link, which one you can share with your friends for they gain access to your Desktop for the time you maintain parsec open.
  - **Passo 5:** Now open the game, and play with your friends!

## Observations:
The game was developed to meet the three main operating systems (Linux, Mac, Windows). If your O.S. is Linux or Mac you will need to make minor changes to the code for the game's audio.

### For Linux:
  - **Step 1:** Open the mypong.py file in an editor, go to line 2 of the file, you will find the following command:
    ```python 3.9
      # import os
    ```
    You must remove the character '#' and the space before the word import.
    
  - **Step 2:** Now go to line 3 where the following code is:
     ```python 3.9
      # from winsound import PlaySound, SND_ASYNC
    ```
    You must add the character '#' at the beginning of that line followed by a single space.
    
  - **Step 3:** After that, go to line 11, where you will find the following section:
    ```python 3.9
     # os.system("aplay bounce.wav&")  # On Linux
    ```
     You must again remove the '#' character and the space.
     
  - **Step 4:** Now on line 12 you will find:
    ```python 3.9
     PlaySound("bounce.wav", SND_ASYNC)  # On Windows
    ```
     You must now add the character '#' at the beginning of the line followed by a space.
     
  - **Step 5:** In lines 16 and 20 you will find something very similar to the content of the line in step 3, and you will repeat the same steps from step 2 in both lines of code.
  
  - **Step 6:** On lines 17 and 21 you will find something very similar to the content of the line in step 4, and you will repeat the same steps from step 3 in both lines of code.
  
  - **Step 7:** Save your changes and you are ready to run the game.

### For Mac:
  - **Step 1:** The steps here are identical to steps 1 and 2 of the configuration for Linux.
  
  - **Step 2:** After that, go to line 10, where you will find the following section:
    ```python 3.9
      # os.system("afplay bounce.wav&")  # On MAC
    ```
     You must again remove the '#' character and the space.
     
  - **Step 3:** Now on line 12 you will find:
    ```python 3.9
      PlaySound("bounce.wav", SND_ASYNC)  # On Windows
    ```
     You must now add the character '#' at the beginning of the line followed by a space.
     
  - **Step 4:** In lines 15 and 19 you will find something very similar to the content of the line in step 2, and you will repeat the same steps from step 2 in both lines of code.
  
  - **Step 5:** On lines 17 and 21 you will find something very similar to the content of the line from step 3, and you will repeat the same steps from step 3 on both lines of code.
  
  - **Step 6:** Save your changes and you are ready to run the game.

## Developers:
- Roberto Antonio  Goncalves Da Silva Filho | [github](https://github.com/robertoantony32)
- Roberto Junio Rodrigues Gomes | [github](https://github.com/Robjunio)
- Valdenei Lopes Da Silva Junior | [github](https://github.com/valdeneijunior)
