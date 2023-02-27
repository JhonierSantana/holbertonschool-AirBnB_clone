<html>
<body>
<h1> AirBnB clone - The console </h1>
<img src= "https://www.tabbykatz.com/hbnb.png" width="800" height="auto"/>
<h2>Background Context</h2>
<hr>
<p>We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track</p>
<p>After 4 months, we will have a complete web application composed by:</p>
<p> - A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging) </p>
<p> - A website (the front-end) that shows the final product to everybody: static and dynamic </p>
<p> - A database or files that store data (data = objects) </p>
<p> - An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them) </p>

<h2>Repository Contents</h2>
<table>
  <tr>
    <th>File</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>console.py</td>
    <td>Command interpreter.</td>
  </tr>
  <tr>
    <td>base_model.py</td>
    <td>Defines all common attributes/methods for other classes.</td>
  </tr>
  <tr>
    <td>file_storage.py</td>
    <td>A class that serializes instances to a JSON file and deserializes JSON file to instances.</td>
  </tr>
  <tr>
    <td>user.py</td>
    <td>A class User that inherits from BaseModel.</td>
  </tr>
  <tr>
    <td>amenity.py</td>
    <td>A class Amenity that inherits from BaseModel.</td>
  </tr>
  <tr>
    <td>city.py</td>
    <td>A class City that inherits from BaseModel.</td>
  </tr>
  <tr>
    <td>place.py</td>
    <td>A class Place that inherits from BaseModel.</td>
  </tr>
  <tr>
    <td>review.py</td>
    <td>A class Review that inherits from BaseModel.</td>
  </tr>
   <tr>
    <td>state.py</td>
    <td>A class State that inherits from BaseModel.</td>
  </tr>
  <tr>
    <td>tests\</td>
    <td>Contains unittests for the project.</td>
  </tr>
</table>
<h2>The Console</h2>
<img src= "https://user-images.githubusercontent.com/93772775/183030202-7fe98cea-20a5-4da6-9023-018752bdc405.png" width="800" height="auto"/>

<h2>Data Diagram</h2>
<img src= "https://user-images.githubusercontent.com/56379934/188288321-f18c568e-eb53-4e07-a967-9430c91d32d6.jpg" width="800" height="auto"/>

<h3>Installation</h3>
<hr>
<p>git clone</p>
<p>cd AirBnB_clone</p>
<p>./console.py</p>
<hr>
<h2>AUTHORS...</h2>
<h5>Jhonier Santana.</h5> <img src="https://www.pofilo.fr/img/SPOF-github/github1600.png" width="100" height="100"/>
<h5>Luisa Maria Lopez.</h5><img src="https://www.pofilo.fr/img/SPOF-github/github1600.png" width="100" height="100"/>
</body>
</html>