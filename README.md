# Film Memory Quiz Night

## Pitch

 - Welcome to Film Memory Quiz Night, a fun and engaging game designed to challenge your memory and sharpen your mind after a busy day! Suitable for all ages, from young learners to adults looking to keep their memory strong, this game offers an enjoyable way to relax in the evening while exercising your cognitive abilities.

 - Film Memory Quiz Night is designed to be played in the evening. It allows you to relax, reflect, and reminisce about films after a full day of activities. With a mix of fun questions and visual prompts, this game is not only entertaining but also a great way to keep your mind active. Try it tonight and enjoy a refreshing brain challenge!

 - The Memory Quiz Night is a recreational quiz game where people can test how much they remember about popular movies. It's a great way to enjoy some friendly competition while testing your knowledge and memory on new and old films. Whether you're at home, in a pub, or at a special venue, the quiz is designed to bring people of all ages together to laugh, talk about favourite films, and have a great time. With trivia questions and memorable movie moments, it's perfect for families, couples and social events!

## Features 

- The Film Memory Quiz Night is designed with a clean and intuitive interface using HTML, CSS, and JavaScript, making it easy for users of all ages to engage. The interface presents questions and answers clearly, with easy-to-use buttons for selecting answers and navigating through the quiz.

### Existing Features

- __Restart Functionality__

   - The quiz includes a handy "Restart Game" button that allows players to reset and start over at any point during the quiz. This option allows participants to retry or play multiple times, enhancing the overall ease of restarting the game.
   - This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the 'back' button. 

![RESTART](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/restart.png)

- __Interactive Answer Feedback__

  - When a participant selects an answer, the system immediately provides feedback. Correct answers turn green, and incorrect answers turn red - indicating the right or wrong answer.
  - In addition, if the correct answer is selected, a related image from the film is displayed, enriching the quiz with a visual element. 
  - An image is displayed solely as a visual correlation to the correct answer, aligning with the purpose of the memory game, which is to exercise the brain and get the cogwheels turning.

![ANSWER FEEDBACK](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/dicaprio.png)

- __Real-Time Scoring and Results__

   - The quiz includes a real-time scoring system that tracks the number of correct answers a player has given. At the end of the quiz, the player's score and percentage are displayed in a result section, providing clear feedback on performance.

![REALTIME SCORE](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/results.png)

- __Registration and Score Submission__

  - Once the quiz is completed, participants can register their scores through a "Register & Send Score" button. This feature redirects users to a registration page, allowing them to input their details and submit their final score and percentage. They can register and submit via a registration form to their email address. This is a great takeaway to keep your scores as part of a memorable experience. It is also an excellent way to increase your subscriber base so more people can join the quiz game.

![REGISTRATION PAGE](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/register.png)

- __Visual Media Integration__ 

  - The quiz supports the display of images related to the films, providing a visually appealing experience. Correct answers are accompanied by relevant images from the film, making the quiz more engaging and enjoyable for participants. The visual image cards are prompted by a correct answer and it's aims is to stimulate your memory. These cards help you stay engaged and strengthen your memory connections, similar to methods used in psychological studies.

![VISUAL MEMORY CARDS](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/imagecards.png)

- __Mobile and Desktop Compatibility__

  - The quiz has been designed to be responsive, ensuring it works well on both mobile devices and desktops. The flexible layout adapts to different screen sizes, making it suitable for players on the go or at home on larger screens.

![MOBILE DESKTOP COMPATIBILITY](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/3screens.png)

- __Interactive Result Screen__

  - After completing the quiz, players are directed to a result screen that shows their performance, including their final score and percentage. Players can either choose to register their score or play again.
  
  - At the last stage of designing the web application, a congratulations page is included for users who score over 70%. An animation displaying confetti is added as visual simuli to congratulate the winner!

 ![RESULTS SCREEN](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/congrats.png)

- __UX DESIGN__

   - I have provided principles of good UX design. It provides a clean, intuitive interface with clear navigation and visual feedback. The layout is simple and user-friendly, ensuring that users can easily follow the flow of the quiz, from answering questions to viewing their results. The interactive elements (i.e., the buttons) are visually distinct, making it easy for users to interact with the application. 

   - The Colour Palette - consisting of a combination of neutral, vibrant, and contrasting colours - supports good UX design in several ways. Dark tones like "Extra Black" (222222) and "Extra Black" (181A20) and Charcoal (333) keeps the palette balanced, when placed next to the pink shades. It offers excellent readability when paired with lighter text and enhance clarity.
  
   - Bright accent colors such as "Deep Pink" (DF0B75) and "Dragonfruit" (EB59A2) draw attention to critical actions or alerts, improving user engagement. Together, this palette supports user-friendly interactions by balancing readability, visual emphasis, and emotional appeal, creating a seamless and intuitive experience.

   - Additionally, the high contrast between buttons and their backgrounds ensures that they are accessible to a wide range of users, including those with visual impairments, by adhering to accessibility guidelines. 

![Colour Swatch](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/colourswatch.png)

 ## Summary

  - The Film Memory Quiz Night offers an engaging and interactive experience with features like real-time feedback, visual elements, scoring systems, and seamless navigation. Whether you're playing on a mobile device or desktop, the quiz provides an accessible, fun, and challenging environment for movie lovers to test their knowledge and enjoy a game night with friends or family.

