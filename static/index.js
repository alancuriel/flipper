const { Scene, PerspectiveCamera,Color, WebGLRenderer, BoxGeometry, MeshBasicMaterial, Mesh, OBJLoader, LoadingManager} = THREE 

let scene = new Scene();
let camera = new PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

let renderer = new WebGLRenderer({alpha: true});

renderer.setSize(window.innerWidth, window.innerHeight); // need to improve
window.addEventListener('resize', function() {
	renderer.setSize(window.innerWidth, window.innerHeight);
});

document.body.appendChild( renderer.domElement );





var loadOBJ = function() {
  //Manager from ThreeJs to track a loader and its status
  var manager = new LoadingManager();
  //Loader for Obj from Three.js
  var loader = new OBJLoader(manager);

  //Launch loading of the obj file, addBananaInScene is the callback when it's ready 
  loader.load('/static/models/10014_dolphin_v2_max2011_it2.obj', function(object) {
    banana = object;
    //Move the banana in the scene
    banana.rotation.x = Math.PI / 2;
    banana.position.y = -200;
    banana.position.z = 50;
    //Go through all children of the loaded object and search for a Mesh
    object.traverse(function(child) {
      //This allow us to check if the children is an instance of the Mesh constructor
      if (child instanceof Mesh) {
        child.material.color = new Color(0X00FF00);
        //Sometimes there are some vertex normals missing in the .obj files, ThreeJs will compute them
        child.geometry.computeVertexNormals();
      }
    });
    
    scene.add(banana);
    // renderer.render();
  });
};

loadOBJ();



// let geometry = new BoxGeometry( 1, 1, 1 );
// let material = new MeshBasicMaterial( { color: 0x00ff00 } );
// let cube = new Mesh( geometry, material );
// scene.add( cube );

camera.position.z = 5;



function resizeCanvasToDisplaySize() {
  const canvas = renderer.domElement;
  // look up the size the canvas is being displayed
  const width = canvas.clientWidth;
  const height = canvas.clientHeight;

  // adjust displayBuffer size to match
  if (canvas.width !== width || canvas.height !== height) {
    // you must pass false here or three.js sadly fights the browser
    renderer.setSize(width, height, false);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();

    // update any render target sizes here
  }
}


let animate = function () {
	// resizeCanvasToDisplaySize();
	requestAnimationFrame( animate );

	// cube.rotation.x += 0.01;
	// cube.rotation.y += 0.01;

	renderer.render( scene, camera );
};

animate();	
