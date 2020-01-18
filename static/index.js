const { Scene, PerspectiveCamera, WebGLRenderer, BoxGeometry, MeshBasicMaterial, Mesh, OBJLoader} = THREE 

let scene = new Scene();
let camera = new PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

let renderer = new WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight); // need to improve
window.addEventListener('resize', function() {
	renderer.setSize(window.innerWidth, window.innerHeight);
});

document.body.appendChild( renderer.domElement );


let loader = OBJLoader();


loader.load(
	// resource URL
	'/static/models/10014_dolphin_v2_max2011_it2.obj',
	// called when resource is loaded
	function ( object ) {
		scene.add( object );
	},
	// called when loading is in progresses
	function ( xhr ) {
		console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );
	},
	// called when loading has errors
	function ( error ) {
		console.log( 'An error happened' );
	}
);

let geometry = new BoxGeometry( 1, 1, 1 );
let material = new MeshBasicMaterial( { color: 0x00ff00 } );
let cube = new Mesh( geometry, material );
scene.add( cube );

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

	cube.rotation.x += 0.01;
	cube.rotation.y += 0.01;

	renderer.render( scene, camera );
};

animate();	