## Testing 

  - The Film Memory Quiz Night web application was successfully tested and met all functional and usability requirements. During testing, the quiz consistently loaded questions and answers without errors, and users received immediate feedback with visual cues for correct and incorrect answers. 

  - The Film Memory Quiz Night web application was tested across multiple major browsers, including Firefox, Safari, Microsoft Edge, and Chrome. In all cases, the application performed seamlessly, with no significant differences in functionality or user experience.

  - The quiz loaded quickly, and all interactive elements, such as buttons, answer selections, and the display of image cards, worked consistently across these browsers. 
  
  - Additionally, the real-time scoring and final result display were accurate in each environment. The application's responsive design also adapted well to different screen sizes, ensuring a smooth experience on both desktop and mobile browsers. This confirms that the web application is fully compatible and operates reliably across all major browsers.



| Test Case                         | Expected Result                                                                     | Test Result |
|-----------------------------------|-----------------------------------------------------------------------              |-------------|
| Open the Index page               | Index page opens with introduction content and play button                          | ✅ PASS          |
| Play button hover and click       | Play button directs user to quiz page                                               | ✅ PASS          |
| Questions load on landing page    | Questions and answer buttons load                                                   | ✅ PASS          |
| Correct answer selection          | Image card appears. Correct answer highlighted in green                             | ✅ PASS          |                                
| Incorrect answer selection        | Red highlight appears on incorrect answer button                                    | ✅ PASS          |
| Restart game button               | Restarts game and redirects to the index page                                       | ✅ PASS          |                       
| Score result page                 | The percentage score and the user's score out of 10 results are generated           | ✅ PASS          |                           
| Congratulations page              | If the score result is over 70%. The congratulations text appears                   | ✅ PASS          |
| Registration page                 | The user can register their email at the end of the quiz                            | ✅ PASS          |                                              
| Submit score via a html form      | A valid email is recorded and the submit button will email the scores to the user   | ✅ PASS          |

## Accessibility

- As noted in the UX Design section, the high contrast between buttons and backgrounds ensures accessibility for users with visual impairments. It is indicated by Lighthouse that SEO needs to be improved. This is not a concern at this time.

 Here is the lighthouse score: 
 ![Lighthouse](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/lighthouse.png)

### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fisahu-dev.github.io%2FFilm-Memory-Quiz-Night%2F)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fisahu-dev.github.io%2FFilm-Memory-Quiz-Night%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- Javascript
   - JSHINT: Fixed errors, now successfully passed the JShint validator. Please see screenshot below.
 [JSHINT](https://github.com/IsaHu-dev/Film-Memory-Quiz-Night/blob/main/media/jshint_validation.png)
  
### Resolved Bugs

- Bug Fixed - in questions.js. Early on in the development of the web app, there was a syntax error. The bug resulted in an "Unexpected end of input". This is now fixed and the questions follow on, once a question is answered. 
- Bug Fix - on the score system total. The total score now reflects accurately, and the fix has been applied in the register.js file. 
- Bug Fix - addressed a styling issue where the correct answer button failed to retain its green colour on smaller devices (e.g., iPhone, Android). Implemented a media query in general.css to ensure the .correct class is consistently applied across different screen resolutions, preventing style overrides. The solution was tested and validated on smaller device types.
- There are presently no bugs in the web application.

## Deployment

The site was deployed to GitHub Pages through the Gitpod environment. The deployment process involves the following steps:

   - Commit changes to the repository with descriptive commit messages using Git, which are then pushed to GitHub. 
  - To deploying the web application:
   
    1. Firstly navigate to your site's repository. 
    2. Click on settings. 
    3. Click Pages under General settings.
    4. Under Build and deployment,select Deploy from a branch. 
    5. Choose a publishing source (i.e. main) from the branch dropdown menu. Then click save.   

  - Navigate to the "Actions" tab on GitHub to monitor the deployment workflow. Upon successful deployment, the GitHub Pages site will automatically refresh, and a link (next to the deploy branch) will appear, confirming that the deployment was completed successfully.

The live link can be found here - [Deployed link](https://isahu-dev.github.io/Film-Memory-Quiz-Night/)

## Credits 

  - I used this tutorial as a rough guide:  https://www.youtube.com/watch?v=eQxcuCMNtFM. I have taken the structure of this tutorial and written my own code. 
  
  - Javascript resources https://javascript.info/, [FreeCodeCamp](https://www.freecodecamp.org/learn/) - free course
  
  - Learning Javascript book. Third Edition. O'Reilly. Author Ethan Brown. [FreeCodeCamp](https://www.freecodecamp.org/learn/) 

  - CSS resource - flex box code ideas. [CSS Tricks](https://css-tricks.com/dont-overthink-flexbox-grids/)


### Content 

- Content is adapted from Movie quizzes online - specifically [Buzzfeed](https://www.buzzfeed.com/kellyrissman/movie-trivia-questions)
- Film quiz ideas were adapted from [Brainscape](https://www.brainscape.com/subjects/film-studies)

### Media

- Vector Graphics used as image cards are from royalty free Vecteezy.  [Vecteezy](https://tinyurl.com/y4bx6umt) 
- Confetti animation video is from royalty free Vecteezy.  [Vecteezy](https://tinyurl.com/y4bx6umt) 
- I created my own artwork for the Pulp Fiction image cards.
- Colour swatch is adapted from [Coolors](https://coolors.co/222222-181a20-5dbea3-ec3992-d9006e)
- The README.md template is adapted from the Love Running README.md. 

### Acknowledgements

- Thanks to mentor, Moritz Wach for the referral of the README.md example of a user testing table - as well as PP2 guidance.
