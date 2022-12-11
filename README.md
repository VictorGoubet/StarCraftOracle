[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]

<a name="readme-top"></a>
<br />
<div align="center">
  <a href="https://github.com/VictorGoubet/StarCraftOracle">
    <img src="https://cdn2.steamgriddb.com/file/sgdb-cdn/logo_thumb/4ccea3161064506dda8e0c9fd416d1ae.png" alt="Logo" width="90" height="80">
  </a>

  <h3 align="center">StarCraft Oracle</h3>

  <p align="center">
    <i>Are you really a GrandMaster ?</i>
    <br />
    <a href="https://github.com/VictorGoubet/StarCraftOracle/blob/master/Notebook.ipynb"><strong>Check the code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/VictorGoubet/StarCraftOracle/issues">Report Bug</a>
    •
    <a href="https://github.com/VictorGoubet/StarCraftOracle/issues">Request Feature</a>
  </p>
</div>


## About The Project
</br>

StarCraft is a famous RTS game where you are part of a faction and must defeat opponents by overpowering them, usually by destroying all of their buildings. Some single-player missions and custom maps feature different objectives. When you are a StarCraft II player, you are ranked among 8 classes: 

- Bronze
- Silver
- Gold
- Platinum
- Diamond
- Master
- GrandMaster
- Professional leagues

To go into an higher league, you have to improve yourself on a lot of multiple factors. The question is, could we use different statistic on the player games behaviors and skills to predict its league. It could allow to discover shadow potential amoung young players, or event to know which skills you should improve to be better at this game and maybe be part of the Professional leagues one day. 

[![Product Name Screen Shot][product-screenshot]](screenshot.PNG)

Will the AI see through you ? Let's see!

<p align="right"><a href="#readme-top">🔝</a></p>


## Implementation

SkillCraft is a dataset composed of a lot of features of over three thousand players playing at StarCraft II from bronze to professional gamers. In our study we will try to predict the league index of a player considering all his others features. Thus, it is a **classification problem.**

In our notebook we have followed the next steps:
- Data exploration 
- Data engeneering
- Modeling
- Optimisation (Tunning)
- Conclusion

We obtain finally a score of **0.45** due to a significant lack of data especially for the level 8 players.
A flask API is available to make predictions on your datas if you want.

To request a prediction from our API the input must be composed of all the columns (minus the leagueIndex) and no missing data with the appropriate datatype (float or int depending on the column). Finally, it must be a dictionnary.  


<p align="right"><a href="#readme-top">🔝</a></p>

## Getting Started


### Prerequisites

You will just need python >= 3.0 ( and < 3.11 if you want to use shap values). You can check the version by using the following command.

  ```sh
  > python -V
  > 3.0.0
  ```

### Installation

You can follow the different steps inorder to get the program working on your computer


1. Clone the repo

   ```sh
   git clone https://github.com/VictorGoubet/StarCraftOracle.git
   ```

2. Install python packages

   ```sh
   pip install -r requirements.txt
   ```

3. Open the notebook inn VS code or using jupyter with the following command

   ```sh
   jupyter notebook
   ```

You can explore the notebook and see the different steps to build the model.

Then, inorder to test the API and start to make some predictions you can
execute the following steps:

1. Starting the server

    ```sh
      python API/server.py
    ```

2. Go to **localhost:5000/API_form** in a browser

3. Try it yourself! 


You can also check the *dev_request_example.py* file to see how to make some prediction using the REST api from code application.


<p align="right"><a href="#readme-top">🔝</a></p>





<!-- CONTACT -->
-----
</br>

[![LinkedIn][linkedin-shield]][linkedin-url]
</br>
Victor Goubet - victorgoubet@orange.fr  


<!-- MARKDOWN LINKS & IMAGES -->
[forks-shield]: https://img.shields.io/github/forks/VictorGoubet/StarCraftOracle.svg?style=for-the-badge
[forks-url]: https://github.com/VictorGoubet/StarCraftOracle/network/members
[stars-shield]: https://img.shields.io/github/stars/VictorGoubet/StarCraftOracle.svg?style=for-the-badge
[stars-url]: https://img.shields.io/github/issues/VictorGoubet/StarCraftOracle/stargazers
[issues-shield]: https://img.shields.io/github/issues/VictorGoubet/StarCraftOracle.svg?style=for-the-badge
[issues-url]: https://github.com/VictorGoubet/StarCraftOracle/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/victorgoubet/
[product-screenshot]: screenshot.PNG
[minmax-screenshot]: MinMax.jpg
