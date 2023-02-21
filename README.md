<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
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



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/bitfl0wer/altminder">
    <img src="images/altminder.jpg" alt="Logo" width="80" height="80" alt="altminder Logo. Dark grey background that displays a red heart with a light-blue eye icon overlayed on top.">
  </a>

<h3 align="center">altminder</h3>

  <p align="center">
    A project that aims to make Discord a tiny bit more accessible for vision impaired users by reminding people to add image descriptions (alt texts) to their images.
    <br />
    <a href="https://discord.com/api/oauth2/authorize?client_id=1003622371191705630&permissions=274877975552&scope=bot%20applications.commands">Invite to Server</a>
    ·
    <a href="https://github.com/bitfl0wer/altminder/issues">Report Bug</a>
    ·
    <a href="https://github.com/bitfl0wer/altminder/issues">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

altminder aims to improve the Discord experience for blind and low vision users by
sending a friendly reminder to include an image description (alt text) to images posted in Discord
chats. These reminders are public, but get deleted automatically (after 30s). Image descriptions
are absolutely crucial for low vision users, since they are often the only way for vision
impaired people to know what an image displays, or, for example, what the text on an an image says.
Not including image descriptions with posted images therefore excludes low vision users from fully
participating in the community (the Discord server).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Python
* [py-cord 2.1.1](https://github.com/Pycord-Development/pycord)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Install Python 3.9 (3.8+ should be fine, but I can only *verify* that it works on Python 3.9)
* [Python Website](https://www.python.org/)
* pip
    ```sh
    python -m ensurepip --upgrade
    ```
* A Discord Bot Application that is added to your desired server(s), and which's token you possess

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/bitfl0wer/altminder.git
   ```
2. (Optional) Create and activate a venv in the project directory
    <br/>
Linux and macOS:
    ```sh
   python -m venv venv
   source ./venv/bin/activate
   ```
3. Install pip requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Start the bot. From the project source (magicaltavern/) type
    ```sh
    TOKEN=YOURBOTTOKENHERE python -m src.bot
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/bitfl0wer/altminder/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the AGPL-3.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Florian - florian@pro-weber.com

Project Link: [https://github.com/bitfl0wer/altminder](https://github.com/bitfl0wer/altminder)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [KreerC for writing the entire first version of the bot!](https://github.com/KreerC)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/bitfl0wer/altminder.svg?style=for-the-badge
[contributors-url]: https://github.com/bitfl0wer/altminder/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/bitfl0wer/altminder.svg?style=for-the-badge
[forks-url]: https://github.com/bitfl0wer/altminder/network/members
[stars-shield]: https://img.shields.io/github/stars/bitfl0wer/altminder.svg?style=for-the-badge
[stars-url]: https://github.com/bitfl0wer/altminder/stargazers
[issues-shield]: https://img.shields.io/github/issues/bitfl0wer/altminder.svg?style=for-the-badge
[issues-url]: https://github.com/bitfl0wer/altminder/issues
[license-shield]: https://img.shields.io/github/license/bitfl0wer/altminder.svg?style=for-the-badge
[license-url]: https://github.com/bitfl0wer/altminder/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/[None]
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
