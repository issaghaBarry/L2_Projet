var test = file_get_contents("test.json");
var chaine = test.parse(test);
var element = document.getElemenById("tot");
element.write(chaine);
