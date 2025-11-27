# annaScript

![Python](https://img.shields.io/badge/Python-3.13.2-blue)
![Version](https://img.shields.io/badge/Version-1.0.0-brightgreen)
![Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![Platforms](https://img.shields.io/badge/Platforms-All-success)

## Introduction

*annaScript* is a simple, easy-to-use markup language that compiles to HTML. It features a rich, simple syntax and an easily extendible
macro system. Because *annaScript* uses a minimalistic approach to parse data, realtime compilation is possible without any noticable lag (Average Compile Time: < 30ms).

Together with [annaScript Studio](https://github.com/hasderhi/annascript-studio), a sophisticated editor for *annaScript* with realtime preview, the language becomes the perfect solution for note taking, especially if you like *markdown* syntax but miss CSS features.

Like mentioned above, extending or adjusting the language is easy due to the macro and theme system. All themes are defined through CSS files. In this repository, you'll find three base themes you can use out of the box, modify or use as template to create new ones.

## Get Started

*Note: In order to benefit from all the features included in the language, it is recommended to use [annaScript Studio](https://github.com/hasderhi/annascript-studio). It not only features real-time preview and accurate syntax highlighting for the language, but also registers the file type ```.ascr``` on Windows, which makes working with *annaScript* files easier overall.*

*This version features a command-line API to work with the compiler, which makes it simple to include *annaScript* in your own software, but isn't ideal for casual use.*

### Download and Usage

#### Python Version (Recommended)

As this version of *annaScript* is mainly meant for developers, the Python version is ideal for customization and modifying the compiler. It has no external dependencies and should run on any full 3.X.X Python installation.

To use it, simply download the latest release and then run main.py

```bash
py main.py path/to/input.ascr path/to/output.html
```

#### `.exe` Version

This repository also contains a Windows executable. However, usage is not recommended as it can be inconvenient. The .exe version mostly exists for reference. Additionally, the executable comes without an installer, so it has to be added to ```$path``` manually to make usage somewhat possible.

If you still want to use it, this is the required command structure (assuming the executable has been added to ```$path```):

```bash
ascrComp.exe /absolute/path/to/input.asrc /absolute/path/to/output.html
```

*Note: The ```/themes``` folder has to be in the same directory as ```output.html```*

### Syntax and Macros

Most of the syntax is similar to *markdown*, with some features extending its functionality. Below you'll find all current elements of *annaScript*'s syntax.

#### Meta tags

These tags that have to be placed at the beginning at the document (but aren't necessary) define meta elements of the document, such as author, title and style. The style tag defines the CSS theme that is linked in the HTML.
Below are all current meta tags available:

```annascript
@title: My Document
@author: Annabeth Kisling
@style: default
@darkmode: true
```

#### Headings

Headings use the same syntax as *markdown*. They are directly equivalent to ```<h1>```-```<h6>``` tags in HTML.

```annascript
# H1 heading
## H2 heading
### H3 heading
#### H4 heading
```

#### Paragraphs

Paragraphs are separated by at least one blank line.

```annascript
This is paragraph one.
It continues here.

This is paragraph two.
```

#### Formatting

Text formatting works by wrapping text in certain characters. Currently, *annaScript* supports **bold**, *italic* and highlighted texts, `code blocks` and sub/superscript.

```annascript
*italic*

**bold**

***both***

==highlight==

`code block`

^^super^^

,,sub,,
```

#### Links

Links follow the same syntax as in *markdown* as well.

```annascript
[Visit My Website](https://tk-dev-software.com)
```

#### Lists

There is support for ordered and unordered lists, as well as for sub items.

Unordered:

```annascript
- Item A
- Item B
    - Subitem
    - Subitem
```

Ordered:

```annascript
1. First
2. Second
```

#### Macros

Macros are the highlight of *annaScript* and are the easiest to add your own elements to your document. All macros follow the same syntax rules:

```annascript
::type optional-attributes
content inside macro...
::
```

There are a few built-in macros:

```annascript
::box type=danger title="Attention!"
Danger awaits...
::

::box type=warning title="Warning!"
Be warned!
::

::box type=info title="Information"
Be informed!
::

::def
(a+b)^^2^^ = a^^2^^ + 2ab + b^^2^^
::

::note
Remember this!
::

::box
Hello, I'm just a box!
::

::center
Centered text
::
```

These macros are equivalent to CSS classes, which makes it easy to add your own. Simply add a new class to your theme CSS file and use its name inside the macro definition.

#### Tables

Tables are written using the separator ("|"). If there are dashes below the first row, the row becomes a table header.

```annascript
| Name  | Age | Grade |
|-------|-----|-------|
| Alice | 17  | A     |
| Bob   | 16  | B     |
```

## Modifying and Developing with annaScript

### Overview

When I started creating *annaScript*, it was because I was fed up with taking notes at school in Word and struggling with its formatting system. I tried using *markdown* but quickly realised that it was missing some features like sub/superscript or macros. Also, it was a problem that different *markdown* engines used different syntax versions.

Because of this, I decided to build my own markup language - *annaScript* was born. The engine itself is really basic and features the typical "interpreted language" features like a simple parser, tokenizer, AST nodes and a HTML renderer. However, because this language is very much tailored to my own specific needs, I decided to keep it easily customiziable so anyone can adjust the syntax to their likings.

### Macros and Themes

If you simply want to create your own elements, you don't need to modify the engine itself. You can simply create your theme (or modify an existing one) and add your macro's CSS definitions inside a CSS class.

Creating and using your own themes is really simple: Navigate to the ```/themes``` folder and create a new folder with your desired theme name (e.g. "myTheme"). Inside that folder, create two CSS files: ```light.css``` and ```dark.css```. Now, you can write your own style definitions for your documents. My recommendation is to start of by modifying one of the built-in themes to understand what elements need to have style attributes.

With the new theme created, import and use it in your document by placing this meta tag at the top:

```@style: myTheme```

Optionally, you can also use dark mode (default is light):

```@darkmode: true```

### Modifying the language's syntax

This is a bit more difficult and requires some knowledge about interpreters and parsing syntax. A detailed explanation would take too long here, but the code is very readable and easy to modify if you have basic knowledge of interpreters. You'll find many tutorials online, for example on YouTube.

Here is a short breakdown what every file is doing:

```ast_nodes.py``` - defines the nodes and syntax of *annaScript*

```inline.py``` - Handles inline characters, escapes code and various characters

```main.py``` - The starting point of the app, calls the parser and reads/writes files

```parser.py``` - Parses the syntax

```renderer.py``` - Renders the output HTML and registers built-in macros

```tokenizer.py``` - Appends token

## Information

This project is the counter part to *annaScript* Studio, my editor for *annaScript*. Check it out [on its GitHub repository](https://github.com/hasderhi/annascript-studio)!

This project is not using any external dependencies. All source code and the built-in themes are made by the author and subject to her copyright. All code is released under the MIT-License (see ```license.md```) and therefore allows anyone to modify, copy, use or release it under the condition the author's work is credited and the license is included.

If you created a theme and think it could be useful for others, feel free to make a pull request to the repo!

## Author

Annabeth Kisling

[annabeth@tk-dev-software.com](mailto:annabeth@tk-dev-software.com)

[tk-dev-software.com](https://tk-dev-software.com)
