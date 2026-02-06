# Défi d’animation #

Ce défi consiste à animer dans un espace deux dimensions à l’aide de vecteurs. En calculant une transformation vectorielle sur un groupe de points et en affichant leur nouvelle position 24 fois par seconde, nous sommes capables d'animer toutes sortes de formes.

<br>

**Logiciels demandés:**

* Langage de votre choix entre C#, Javascript, Python et Java
* Framework GUI compatible avec le langage choisi
* Pour C#, utilisez WPF, Winforms ou WinUI 3
* Pour Javascript, utilisez HTML, CSS et SVG
* Pour Java, utilisez JavaFX, vous pouvez utiliser un framework pour gerer vos paquets come Maven et Gradle
* Pour Python, vous avez besoin de Numpy et Pygames
* Vous avez le droit d'utiliser un GUI builder (SceneBuilder, PyQt, Tkinter, etc), mais j'ai besoin de pouvoir exécuter votre code sans l'installer 

<br>
  
* Pour le dernier exercise, il se peut que vous ayez besoin d'une librairie pour calculer les nombres complexes, à moins que vous voulez créer votre propre classe 
* C#: System.Numerics.Complex, Java: Apache Commons Math library, Javascript: Math.JS, Python: Numpy

<br>

**Critère d’évaluation:**

* Une bonne séparation du code pour la logique et du code pour l’affichage selon les principes de model-view-controller sera récompensé dans le pointage  
* Les détails et l’originalité sont favorisés  
* Calculs efficaces

<br>

**Si vous n'avez jamais fait de dessins / de GUI:**
* C#:      [System.Drawing](https://learn.microsoft.com/en-us/dotnet/api/system.drawing?view=windowsdesktop-10.0), [WinUI 3](https://learn.microsoft.com/en-us/windows/apps/winui/winui3/)
* Javascript: [Canvas](https://www.w3schools.com/html/html5_canvas.asp), [SVG](https://www.w3schools.com/html/html5_svg.asp), [DOM](https://www.w3schools.com/js/js_htmldom.asp)
* Java:  [2D shapes](https://www.tutorialspoint.com/javafx/javafx_2d_shapes.htm), [JavaFx](https://openjfx.io/openjfx-docs/#introduction)
* Python: [Pygame display](https://www.pygame.org/docs/ref/display.html), [Pygame draw](https://www.pygame.org/docs/ref/draw.html)
_________________ 


<br>

**1\.**

Pour commencer, créez une interface graphique avec trois boutons, chacun déclenchant une animation, et un rectangle où les animations seront affichées pendant 5 secondes.

**1B\.**
Dessinez les arrêtes d'un carré

**1C\.**
Remplissez le carré de votre couleur préférée!

<br>

_________________ 


<br>


**2\.**


Pour la première animation, on va y aller simple. Il faut simplement dessiner le classique bonhomme sourire et le faire tourner.

<img height="412" alt="Exemple 1" src="smiley.gif" />


<br>

_________________ 

<br>

**3\.**

Maintenant, on va ajouter plus de formes. Après avoir fait une automobile, il faut la faire accélérer pendant 5 secondes de manière à ce qu'elle traverse le rectangle.

<img height="412" alt="Exemple 3" src="vroom.gif" />

<br>

**3B\.**  
Ajoutez des rayons sur les roues et faites les tourner en suivant l'accélération.  


<br>

_________________ 

<br>

**4\.**

Pour cette partie, il faut animer un objet 3D dans un espace 2D. On considère un cube représenté en projection dimétrique. Le quatres sommets enlignés (voir image) font partie de la circonférence d'un cercle. On souhaite faire pivoter le cube en déplaçant ces quatre sommets sur le cercle.

   <img width="736" height="412" alt="referenceCube" src="referenceCube.png" />
   <img height="412" alt="Exemple 3" src="cubic.gif" />


**4A\.**  
Commencez simplement par animer toutes les arrêtes.

**4B\.**  
N'animez que les arrêtes qui sont visibles.

**4C\.**  
Coloriez les faces visibles

**4D\.**  
simulez de l’éclairage en changeant la couleur des arêtes et en ajoutant des dégradés sur les faces.  


**Pistes de solution:**

* Utiliser des angles d'Euler peut causer un blocage de cardan [gimball locks](https://www.youtube.com/watch?v=zc8b2Jo7mno), c'est à dire, faire une rotation en x,y,z fait en sort que le z est dependant du y qui est dépendant du x, causant la perte d'un degrée de libertée
* Une solution pour éviter ce problème est d'utiliser des [quaternions](https://mathworld.wolfram.com/Quaternion.html), [c'est un système qui utilise les nombres complexes](https://www.youtube.com/watch?v=d4EgbgTm0Bg), [pour mieux représenter le rotations en 3D](https://www.youtube.com/watch?v=zjMuIxRvygQ)
* En restant avec les angles d'Euler, une autre manière de visualiser le problème: plutôt qu'un cube qui subit une rotation en xy, nous pouvons le voir comme un vecteur qui subit une rotation en w et le cube qui suit le vecteur

     <img width="582" height="352" alt="vecteurRotate" src="vecteurRotate.png" /> 

* Pour la rotation d'objets suivant un vecteur de 3 dimensions, on peut utiliser [la formule de Rodrigues](https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula) [qui permet de calculer efficacement une matrice de rotation](https://mathworld.wolfram.com/RodriguesRotationFormula.html), [avec un angle et un vecteur unitaire](https://www.youtube.com/watch?v=CQSC5W5bPXQ)
