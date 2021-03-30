# Velokaz Scrapper
A web scrapping script for Velokaz

## How to create a schema file
### Intro
A schema file is a sort of strategy that the script understands in order to parse you page content.

### Skeleton
A schema entry holds the target DOM element information, there are 4 types of elements  :
* Normal element (with no id of class)
* Class based element
* Id based element
* Attribut based element

each element has its own properties, for example a class based element has a target (class value) and a method (all elements or first occurence).
```json
  {
    "element": "div",
    "type": "class",
    "target": "navbar",
    "method": "one"
  }
```

### Properties
He is the list of all possible properties

<table width=100%>
  <thead>
    <tr>
      <th>Property name</th>
      <th>Description</th>
      <th>Possible Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>schema</td>
      <td>Root element that hold the strategy</td>
      <td>array</td>
    </tr>
    <tr>
      <td>url</td>
      <td>The link of the page you want to scrape</td>
      <td>string</td>
    </tr>
    <tr>
      <td>process</td>
      <td>A collection of selectors that defines the strategy</td>
      <td>array</td>
    </tr>
    <tr>
      <td>element</td>
      <td>The name of DOM tag (eg. div, table, img, a...)</td>
      <td>string</td>
    </tr>
    <tr>
      <td>target</td>
      <td>The value of the class, id or attribute</td>
      <td>any string</td>
    </tr>
    <tr>
      <td>type</td>
      <td>The selector type used to parse data</td>
      <td>['class', 'id', 'attribute', 'normal']</td>
    </tr>
    <tr>
      <td>occurs</td>
      <td>Extraction method helps to get specific data, if n integer is provided, it returns a limit of n elements</td>
      <td>['first', 'all', 'last', n-integer]</td>
    </tr>
    <tr>
      <td>is_list</td>
      <td>Define whether to return a simple list of a Tag element</td>
      <td>boolean</td>
    </tr>
    <tr>
      <td>is_list</td>
      <td>Define whether to return a simple list of a Tag element</td>
      <td>boolean</td>
    </tr>
  </tbody>
</table>

<br><br>
<img src="http://devcrawlers.com/img/blog/articles/velokaz_logo.jpg" alt="Velokaz Logo" height=30/>
