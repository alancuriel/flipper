const { Scene, PerspectiveCamera, Geometry, LineBasicMaterial, WireframeGeometry, DirectionalLight, OrbitControls, Color, AmbientLight, WebGLRenderer, BoxGeometry,
	MeshBasicMaterial, LineSegments, Mesh, OBJLoader, LoadingManager} = THREE 

let scene = new Scene();
let camera = new PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

let renderer = new WebGLRenderer();

let controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.25;
controls.enableZoom = true;



var keyLight = new DirectionalLight(new Color('hsl(30, 100%, 75%)'), 1.0);
keyLight.position.set(-100, 0, 100);

var fillLight = new DirectionalLight(new Color('hsl(240, 100%, 75%)'), 1.0);
fillLight.position.set(100, 0, 100);

var backLight = new DirectionalLight(0x000000, 1);
backLight.position.set(100, 0, -100).normalize();

scene.add(keyLight);
scene.add(fillLight);
scene.add(backLight);



// var light = new THREE.AmbientLight( 0x000000 ); // soft white light
// scene.add( light );


renderer.setSize(window.innerWidth, window.innerHeight); // need to improve
window.addEventListener('resize', function() {
	renderer.setSize(window.innerWidth, window.innerHeight);
});

document.body.appendChild( renderer.domElement );

let manager = new LoadingManager();
let loader = new OBJLoader(manager);
var dolphinOBJ; // global reference for dolphin
loader.setPath('static/models/');
loader.load('10014_dolphin_v2_max2011_it2.obj', function(object){

	// object.traverse( function ( child ) {

	// if ( child.isMesh ) {

	// 	child.geometry = new Geometry().fromBufferGeometry( child.geometry );
	// 	console.log(geometry.vertices)

	// 	// var wireframeGeomtry = new WireframeGeometry( child.geometry );
	// 	// var wireframeMaterial = new LineBasicMaterial( { color: 0xffffff } );
	// 	// var wireframe = new LineSegments( wireframeGeomtry, wireframeMaterial );
	// 	// child.add(wireframe);

	// 	}
	// });

	object.position.y -= 10;
	object.rotation.x += 20;
	object.rotation.y += 10;
	object.rotateZ( Math.PI  );
	// console.log(object.attributes.position)
	dolphinOBJ = object;
	scene.add(object); 



});




// let geometry = new BoxGeometry( 1, 1, 1 );
// let material = new MeshBasicMaterial( { color: 0x00ff00 } );
// let cube = new Mesh( geometry, material );
// scene.add( cube );
camera.position.z -= 250;
// console.log(dolphinOBJ.attributes.position)
// camera.position.z = 5;

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

let animate = function () {
	requestAnimationFrame( animate );
	controls.update();
	// dolphinOBJ.attributes.position.needsUpdate = true; 

	dolphinOBJ.rotation.z += 0.01;
	// dolphinOBJ.rotation.z += 0.01;

	renderer.render( scene, camera );
};

animate();	
