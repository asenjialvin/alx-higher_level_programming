# JavaScript Web jQuery Project

This repository contains solutions to a set of tasks focused on utilizing JavaScript and jQuery for web development.

## Table of Contents

- [Project Description](#project-description)
- [Requirements](#requirements)
- [Manual QA Review](#manual-qa-review)
- [Tasks](#tasks)
  - [Task 0: No JQuery](#task-0-no-jquery)
  - [Task 1: With JQuery](#task-1-with-jquery)
  - [Task 2: Click and turn red](#task-2-click-and-turn-red)
  - [Task 3: Add `.red` class](#task-3-add-red-class)
  - [Task 4: Toggle classes](#task-4-toggle-classes)
  - [Task 5: List of elements](#task-5-list-of-elements)
  - [Task 6: Change the text](#task-6-change-the-text)
  - [Task 7: Star wars character](#task-7-star-wars-character)
  - [Task 8: Star Wars movies](#task-8-star-wars-movies)
  - [Task 9: Say Hello!](#task-9-say-hello)

## Project Description

This project focuses on practicing JavaScript and jQuery for front-end web development. It involves manipulating the Document Object Model (DOM), handling events, making API requests, and utilizing jQuery for DOM manipulation.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Chrome (version 57.0)
- All files should end with a new line
- A `README.md` file at the root of the folder is mandatory
- Code should be semistandard compliant with the flag `--global $`: `semistandard *.js --global $`
- jQuery version 3.x must be used
- Not allowed to use `var`
- HTML should not reload for each action, including DOM manipulation, updating values, and fetching data

## Manual QA Review

It is the responsibility of the developer to request a review from a peer before the project’s deadline. If no peers are available for review, a review should be requested from a TA or staff member.

## Tasks

### Task 0: No JQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) without using the JQuery API.

### Task 1: With JQuery

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) using the JQuery API.

### Task 2: Click and turn red

Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag DIV#red_header using the JQuery API.

### Task 3: Add `.red` class

Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag DIV#red_header using the JQuery API.

### Task 4: Toggle classes

Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag DIV#toggle_header using the JQuery API. The `<header>` element must always have one class: `red` or `green`, never both at the same time and never empty.

### Task 5: List of elements

Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag DIV#add_item using the JQuery API. The new element must be: `<li>Item</li>` and added to UL.my_list.

### Task 6: Change the text

Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on DIV#update_header using the JQuery API.

### Task 7: Star wars character

Write a JavaScript script that fetches the character name from the URL: https://swapi-api.alx-tools.com/api/people/5/?format=json and displays the name in the HTML tag DIV#character using the JQuery API.

### Task 8: Star Wars movies

Write a JavaScript script that fetches and lists the titles for all movies from the URL: https://swapi-api.alx-tools.com/api/films/?format=json. All movie titles must be listed in the HTML tag UL#list_movies using the JQuery API.

### Task 9: Say Hello!

Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello using the JQuery API.
