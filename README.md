[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7956984&assignment_repo_type=AssignmentRepo)
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Depen-Tool</h3>

  <p align="center">
    A CLI Tool to check & update dependency versions in Github Repositories
    <br />
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-psai11"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-psai11">View Demo</a>
    ·
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-psai11/issues">Report Bug</a>
    ·
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-psai11/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
<!--     <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This is a CLI tool for updating dependencies of Github Repositories.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

<!-- * [Next.js](https://nextjs.org/) -->
<!-- * [React.js](https://reactjs.org/) -->
<!-- * [Vue.js](https://vuejs.org/) -->
<!-- * [Angular](https://angular.io/) -->
<!-- * [Svelte](https://svelte.dev/)
* [Laravel](https://laravel.com)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com) -->
* [Python](https://www.python.org/)
* [Node.JS](https://nodejs.org/en/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is how you may setup this project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
The following are some necessary python libraries to be installed.
* python
  ```sh
  pip install PyGithub
  ```
  ```sh
  pip install pandas
  ```
  ```sh
  pip install argparse
  ```
  ```sh
  pip install json
  ```
 * _MAKE SURE THE GITHUB ACCOUNT THAT CONTAINS REPOSITORIES ON WHICH YOU WANT RUN THIS TOOL, IS `ALREADY LOGED INTO YOUR TERMINAL`_
 * _MAKE SURE YOU CARRY THE `GITHUB ACCESS CODE` TO THE ABOVE MENTIONED GITHUB ACCOUNT_
  

### Installation

1. Get a Github Access Key at [Github Access Tokens](https://github.com/settings/tokens)
2. Create a Folder with any random name
3. Open Terminal in the above mentioned Folder (For easy navigation through output files, that will be genarated later)
4. Clone the repo
   ```sh
   git clone https://github.com/dyte-submissions/dyte-vit-2022-psai11.git
   ```
5. Install NPM packages
   ```sh
   npm install
   ```
<!-- 4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
 -->
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Here is a detailed Walkthrough of how one may use this tool.<br>
* Open the folder that contains your `SDKtool.exe`.
* Run terminal in this folder.
* Create a `.csv` file containing github repository links in the following manner. Let it be named `input.csv`.
![image](https://user-images.githubusercontent.com/61933732/171466662-cd9f33b2-ffcc-412f-9530-18c461f024b6.png)
* Save the `input.csv` file in the same folder where `SDKtool.exe` exists
![image](https://user-images.githubusercontent.com/61933732/171467074-0bf290c9-9206-49e3-90cd-d5963ca321ae.png)
* To check dependencies of github repositories mentioned in `input.csv` with respect to `QueryDependency@RequiredVersion`(for example `axios@0.23.0`) run the following command:
  ```sh
  SDKtool.exe input.csv axios@0.23.0
  ```
  _OR_
  ```sh
  SDKtool.exe input.csv QueryDependency@RequiredVersion
  ```
* Running the above command will provide a new `output.csv`
![image](https://user-images.githubusercontent.com/61933732/171467595-fcf9c294-65db-430a-b41a-ba6ad6481915.png)
* To update the dependencies of github repositories which where less than `RequiredVersion` run the following command:
  ```sh
  SDKtool.exe input.csv axios@0.23.0 --update
  ```
  _OR_
  ```sh
  SDKtool.exe input.csv QueryDependency@RequiredVersion --update
  ```
* Running the above command will update the dependencies and send a Pull Request to the github repository, create an output file named `PROutput.csv`
![image](https://user-images.githubusercontent.com/61933732/171468974-f4c66cae-8d37-4ad8-ad53-18434282eed4.png)

* PR is created in the link given in `PROutput.csv`
![image](https://user-images.githubusercontent.com/61933732/171470644-2b2bc7ba-ca74-42b1-9907-1ae6f59cfccf.png)

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Check dependency valid or not
- [x] Check dependency version valid or not
- [x] Check deprecation of dependencies
- [x] Clone repositories from CSV file
- [x] Check version satisfiability in each repository
- [x] Create Output File with version & version satisfiability 
- [x] Update version of un satisfied dependencies
- [x] Create new Output File with PR links 

See the [open issues](https://github.com/dyte-submissions/dyte-vit-2022-psai11/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@SaiChai91235079](https://twitter.com/SaiChai91235079) - saichaita@gamil.com

Project Link: [https://github.com/dyte-submissions/dyte-vit-2022-psai11](https://github.com/dyte-submissions/dyte-vit-2022-psai11)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments -->

<!-- * []() -->
<!-- * []() -->
<!-- * []() -->

<!-- <p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
